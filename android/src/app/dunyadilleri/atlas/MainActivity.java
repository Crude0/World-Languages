package app.dunyadilleri.atlas;

import android.app.Activity;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

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
        web.setOverScrollMode(View.OVER_SCROLL_NEVER);
        setContentView(web, new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));

        if (state != null) {
            web.restoreState(state);
        } else {
            web.loadUrl("file:///android_asset/app.html");
        }
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
