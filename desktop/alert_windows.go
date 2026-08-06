package main

import (
	"syscall"
	"unsafe"
)

// alert Windows'ta yerel bir MessageBox gösterir (konsol penceresi yok).
func alert(msg string) {
	box := syscall.NewLazyDLL("user32.dll").NewProc("MessageBoxW")
	text, err := syscall.UTF16PtrFromString(msg)
	if err != nil {
		return
	}
	title, err := syscall.UTF16PtrFromString(appName)
	if err != nil {
		return
	}
	const mbIconError = 0x00000010
	box.Call(0, uintptr(unsafe.Pointer(text)), uintptr(unsafe.Pointer(title)), mbIconError)
}
