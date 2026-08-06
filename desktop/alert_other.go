//go:build !darwin && !windows

package main

import (
	"fmt"
	"os"
)

func alert(msg string) { fmt.Fprintln(os.Stderr, appName+": "+msg) }
