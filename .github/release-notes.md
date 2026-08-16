**If you opened the web version after 0.9.0 and saw the old interface, this is
why.** The service worker served the page from its cache first and refreshed the
network copy in the background, so a newly released version only appeared on the
*second* reload. Measured on a test site: caching an old page, replacing the file
on the server, then reloading — the new version arrived on reload **2**.

Page requests now go to the network first and fall back to the cache when the
network is unavailable. Same measurement: reload **1**. With the server fully
down the page still opens, so offline use is unaffected. Icons and the manifest,
which do not change between versions, are still served from the cache first.

If you are still seeing the old interface right now, one reload will fix it — or
one more if the previous worker is still in control.

Everything else is as described in
[0.9.0](https://github.com/Crude0/World-Languages/releases/tag/v0.9.0).
