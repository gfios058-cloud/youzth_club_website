# YOUZTH CLUB

A single-page Streamlit landing website for YOUZTH CLUB.

## Run locally

```powershell
pip install -r requirements.txt
streamlit run app.py
```

If the `streamlit` command is not on your PATH, use `python -m streamlit run app.py`.

Applications are saved to `data/applications.sqlite3` on the machine running the app. The `data/` directory is ignored by Git because it contains applicant details. The storage function is in `applications.py`, so a hosted database or another delivery service can replace the local SQLite implementation later.

The introduction video is embedded from YouTube and needs a visitor's browser to have access to YouTube.
