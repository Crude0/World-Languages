#!/usr/bin/env bash
# APK derleme: aapt2 -> javac -> d8 -> zipalign -> apksigner
# Gradle/AGP kullanılmıyor; ek bağımlılık indirilmiyor.
set -euo pipefail

SDK=${ANDROID_HOME:-/opt/android-sdk}
BT="$SDK/build-tools/34.0.0"
PLATFORM="$SDK/platforms/android-34/android.jar"
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/build"
NAME="Dunya-Dilleri-Atlasi"

rm -rf "$OUT"
mkdir -p "$OUT/res" "$OUT/gen" "$OUT/classes" "$OUT/dex"

echo "· telefon arayüzü üretiliyor"
python3 "$HERE/../build_mobile.py" >/dev/null

echo "· kaynaklar derleniyor (aapt2 compile)"
"$BT/aapt2" compile --dir "$HERE/res" -o "$OUT/res.zip"

echo "· paket bağlanıyor (aapt2 link)"
"$BT/aapt2" link \
  -o "$OUT/base.apk" \
  -I "$PLATFORM" \
  --manifest "$HERE/AndroidManifest.xml" \
  -R "$OUT/res.zip" \
  -A "$HERE/assets" \
  --java "$OUT/gen" \
  --min-sdk-version 24 \
  --target-sdk-version 34 \
  --auto-add-overlay

echo "· java derleniyor"
javac -nowarn -source 17 -target 17 -encoding UTF-8 \
  -classpath "$PLATFORM" \
  -d "$OUT/classes" \
  $(find "$HERE/src" "$OUT/gen" -name '*.java')

echo "· dex üretiliyor"
"$BT/d8" --lib "$PLATFORM" --min-api 24 --release \
  --output "$OUT/dex" $(find "$OUT/classes" -name '*.class')

echo "· dex pakete ekleniyor"
cp "$OUT/base.apk" "$OUT/unsigned.apk"
(cd "$OUT/dex" && zip -q -X "$OUT/unsigned.apk" classes.dex)

echo "· hizalama"
"$BT/zipalign" -p -f 4 "$OUT/unsigned.apk" "$OUT/aligned.apk"

echo "· imzalama"
KS="$HERE/atlas.keystore"
if [ ! -f "$KS" ]; then
  keytool -genkeypair -v -keystore "$KS" -alias atlas \
    -keyalg RSA -keysize 2048 -validity 10000 \
    -storepass atlas123 -keypass atlas123 \
    -dname "CN=Dunya Dilleri Atlasi, OU=Acik veri, O=Atlas, L=Istanbul, C=TR" >/dev/null 2>&1
fi
"$BT/apksigner" sign --ks "$KS" --ks-key-alias atlas \
  --ks-pass pass:atlas123 --key-pass pass:atlas123 \
  --v1-signing-enabled true --v2-signing-enabled true --v3-signing-enabled true \
  --out "$HERE/../desktop/dist/$NAME.apk" "$OUT/aligned.apk"

"$BT/apksigner" verify --print-certs "$HERE/../desktop/dist/$NAME.apk" | head -4
ls -la "$HERE/../desktop/dist/$NAME.apk"
