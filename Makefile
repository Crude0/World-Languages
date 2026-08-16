# Dünya Dilleri Atlası — derleme
SHELL := /bin/bash
PY    := python3

VER := $(shell tr -d '[:space:]' < VERSION)

.PHONY: all data web desktop android check clean

all: web

## veri: sınırlar + dil katmanları -> data.json
data:
	$(PY) build_map.py
	$(PY) build_subs.py
	$(PY) build_data.py

## web: tek dosyalık sayfa (docs/index.html ve docs/mobile.html)
web: data
	$(PY) build_page.py
	$(PY) build_mobile.py
	@mkdir -p docs
	@cp preview.html docs/index.html
	@cp mobile-preview.html docs/mobile.html
	$(PY) pwa.py
	@echo "hazır: docs/index.html"

## desktop: macOS .app + .dmg, Windows .exe  (Go 1.21+ gerekir)
desktop: web
	cd desktop && CGO_ENABLED=0 GOOS=darwin  GOARCH=arm64 go build -ldflags "-s -w -X main.version=$(VER)" -o out/mac-arm64 .
	cd desktop && CGO_ENABLED=0 GOOS=darwin  GOARCH=amd64 go build -ldflags "-s -w -X main.version=$(VER)" -o out/mac-amd64 .
	cd desktop && CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -ldflags "-s -w -H windowsgui -X main.version=$(VER)" -o out/win-amd64.exe .
	cd desktop && $(PY) package.py

## android: imzalı APK  (Android SDK build-tools 34 + JDK 17 gerekir)
android: data
	./android/build.sh

## check: Playwright ile arayüz denetimi  (npm i playwright)
check: web
	cd tools && node check-desktop.mjs
	cd tools && node check-mobile.mjs

clean:
	rm -f map_paths.json sub_paths.json data.json dunya-dilleri.html \
	      preview.html mobile-preview.html desktop/app.html
	rm -rf desktop/out desktop/dist desktop/dmgroot android/build android/assets __pycache__
