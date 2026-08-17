<!-- title: One list, not two -->
**"I speak" was showing the same thing twice.** The languages you had picked
appeared both as a row of removable chips and as blue, checkmarked rows in the
list below — two representations of one piece of state, taking up room for
nothing. The chip row is gone; the checkmarked row in the list already both
shows the selection and removes it when tapped.

Removing it exposed a case where your picks could have become unreachable:
searching for a language filtered them out of the list. Your selected languages
are now pinned to the top of the list regardless of the search. The same
duplication existed in the desktop "My languages" sheet, and is gone there too.

Two small fixes alongside it:

- The three figures on the phone use a compact form. "1.7 billion" did not fit
  a row of three boxes and wrapped onto two lines; it now reads "1.7B".
- The search field had **two clear buttons** side by side: ours, and the one the
  browser draws by itself for `type="search"`. The browser's is now hidden —
  ours is sized for a fingertip and clears the filter as well.
