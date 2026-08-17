<!-- title: The save bridge, now measured on a real Mac -->
**PNG and SVG still saved nothing in the macOS app.** The bridge added in
0.12.0 works when it installs and says nothing when it does not: the setup sat
inside a `try/catch` that swallowed the error, and the page — finding no bridge
— fell back to `<a download>` and reported "Saved", even though that path does
nothing at all inside a WKWebView. The failure was silent twice over.

Three things changed:

- **The page no longer lies.** It now checks whether it is running inside an app
  shell (`window.webkit.messageHandlers` in WKWebView, `window.chrome.webview`
  in WebView2, `; wv)` in the Android WebView's user agent) and, with no bridge
  present, the button reads "This build cannot save". Nothing changed in a real
  browser: the download happens and the button says "Saved".
- **The bridge's error is no longer swallowed.** Its install status is kept as a
  string, and the writing itself was split into a separate function.
- **It is measured on a real Mac.** The script's check mode — the one the
  release workflow already runs on a macOS runner to verify the About panel —
  now also reports that the bridge installed *and* that the write path to
  Downloads works, by writing a small file, confirming it exists and deleting
  it. If either fails, the release does not go out at all. This bridge was
  written without a Mac to hand, so this was the only honest way to know.

The `protocols` declaration was also dropped from the subclass registration:
WebKit calls the method directly, so declaring conformance adds nothing, but on
some JXA versions it takes the whole registration down with it — the most
likely reason the bridge was quietly failing to install.
