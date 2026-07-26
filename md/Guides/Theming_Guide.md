# Theming Guide

A second subfolder (`Guides/`) entry, so the sidebar has more than one item
grouped under "Guides".

## Switching themes

Use the theme selector in the header. Available themes ship as separate
CSS files in `css/`:

- `theme-dark.css` — default dark theme
- `theme-light-blue.css` / `theme-light-red.css`
- `theme-dracula.css`, `theme-alucard.css`
- `theme-nord-dark.css`, `theme-nord-blue.css`, `theme-nord-red.css`
- `theme-solarized-dark.css`, `theme-solarized-light.css`
- `theme-terminal.css`
- `theme-hackthebox.css`

## Adding your own theme

1. Copy an existing `theme-*.css` file in `css/` as a starting point
2. Update the CSS variables for colours, fonts and syntax highlighting
3. Add an `<option>` for it in `index.html`'s theme selector

```css
:root[data-theme="my-theme"] {
  --bg: #0d1117;
  --fg: #c9d1d9;
  --accent: #58a6ff;
}
```

Re-run nothing — theme CSS is picked up automatically from `css/` once
referenced in the selector.
