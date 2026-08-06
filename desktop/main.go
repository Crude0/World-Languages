// Dünya Dilleri Atlası — yerel masaüstü başlatıcısı.
// Gömülü tek dosyalık haritayı kullanıcı klasörüne yazar ve tarayıcıda açar.
// İnternet bağlantısı gerektirmez, arka planda hiçbir şey çalışmaz.
package main

import (
	"crypto/sha256"
	_ "embed"
	"errors"
	"fmt"
	"net/url"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
)

//go:embed app.html
var page []byte

const (
	appName  = "Dünya Dilleri Atlası"
	dirName  = "DunyaDilleriAtlasi"
	fileName = "dunya-dilleri-atlasi.html"
)

func main() {
	path, err := writePage()
	if err != nil {
		alert(fmt.Sprintf("Harita dosyası yazılamadı.\n\n%v", err))
		os.Exit(1)
	}

	// Önce işletim sisteminin kendi pencere bileşeni (macOS: WKWebView,
	// Windows: WebView2). Başarısız olursa kurulu tarayıcıyı uygulama
	// kipinde açan eski yönteme düşülür.
	var nativeErr error
	if os.Getenv("DUNYA_TARAYICI") == "" {
		if nativeErr = showNative(path); nativeErr == nil {
			return
		}
	}
	if err := open(path); err != nil {
		msg := fmt.Sprintf("Harita açılamadı.\n\nDosyayı elle açabilirsiniz:\n%s\n\n%v", path, err)
		if nativeErr != nil {
			msg += fmt.Sprintf("\n\nYerleşik pencere: %v", nativeErr)
		}
		alert(msg)
		os.Exit(1)
	}
}

// writePage haritayı kalıcı bir kullanıcı klasörüne yazar; içerik aynıysa dokunmaz.
func writePage() (string, error) {
	dir, err := dataDir()
	if err != nil {
		return "", err
	}
	path := filepath.Join(dir, fileName)
	if old, err := os.ReadFile(path); err == nil && sha256.Sum256(old) == sha256.Sum256(page) {
		return path, nil
	}
	if err := os.MkdirAll(dir, 0o755); err != nil {
		return "", err
	}
	if err := os.WriteFile(path, page, 0o644); err != nil {
		// ev dizini yazılamıyorsa geçici klasöre düş
		alt := filepath.Join(os.TempDir(), dirName)
		if e := os.MkdirAll(alt, 0o755); e != nil {
			return "", err
		}
		path = filepath.Join(alt, fileName)
		if e := os.WriteFile(path, page, 0o644); e != nil {
			return "", err
		}
	}
	return path, nil
}

func dataDir() (string, error) {
	switch runtime.GOOS {
	case "darwin":
		home, err := os.UserHomeDir()
		if err != nil {
			return "", err
		}
		return filepath.Join(home, "Library", "Application Support", dirName), nil
	case "windows":
		if base := os.Getenv("LOCALAPPDATA"); base != "" {
			return filepath.Join(base, dirName), nil
		}
		return filepath.Join(os.TempDir(), dirName), nil
	default:
		base, err := os.UserCacheDir()
		if err != nil {
			return "", err
		}
		return filepath.Join(base, dirName), nil
	}
}

// fileURL yolun doğru kaçışlanmış file:// adresini üretir.
func fileURL(path string) string {
	p := filepath.ToSlash(path)
	if runtime.GOOS == "windows" {
		p = "/" + p
	}
	u := url.URL{Scheme: "file", Path: p}
	return u.String()
}

// open önce Chromium tabanlı bir tarayıcıyı uygulama penceresi kipinde dener,
// bulunamazsa sistemin varsayılan tarayıcısına devreder.
func open(path string) error {
	target := fileURL(path)
	for _, bin := range appModeBrowsers() {
		if _, err := os.Stat(bin); err != nil {
			continue
		}
		cmd := exec.Command(bin, "--app="+target, "--window-size=1440,940")
		if err := cmd.Start(); err == nil {
			go cmd.Wait()
			return nil
		}
	}
	return openDefault(path, target)
}

func appModeBrowsers() []string {
	switch runtime.GOOS {
	case "darwin":
		home, _ := os.UserHomeDir()
		names := []string{
			"Google Chrome.app/Contents/MacOS/Google Chrome",
			"Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
			"Brave Browser.app/Contents/MacOS/Brave Browser",
			"Vivaldi.app/Contents/MacOS/Vivaldi",
			"Chromium.app/Contents/MacOS/Chromium",
		}
		var out []string
		for _, n := range names {
			out = append(out, filepath.Join("/Applications", n))
			if home != "" {
				out = append(out, filepath.Join(home, "Applications", n))
			}
		}
		return out
	case "windows":
		names := []struct{ env, rel string }{
			{"ProgramFiles", `Microsoft\Edge\Application\msedge.exe`},
			{"ProgramFiles(x86)", `Microsoft\Edge\Application\msedge.exe`},
			{"ProgramFiles", `Google\Chrome\Application\chrome.exe`},
			{"ProgramFiles(x86)", `Google\Chrome\Application\chrome.exe`},
			{"LOCALAPPDATA", `Google\Chrome\Application\chrome.exe`},
			{"ProgramFiles", `BraveSoftware\Brave-Browser\Application\brave.exe`},
		}
		var out []string
		for _, n := range names {
			if base := os.Getenv(n.env); base != "" {
				out = append(out, filepath.Join(base, n.rel))
			}
		}
		return out
	}
	return nil
}

func openDefault(path, target string) error {
	switch runtime.GOOS {
	case "darwin":
		return exec.Command("/usr/bin/open", path).Run()
	case "windows":
		return exec.Command("rundll32.exe", "url.dll,FileProtocolHandler", target).Start()
	default:
		if _, err := exec.LookPath("xdg-open"); err == nil {
			return exec.Command("xdg-open", target).Start()
		}
		return errors.New("uygun bir tarayıcı bulunamadı")
	}
}
