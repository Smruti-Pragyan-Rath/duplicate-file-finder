# 🔍 Duplicate File Finder

A simple web app that scans a folder and finds duplicate files — even if they've been renamed — by comparing file size first, then verifying with a SHA-256 hash.

**🔗 Live demo:** https://duplicate-file-finder-my7ayjcnekkssyq57znagz.streamlit.app/
![screenshot](screenshot.png)

## How it works

1. Upload a folder through the browser.
2. Files are first grouped by **size** — files with a unique size can't have duplicates, so they're dropped immediately (this keeps things fast).
3. Remaining files are hashed using **SHA-256**, a cryptographic hash that produces an identical output only if two files have identical content.
4. Files with matching hashes are grouped and shown as confirmed duplicates.

This two-step approach (size check → hash check) avoids hashing every single file, which matters a lot on large folders.

## Tech stack

- **Python** — core logic (`os`, `hashlib`)
- **Streamlit** — web interface
- Deployed on **Streamlit Community Cloud**

## Run it locally

```bash
git clone https://github.com/your-username/duplicate-file-finder.git
cd duplicate-file-finder
pip install -r requirements.txt
streamlit run streamlit_app_upload.py
```

## Project structure

```
duplicate-file-finder/
├── streamlit_app_upload.py   # main app
├── requirements.txt          # dependencies
└── README.md
```

## Possible improvements

- Option to auto-delete or move duplicates
- Progress bar for large folders
- Support for comparing images by visual similarity, not just exact byte match

## Author

Your Name — Smruti Pragyan Rath 
