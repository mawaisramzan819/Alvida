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

# Visual Theme Tokens — Locked "Romantic Midnight Editorial" Design System
THEME = {
    "bg_deep": "#090D1B",
    "bg_sidebar": "#101428",
    "surface_dark": "#18172B",
    "surface_dark_2": "#242036",
    "surface_light": "#F8EDE4",
    "surface_light_soft": "#F3E2DA",
    "accent_primary": "#E96582",
    "accent_primary_hover": "#F07D92",
    "accent_soft": "#F39AA7",
    "accent_peach": "#F5B18F",
    "accent_gold": "#EAB378",
    "text_primary_dark_bg": "#FFF4ED",
    "text_secondary_dark_bg": "#C9B7B5",
    "text_primary_light_bg": "#302436",
    "text_secondary_light_bg": "#725E67",
    "border_dark": "rgba(235,151,155,.22)",
    "border_light": "#E7C9C2",
}

# Typography Google Fonts (Cormorant Garamond, Allura, Inter)
GOOGLE_FONTS = [
    "https://fonts.googleapis.com/css2?family=Allura&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Great+Vibes&family=Inter:wght@400;500;600;700&display=swap"
]

# Audio Settings
AUDIO_CONFIG = {
    "filename": "farewell.mp3",
    "song_title": "A Song for the Journey",
    "song_artist": "Safarnama — Lucky Ali",
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
    {"id": "home",       "label": "Home",                 "icon": "🏠", "num": 0},
    {"id": "welcome",    "label": "Welcome",              "icon": "♡",  "num": 1},
    {"id": "memories",   "label": "Memories",             "icon": "🖼️", "num": 2},
    {"id": "words",      "label": "Words From My Heart",  "icon": "🪶", "num": 3},
    {"id": "respect",    "label": "Why I Respect You",    "icon": "⭐", "num": 4},
    {"id": "intentions", "label": "Intentions",           "icon": "💝", "num": 5},
    {"id": "dua",        "label": "Dua",                  "icon": "🤲", "num": 6},
    {"id": "goodbye",    "label": "Final Note",           "icon": "✉️", "num": 7},
]

# Story chapters excluding home
TOTAL_STORY_CHAPTERS = 7
