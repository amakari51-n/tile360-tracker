# Tile 360 Tracker

A web app to see all your Tile trackers on a map, with custom labels and notes.

---

## Deploy to Render (free, 5 minutes)

### Step 1 — Put the code on GitHub
1. Go to https://github.com/new and create a new **public** repository called `tile360-tracker`
2. Upload all these files (drag & drop onto the GitHub page):
   - `main.py`
   - `requirements.txt`
   - `render.yaml`
   - `static/index.html`

### Step 2 — Deploy on Render
1. Go to https://render.com and sign up (free)
2. Click **New → Web Service**
3. Connect your GitHub account and select the `tile360-tracker` repo
4. Render will auto-detect the `render.yaml` settings
5. Click **Deploy** — takes ~2 minutes
6. You'll get a URL like `https://tile360-tracker.onrender.com`

That URL works from any device, anywhere.

---

## Using the app

- Open the URL in any browser
- Sign in with your **Tile app email and password**
- All your Tiles appear on the map
- Click any Tile to add a custom label and notes
- Labels are saved in your browser's local storage
- Hit **Refresh** to pull latest locations

### Colour legend
- 🟢 Green dot = seen in the last hour
- 🟡 Amber dot = seen 1–24 hours ago  
- ⚫ Grey dot  = not seen in over 24 hours

---

## Important notes

- Tile has **no official public API**. This app uses the same unofficial API that the Tile app itself uses. It may stop working if Tile changes their API.
- Your credentials are only used to get a session token from Tile's servers. They are never logged or stored by this app.
- The free Render tier spins down after 15 minutes of inactivity — the first load after a sleep takes ~30 seconds.
