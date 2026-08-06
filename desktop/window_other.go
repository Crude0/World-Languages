//go:build !darwin && !windows

package main

import "errors"

func showNative(string) error {
	return errors.New("bu platformda yerleşik pencere yok")
}
