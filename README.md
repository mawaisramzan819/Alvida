# 🕊️ A Farewell & A Sincere Dua — Streamlit Web App

A peaceful, elegant, emotionally mature digital farewell web application. Designed as a private digital farewell letter for someone special getting married soon — centered on gratitude, acceptance, respect, and sincere prayers (*dua*).

---

## 🌟 Visual & Emotional Design Highlights

* **Atmospheric Theme:** Deep obsidian / charcoal backdrop with warm champagne gold accents (`#C5A880`).
* **Glassmorphism:** Frosted translucent cards with subtle hairline borders, soft glow effects, and gentle hover transitions.
* **Urdu Typography & RTL:** Beautiful, legible Urdu script using `Noto Nastaliq Urdu` and `Amiri` fonts with right-to-left layout.
* **100% Respectful & Mature Tone:** Zero guilt-tripping, manipulation, or pressure. Every section reflects gratitude, emotional closure, and pure goodwill.
* **Centralized Configuration:** Edit the entire letter, memories, wishes, and names from a single file (`content.py`).
* **Background Music Support:** Built-in audio controller that seamlessly supports any local `.mp3`, `.wav`, or `.ogg` file.
* **High Privacy:** No database, no tracking, no external analytics, and no telemetry.

---

## 📁 Project Structure

```text
farewell_app/
│
├── app.py                  # Main Streamlit application & layout controller
├── config.py               # Visual theme, audio settings, and feature flags
├── content.py              # ALL customizable text, memories, duas, and placeholders
├── requirements.txt        # Minimal dependencies (streamlit)
├── README.md               # Complete documentation and customization guide
├── .gitignore              # Git ignore rules
│
└── assets/
    ├── css/
    │   └── style.css       # Custom responsive CSS, glassmorphism, & typography
    ├── images/             # Directory for optional personal photos/images
    └── music/              # Directory for your background music file (e.g. farewell.mp3)
```

---

## 🚀 Quick Start (Running Locally)

### 1. Prerequisites
Ensure you have Python 3.9+ installed.

### 2. Navigate to the project directory
```bash
cd farewell_app
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application
```bash
streamlit run app.py
```
The application will automatically open in your default browser at `http://localhost:8501`.

---

## ✍️ How to Personalize the Content

All text is organized in [`content.py`](content.py). You never have to touch the UI code to customize the words.

### 1. Change Names and Placeholders
Open `content.py` and modify:
```python
RECIPIENT_NAME = "Her Name"   # Her name (displayed in greeting)
SENDER_NAME = "Your Name"     # Your name (only shown if configured in config.py)
```

### 2. Customize the Memories (Section 3)
In `content.py`, locate the `MEMORIES_SECTION` dictionary and replace the placeholder text in each card:
```python
{
    "id": 1,
    "category": "Your Smile",
    "icon": "✨",
    "placeholder": "Write your personal memory here...",
    "reflection": "May the brightness of your smile never fade.",
}
```

### 3. Customize Wishes, Duas, and Messages
You can customize:
* `OPENING_SECTION`: Hero screen text and button label.
* `MESSAGE_SECTION`: Heartfelt paragraphs for the main letter.
* `WISHES_SECTION`: The 6 blessing cards (Peace, Happiness, Respect, Love, Success, Future).
* `DUA_SECTION`: Urdu script and English translation of the main prayer.
* `FUTURE_SECTION`: Words dedicated to her future self.
* `THANK_YOU_SECTION`: Gratitude quotes and lines.
* `GOODBYE_SECTION`: Parting words and the interactive "One Last Dua" prayer.

---

## 🎵 Adding Background Music

1. Choose any relaxing instrumental, piano, or ambient audio track (`.mp3`, `.wav`, or `.ogg`).
2. Place the audio file inside `assets/music/` and name it `farewell.mp3` (or configure your filename in `config.py` under `AUDIO_CONFIG["filename"]`).
3. When the app is launched and the farewell is opened, an audio player will appear at the top allowing the recipient to play background music.
4. *If no music file is present, the app runs gracefully without errors and hides the audio section.*

---

## ⚙️ Visual Theme & Settings (`config.py`)

In [`config.py`](config.py), you can toggle features:

```python
SETTINGS = {
    # Set to True to display sender signature at the end, False for respectful anonymous closing
    "show_sender_name": False,
    # Set to True to display recipient name in headings
    "show_recipient_name": True,
    # Enable subtle floating ambient glow in background
    "enable_ambient_particles": True,
}
```

---

## 📱 Mobile & Tablet Responsiveness

The styling in `assets/css/style.css` includes custom media queries that adapt automatically to:
* Desktop screens (wide elegant layout)
* Tablets (balanced 2-column memory cards)
* Mobile phones (single-column cards, touch-friendly buttons, and comfortable Urdu line-heights)

---

## 🔒 Privacy & Safety Guarantee

This project is built as a private personal keepsake:
* **No databases:** Zero storage of user data.
* **No analytics:** No Google Analytics, Mixpanel, or third-party beacons.
* **Self-contained:** Can run completely offline on your local machine.
