# Getting Started Checklist

Demonstrates a guide filed under a subfolder (`Guides/`) so you can see how
the portal groups files by directory.

## Before you begin

- [x] Clone or download this repository
- [x] Confirm Python 3 is installed (`python3 --version`)
- [ ] Run `generate_index.py` after adding your own notes
- [ ] Open `index.html` in a browser

## Folder conventions

Put related guides in a subfolder — like this one — and the sidebar groups
them together automatically. Files at the root of `md/` are listed above
any subfolders.

## Minimal example

```bash
cd md
mkdir "My Course"
mv my-notes.md "My Course/"
cd ..
python3 generate_index.py
```

Re-run the generator any time you add, remove, or rename files.
