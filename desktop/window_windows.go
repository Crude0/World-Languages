package main

import (
	"encoding/base64"
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	webview2 "github.com/jchv/go-webview2"
	"github.com/jchv/go-webview2/webviewloader"
	"golang.org/x/sys/windows"
)

// DPI farkındalığı: bildirilmezse Windows pencereyi 96 DPI'da çizip yukarı
// ölçekler, 2K/4K ekranlarda her şey bulanık görünür. Pencere açılmadan önce
// çağrılmalı; sürüme göre üç kademeli geri düşüş var.
func dpiAware() {
	user32 := windows.NewLazySystemDLL("user32.dll")
	if p := user32.NewProc("SetProcessDpiAwarenessContext"); p.Find() == nil {
		// DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = -4
		if r, _, _ := p.Call(^uintptr(3)); r != 0 {
			return
		}
	}
	shcore := windows.NewLazySystemDLL("shcore.dll")
	if p := shcore.NewProc("SetProcessDpiAwareness"); p.Find() == nil {
		if r, _, _ := p.Call(2); r == 0 { // PROCESS_PER_MONITOR_DPI_AWARE
			return
		}
	}
	if p := user32.NewProc("SetProcessDPIAware"); p.Find() == nil {
		p.Call()
	}
}

// scale pencere boyutunu ekranın ölçeğine göre büyütür: DPI farkındalığı
// açıkken ölçüler fiziksel piksel olur, yoksa pencere küçücük kalır.
func scale(v uint) uint {
	user32 := windows.NewLazySystemDLL("user32.dll")
	dpi := uintptr(96)
	if p := user32.NewProc("GetDpiForSystem"); p.Find() == nil {
		if r, _, _ := p.Call(); r >= 96 {
			dpi = r
		}
	}
	return v * uint(dpi) / 96
}

// bindSave sayfadan gelen baytları İndirilenler klasörüne yazar. WebView2'nin
// bir indirme işleyicisi yok: sayfadaki <a download> tıklaması sessizce
// yutuluyordu, yani dışa aktarma "İndirildi" yazıp hiçbir dosya bırakmıyordu.
// Sayfa köprüyü bulursa baytları base64 olarak buraya veriyor.
func bindSave(w webview2.WebView) {
	_ = w.Bind("atlasSaveFile", func(name, b64 string) (bool, error) {
		data, err := base64.StdEncoding.DecodeString(b64)
		if err != nil {
			return false, nil
		}
		// Ad sayfadan geliyor; hedef klasörün dışına çıkmasın.
		name = filepath.Base(strings.NewReplacer(`\`, "-", "/", "-", ":", "-").Replace(name))
		if name == "" || name == "." || name == ".." {
			return false, nil
		}
		home, err := os.UserHomeDir()
		if err != nil {
			return false, nil
		}
		dir := filepath.Join(home, "Downloads")
		if err := os.MkdirAll(dir, 0o755); err != nil {
			return false, nil
		}
		if err := os.WriteFile(filepath.Join(dir, name), data, 0o644); err != nil {
			return false, nil
		}
		return true, nil
	})
}

// showNative Windows'un kendi WebView2 bileşeniyle gerçek bir pencere açar.
// WebView2 çalışma zamanı yoksa (Windows 10 öncesi kurulumlar) hata döner ve
// çağıran taraf tarayıcı kipine düşer.
func showNative(htmlPath string) (err error) {
	v, e := webviewloader.GetInstalledVersion()
	if e != nil || v == "" {
		return errors.New("WebView2 çalışma zamanı bulunamadı")
	}
	defer func() {
		if r := recover(); r != nil {
			err = fmt.Errorf("webview2: %v", r)
		}
	}()

	data, e := dataDir()
	if e != nil {
		return e
	}
	dpiAware()
	w := webview2.NewWithOptions(webview2.WebViewOptions{
		AutoFocus: true,
		DataPath:  data,
		WindowOptions: webview2.WindowOptions{
			Title:  appName,
			Width:  scale(1280),
			Height: scale(820),
			IconId: 1, // kaynak dosyasındaki GROUP_ICON kimliği
			Center: true,
		},
	})
	if w == nil {
		return errors.New("pencere oluşturulamadı")
	}
	defer w.Destroy()
	bindSave(w) // Navigate'ten önce: Bind sayfa açılış betiğine yazılıyor
	w.Navigate(fileURL(htmlPath))
	w.Run()
	return nil
}
