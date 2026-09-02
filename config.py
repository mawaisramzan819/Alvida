"""
=============================================================================
CONFIGURATION — A Farewell That Stays (Exact Reference UI)
Deep Midnight Purple/Navy + Warm Rose-Coral + Peach Cream Cards
=============================================================================
"""

from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
MUSIC_DIR = ASSETS_DIR / "music"
IMAGES_DIR = ASSETS_DIR / "images"
CSS_DIR = ASSETS_DIR / "css"

# Application Metadata
APP_TITLE = "A Farewell That Stays"
APP_ICON = "💗"
PAGE_LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Visual Theme Tokens (Sampled from Reference Mockup)
THEME = {
    "bg_deep": "#0e101a",
    "bg_navy": "#141324",
    "bg_surface": "#1b172a",
    "bg_sidebar": "#161324",
    "bg_card_light": "#fbf5f2",
    "bg_card_dark": "#161a2e",
    "border_subtle": "rgba(255, 180, 180, 0.12)",
    "border_rose": "rgba(229, 115, 115, 0.35)",
    "accent_rose": "#e26a6a",
    "accent_coral": "#ff8a80",
    "accent_blush": "#fce4ec",
    "accent_gold": "#f59e0b",
    "text_primary": "#ffffff",
    "text_secondary": "#cbd5e1",
    "text_muted": "#baa9b4",
    "text_dark_card": "#2d1f23",
    "text_dark_card_desc": "#635156",
}

# Typography Google Fonts
GOOGLE_FONTS = [
    "https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=Amiri:ital,wght@0,400;0,700;1,400&display=swap"
]

# Audio Settings
AUDIO_CONFIG = {
    "filename": "farewell.mp3",
    "song_title": "A Song for the Journey",
    "song_artist": "Safarnama – Lucky Ali",
    "enable_audio": True,
}

# Personalization Settings
SETTINGS = {
    "show_sender_name": False,
    "show_recipient_name": True,
    "enable_ambient_particles": True,
}

# Navigation Chapters (Exact 8 Chapters from Reference UI)
CHAPTERS = [
    {"id": "home",       "label": "Home",               "icon": "🏠", "num": 0},
    {"id": "welcome",    "label": "Welcome",            "icon": "♡",  "num": 1},
    {"id": "memories",   "label": "Memories",           "icon": "🖼️", "num": 2},
    {"id": "words",      "label": "Words from My Heart","icon": "🪶", "num": 3},
    {"id": "respect",    "label": "Why I Respect You",  "icon": "⭐", "num": 4},
    {"id": "intentions", "label": "Intentions",         "icon": "💝", "num": 5},
    {"id": "dua",        "label": "Dua",                "icon": "🤲", "num": 6},
    {"id": "goodbye",    "label": "Final Note",         "icon": "✉️", "num": 7},
]

# Story chapters excluding home
TOTAL_STORY_CHAPTERS = 7
