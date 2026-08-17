package app.dunyadilleri.atlas;

import android.app.Activity;
import android.content.ContentValues;
import android.net.Uri;
import android.os.Build;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Base64;
import android.webkit.JavascriptInterface;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStream;

/**
 * Sayfanın PNG/SVG dışa aktarma köprüsü.
 *
 * WebView'in bir indirme işleyicisi yok: sayfadaki {@code <a download>}
 * tıklaması sessizce yutuluyordu, yani dışa aktarma "İndirildi" yazmasına
 * rağmen ne İndirilenler'e ne galeriye dosya bırakıyordu. Sayfa baytları
 * base64 olarak buraya veriyor.
 *
 * Android 10 ve sonrasında MediaStore kullanılıyor; o yol izin gerektirmez,
 * uygulama hiçbir izin istemeye devam ediyor. Daha eski sürümlerde herkese
 * açık klasöre yazmak WRITE_EXTERNAL_STORAGE isterdi, o yüzden orada
 * uygulamanın kendi dış klasörüne yazılıyor ve tam yol bildiriliyor.
 *
 * Neden üst düzey bir sınıf ve neden Runnable'ı kendisi uyguluyor: bu depodaki
 * derleme zinciri Gradle kullanmıyor, dex'i doğrudan build-tools 34'ün d8'i
 * üretiyor ve o d8 buradaki JDK ile derlenen iç/anonim sınıflarda içeriden
 * çöküyor ("Cannot invoke String.length()"). Tek üst düzey sınıf + kendi
 * Runnable'ı olmak bu tuzağı hiç doğurmuyor.
 */
final class Saver implements Runnable {

    private final Activity act;
    /** Bildirilecek yer; JS iş parçacığında yazılıp arayüz parçacığında okunuyor. */
    private volatile String note = "";

    Saver(Activity act) {
        this.act = act;
    }

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
                Uri uri = act.getContentResolver().insert(
                        MediaStore.Downloads.EXTERNAL_CONTENT_URI, cv);
                if (uri == null) {
                    return false;
                }
                OutputStream out = act.getContentResolver().openOutputStream(uri);
                if (out == null) {
                    return false;
                }
                try {
                    out.write(data);
                } finally {
                    out.close();
                }
                note = name;
            } else {
                File dir = act.getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS);
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
                note = f.getAbsolutePath();
            }
            // @JavascriptInterface çağrıları arka planda geliyor; Toast arayüz
            // parçacığında gösterilmeli.
            act.runOnUiThread(this);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    @Override
    public void run() {
        Toast.makeText(act, note, Toast.LENGTH_LONG).show();
    }
}
