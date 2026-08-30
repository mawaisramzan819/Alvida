"""
Configuration settings for the Streamlit Farewell Web App.
Premium Modern Dark Cinematic Theme (Deep Navy, Charcoal, Warm Champagne Gold, Sunset Orange).
"""

from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
MUSIC_DIR = ASSETS_DIR / "music"
IMAGES_DIR = ASSETS_DIR / "images"
CSS_DIR = ASSETS_DIR / "css"

# Application Metadata
APP_TITLE = "A Farewell — With Gratitude"
APP_ICON = "🪷"
PAGE_LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "collapsed"

# Visual Theme Tokens (Deep Navy, Charcoal, Champagne Gold, Sunset Orange, Muted Blue/Teal)
THEME = {
    "bg_midnight": "#070a13",
    "bg_navy": "#0c111d",
    "bg_surface": "#121826",
    "bg_card": "rgba(18, 24, 38, 0.75)",
    "bg_card_hover": "rgba(25, 34, 54, 0.9)",
    "border_subtle": "rgba(255, 255, 255, 0.08)",
    "border_gold": "rgba(245, 158, 11, 0.35)",
    "accent_gold": "#f59e0b",
    "accent_gold_light": "#fbbf24",
    "accent_sunset": "#ea580c",
    "accent_blue": "#38bdf8",
    "accent_teal": "#14b8a6",
    "text_primary": "#f8fafc",
    "text_secondary": "#cbd5e1",
    "text_muted": "#94a3b8",
}

# Typography Google Fonts
GOOGLE_FONTS = [
    "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Outfit:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Caveat:wght@400;600;700&family=Noto+Nastaliq+Urdu:wght@400;500;600;700&family=Amiri:ital,wght@0,400;0,700;1,400&display=swap"
]

# Audio Settings
AUDIO_CONFIG = {
    # Place your audio file in assets/music/farewell.mp3
    "filename": "farewell.mp3",
    "enable_audio": True,
}

# Personalization Settings
SETTINGS = {
    "show_sender_name": False,
    "show_recipient_name": True,
    "enable_ambient_particles": True,
}

# Navigation Chapters
CHAPTERS = [
    {"id": "home", "label": "Home", "icon": "🏠"},
    {"id": "message", "label": "Message", "icon": "✉️"},
    {"id": "memories", "label": "Memories", "icon": "💭"},
    {"id": "wishes", "label": "Wishes", "icon": "🌟"},
    {"id": "dua", "label": "Dua", "icon": "🤲"},
    {"id": "future", "label": "Future", "icon": "🖋️"},
    {"id": "thankyou", "label": "Thank You", "icon": "🤍"},
    {"id": "goodbye", "label": "Goodbye", "icon": "🌙"},
]
