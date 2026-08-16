A follow-up to 0.9.0, fixing one thing that release introduced.

When the table is open the map area is hidden, and so is the full-screen
button. But the macOS menu item **Map Only (⇧⌘F)**, added in 0.9.0, presses that
button directly — so going full screen from the menu while the table was open
filled the screen with an empty ocean. Full screen now always closes the table
first.

Resizing the window also re-rendered the map and rewrote the address bar for no
reason. That work is only needed in full screen, where the wrapper's size is set
from script rather than by layout.

Everything else is as described in [0.9.0](https://github.com/Crude0/World-Languages/releases/tag/v0.9.0):
the desktop controls moved onto the map, there is a full-screen mode, and the
**I speak** layer has a new colour scale and tooltip.
