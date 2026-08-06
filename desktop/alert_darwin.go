package main

import (
	"os/exec"
	"strings"
)

// alert macOS'ta yerel bir uyarı penceresi gösterir.
func alert(msg string) {
	script := `display dialog "` + strings.NewReplacer(`\`, `\\`, `"`, `\"`).Replace(msg) +
		`" with title "` + appName + `" buttons {"Tamam"} default button 1 with icon stop`
	_ = exec.Command("/usr/bin/osascript", "-e", script).Run()
}
