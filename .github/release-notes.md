<!-- title: The walkthrough gets a permanent door -->
**The walkthrough can now be opened at any time: View → Walkthrough.** The
first-visit bubble appears once and only when no languages have been picked —
so anyone already using the app never saw it. On the desktop app this is even
sharper: `localStorage` is tied to the bundle, so replacing the .app keeps the
old state, and an existing user installing the new version never meets the
bubble at all. The walkthrough is always reachable now; started from
fullscreen it returns to windowed mode first, because two of the things it
points at live in the left column.

**When the walkthrough ends it keeps pointing.** After "Try it" a soft
two-stop highlight follows: first the language picker, then — once the first
language is ticked — the fullscreen button. The dimming is light and the
overlay lets clicks through, so the highlighted thing can actually be pressed.
A ring pulses around it with a one-line caption, and it lifts by itself once
the target is used or the time is up.

**The light around the bubble was invisible in the dark theme.** Its background
was `--ink`, which turns white in the dark theme — a white bubble under a white
light. The bubble carries its own colours now and stays dark in both themes.
The light itself got stronger too: a wider arc with a halo breathing on the
same beat. Measured — in the light theme the edge sits at 65 and the light
peaks at 252; in the dark theme 81 → 199, and the peak travels from the top
edge to the right, then to the bottom.

**Hovering the bubble brings up a holographic surface.** A glare under the
pointer, foil bands whose angle turns with it, and star dust over them — the
three drift at three different rates, and that difference is what reads as
depth. The bubble also leans a few degrees toward the pointer. All of it is
confined to a mask that follows the cursor: in the first attempt the foil
covered the whole box and its tiling seams showed, now it is a patch that
travels.
