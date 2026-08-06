package main

import (
	"errors"
	"fmt"

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
	w.Navigate(fileURL(htmlPath))
	w.Run()
	return nil
}
