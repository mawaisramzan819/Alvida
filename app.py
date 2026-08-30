"""
=============================================================================
STREAMLIT FAREWELL WEB APP
Interactive Cinematic Storytelling Web Experience (Emotional Roman Urdu)
(Automatic Startup Flow: 3s STARTING Loader -> Background Music By Default)
=============================================================================
"""

import base64
import importlib
from pathlib import Path
import time
import streamlit as st
import streamlit.components.v1 as components

import config
import content

# Ensure fresh reload of configuration and content modules
try:
    importlib.reload(config)
    importlib.reload(content)
except Exception:
    pass


# -----------------------------------------------------------------------------
# 1. Bulletproof Safe HTML Renderer
# -----------------------------------------------------------------------------
def ui(html_content: str):
    """Render HTML safely without markdown indentation interpreting it as code blocks."""
    lines = [line.strip() for line in html_content.strip().splitlines() if line.strip()]
    clean_html = "".join(lines)
    st.markdown(clean_html, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. Page Configuration & Stylesheet Injection
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def load_styles():
    """Load and inject custom stylesheet."""
    css_path = config.CSS_DIR / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. Startup Machine & Default Background Audio Controller (components.html iframe execution)
# -----------------------------------------------------------------------------
def render_startup_state_machine():
    """Render Startup Loader and Auto-Play Background Music seamlessly by default."""
    components.html("""
    <script>
    (function() {
        const pDoc = window.parent.document;
        
        // 1. Create Audio Element on parent document
        let audio = pDoc.getElementById('farewellBgAudioMain');
        if (!audio) {
            audio = pDoc.createElement('audio');
            audio.id = 'farewellBgAudioMain';
            audio.loop = true;
            audio.preload = 'auto';
            audio.src = '/app/static/farewell.mp3';
            pDoc.body.appendChild(audio);
            window.parent.__farewell_audio = audio;
        }

        // Function to attempt smooth audio playback
        function triggerAudioPlayback() {
            if (!audio) return;
            if (audio.paused) {
                audio.volume = 0;
                let playPromise = audio.play();
                if (playPromise !== undefined) {
                    playPromise.then(() => {
                        let start = performance.now();
                        function fadeIn() {
                            let el = performance.now() - start;
                            let frac = Math.min(el / 1500, 1);
                            audio.volume = frac * 0.18;
                            if (frac < 1) requestAnimationFrame(fadeIn);
                        }
                        requestAnimationFrame(fadeIn);
                    }).catch(err => {
                        console.log("Autoplay waiting for user gesture:", err);
                    });
                }
            }
        }

        // Immediately try auto-playing on page load
        triggerAudioPlayback();

        // Fallback interaction listeners across document and window for instant start on any gesture
        const handleFirstInteraction = function() {
            triggerAudioPlayback();
        };
        pDoc.addEventListener('click', handleFirstInteraction, { passive: true });
        pDoc.addEventListener('touchstart', handleFirstInteraction, { passive: true });
        pDoc.addEventListener('keydown', handleFirstInteraction, { passive: true });
        pDoc.addEventListener('pointerdown', handleFirstInteraction, { passive: true });
        window.addEventListener('click', handleFirstInteraction, { passive: true });

        // Avoid duplicate overlay creation
        if (pDoc.getElementById('startupMasterOverlay')) return;

        // 2. Create Full-Screen Master Overlay for 3-Second Loading Animation
        const overlay = pDoc.createElement('div');
        overlay.id = 'startupMasterOverlay';
        overlay.style.cssText = 'position:fixed; inset:0; z-index:99999999; background:#060911; display:flex; align-items:center; justify-content:center; font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; transition:opacity 0.5s ease-out;';

        overlay.innerHTML = `
            <style>
                @keyframes fillCircularRing {
                    0% { stroke-dashoffset: 301.59; }
                    100% { stroke-dashoffset: 0; }
                }
                @keyframes stage1FadeOut {
                    0% { opacity: 1; transform: scale(1); }
                    100% { opacity: 0; transform: scale(0.96); }
                }
                @property --num {
                    syntax: '<integer>';
                    initial-value: 0;
                    inherits: false;
                }
                @keyframes countPercent {
                    0% { --num: 0; }
                    100% { --num: 100; }
                }
                .css-pct-counter {
                    counter-reset: num var(--num);
                    animation: countPercent 3s cubic-bezier(0.4, 0, 0.2, 1) forwards;
                }
                .css-pct-counter::after {
                    content: counter(num) "%";
                }
            </style>

            <!-- 3-Second Circular STARTING Loader -->
            <div id="pStage1" style="animation: stage1FadeOut 0.4s ease 3s forwards; text-align:center; padding:2.5rem 2rem; max-width:580px; width:90%; background:rgba(14,20,32,0.85); border:1.5px solid rgba(245,158,11,0.4); border-radius:28px; box-shadow:0 30px 80px rgba(0,0,0,0.8),0 0 50px rgba(245,158,11,0.2);">
                <div style="position:relative; width:130px; height:130px; margin:0 auto 1.5rem auto;">
                    <svg width="130" height="130" viewBox="0 0 130 130" style="transform:rotate(-90deg);">
                        <circle cx="65" cy="65" r="48" stroke="rgba(255,255,255,0.07)" stroke-width="4.5" fill="none"/>
                        <circle cx="65" cy="65" r="48" stroke="url(#cGrad)" stroke-width="5" stroke-linecap="round" fill="none"
                            style="stroke-dasharray:301.59; stroke-dashoffset:301.59; animation:fillCircularRing 3s cubic-bezier(0.4, 0, 0.2, 1) forwards; filter:drop-shadow(0 0 12px rgba(245,158,11,0.75));"/>
                        <defs>
                            <linearGradient id="cGrad" x1="0" y1="0" x2="1" y2="1">
                                <stop offset="0%" stop-color="#ea580c"/>
                                <stop offset="50%" stop-color="#f59e0b"/>
                                <stop offset="100%" stop-color="#fde047"/>
                            </linearGradient>
                        </defs>
                    </svg>
                    <div style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center;">
                        <span class="css-pct-counter" style="font-size:1.3rem; font-weight:800; color:#fde68a;"></span>
                    </div>
                </div>
                <div style="font-size:1.8rem; font-weight:800; letter-spacing:5px; color:#ffffff; margin-bottom:0.5rem; text-shadow:0 0 20px rgba(245,158,11,0.6);">STARTING...</div>
                <div style="font-style:italic; font-size:1.25rem; color:#f59e0b; margin-bottom:0.6rem;">Hamari adhoori kahani shuru ho rahi hai...</div>
                <div style="font-style:italic; font-size:1.05rem; color:#94a3b8;">“Dil ke woh alfaaz jo sirf ap k  liye the...”</div>
            </div>
        `;

        pDoc.body.appendChild(overlay);

        // After 3 seconds, smoothly fade out and dismiss the overlay automatically
        setTimeout(() => {
            overlay.style.opacity = '0';
            overlay.style.pointerEvents = 'none';
            setTimeout(() => {
                overlay.remove();
            }, 500);
        }, 3150);
    })();
    </script>
    """, height=0, width=0)


def sync_audio_player():
    """Sync background audio playback with current music_playing state."""
    is_playing = st.session_state.get("music_playing", True)
    if is_playing:
        components.html("""
        <script>
        (function() {
            try {
                const pDoc = window.parent.document;
                let audio = pDoc.getElementById('farewellBgAudioMain');
                if (!audio) {
                    audio = pDoc.createElement('audio');
                    audio.id = 'farewellBgAudioMain';
                    audio.loop = true;
                    audio.preload = 'auto';
                    audio.src = '/app/static/farewell.mp3';
                    pDoc.body.appendChild(audio);
                    window.parent.__farewell_audio = audio;
                }
                if (audio) {
                    if (audio.paused) {
                        audio.volume = 0;
                        let playPromise = audio.play();
                        if (playPromise !== undefined) {
                            playPromise.then(() => {
                                let start = performance.now();
                                function fadeIn() {
                                    let el = performance.now() - start;
                                    let frac = Math.min(el / 400, 1);
                                    audio.volume = frac * 0.18;
                                    if (frac < 1) requestAnimationFrame(fadeIn);
                                }
                                requestAnimationFrame(fadeIn);
                            }).catch(err => {
                                console.log("Play error / interaction required:", err);
                                const onAction = () => {
                                    audio.play().then(() => {
                                        audio.volume = 0.18;
                                    }).catch(()=>{});
                                    pDoc.removeEventListener('click', onAction);
                                    pDoc.removeEventListener('touchstart', onAction);
                                };
                                pDoc.addEventListener('click', onAction, { passive: true });
                                pDoc.addEventListener('touchstart', onAction, { passive: true });
                            });
                        }
                    }
                }
            } catch(e) {}
        })();
        </script>
        """, height=0, width=0)
    else:
        components.html("""
        <script>
        (function() {
            try {
                const pDoc = window.parent.document;
                let audio = pDoc.getElementById('farewellBgAudioMain');
                if (audio && !audio.paused) {
                    let start = performance.now();
                    let initVol = audio.volume;
                    function fadeOut() {
                        let el = performance.now() - start;
                        let frac = Math.min(el / 300, 1);
                        audio.volume = Math.max(0, initVol * (1 - frac));
                        if (frac < 1) {
                            requestAnimationFrame(fadeOut);
                        } else {
                            audio.pause();
                        }
                    }
                    requestAnimationFrame(fadeOut);
                }
            } catch(e) {}
        })();
        </script>
        """, height=0, width=0)


# -----------------------------------------------------------------------------
# 4. Cinematic Vector Artworks (SVG)
# -----------------------------------------------------------------------------
def get_hero_sunset_svg():
    """Cinematic mountain sunset with golden sun rays and calm lake."""
    return """
    <svg width="100%" height="240" viewBox="0 0 450 240" fill="none" xmlns="http://www.w3.org/2000/svg" style="border-radius: 18px;">
        <defs>
            <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#1e1b4b"/>
                <stop offset="35%" stop-color="#b45309"/>
                <stop offset="65%" stop-color="#f59e0b"/>
                <stop offset="100%" stop-color="#fef08a"/>
            </linearGradient>
            <radialGradient id="sunGlow" cx="65%" cy="50%" r="40%">
                <stop offset="0%" stop-color="#ffffff"/>
                <stop offset="30%" stop-color="#fde047"/>
                <stop offset="60%" stop-color="#f97316"/>
                <stop offset="100%" stop-color="transparent"/>
            </radialGradient>
        </defs>
        <rect width="450" height="240" fill="url(#skyGrad)"/>
        <circle cx="310" cy="110" r="55" fill="url(#sunGlow)"/>
        <path d="M0 160 L90 120 L210 165 L320 115 L450 160 L450 240 L0 240 Z" fill="#451a03" opacity="0.8"/>
        <path d="M0 175 L120 145 L250 185 L360 140 L450 180 L450 240 L0 240 Z" fill="#1c1917" opacity="0.9"/>
        <rect y="195" width="450" height="45" fill="#0c0a09"/>
        <path d="M260 195 L360 195 L330 240 L290 240 Z" fill="#f59e0b" opacity="0.35"/>
        <path d="M0 200 C40 190 70 215 110 240 L0 240 Z" fill="#040306"/>
        <path d="M340 240 C380 200 410 190 450 185 L450 240 Z" fill="#040306"/>
    </svg>
    """


def get_flower_rock_svg():
    """Blooming delicate white flower on cliff with sunset."""
    return """
    <svg width="100%" height="220" viewBox="0 0 320 220" fill="none" xmlns="http://www.w3.org/2000/svg" style="border-radius: 16px;">
        <defs>
            <linearGradient id="flowerSky" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#0f172a"/>
                <stop offset="60%" stop-color="#7c2d12"/>
                <stop offset="100%" stop-color="#ea580c"/>
            </linearGradient>
        </defs>
        <rect width="320" height="220" fill="url(#flowerSky)"/>
        <path d="M140 220 C160 170 210 160 280 175 C300 180 320 205 320 220 Z" fill="#09090b"/>
        <path d="M245 170 Q240 135 248 115" stroke="#4ade80" stroke-width="2.5" fill="none"/>
        <path d="M242 145 Q230 140 232 150" stroke="#22c55e" stroke-width="2" fill="none"/>
        <circle cx="248" cy="115" r="16" fill="#ffffff" opacity="0.95"/>
        <circle cx="248" cy="115" r="5" fill="#facc15"/>
    </svg>
    """


# -----------------------------------------------------------------------------
# 5. 1.25-Second Destination Chapter Navigation Loader
# -----------------------------------------------------------------------------
def render_nav_analyzing_loader(target_section_key: str):
    """Render the exact 1.25-second destination chapter loader with glowing progress line."""
    default_loaders = {
        "home": {"title": "Home", "message": "Dil ki baat dobara khul rahi hai..."},
        "message": {"title": "Message", "message": "Woh alfaaz jo kabhi keh nahi saka..."},
        "memories": {"title": "Memories", "message": "Purani yaadon ko sameta ja raha hai..."},
        "wishes": {"title": "Wishes", "message": "Adhoori khwahishon ko parha ja raha hai..."},
        "dua": {"title": "Dua", "message": "Dil se nikli dua khul rahi hai..."},
        "future": {"title": "Future", "message": "Woh mustaqbil jo ap k  saath socha tha..."},
        "thankyou": {"title": "Thank You", "message": "ap koara shukriya ada kiya ja raha hai..."},
        "goodbye": {"title": "Goodbye", "message": "Woh alvida jo main kehna nahi chahta..."},
    }
    
    loaders_dict = getattr(content, "CHAPTER_LOADERS", default_loaders)
    loader_info = loaders_dict.get(target_section_key, default_loaders.get(target_section_key, default_loaders["home"]))

    loader_placeholder = st.empty()
    steps = 25
    sleep_duration = 0.05  # 25 * 0.05 = 1.25 seconds
    
    for i in range(1, steps + 1):
        percent = int((i / steps) * 100)
        loader_html = (
            f'<div class="nav-analyzing-modal-backdrop">'
            f'<div class="analyzing-container-inline">'
            f'<div class="analyzing-spinner-icon">✦</div>'
            f'<div class="analyzing-title">{loader_info["title"].upper()}...</div>'
            f'<div class="analyzing-chapter-badge">{loader_info["message"]}</div>'
            f'<div class="analyzing-progress-track-inline">'
            f'<div class="analyzing-progress-bar-fill" style="width: {percent}%;"></div>'
            f'</div>'
            f'<div class="analyzing-percent-text">{percent}%</div>'
            f'<div class="analyzing-subtext">“{loader_info["title"]} Chapter Tayyar Ho Raha Hai...”</div>'
            f'</div>'
            f'</div>'
        )
        loader_placeholder.markdown(loader_html, unsafe_allow_html=True)
        time.sleep(sleep_duration)

    loader_placeholder.empty()
    st.session_state["active_section"] = target_section_key
    st.session_state["pending_section"] = None
    st.rerun()


# -----------------------------------------------------------------------------
# 6. Sidebar Navigation Component (Inter Font)
# -----------------------------------------------------------------------------
def render_sidebar(active_section: str, is_loading: bool = False):
    """Render Left Navigation Sidebar with interactive chapter triggers."""
    ui("""
    <div class="sunset-sidebar">
        <div class="sidebar-logo-wrap">
            <div class="sidebar-lotus-icon">🪷</div>
            <div class="sidebar-brand-name">Hamari Kahani</div>
            <div class="sidebar-brand-sub">Ek Aakhri Baat</div>
        </div>
        <div class="sidebar-nav-container">
    """)

    chapters_list = getattr(config, "CHAPTERS", [
        {"id": "home", "label": "Home", "icon": "🏠"},
        {"id": "message", "label": "Message", "icon": "✉️"},
        {"id": "memories", "label": "Memories", "icon": "💭"},
        {"id": "wishes", "label": "Wishes", "icon": "🌟"},
        {"id": "dua", "label": "Dua", "icon": "🤲"},
        {"id": "future", "label": "Future", "icon": "🖋️"},
        {"id": "thankyou", "label": "Thank You", "icon": "🤍"},
        {"id": "goodbye", "label": "Goodbye", "icon": "🌙"},
    ])

    for ch in chapters_list:
        is_active = (ch["id"] == active_section)
        wrap_class = "active-nav-btn" if is_active else "inactive-nav-btn"
        
        col_wrap = st.container()
        with col_wrap:
            ui(f'<div class="{wrap_class}">')
            if st.button(
                f"{ch['icon']}  {ch['label']}",
                key=f"nav_btn_{ch['id']}",
                use_container_width=True,
                disabled=is_loading
            ):
                if st.session_state["active_section"] != ch["id"]:
                    st.session_state["pending_section"] = ch["id"]
                    st.session_state["selected_memory"] = None
                    st.rerun()
            ui('</div>')

    # Sidebar Music Status & Smooth Fade Toggle Widget
    is_music_on = st.session_state.get("music_playing", True)
    sound_bars = """
    <div class="sound-wave-bars">
        <span class="sound-bar"></span>
        <span class="sound-bar"></span>
        <span class="sound-bar"></span>
        <span class="sound-bar"></span>
    </div>
    """ if is_music_on else ""

    ui(f"""
        </div>
        <div class="sidebar-music-widget">
            <div style="display:flex; align-items:center; gap:8px;">
                <span style="color:#f59e0b;">♪</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:600; font-family:var(--font-ui);">Music</span>
                {sound_bars}
            </div>
    """)

    toggle_btn_label = "⏸ stop music" if is_music_on else "▶ Start music"
    if st.button(toggle_btn_label, key="sidebar_music_toggle_btn", use_container_width=False, disabled=is_loading):
        st.session_state["music_playing"] = not is_music_on
        st.rerun()

    ui("""
        </div>
    </div>
    """)


# -----------------------------------------------------------------------------
# 7. Dedicated Chapter Views (Intimate Letter Typography)
# -----------------------------------------------------------------------------

def render_home_chapter():
    """CHAPTER 1 — HOME EXPERIENCE (Roman Urdu)"""
    sec = content.OPENING_SECTION
    hero_svg = get_hero_sunset_svg()
    is_music_on = st.session_state.get("music_playing", True)
    music_btn_label = "⏸ stop music" if is_music_on else "▶ Start music"
    bottom_quote = sec.get(
        "bottom_quote",
        "“Agar main is kahani ka anjaam badal sakta, to main ek baar phir sirf tumhein hi chunta.”"
    )

    ui(f"""
    <div>
        <div class="hero-sunset-card">
            <div>
                <div class="chapter-eyebrow-container stagger-heading">
                    <span class="eyebrow-line"></span>
                    <span class="chapter-eyebrow-text">{sec['eyebrow']}</span>
                    <span class="eyebrow-line"></span>
                </div>
                
                <h1 class="chapter-heading-main stagger-heading" style="text-align: left; margin-left: 0; font-size: 3.1rem !important;">
                    Maine kabhi nahi socha tha ke hamari kahani ka aakhri lafz <span class="heading-accent">“Alvida”</span> hoga.
                </h1>
                
                <p class="letter-paragraph stagger-p1" style="font-size: 18px; line-height: 1.9; color: #cbd5e1; margin-bottom: 2.2rem;">
                    {sec['subtitle']}
                </p>
                <div class="hero-buttons-container stagger-p2">
    """)

    col1, col2 = st.columns([1.5, 1.5])
    with col1:
        if st.button(f"{sec['primary_button']}", key="home_primary_cta", use_container_width=True):
            st.session_state["pending_section"] = "message"
            st.rerun()
    with col2:
        if st.button(f"{music_btn_label}", key="home_secondary_cta", use_container_width=True):
            st.session_state["music_playing"] = not is_music_on
            st.rerun()

    ui(f"""
                </div>
            </div>
            <div style="position:relative; display:flex; align-items:center; justify-content:center;">
                {hero_svg}
                <div class="cursive-quote-overlay">Sirf ap...</div>
            </div>
        </div>

        <div class="emotional-blockquote stagger-quote" style="text-align: center; max-width: 860px; margin: 2rem auto;">
            {bottom_quote}
        </div>
    </div>
    """)


def render_message_chapter():
    """CHAPTER 2 — MESSAGE EXPERIENCE (Intimate Letter Area)"""
    sec = content.MESSAGE_SECTION
    flower_svg = get_flower_rock_svg()

    ui(f"""
    <div>
        <div style="text-align: center; margin-bottom: 2rem;">
            <div class="chapter-eyebrow-container stagger-heading">
                <span class="eyebrow-line"></span>
                <span class="chapter-eyebrow-text">EK AAKHRI PUKAAR</span>
                <span class="eyebrow-line"></span>
            </div>
            
            <h1 class="chapter-heading-main stagger-heading">
                Woh alfaaz jo main <span class="heading-accent">keh nahi saka</span>
            </h1>
            
            <div class="chapter-subtitle-italic stagger-subtitle">
                “{sec['subtitle']}”
            </div>
        </div>
        
        <div class="intimate-letter-card">
            <div class="decorative-quote-mark">“</div>
            <div class="intimate-letter-grid">
                <div>
                    <p class="letter-paragraph stagger-p1">
                        Main maanta hoon ke hamare darmiyan jo sab se gehra zakhm bana, uski wajah <span class="text-amber-glow">meri ghalti thi</span>. Maine woh baatein doosron ko bata dein jo sirf ap k  aur mere darmiyan rehni chahiye theen.
                    </p>
                    
                    <p class="letter-paragraph stagger-p2">
                        Us waqt main samajh nahi saka ke kisi se mohabbat karne ka matlab uske <span class="text-amber-glow">bharose</span>, uski <span class="text-ivory-focus">izzat</span> aur uski privacy ki hifazat karna bhi hota hai.
                    </p>
                    
                    <p class="letter-paragraph letter-accented-paragraph stagger-p3">
                        Main guzra hua waqt badal nahi sakta. ap koein meri wajah se jo baatein sunni pareen aur jo takleef mili, main usay mita nahi sakta. Lekin agar mera afsos waqt ko peechhe le ja sakta, to main apni kahani ko poori duniya se chhupa kar sirf apne dil mein rakhta.
                    </p>
                    
                    <p class="letter-paragraph stagger-p4">
                        <span class="text-amber-glow">Do saal ki khamoshi</span> mein bhi koi din aisa nahi tha jab ap meri yaadon se door rahi ho.
                    </p>
                    
                    <div class="emotional-blockquote stagger-quote" style="margin-top: 2rem; margin-bottom: 1.5rem;">
                        “Main ye sab is liye nahi likh raha ke main ap koein khushi se alvida keh raha hoon. Main ye is liye likh raha hoon kyun ke <span class="text-amber-glow">mera dil aaj bhi ap koein khone ke liye tayyar nahi</span>.”
                    </div>
                    
                    <div class="handwritten-bottom-note stagger-quote">
                        — Kash ap ruk jao...
                    </div>
                </div>
                
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative;">
                    {flower_svg}
                    <div class="handwritten-bottom-note" style="margin-top: 1rem; font-size: 1.4rem; text-align: center;">
                        “ap meri aakhri dua ho...”
                    </div>
                </div>
            </div>
        </div>
    </div>
    """)


def render_memories_chapter():
    """CHAPTER 3 — MEMORIES EXPERIENCE (8 Closed Cards + Dedicated Opened Letter View)"""
    sec = content.MEMORIES_SECTION
    cards = sec["cards"]
    selected_idx = st.session_state.get("selected_memory", None)

    # VIEW A: A Memory Letter is OPEN
    if selected_idx is not None and 0 <= selected_idx < len(cards):
        selected_card = cards[selected_idx]
        total_memories = len(cards)
        is_first = (selected_idx == 0)
        is_last = (selected_idx == total_memories - 1)

        ui(f"""
        <div class="chapter-content-animated" style="max-width: 820px; margin: 0 auto;">
            <div style="text-align: center; margin-bottom: 2rem;">
                <div class="chapter-eyebrow-container stagger-heading">
                    <span class="eyebrow-line"></span>
                    <span class="chapter-eyebrow-text">YAAD #{selected_idx + 1} / {total_memories}</span>
                    <span class="eyebrow-line"></span>
                </div>
                
                <h1 class="chapter-heading-main stagger-heading">
                    {selected_card['category']}
                </h1>
            </div>
            
            <div class="intimate-letter-card stagger-p1" style="box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8), 0 0 40px rgba(245, 158, 11, 0.15);">
                <div class="decorative-quote-mark">“</div>
                
                <div style="text-align: center; margin-bottom: 1.5rem;">
                    <div style="font-size: 3.2rem; filter: drop-shadow(0 0 16px rgba(245, 158, 11, 0.6));">{selected_card['icon']}</div>
                </div>
                
                <div class="letter-paragraph" style="font-size: 19px; line-height: 2; color: #f1f5f9; background: rgba(245, 158, 11, 0.04); padding: 1.8rem 2rem; border-left: 3.5px solid var(--gold-primary); border-radius: 0 16px 16px 0; margin-bottom: 2rem;">
                    {selected_card['placeholder']}
                </div>
                
                <div class="handwritten-bottom-note" style="text-align: center; margin-bottom: 2.2rem; font-size: 1.7rem;">
                    “Yeh lamha hamesha mere dil ke paas rahega...”
                </div>
                
                <div style="margin-top: 1rem; padding-top: 1.5rem; border-top: 1px solid rgba(255, 255, 255, 0.08);">
        """)

        # 3 Bottom Navigation Controls: [← back] [close] [Agli Yaad → / Yaadon Par Wapas]
        col_btn1, col_btn2, col_btn3 = st.columns([1.2, 1.4, 1.2])

        with col_btn1:
            if st.button("← back", key=f"prev_memory_opened_{selected_idx}", use_container_width=True, disabled=is_first):
                if selected_idx > 0:
                    st.session_state["selected_memory"] = selected_idx - 1
                    st.rerun()

        with col_btn2:
            if st.button("close ×", key=f"close_memory_opened_{selected_idx}", use_container_width=True):
                st.session_state["selected_memory"] = None
                st.rerun()

        with col_btn3:
            next_label = "Yaadon Par Wapas" if is_last else "Agli Yaad →"
            if st.button(next_label, key=f"next_memory_opened_{selected_idx}", use_container_width=True):
                if is_last:
                    st.session_state["selected_memory"] = None
                else:
                    st.session_state["selected_memory"] = selected_idx + 1
                st.rerun()

        ui("""
                </div>
            </div>
        </div>
        """)
        return

    # VIEW B: Closed 8-Card Memories Grid
    ui(f"""
    <div class="chapter-content-animated">
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <div class="chapter-eyebrow-container stagger-heading">
                <span class="eyebrow-line"></span>
                <span class="chapter-eyebrow-text">SAFAR-E-YADEIN</span>
                <span class="eyebrow-line"></span>
            </div>
            
            <h1 class="chapter-heading-main stagger-heading">
                Woh yaadein jo aaj bhi <span class="heading-accent">mere saath hain</span>
            </h1>
            
            <div class="chapter-subtitle-italic stagger-subtitle">
                “{sec['subtitle']}”
            </div>
        </div>
    </div>
    """)

    for row_start in [0, 4]:
        cols = st.columns(4, gap="medium")
        for i in range(4):
            idx = row_start + i
            if idx < len(cards):
                card = cards[idx]
                with cols[i]:
                    ui(f"""
                    <div class="memory-compact-card stagger-p{min(i + 1, 4)}">
                        <div>
                            <div class="memory-compact-icon">{card['icon']}</div>
                            <div class="memory-compact-title">{card['category']}</div>
                        </div>
                    """)
                    if st.button("open →", key=f"open_closed_card_btn_{idx}", use_container_width=True):
                        st.session_state["selected_memory"] = idx
                        st.rerun()
                    ui("""
                    </div>
                    """)


def render_wishes_chapter():
    """CHAPTER 4 — WISHES EXPERIENCE (5 Heartfelt Roman Urdu Wishes)"""
    sec = content.WISHES_SECTION
    
    cards_html = ""
    for idx, card in enumerate(sec["cards"]):
        accent_cls = f"wish-accent-{card['accent_type']}"
        cards_html += f"""
        <div class="wish-glass-card {accent_cls} stagger-p{min(idx + 1, 5)}">
            <div style="font-size: 1.6rem; margin-bottom: 0.8rem;">{card['icon']}</div>
            <div class="wish-card-title">{card['title']}</div>
            <div class="wish-card-desc">{card['description']}</div>
        </div>
        """

    ui(f"""
    <div>
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <div class="chapter-eyebrow-container stagger-heading">
                <span class="eyebrow-line"></span>
                <span class="chapter-eyebrow-text">DIL KI KHWAHISHEIN</span>
                <span class="eyebrow-line"></span>
            </div>
            
            <h1 class="chapter-heading-main stagger-heading">
                Meri adhoori <span class="heading-accent">khwahishein</span>
            </h1>
            
            <div class="chapter-subtitle-italic stagger-subtitle">
                “Kash ye sab badal sakta...”
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
            {cards_html}
        </div>
    </div>
    """)


def render_dua_chapter():
    """CHAPTER 5 — DUA EXPERIENCE (Serene Prayer Horizon)"""
    sec = content.DUA_SECTION

    ui(f"""
    <div>
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <div class="chapter-eyebrow-container stagger-heading">
                <span class="eyebrow-line"></span>
                <span class="chapter-eyebrow-text">EK KHALIS DUA</span>
                <span class="eyebrow-line"></span>
            </div>
            
            <h1 class="chapter-heading-main stagger-heading">
                Jab kuch na kar saka to <span class="heading-accent">ap k  liye dua ki</span>
            </h1>
            
            <div class="chapter-subtitle-italic stagger-subtitle">
                “Rab ke huzoor dil ka har haal rakh diya...”
            </div>
        </div>
        
        <div class="dua-scenic-card">
            <div style="max-width: 800px; margin: 0 auto; text-align: left;">
                <p class="letter-paragraph stagger-p1" style="font-size: 19px;">
                    <span class="text-ivory-focus">Ya Allah,</span> Ap hamare dilon ka haal jaanty hain. Ap hamari mohabbat, hamari ghaltiyan, hamari takleef aur woh har baat jaanty hain jo hum kabhi ek doosre se keh nahi sake.
                </p>
                
                <p class="letter-paragraph stagger-p2" style="font-size: 19px;">
                    Agar hamara saath hum dono ke haq mein behtar hai, to <span class="text-amber-glow">hamare darmiyan khari har deewar hata de</span>. Hamari ghaltiyan maaf kar de, hamare dil narm kar de aur izzat ke saath hamare raste dobara mila de.
                </p>
                
                <p class="letter-paragraph stagger-p3" style="font-size: 19px;">
                    Aur agar hamara saath muqaddar mein nahi, to woh jahan bhi rahe usay hamesha khush, mehfooz aur pur-sukoon rakhna—chahe uske saath khara hone wala shakhs main na rahun.
                </p>
                
                <div class="emotional-blockquote stagger-quote" style="text-align: center; margin-top: 2rem;">
                    “Lekin Ya Allah… agar abhi bhi koi rasta baqi hai, to isay hamara aakhri alvida mat banne dena.”
                </div>
            </div>
            
            <div style="margin-top: 2rem; font-size: 2rem; color: #f59e0b;">
                🤲 🤍
            </div>
        </div>
    </div>
    """)


def render_future_chapter():
    """CHAPTER 6 — FUTURE EXPERIENCE (Envisioned Tomorrow)"""
    fut = content.FUTURE_SECTION

    ui(f"""
    <div>
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <div class="chapter-eyebrow-container stagger-heading">
                <span class="eyebrow-line"></span>
                <span class="chapter-eyebrow-text">SOCHA HUA KAL</span>
                <span class="eyebrow-line"></span>
            </div>
            
            <h1 class="chapter-heading-main stagger-heading">
                Woh mustaqbil jo maine <span class="heading-accent">ap k  saath socha tha</span>
            </h1>
            
            <div class="chapter-subtitle-italic stagger-subtitle">
                “{fut['subtitle']}”
            </div>
        </div>
        
        <div class="future-scenic-card">
            <div class="future-art-box">
                <div style="font-family: var(--font-handwritten); font-size: 1.8rem; color: #fde047; line-height: 1.4;">
                    “{fut['quote_art']}”
                </div>
            </div>
            <div>
                <p class="letter-paragraph stagger-p1">
                    Jab bhi maine apne career, kamyabi aur ek behtar zindagi ka socha, <span class="text-ivory-focus">us tasveer mein ap hamesha mere saath theen</span>.
                </p>
                
                <p class="letter-paragraph stagger-p2">
                    Main ap koein sirf apne aasaan dino mein nahi chahta tha. Main ap k  liye ek aisa insaan banna chahta tha jo izzat ke saath ap koara haath maang sake aur zindagi bhar ap k  saath khara reh sake.
                </p>
                
                <p class="letter-paragraph stagger-p3">
                    Shayad mujhe bohat waqt lag gaya. Shayad zindagi mujhse zyada tez chalti rahi. Lekin jis mustaqbil ke liye main mehnat kar raha tha, <span class="text-amber-glow">woh ap k  baghair kabhi mukammal nahi tha</span>.
                </p>
            </div>
        </div>
    </div>
    """)


def render_thankyou_chapter():
    """CHAPTER 7 — THANK YOU EXPERIENCE (Heartfelt Gratitude)"""
    ty = content.THANK_YOU_SECTION
    thank_lines = "".join(f'<div class="letter-paragraph stagger-p{min(i+1, 5)}" style="margin-bottom:1rem; display:flex; align-items:center; justify-content:center; gap:10px;"><span style="color:#f59e0b;">✦</span><span>{line}</span></div>' for i, line in enumerate(ty["lines"]))

    ui(f"""
    <div>
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <div class="chapter-eyebrow-container stagger-heading">
                <span class="eyebrow-line"></span>
                <span class="chapter-eyebrow-text">DIL KI GEHRAIYON SE</span>
                <span class="eyebrow-line"></span>
            </div>
            
            <h1 class="chapter-heading-main stagger-heading">
                Meri zindagi mein aane ka <span class="heading-accent">shukriya</span>
            </h1>
            
            <div class="chapter-subtitle-italic stagger-subtitle">
                “{ty['main_quote']}”
            </div>
        </div>
        
        <div class="thankyou-centered-card">
            <div style="max-width: 780px; margin: 0 auto 2.5rem auto;">
                {thank_lines}
            </div>
            
            <div class="emotional-blockquote stagger-quote" style="text-align: center; max-width: 760px; margin: 0 auto 2rem auto;">
                “{ty['final_line']}”
            </div>
            
            <div style="color: #f59e0b; font-size: 2rem;">
                🤍
            </div>
        </div>
    </div>
    """)


def render_goodbye_chapter():
    """CHAPTER 8 — GOODBYE & FINAL WORDS (Emotional Climax)"""
    gb = content.GOODBYE_SECTION

    ui(f"""
    <div>
        <div style="text-align: center; margin-bottom: 2.5rem;">
            <div class="chapter-eyebrow-container stagger-heading">
                <span class="eyebrow-line"></span>
                <span class="chapter-eyebrow-text">WOH LAFZ JO MAIN KEH NAHI PA RAHA</span>
                <span class="eyebrow-line"></span>
            </div>
            
            <h1 class="chapter-heading-main stagger-heading" style="font-size: 3.6rem !important;">
                Main ap koein alvida <span class="heading-accent">kaise kahun?</span>
            </h1>
        </div>
        
        <div class="goodbye-monolith-card">
            <div style="max-width: 780px; margin: 0 auto 2.2rem auto; text-align: left;">
                <p class="letter-paragraph stagger-p1">
                    Main us shakhs ko alvida kaise kahun jo meri itni saari yaadon mein basa hua hai?
                </p>
                
                <p class="letter-paragraph stagger-p2">
                    Main kaise maan loon ke jisne kabhi meri zindagi ke liye dua ki, woh ab meri zindagi ka hissa nahi rahegi?
                </p>
                
                <p class="letter-paragraph stagger-p3">
                    Main jaanta hoon ke maine ap koein takleef di. Main ye bhi jaanta hoon ke sirf mohabbat guzra hua sab kuch nahi mita sakti. Lekin <span class="text-amber-glow">ap koein kho dena aaj bhi mere dil ko qabool nahi</span>.
                </p>
                
                <p class="letter-paragraph stagger-p4">
                    Main ap par koi zabardasti nahi karna chahta. Main ap koari takleef ko chota bhi nahi kehna chahta. Main sirf itna chahta hoon ke agar ap k  dil ke kisi kone mein hamari kahani abhi bhi zinda hai, to please isay yahin khatam mat hone dena.
                </p>
            </div>
            
            <div class="emotional-blockquote stagger-p5" style="text-align: center; max-width: 760px; margin: 2rem auto;">
                “{gb['highlighted_line']}”
            </div>
    """)

    # Interactive 'Meri Aakhri Baat Parho' button
    if not st.session_state.get("show_final_dua", False):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(f"{gb['button_label']}", key="reveal_final_sunset_dua", use_container_width=True):
                st.session_state["show_final_dua"] = True
                st.rerun()
    else:
        ui(f"""
        <div class="revealed-final-prayer-box">
            <div style="font-family: var(--font-ui); color: #f59e0b; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-bottom: 1rem; letter-spacing: 2.5px;">
                ✦ MERI AAKHRI BAAT ✦
            </div>
            <div class="letter-paragraph" style="color: #ffffff; font-size: 19px; line-height: 2; max-width: 720px; margin: 0 auto; text-align: center;">
                {gb['revealed_text']}
            </div>
        </div>
        """)

    # Final Closing Quote in Cormorant Garamond Italic
    ui(f"""
            <div style="margin-top: 3.5rem; padding-top: 2.5rem; border-top: 1px solid rgba(255, 255, 255, 0.08);">
                <div style="color: #f59e0b; font-size: 1.8rem; margin-bottom: 0.8rem;">🪷</div>
                <div style="font-family: var(--font-heading); font-style: italic; font-size: 1.8rem; color: #fde68a; line-height: 1.4; max-width: 680px; margin: 0 auto;">
                    {gb['final_quote']}
                </div>
            </div>
        </div>
    </div>
    """)


# -----------------------------------------------------------------------------
# 8. Main Application Controller & Dynamic State Router
# -----------------------------------------------------------------------------
def main():
    # Initialize Independent Session State Variables
    is_initial_load = "session_started" not in st.session_state
    if is_initial_load:
        st.session_state["session_started"] = True
        st.session_state["active_section"] = "home"
        st.session_state["pending_section"] = None
        st.session_state["music_playing"] = True
        st.session_state["show_final_dua"] = False
        st.session_state["selected_memory"] = None

    load_styles()

    # Sync Persistent Audio State with Browser
    sync_audio_player()

    # Render 3-State Startup Machine via components.html on Initial Load / Refresh
    if is_initial_load:
        render_startup_state_machine()

    active_section = st.session_state.get("active_section", "home")
    pending_section = st.session_state.get("pending_section", None)

    # Main Two-Column Layout (Sidebar + Dedicated Content Area)
    col_nav, col_content = st.columns([1, 4.4], gap="large")

    with col_nav:
        render_sidebar(active_section, is_loading=(pending_section is not None))

    with col_content:
        # Navigation Click: 5-Second ANALYZING Loader
        if pending_section is not None:
            render_nav_analyzing_loader(pending_section)
        else:
            # Render Dedicated Chapter Interface
            if active_section == "home":
                render_home_chapter()
            elif active_section == "message":
                render_message_chapter()
            elif active_section == "memories":
                render_memories_chapter()
            elif active_section == "wishes":
                render_wishes_chapter()
            elif active_section == "dua":
                render_dua_chapter()
            elif active_section == "future":
                render_future_chapter()
            elif active_section == "thankyou":
                render_thankyou_chapter()
            elif active_section == "goodbye":
                render_goodbye_chapter()


if __name__ == "__main__":
    main()
