package app.dunyadilleri.atlas;

import android.app.Activity;
import android.content.ContentValues;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Base64;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.JavascriptInterface;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStream;

/**
 * Tek dosyalık haritayı varlıklardan (assets) yükleyen WebView kabuğu.
 * Ağ erişimi yok; uygulama izin istemez, arka planda hiçbir şey çalışmaz.
 */
public class MainActivity extends Activity {

    private WebView web;

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);

        web = new WebView(this);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        // Haritanın kendi kıstırma-yakınlaştırması var; tarayıcınınki devre dışı
        s.setSupportZoom(false);
        s.setBuiltInZoomControls(false);
        s.setDisplayZoomControls(false);
        s.setUseWideViewPort(true);
        s.setLoadWithOverviewMode(false);
        s.setTextZoom(100);
        // Sayfa iki temayı da destekliyor (color-scheme: light dark), bu yüzden
        // WebView kendi algoritmik karartmasını uygulamaz; bayrak yalnızca
        // prefers-color-scheme'in sistem ayarını yansıtmasını sağlar. Sayfa
        // "light" bildirdiği sürece WebView araya girip yüzeyleri tek tek
        // karartıyordu — açık temada panelin koyu kalmasının sebebi buydu.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            s.setAlgorithmicDarkeningAllowed(true);
        }
        web.setWebViewClient(new WebViewClient());
        // Sayfadaki PNG/SVG dışa aktarma köprüsü. WebView'in indirme işleyicisi
        // olmadığı için <a download> tıklaması sessizce yutuluyordu: sayfa
        // "indirildi" diyor, dosya hiçbir yere yazılmıyordu.
        web.addJavascriptInterface(new Saver(), "AtlasSave");
        web.setOverScrollMode(View.OVER_SCROLL_NEVER);
        setContentView(web, new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));

        if (state != null) {
            web.restoreState(state);
        } else {
            web.loadUrl("file:///android_asset/app.html");
        }
    }

    /**
     * Sayfadan gelen baytları İndirilenler klasörüne yazar.
     * Android 10 ve sonrasında MediaStore kullanılıyor; bu yol izin
     * gerektirmez, uygulama hiçbir izin istemeye devam etmez. Daha eski
     * sürümlerde herkese açık klasöre yazmak WRITE_EXTERNAL_STORAGE isterdi,
     * o yüzden orada uygulamanın kendi dış klasörüne yazılır ve yol bildirilir.
     */
    private class Saver {
        @JavascriptInterface
        public boolean save(String name, String mime, String b64) {
            if (name == null || b64 == null) {
                return false;
            }
            try {
                byte[] data = Base64.decode(b64, Base64.DEFAULT);
                String type = (mime == null || mime.isEmpty())
                        ? "application/octet-stream" : mime;
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                    ContentValues cv = new ContentValues();
                    cv.put(MediaStore.Downloads.DISPLAY_NAME, name);
                    cv.put(MediaStore.Downloads.MIME_TYPE, type);
                    Uri uri = getContentResolver().insert(
                            MediaStore.Downloads.EXTERNAL_CONTENT_URI, cv);
                    if (uri == null) {
                        return false;
                    }
                    OutputStream out = getContentResolver().openOutputStream(uri);
                    if (out == null) {
                        return false;
                    }
                    try {
                        out.write(data);
                    } finally {
                        out.close();
                    }
                    toast(name);
                } else {
                    File dir = getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS);
                    if (dir == null || (!dir.exists() && !dir.mkdirs())) {
                        return false;
                    }
                    File f = new File(dir, name);
                    FileOutputStream out = new FileOutputStream(f);
                    try {
                        out.write(data);
                    } finally {
                        out.close();
                    }
                    toast(f.getAbsolutePath());
                }
                return true;
            } catch (Exception e) {
                return false;
            }
        }
    }

    /** JavascriptInterface çağrıları arka planda geliyor; Toast ana iş parçacığında. */
    private void toast(final String text) {
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Toast.makeText(MainActivity.this, text, Toast.LENGTH_LONG).show();
            }
        });
    }

    @Override
    protected void onSaveInstanceState(Bundle out) {
        super.onSaveInstanceState(out);
        web.saveState(out);          // ekran döndürmede harita kaybolmasın
    }

    @Override
    public void onBackPressed() {
        if (web.canGoBack()) {
            web.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onDestroy() {
        if (web != null) {
            web.destroy();
            web = null;
        }
        super.onDestroy();
    }
}
