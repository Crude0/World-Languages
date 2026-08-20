# Dünya Dilleri Atlası — derleme
SHELL := /bin/bash
PY    := python3

VER := $(shell tr -d '[:space:]' < VERSION)

.PHONY: all data web desktop android check clean publish dist-check

all: web

## veri: sınırlar + dil katmanları -> data.json
data:
	$(PY) src/build_map.py
	$(PY) src/build_subs.py
	$(PY) src/build_data.py

## web: tek dosyalık sayfa (docs/index.html ve docs/mobile.html)
web: data
	$(PY) src/build_page.py
	$(PY) src/build_mobile.py
	@mkdir -p docs
	@cp preview.html docs/index.html
	@cp mobile-preview.html docs/mobile.html
	$(PY) src/pwa.py
	@echo "hazır: docs/index.html"

## desktop: macOS .app + .dmg, Windows .exe  (Go 1.21+ gerekir)
desktop: web
	cd desktop && CGO_ENABLED=0 GOOS=darwin  GOARCH=arm64 go build -ldflags "-s -w -X main.version=$(VER)" -o out/mac-arm64 .
	cd desktop && CGO_ENABLED=0 GOOS=darwin  GOARCH=amd64 go build -ldflags "-s -w -X main.version=$(VER)" -o out/mac-amd64 .
	cd desktop && CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -ldflags "-s -w -H windowsgui -X main.version=$(VER)" -o out/win-amd64.exe .
	cd desktop && $(PY) package.py
	$(MAKE) publish

## publish: paketleri depodaki dist/ klasörüne taşır.
## Yayım iş akışı dist/ içindekileri yüklüyor; package.py ise desktop/dist/
## altına yazıyor ve orası .gitignore'da. Aradaki kopyalama eksikti, bu yüzden
## 0.9.0–0.9.2 sürümleri 0.8.0 ikililerini yayımladı. Artık derlemenin parçası.
.PHONY: publish
publish:
	@mkdir -p dist
	@cp -p "desktop/dist/Dunya-Dilleri-Atlasi-mac.zip" dist/ 2>/dev/null || true
	@cp -p "desktop/dist/Dunya-Dilleri-Atlasi.dmg"     dist/ 2>/dev/null || true
	@cp -p "desktop/dist/Dunya Dilleri Atlasi.exe"     dist/ 2>/dev/null || true
	@cp -p "desktop/dist/Dunya-Dilleri-Atlasi.apk"     dist/ 2>/dev/null || true
	@$(PY) tools/check-dist.py

## android: imzalı APK  (Android SDK build-tools 34 + JDK 17 gerekir)
android: data
	./android/build.sh
	$(MAKE) publish

## dist: paketlerin bu sürümle tutarlı olduğunu doğrular
.PHONY: dist-check
dist-check:
	$(PY) tools/check-dist.py

## shots: README görselleri ve düğmeleri  (npm i playwright)
## Kareler elle alındığı sürece bayatlıyordu: 0.22 yayımlandığında README
## hâlâ 0.16'nın arayüzünü gösteriyordu. Artık sürümle birlikte tazeleniyor.
.PHONY: shots
shots: web
	node tools/shots.mjs
	$(PY) tools/make_buttons.py

## check: Playwright ile arayüz denetimi  (npm i playwright)
check: web
	cd tools && node check-desktop.mjs
	cd tools && node check-mobile.mjs

clean:
	rm -f map_paths.json sub_paths.json data.json dunya-dilleri.html \
	      preview.html mobile-preview.html desktop/app.html
	rm -rf desktop/out desktop/dist desktop/dmgroot android/build android/assets __pycache__
