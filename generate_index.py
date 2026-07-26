#!/usr/bin/env python3
"""
Generate md/index.json — recursive scan of all .md files.

Run from the folder containing index.html:
    python3 generate_index.py

Output format — array of objects with path and optional tag:
    [
      { "path": "CCSP_Revision_Guide_v5.md",          "tag": "(ISC)²" },
      { "path": "Certifications/CISSP_v12.md",         "tag": "(ISC)²" },
      { "path": "Reference/Defense_in_Depth.md",       "tag": "" }
    ]

After generating, edit md/index.json to set the "tag" field for each file.
Tags appear as small badges on the index page. Leave blank for no badge.

Root-level files are listed before subfolders. Sort order is natural
(numbers compared numerically, so v2 < v10).
"""
import os
import json
import re

MD_DIR   = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'md')
OUT_FILE = os.path.join(MD_DIR, 'index.json')


def natural_key(s):
    """Sort key: split on digit runs so '10' sorts after '9', case-insensitive."""
    parts = re.split(r'(\d+)', s.lower())
    return [int(p) if p.isdigit() else p for p in parts]


def collect():
    root_files = []
    sub_files  = {}   # folder_rel_path → [file_rel_paths]

    for dirpath, dirnames, filenames in os.walk(MD_DIR):
        dirnames[:] = sorted(
            (d for d in dirnames if not d.startswith('.')),
            key=natural_key
        )
        for fname in filenames:
            if not fname.endswith('.md'):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fname), MD_DIR)
            rel = rel.replace(os.sep, '/')
            if rel.startswith('.'):
                continue
            if '/' in rel:
                folder = rel.rsplit('/', 1)[0]
                sub_files.setdefault(folder, []).append(rel)
            else:
                root_files.append(rel)

    root_files.sort(key=lambda f: natural_key(f))
    result = []
    for path in root_files:
        result.append({ "path": path, "tag": "" })

    for folder in sorted(sub_files.keys(), key=natural_key):
        sub_files[folder].sort(key=lambda f: natural_key(f.split('/')[-1]))
        for path in sub_files[folder]:
            result.append({ "path": path, "tag": "" })

    return result


def merge_existing(new_entries):
    """Preserve any tags already set in the existing index.json."""
    if not os.path.exists(OUT_FILE):
        return new_entries
    try:
        with open(OUT_FILE, 'r', encoding='utf-8') as fp:
            existing = json.load(fp)
        # Build a lookup of path → tag from existing entries
        existing_tags = {}
        for entry in existing:
            if isinstance(entry, dict) and entry.get('path'):
                existing_tags[entry['path']] = entry.get('tag', '')
            elif isinstance(entry, str):
                existing_tags[entry] = ''
        # Apply preserved tags to new entries
        for entry in new_entries:
            if entry['path'] in existing_tags:
                entry['tag'] = existing_tags[entry['path']]
    except Exception:
        pass  # If anything goes wrong, just use the new entries as-is
    return new_entries


if __name__ == '__main__':
    entries = collect()
    entries = merge_existing(entries)

    with open(OUT_FILE, 'w', encoding='utf-8') as fp:
        json.dump(entries, fp, indent=2, ensure_ascii=False)

    print(f'Written {len(entries)} file(s) to {OUT_FILE}')
    print('Edit the "tag" field for each entry to set the badge label.')
    for e in entries:
        tag_display = f'  [{e["tag"]}]' if e['tag'] else ''
        print(f'  {e["path"]}{tag_display}')


