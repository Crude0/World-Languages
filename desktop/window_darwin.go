package main

import (
	"bytes"
	_ "embed"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"time"
)

//go:embed atlas.jxa
var jxa []byte

// showNative macOS'un kendi WebKit'iyle gerçek bir uygulama penceresi açar.
// Pencere ayakta kaldığı sürece bu çağrı bloke olur; açılamazsa hata döner ve
// çağıran taraf tarayıcı kipine düşer.
func showNative(htmlPath string) error {
	if _, err := os.Stat("/usr/bin/osascript"); err != nil {
		return err
	}
	script := filepath.Join(filepath.Dir(htmlPath), "pencere.js")
	if err := os.WriteFile(script, jxa, 0o644); err != nil {
		return err
	}

	// Betik argümanları sırayla: html, ikon, sürüm. Sürüm Hakkında
	// panelinde görünüyor; ikon bulunamazsa yeri boş geçilir.
	args := []string{"-l", "JavaScript", script, htmlPath, iconPath(), version}
	cmd := exec.Command("/usr/bin/osascript", args...)
	var stderr bytes.Buffer
	cmd.Stderr = &stderr
	if err := cmd.Start(); err != nil {
		return err
	}

	done := make(chan error, 1)
	go func() { done <- cmd.Wait() }()

	// İlk saniyelerde ölürse pencere hiç açılmamıştır: tarayıcıya düşelim.
	select {
	case err := <-done:
		if err != nil {
			msg := strings.TrimSpace(stderr.String())
			if msg == "" {
				return err
			}
			return fmt.Errorf("%v: %s", err, msg)
		}
		return nil
	case <-time.After(2500 * time.Millisecond):
	}
	<-done // pencere açıldı; kullanıcı kapatana kadar bekle
	return nil
}

// iconPath paket içindeki .icns dosyasını bulur (Contents/MacOS -> Contents/Resources).
func iconPath() string {
	exe, err := os.Executable()
	if err != nil {
		return ""
	}
	p := filepath.Join(filepath.Dir(exe), "..", "Resources", "AppIcon.icns")
	if _, err := os.Stat(p); err != nil {
		return ""
	}
	abs, err := filepath.Abs(p)
	if err != nil {
		return ""
	}
	return abs
}
