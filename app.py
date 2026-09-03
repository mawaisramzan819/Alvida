"""
=============================================================================
A FAREWELL THAT STAYS — EXACT UI/UX REFERENCE IMPLEMENTATION
Full-fidelity layout matching reference mockup: Fixed Sidebar + Panoramic Hero + 2x4 Card Grid
=============================================================================
"""

import base64
import importlib
import json
from pathlib import Path
import time
import streamlit as st
import streamlit.components.v1 as components

import config
import content

# Ensure fresh reload of config and content
try:
    importlib.reload(config)
    importlib.reload(content)
except Exception:
    pass

# Page Configuration — Wide layout with collapsed sidebar (permanently suppressed)
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout=config.PAGE_LAYOUT,
    initial_sidebar_state="collapsed",
)


# -----------------------------------------------------------------------------
# 1. Safe HTML Renderer
# -----------------------------------------------------------------------------
def ui(html_content: str):
    """Render HTML safely without indentation interpreting as markdown code block."""
    lines = [line.strip() for line in html_content.strip().splitlines() if line.strip()]
    clean_html = "".join(lines)
    st.markdown(clean_html, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. Stylesheet & Viewport Injection
# -----------------------------------------------------------------------------
def load_styles():
    """Load custom CSS and inject mobile viewport meta without markdown leakage."""
    ui('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">')
    css_path = config.CSS_DIR / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            ui(f"<style>{f.read()}</style>")


# -----------------------------------------------------------------------------
# 3. Audio Loader (Base64 Caching for Zero-Latency Playback)
# -----------------------------------------------------------------------------
@st.cache_data
def get_audio_base64():
    """Load background audio file into base64 data URI string."""
    candidate_paths = [
        config.MUSIC_DIR / "farewell.mp3",
        config.BASE_DIR / "static" / "farewell.mp3",
        config.MUSIC_DIR / "farewell.mp3.mp3",
        config.BASE_DIR / "static" / "assets" / "music" / "farewell.mp3",
    ]
    for p in candidate_paths:
        if p.exists():
            try:
                with open(p, "rb") as f:
                    return base64.b64encode(f.read()).decode("ascii")
            except Exception:
                pass
    return ""


# -----------------------------------------------------------------------------
# 4. Thumbnail & Hero Image Base64 Loaders (Instant In-Memory Rendering)
# -----------------------------------------------------------------------------
@st.cache_data
def get_thumbnail_b64(name: str):
    """Load card thumbnail into base64 string."""
    path = config.IMAGES_DIR / "thumbnails" / f"{name}.png"
    if path.exists():
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode("ascii")
        except Exception:
            pass
    return ""


@st.cache_data
def get_hero_panorama_b64():
    """Load master cinematic hero artwork into base64 string."""
    for name in ["hero_cinematic_master.jpg", "hero_panorama_hd.jpg", "hero_panorama_clean.jpg", "hero_banner_ref.jpg"]:
        path = config.IMAGES_DIR / name
        if path.exists():
            try:
                with open(path, "rb") as f:
                    return base64.b64encode(f.read()).decode("ascii")
            except Exception:
                pass
    return ""


# -----------------------------------------------------------------------------
# 4b. Ambient Atmospheric Engine (Chapter-Specific Moods)
# -----------------------------------------------------------------------------
def render_cinematic_atmosphere(active_section: str):
    """Render subtle, emotional ambient background layers tailored to chapter mood."""
    stars_html = ""
    if active_section == "dua":
        stars_html = """
        <div class="ambient-stars-container">
            <span class="celestial-star s1"></span>
            <span class="celestial-star s2"></span>
            <span class="celestial-star s3"></span>
            <span class="celestial-star s4"></span>
            <span class="celestial-star s5"></span>
            <span class="celestial-star s6"></span>
            <span class="celestial-star s7"></span>
            <span class="celestial-star s8"></span>
        </div>
        """

    memories_leak_html = ""
    if active_section == "memories":
        memories_leak_html = """
        <div class="ambient-light-leak-1"></div>
        <div class="ambient-light-leak-2"></div>
        <div class="ambient-film-grain"></div>
        """

    dawn_html = ""
    if active_section == "goodbye":
        dawn_html = """
        <div class="ambient-dawn-horizon"></div>
        <div class="ambient-dawn-warmth"></div>
        """

    ui(f"""
    <div class="ambient-atmosphere-layer mood-{active_section}" aria-hidden="true">
        <div class="ambient-bokeh-orb orb-1"></div>
        <div class="ambient-bokeh-orb orb-2"></div>
        <div class="ambient-atmosphere-haze"></div>
        {memories_leak_html}
        {stars_html}
        {dawn_html}
        <div class="ambient-dust-field">
            <span class="ambient-dust-speck d1"></span>
            <span class="ambient-dust-speck d2"></span>
            <span class="ambient-dust-speck d3"></span>
            <span class="ambient-dust-speck d4"></span>
            <span class="ambient-dust-speck d5"></span>
            <span class="ambient-dust-speck d6"></span>
            <span class="ambient-dust-speck d7"></span>
            <span class="ambient-dust-speck d8"></span>
        </div>
    </div>
    """)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# 5. Startup State Machine & Audio Engine (DOM Persistent Injection)
# -----------------------------------------------------------------------------
def render_initial_splash_loader():
    """Initial App Launch Splash with 2.5s Sweeping Visual Analyzer (Zero Audio on Launch)."""
    # 1. Visual HTML & CSS Overlay (Rendered via ui() to strip all indentation and prevent markdown leaks)
    ui("""
    <style>
    .cinematic-splash-overlay {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background: radial-gradient(circle at center, #1e131d 0%, #0a070a 100%) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        z-index: 99999999 !important;
        text-align: center !important;
        padding: 2rem !important;
        animation: splashFadeOut 2.5s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
        pointer-events: none !important;
    }
    @keyframes splashFadeOut {
        0% { opacity: 1; visibility: visible; pointer-events: auto; }
        72% { opacity: 1; visibility: visible; pointer-events: auto; }
        98% { opacity: 0; visibility: visible; pointer-events: none; }
        100% { opacity: 0; visibility: hidden; pointer-events: none; display: none; }
    }
    .loader-heart-orb {
        width: 70px !important;
        height: 70px !important;
        border-radius: 50% !important;
        background: radial-gradient(circle, rgba(244, 143, 177, 0.25) 0%, transparent 70%) !important;
        border: 2px solid rgba(244, 143, 177, 0.6) !important;
        box-shadow: 0 0 25px rgba(244, 143, 177, 0.45) !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        font-size: 28px !important;
        animation: orbPulse 1.6s ease-in-out infinite alternate !important;
        margin: 0 auto 24px auto !important;
    }
    @keyframes orbPulse {
        0% { transform: scale(0.92); box-shadow: 0 0 15px rgba(244, 143, 177, 0.3); }
        100% { transform: scale(1.08); box-shadow: 0 0 35px rgba(244, 143, 177, 0.7); }
    }
    .analyzer-track {
        width: 280px !important;
        height: 4px !important;
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 999px !important;
        overflow: hidden !important;
        position: relative !important;
        margin: 20px auto 14px auto !important;
    }
    .analyzer-glow-fill {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        height: 100% !important;
        width: 100% !important;
        background: linear-gradient(90deg, #e2557e, #f78da7, #ffffff) !important;
        border-radius: 999px !important;
        animation: analyzerFill 1.8s cubic-bezier(0.16, 1, 0.3, 1) infinite !important;
    }
    @keyframes analyzerFill {
        0% { transform: translateX(-100%); }
        60% { transform: translateX(0%); }
        100% { transform: translateX(100%); }
    }
    .loader-title-glow {
        color: #ffffff !important;
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: 1.65rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em !important;
        margin-bottom: 6px !important;
        text-shadow: 0 0 18px rgba(244, 143, 177, 0.35);
    }
    .loader-sub-glow {
        color: #e2a8b8 !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 0.95rem !important;
        margin-bottom: 12px !important;
        font-style: italic !important;
    }
    .loader-quote-glow {
        color: #9d8c96 !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 0.85rem !important;
        max-width: 440px !important;
        line-height: 1.5 !important;
        font-style: italic !important;
        margin: 0 auto !important;
    }
    </style>
    <div class="cinematic-splash-overlay" id="cinematicInitialSplashOverlay">
        <div class="loader-heart-orb">❤️</div>
        <div class="loader-title-glow">A Farewell That Stays</div>
        <div class="loader-sub-glow">Opening a story that was never forgotten...</div>
        <div class="analyzer-track"><div class="analyzer-glow-fill"></div></div>
        <div class="loader-quote-glow">“Some goodbyes stay in the heart forever.”</div>
    </div>
    """)


def render_full_screen_initial_loader():
    """Alias for render_initial_splash_loader."""
    render_initial_splash_loader()


def render_initial_splash_screen():
    """Alias for render_initial_splash_loader."""
    render_initial_splash_loader()


def render_startup_screen():
    """Alias for render_initial_splash_loader."""
    render_initial_splash_loader()


# -----------------------------------------------------------------------------
# 6. Interactive Sidebar Music, 3D WebGL & Navigation JavaScript Bridge
# -----------------------------------------------------------------------------
def get_farewell_3d_js():
    """Read the 3D WebGL script from assets/js/farewell_3d.js."""
    js_path = config.BASE_DIR / "assets" / "js" / "farewell_3d.js"
    if js_path.exists():
        return js_path.read_text(encoding="utf-8")
    return ""


def render_sidebar_and_navigation_bridge(active_view: str = "landing", active_section: str = "home"):
    """Register global navigation helper, bind sidebar music controls, and orchestrate 3D WebGL engine."""
    three_d_code = get_farewell_3d_js()
    three_d_json = json.dumps(three_d_code)
    active_3d = active_section if active_view == "section" else "home"

    components.html(
        f"""
    <script>
    (function() {{
        const pDoc = window.parent.document;

        // 1. Dynamic Audio Resolver
        window.parent.__farewellGetAudio = function() {{
            let a = pDoc.getElementById('farewellBgAudioMain') || window.parent.__farewell_audio;
            if (!a) {{
                const audios = pDoc.getElementsByTagName('audio');
                if (audios.length > 0) a = audios[0];
            }}
            return a;
        }};

        // 2. Format Seconds into MM:SS
        function fmtTime(sec) {{
            if (!sec || isNaN(sec)) return "00:00";
            const m = Math.floor(sec / 60);
            const s = Math.floor(sec % 60);
            return (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
        }}

        // 3. Real-Time UI Synchronizer (Runs purely in browser JS - NO Streamlit Python reruns!)
        window.parent.__farewellUpdateMusicUI = function() {{
            const audio = window.parent.__farewellGetAudio();
            const isPaused = !audio || audio.paused;

            // 1. All Play/Pause buttons (Top-Center Player, Sidebar, etc.)
            const playBtns = pDoc.querySelectorAll('#musicBtnPlayPause, .tc-music-playpause, .music-ctrl-playpause-glow');
            playBtns.forEach(btn => {{
                btn.innerHTML = isPaused ? '▶' : '❚❚';
                btn.title = isPaused ? 'Start Music' : 'Pause Music';
            }});

            // 2. All Stop / Start Pill Buttons
            const stopStartBtns = pDoc.querySelectorAll('#musicBtnStopStart, .music-stop-start-pill');
            stopStartBtns.forEach(btn => {{
                const icon = btn.querySelector('#musicBtnStopStartIcon') || btn.querySelector('span:first-child');
                const text = btn.querySelector('#musicBtnStopStartText') || btn.querySelector('span:last-child');
                if (icon) icon.textContent = isPaused ? '▶' : '⏸';
                if (text) text.textContent = isPaused ? 'Start Music' : 'Stop Music';
                btn.classList.toggle('is-stopped', isPaused);
                btn.title = isPaused ? 'Click to Start Music' : 'Click to Stop Music';
            }});

            // 3. All Timeline, Time Text & Track Seekers
            if (audio) {{
                const curTimes = pDoc.querySelectorAll('#musicTimeCurrent, .music-time-current');
                curTimes.forEach(el => {{ el.textContent = fmtTime(audio.currentTime); }});

                if (audio.duration && !isNaN(audio.duration)) {{
                    const totTimes = pDoc.querySelectorAll('#musicTimeTotal, .music-time-total');
                    totTimes.forEach(el => {{ el.textContent = fmtTime(audio.duration); }});

                    const pct = Math.min(100, Math.max(0, (audio.currentTime / audio.duration) * 100));
                    const fills = pDoc.querySelectorAll('#musicProgressFill, .music-progress-fill, .tc-music-fill');
                    fills.forEach(f => {{ f.style.width = pct + '%'; }});

                    const dots = pDoc.querySelectorAll('#musicProgressDot, .music-progress-dot, .tc-music-dot');
                    dots.forEach(d => {{ d.style.left = pct + '%'; }});
                }}
            }}
        }};

        // 4. Guaranteed Audio Toggle Function
        window.parent.__farewellToggleAudio = function() {{
            const audio = window.parent.__farewellGetAudio();
            if (!audio) {{
                console.warn('Farewell: No audio element available on document.');
                return;
            }}
            if (audio.paused) {{
                audio.play().then(() => {{
                    try {{ localStorage.setItem('farewell_music_paused', 'false'); }} catch(e) {{}}
                    if (window.parent.__farewellUpdateMusicUI) {{
                        window.parent.__farewellUpdateMusicUI();
                    }}
                }}).catch(err => {{
                    console.error('Audio play error:', err);
                }});
            }} else {{
                audio.pause();
                try {{ localStorage.setItem('farewell_music_paused', 'true'); }} catch(e) {{}}
                if (window.parent.__farewellUpdateMusicUI) {{
                    window.parent.__farewellUpdateMusicUI();
                }}
            }}
        }};

        // 5. Rewind & Fast-Forward
        window.parent.__farewellRewind = function() {{
            const a = window.parent.__farewellGetAudio();
            if (a) {{
                a.currentTime = Math.max(0, a.currentTime - 10);
                window.parent.__farewellUpdateMusicUI();
            }}
        }};

        window.parent.__farewellForward = function() {{
            const a = window.parent.__farewellGetAudio();
            if (a && a.duration) {{
                a.currentTime = Math.min(a.duration, a.currentTime + 10);
                window.parent.__farewellUpdateMusicUI();
            }}
        }};

        // 6. Global Navigation Triggers (Reliable, fast, and instant 0.0ms analyzer overlay)
        window.parent.__farewellShowInstantAnalyzer = function(chapterId, mode) {{
            try {{
                let overlay = pDoc.getElementById('instantNavAnalyzerOverlay');
                if (!overlay) {{
                    overlay = pDoc.createElement('div');
                    overlay.id = 'instantNavAnalyzerOverlay';
                    overlay.className = 'section-analyzer-backdrop';
                    overlay.style.cssText = 'position:fixed!important;top:0!important;left:0!important;width:100vw!important;height:100vh!important;z-index:99999999!important;display:flex!important;flex-direction:column!important;justify-content:center!important;align-items:center!important;background:radial-gradient(circle at center, #1e131d 0%, #0a070a 100%)!important;';
                    pDoc.body.appendChild(overlay);
                }}

                let title = "Opening Chapter...";
                let sub = "Agla safha khul raha hai...";
                let icon = "✦";
                let quote = "“Har safha dil se likhi yaadon aur sachche jazbaat se sajjaya gaya hai.”";

                const chapMap = {{
                    'home': {{ label: 'Story Overview', icon: '🏠' }},
                    'welcome': {{ label: 'Welcome', icon: '♡' }},
                    'memories': {{ label: 'Memories', icon: '🖼️' }},
                    'words': {{ label: 'Words From My Heart', icon: '🪶' }},
                    'respect': {{ label: 'Why I Respect You', icon: '⭐' }},
                    'intentions': {{ label: 'Intentions', icon: '💝' }},
                    'dua': {{ label: 'Dua', icon: '🤲' }},
                    'goodbye': {{ label: 'Final Note', icon: '✉️' }}
                }};

                if (mode === 'journey_start') {{
                    icon = '✦';
                    title = '✦ Journey Starting...';
                    sub = 'Hamara safar shuru ho raha hai...';
                    quote = '“Kuch alvida asal mein khatam nahi hotay, wo bas khoobsurat yaadon ki shuruat ban jatay hain.”';
                }} else if (mode === 'back_to_menu') {{
                    icon = '✦';
                    title = 'Going back to journey...';
                    sub = 'Hamari kahani ke safhay par wapis ja rahe hain...';
                    quote = '“Har safha dil se likhi yaadon aur sachche jazbaat se sajjaya gaya hai.”';
                }} else if (mode === 'prev') {{
                    const item = chapMap[chapterId] || {{ label: 'Previous Chapter', icon: '✦' }};
                    icon = item.icon;
                    title = `Back to ${{item.label}}...`;
                    sub = 'Opening previous chapter...';
                }} else {{
                    const item = chapMap[chapterId] || {{ label: 'Next Chapter', icon: '✦' }};
                    icon = item.icon;
                    title = `Opening: ${{item.label}}...`;
                    sub = 'Agla safha khul raha hai...';
                }}

                overlay.innerHTML = `
                    <div class="section-analyzer-orb">${{icon}}</div>
                    <div class="section-analyzer-title">${{title}}</div>
                    <div class="section-analyzer-sub">${{sub}}</div>
                    <div class="section-analyzer-track"><div class="section-analyzer-fill"></div></div>
                    <div class="section-analyzer-quote">${{quote}}</div>
                `;
                overlay.style.display = 'flex';
            }} catch(e) {{}}
        }};

        try {{
            const curInstant = pDoc.getElementById('instantNavAnalyzerOverlay');
            if (curInstant) {{
                curInstant.remove();
            }}
        }} catch(e) {{}}

        window.parent.__farewellResetScroll = function() {{
            try {{ window.parent.scrollTo({{ top: 0, left: 0, behavior: 'instant' }}); }} catch(e) {{ try {{ window.parent.scrollTo(0, 0); }} catch(e) {{}} }}
            try {{ if (pDoc.documentElement) pDoc.documentElement.scrollTop = 0; }} catch(e) {{}}
            try {{ if (pDoc.body) pDoc.body.scrollTop = 0; }} catch(e) {{}}
            try {{
                pDoc.querySelectorAll('[data-testid="stMain"], [data-testid="stAppViewContainer"], section.main, .main, .main .block-container').forEach(el => {{ el.scrollTop = 0; }});
            }} catch(e) {{}}
        }};

        function clickStreamlitBridge(keyId, textId) {{
            // 1. Check parent doc and local doc by class
            let btn = pDoc.querySelector(`.st-key-${{keyId}} button`) ||
                      pDoc.querySelector(`div[class*="${{keyId}}"] button`) ||
                      pDoc.querySelector(`button[key="${{keyId}}"]`) ||
                      document.querySelector(`.st-key-${{keyId}} button`);
            if (btn) {{
                btn.click();
                return true;
            }}
            // 2. Iterate all buttons across parent document
            const allBtns = pDoc.querySelectorAll('button');
            for (let b of allBtns) {{
                const txt = (b.innerText || b.textContent || '').trim();
                if (txt === textId || txt.includes(textId)) {{
                    b.click();
                    return true;
                }}
            }}
            return false;
        }}

        window.parent.__farewellStartJourney = function() {{
            // 1. Play audio starting from 00:00 using direct user gesture token
            const audio = window.parent.__farewellGetAudio();
            if (audio) {{
                try {{
                    audio.currentTime = 0;
                    audio.volume = 0.22;
                    audio.play().then(() => {{
                        try {{ localStorage.setItem('farewell_music_paused', 'false'); }} catch(e) {{}}
                        if (window.parent.__farewellUpdateMusicUI) {{
                            window.parent.__farewellUpdateMusicUI();
                        }}
                    }}).catch(e => console.log("Audio play initiated on Start Journey:", e));
                }} catch(e) {{}}
            }}

            window.parent.__farewellShowInstantAnalyzer(null, 'journey_start');
            const container = pDoc.querySelector('.v2-main-wrap, .landing-page-wrap');
            if (container) {{ container.classList.add('view-exit'); }}
            window.parent.__farewellResetScroll();
            clickStreamlitBridge('_bridge_menu', 'bridge_go_menu');
        }};

        window.parent.__farewellGoToMenu = function() {{
            window.parent.__farewellShowInstantAnalyzer(null, 'back_to_menu');
            const container = pDoc.querySelector('.v2-chapter-container, .v2-main-wrap');
            if (container) {{ container.classList.add('view-exit'); }}
            window.parent.__farewellResetScroll();
            clickStreamlitBridge('_bridge_back_to_menu', 'bridge_back_to_menu');
        }};

        window.parent.__farewellGoToLanding = function() {{
            const container = pDoc.querySelector('.v2-chapter-container, .v2-main-wrap');
            if (container) {{ container.classList.add('view-exit'); }}
            window.parent.__farewellResetScroll();
            clickStreamlitBridge('_bridge_landing', 'bridge_go_landing');
        }};

        window.parent.__farewellNav = function(chapterId) {{
            if (!chapterId) return;
            window.parent.__farewellShowInstantAnalyzer(chapterId, 'next');
            const container = pDoc.querySelector('.v2-chapter-container, .v2-main-wrap');
            if (container) {{ container.classList.add('view-exit'); }}
            window.parent.__farewellResetScroll();
            clickStreamlitBridge(`_bridge_${{chapterId}}`, `bridge_go_${{chapterId}}`);
        }};

        window.parent.__farewellCloseFinalModal = function() {{
            window.parent.__farewellResetScroll();
            clickStreamlitBridge('_bridge_close_final_modal', 'bridge_close_final_modal');
        }};

        window.parent.__farewellCloseRespectModal = function() {{
            window.parent.__farewellResetScroll();
            clickStreamlitBridge('_bridge_close_respect_modal', 'bridge_close_respect_modal');
        }};

        // 7. Global Event Delegation on Parent Document (Intercepts clicks regardless of Streamlit DOM updates)
        if (window.parent.__farewellClickDelegation) {{
            pDoc.removeEventListener('click', window.parent.__farewellClickDelegation, true);
        }}

        window.parent.__farewellClickDelegation = function(e) {{
            const target = e.target;
            if (!target) return;

            const closeFinalModalTrigger = target.closest('.final-spotlight-close-btn, #finalSpotlightModalOverlay');
            if (closeFinalModalTrigger && (target.id === 'finalSpotlightModalOverlay' || target.closest('.final-spotlight-close-btn'))) {{
                e.preventDefault();
                e.stopPropagation();
                window.parent.__farewellCloseFinalModal();
                return;
            }}

            const closeRespectTrigger = target.closest('.respect-spotlight-close-btn, #respectSpotlightModalOverlay');
            if (closeRespectTrigger && (target.id === 'respectSpotlightModalOverlay' || target.closest('.respect-spotlight-close-btn'))) {{
                e.preventDefault();
                e.stopPropagation();
                window.parent.__farewellCloseRespectModal();
                return;
            }}

            const startJourneyBtn = target.closest('#heroStartJourneyBtn, .hero-btn-primary');
            if (startJourneyBtn) {{
                e.preventDefault();
                e.stopPropagation();
                window.parent.__farewellStartJourney();
                return;
            }}

            const backIntro = target.closest('#btnBackIntro, .bottom-back-btn, [data-action="landing"], .sidebar-brand-wrapper');
            if (backIntro) {{
                e.preventDefault();
                e.stopPropagation();
                window.parent.__farewellGoToLanding();
                return;
            }}

            const card = target.closest('.ref-card, .journey-card, [data-chapter]');
            if (card) {{
                const chap = card.getAttribute('data-chapter');
                if (chap) {{
                    e.preventDefault();
                    e.stopPropagation();
                    window.parent.__farewellNav(chap);
                    return;
                }}
            }}

            const stopStart = target.closest('#musicBtnStopStart');
            const playPause = target.closest('#musicBtnPlayPause, .tc-music-playpause, .music-ctrl-playpause-glow');
            const prevBtn = target.closest('#musicBtnPrev, .tc-music-btn:first-child, .music-btn-prev');
            const nextBtn = target.closest('#musicBtnNext, .tc-music-btn:last-child, .music-btn-next');
            const heartBtn = target.closest('#tcMusicHeart, #musicBtnHeart, .music-ctrl-heart, .tc-music-heart');
            const track = target.closest('#musicProgressTrack, .tc-music-track, .music-progress-track');

            if (playPause || stopStart) {{
                e.preventDefault();
                e.stopPropagation();
                window.parent.__farewellToggleAudio();
                return;
            }}

            if (prevBtn) {{
                e.preventDefault();
                e.stopPropagation();
                window.parent.__farewellRewind();
                return;
            }}

            if (nextBtn) {{
                e.preventDefault();
                e.stopPropagation();
                window.parent.__farewellForward();
                return;
            }}

            if (heartBtn) {{
                e.preventDefault();
                e.stopPropagation();
                const isFav = heartBtn.classList.toggle('favorited');
                heartBtn.textContent = isFav ? '♥' : '♡';
                heartBtn.style.color = isFav ? '#E96582' : '#C9B7B5';
                return;
            }}

            if (track) {{
                e.preventDefault();
                e.stopPropagation();
                const a = window.parent.__farewellGetAudio();
                if (a && a.duration) {{
                    const rect = track.getBoundingClientRect();
                    const clickX = e.clientX - rect.left;
                    const pct = Math.max(0, Math.min(1, clickX / rect.width));
                    a.currentTime = pct * a.duration;
                    window.parent.__farewellUpdateMusicUI();
                }}
                return;
            }}
        }};

        pDoc.addEventListener('click', window.parent.__farewellClickDelegation, true);

        // 8. Attach audio event listeners & auto-mount audio element in post-journey view
        const isJourneyView = ('{active_view}' === 'journey_menu' || '{active_view}' === 'section' || '{active_view}' === 'menu');
        
        if (isJourneyView) {{
            let audio = window.parent.__farewellGetAudio();
            if (!audio) {{
                audio = pDoc.createElement('audio');
                audio.id = 'farewellBgAudioMain';
                audio.loop = true;
                audio.preload = 'auto';
                audio.innerHTML = '<source src="app/static/farewell.mp3" type="audio/mp3"><source src="static/farewell.mp3" type="audio/mp3"><source src="/app/static/farewell.mp3" type="audio/mp3">';
                try {{ if (pDoc.body) pDoc.body.appendChild(audio); }} catch(e) {{ document.body.appendChild(audio); }}
                window.parent.__farewell_audio = audio;
            }}

            if (audio) {{
                audio.onplay = () => window.parent.__farewellUpdateMusicUI();
                audio.onpause = () => window.parent.__farewellUpdateMusicUI();
                audio.ontimeupdate = () => window.parent.__farewellUpdateMusicUI();

                const isMuted = (localStorage.getItem('farewell_music_paused') === 'true');
                if (audio.paused && !isMuted) {{
                    audio.volume = 0.22;
                    audio.play().then(() => {{
                        if (window.parent.__farewellUpdateMusicUI) {{
                            window.parent.__farewellUpdateMusicUI();
                        }}
                    }}).catch(err => {{
                        console.warn('Autoplay initiated in journey:', err);
                    }});
                }}
            }}
        }} else {{
            // On landing, guarantee 100% complete silence
            const audio = window.parent.__farewellGetAudio();
            if (audio && !audio.paused) {{
                try {{ audio.pause(); audio.currentTime = 0; }} catch(e) {{}}
            }}
        }}

        // Initial sync
        window.parent.__farewellUpdateMusicUI();

        // Continuous sync loop on parent window
        if (!window.parent.__farewellSyncInterval) {{
            window.parent.__farewellSyncInterval = setInterval(() => {{
                if (window.parent.__farewellUpdateMusicUI) {{
                    window.parent.__farewellUpdateMusicUI();
                }}
            }}, 300);
        }}

        // 9. Load Three.js and Farewell 3D WebGL Engine
        function inject3DEngine() {{
            if (!pDoc.getElementById('farewell3DScript')) {{
                const s3d = pDoc.createElement('script');
                s3d.id = 'farewell3DScript';
                s3d.textContent = {three_d_json};
                pDoc.body.appendChild(s3d);
            }}
            if (window.parent.__farewellSet3DChapter) {{
                window.parent.__farewellSet3DChapter('{active_3d}');
            }}
        }}

        if (!window.parent.THREE) {{
            const threeScript = pDoc.createElement('script');
            threeScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
            threeScript.onload = function() {{
                inject3DEngine();
            }};
            pDoc.head.appendChild(threeScript);
        }} else {{
            inject3DEngine();
        }}

        // 10. Scroll & Mouse Parallax Bridge
        function setupScrollAndParallax() {{
            function handleScroll() {{
                const docEl = pDoc.documentElement || pDoc.body;
                const scrollTop = window.parent.pageYOffset || docEl.scrollTop || 0;
                const maxScroll = (docEl.scrollHeight || 1) - (window.parent.innerHeight || 1);
                const progress = maxScroll > 0 ? Math.max(0, Math.min(1, scrollTop / maxScroll)) : 0;
                if (window.parent.__farewellOnScroll) {{
                    window.parent.__farewellOnScroll(progress);
                }}
            }}

            window.parent.addEventListener('scroll', handleScroll, {{ passive: true }});
            pDoc.addEventListener('scroll', handleScroll, {{ passive: true }});

            const scrollContainers = pDoc.querySelectorAll('[data-testid="stMain"], [data-testid="stAppViewContainer"], .main');
            scrollContainers.forEach(el => el.addEventListener('scroll', handleScroll, {{ passive: true }}));
        }}

        setupScrollAndParallax();

        if (window.parent.__farewellSet3DChapter) {{
            window.parent.__farewellSet3DChapter('{active_3d}');
        }}
    }})();
    </script>
    """,
        height=0,
        width=0,
    )


# -----------------------------------------------------------------------------
# 7. Multi-Container Scroll Reset to Top
# -----------------------------------------------------------------------------
def reset_scroll_to_top():
    """Scroll parent window and all Streamlit scroll containers to the top."""
    components.html(
        """
    <script>
    (function() {
        const p = window.parent;
        const pDoc = p.document;

        if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
        if (p && 'scrollRestoration' in p.history) p.history.scrollRestoration = 'manual';

        function doScroll() {
            const scrollTargets = [
                window,
                p,
                document.documentElement,
                document.body,
                pDoc.documentElement,
                pDoc.body,
                pDoc.querySelector('[data-testid="stAppViewContainer"]'),
                pDoc.querySelector('.main'),
                pDoc.querySelector('[data-testid="stMain"]'),
                pDoc.querySelector('.main .block-container')
            ];
            scrollTargets.forEach(target => {
                if (target && typeof target.scrollTo === 'function') {
                    try { target.scrollTo({ top: 0, left: 0, behavior: 'instant' }); } catch(e) { try { target.scrollTo(0, 0); } catch(e) {} }
                }
                if (target && 'scrollTop' in target) {
                    try { target.scrollTop = 0; } catch(e) {}
                }
            });
            try {
                const selectors = [
                    '[data-testid="stMain"]',
                    '[data-testid="stAppViewContainer"]',
                    '[data-testid="stMainBlockContainer"]',
                    '.main',
                    'section.main',
                    '.main .block-container'
                ];
                selectors.forEach(sel => {
                    pDoc.querySelectorAll(sel).forEach(el => { el.scrollTop = 0; });
                });
            } catch(e) {}
        }
        doScroll();
        requestAnimationFrame(doScroll);
        setTimeout(doScroll, 20);
        setTimeout(doScroll, 60);
        setTimeout(doScroll, 120);
        setTimeout(doScroll, 250);
        setTimeout(doScroll, 450);
    })();
    </script>
    """,
        height=0,
        width=0,
    )


# -----------------------------------------------------------------------------
# 8. Navigation Transitions: Journey Loader & Section Router
# -----------------------------------------------------------------------------
def render_journey_analyzer_loader():
    """Journey Transition Analyzer (Start the Journey Par)"""
    reset_scroll_to_top()
    ui("""
    <style>
    .cinematic-loader-backdrop {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background: radial-gradient(circle at center, #1e131d 0%, #0a070a 100%) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        z-index: 99999999 !important;
        text-align: center !important;
        padding: 2rem !important;
    }
    .loader-heart-orb {
        width: 70px !important;
        height: 70px !important;
        border-radius: 50% !important;
        background: radial-gradient(circle, rgba(244, 143, 177, 0.25) 0%, transparent 70%) !important;
        border: 2px solid rgba(244, 143, 177, 0.6) !important;
        box-shadow: 0 0 25px rgba(244, 143, 177, 0.45) !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        font-size: 28px !important;
        animation: orbPulse 1.6s ease-in-out infinite alternate !important;
        margin: 0 auto 24px auto !important;
    }
    @keyframes orbPulse {
        0% { transform: scale(0.92); box-shadow: 0 0 15px rgba(244, 143, 177, 0.3); }
        100% { transform: scale(1.08); box-shadow: 0 0 35px rgba(244, 143, 177, 0.7); }
    }
    .analyzer-track {
        width: 280px !important;
        height: 4px !important;
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 999px !important;
        overflow: hidden !important;
        position: relative !important;
        margin: 20px auto 14px auto !important;
    }
    .analyzer-glow-fill {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        height: 100% !important;
        width: 100% !important;
        background: linear-gradient(90deg, #e2557e, #f78da7, #ffffff) !important;
        border-radius: 999px !important;
        animation: analyzerFill 2.0s cubic-bezier(0.16, 1, 0.3, 1) infinite !important;
    }
    @keyframes analyzerFill {
        0% { transform: translateX(-100%); }
        60% { transform: translateX(0%); }
        100% { transform: translateX(100%); }
    }
    .loader-title-glow {
        color: #ffffff !important;
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: 1.65rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        margin-bottom: 6px !important;
        text-shadow: 0 0 18px rgba(244, 143, 177, 0.4) !important;
    }
    .loader-sub-glow {
        color: #f7a8b8 !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 1.05rem !important;
        letter-spacing: 0.2px !important;
        margin-bottom: 12px !important;
        font-style: italic !important;
    }
    .loader-quote-glow {
        color: #9d8c96 !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 0.85rem !important;
        max-width: 440px !important;
        line-height: 1.5 !important;
        font-style: italic !important;
        margin: 0 auto !important;
    }
    </style>
    <div class="cinematic-loader-backdrop">
        <div class="loader-heart-orb">✦</div>
        <div class="loader-title-glow">Journey Starting...</div>
        <div class="loader-sub-glow">Hamara safar shuru ho raha hai...</div>
        <div class="analyzer-track"><div class="analyzer-glow-fill"></div></div>
        <div class="loader-quote-glow">
            “Kuch alvida asal mein khatam nahi hotay, wo bas khoobsurat yaadon ki shuruat ban jatay hain.”
        </div>
    </div>
    """)


def render_journey_loader():
    """Alias for render_journey_analyzer_loader."""
    render_journey_analyzer_loader()


# -----------------------------------------------------------------------------
# 8. Dedicated Dynamic Transition Analyzers (All Navigation Directions)
# -----------------------------------------------------------------------------
def render_dynamic_transition_analyzer(target_id: str = None, mode: str = "next"):
    """
    Render dedicated 1.0s dynamic Transition Analyzer for any navigation flow:
    - mode="next": "Opening: [Chapter Title]..." / "Agla safha khul raha hai..."
    - mode="prev": "Back to [Chapter Title]..." / "Opening previous chapter..."
    - mode="back_to_menu": "Going back to journey..." / "Returning to chapters overview..."
    - mode="journey_start": "✦ Journey Starting..." / "Hamara safar shuru ho raha hai..."
    """
    reset_scroll_to_top()
    target_label = "Chapter"
    target_icon = "✦"
    subtitle = "Agla safha khul raha hai..."
    quote = "“Har safha dil se likhi yaadon aur sachche jazbaat se sajjaya gaya hai.”"

    if target_id:
        for c in config.CHAPTERS:
            if c["id"] == target_id:
                target_label = c["label"]
                target_icon = c.get("icon", "✦")
                break

    if mode == "journey_start":
        target_icon = "✦"
        title = "✦ Journey Starting..."
        subtitle = "Hamara safar shuru ho raha hai..."
        quote = "“Kuch alvida asal mein khatam nahi hotay, wo bas khoobsurat yaadon ki shuruat ban jatay hain.”"
    elif mode == "back_to_menu":
        target_icon = "✦"
        title = "Going back to journey..."
        subtitle = "Hamari kahani ke safhay par wapis ja rahe hain..."
        quote = "“Har safha dil se likhi yaadon aur sachche jazbaat se sajjaya gaya hai.”"
    elif mode == "prev":
        title = f"Back to {target_label}..."
        subtitle = "Opening previous chapter..."
        quote = "“Pichhli yaadein aur khoobsurat lamhe...”"
    else:
        title = f"Opening: {target_label}..."
        subtitle = "Agla safha khul raha hai..."
        quote = "“Har safha dil se likhi yaadon aur sachche jazbaat se sajjaya gaya hai.”"

    ui(f"""
    <style>
    .section-analyzer-backdrop {{
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background: radial-gradient(circle at center, #1e131d 0%, #0a070a 100%) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        z-index: 99999999 !important;
        text-align: center !important;
        padding: 2rem !important;
    }}
    .section-analyzer-orb {{
        width: 64px !important;
        height: 64px !important;
        border-radius: 50% !important;
        background: radial-gradient(circle, rgba(244, 143, 177, 0.25) 0%, transparent 70%) !important;
        border: 2px solid rgba(244, 143, 177, 0.6) !important;
        box-shadow: 0 0 25px rgba(244, 143, 177, 0.45) !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        font-size: 26px !important;
        animation: orbPulse 1.0s ease-in-out infinite alternate !important;
        margin: 0 auto 20px auto !important;
    }}
    .section-analyzer-title {{
        color: #ffffff !important;
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        font-size: 1.55rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em !important;
        margin-bottom: 6px !important;
        text-shadow: 0 0 18px rgba(244, 143, 177, 0.35);
    }}
    .section-analyzer-sub {{
        color: #e2a8b8 !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 0.95rem !important;
        margin-bottom: 14px !important;
        font-style: italic !important;
    }}
    .section-analyzer-track {{
        width: 240px !important;
        height: 4px !important;
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 999px !important;
        overflow: hidden !important;
        position: relative !important;
        margin: 0 auto 14px auto !important;
    }}
    .section-analyzer-fill {{
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        height: 100% !important;
        width: 100% !important;
        background: linear-gradient(90deg, #e2557e, #f78da7, #ffffff) !important;
        border-radius: 999px !important;
        animation: sectionAnalyzerFill 1.0s cubic-bezier(0.16, 1, 0.3, 1) infinite !important;
    }}
    @keyframes sectionAnalyzerFill {{
        0% {{ transform: translateX(-100%); }}
        60% {{ transform: translateX(0%); }}
        100% {{ transform: translateX(100%); }}
    }}
    .section-analyzer-quote {{
        color: #9d8c96 !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 0.85rem !important;
        max-width: 400px !important;
        line-height: 1.5 !important;
        font-style: italic !important;
        margin: 0 auto !important;
    }}
    </style>
    <div class="section-analyzer-backdrop">
        <div class="section-analyzer-orb">{target_icon}</div>
        <div class="section-analyzer-title">{title}</div>
        <div class="section-analyzer-sub">{subtitle}</div>
        <div class="section-analyzer-track">
            <div class="section-analyzer-fill"></div>
        </div>
        <div class="section-analyzer-quote">{quote}</div>
    </div>
    """)


def render_dynamic_section_analyzer(target_id: str):
    """Alias for render_dynamic_transition_analyzer with mode='next'."""
    render_dynamic_transition_analyzer(target_id=target_id, mode="next")


def render_section(section_id: str):
    """Render the requested section view with mutually exclusive layout."""
    sec = section_id or "welcome"
    if "visited_chapters" in st.session_state:
        st.session_state.visited_chapters.add(sec)

    # Mount Music Player inside Journey chapters
    render_top_center_music_player()

    router = {
        "home": render_home_overview,
        "welcome": render_welcome,
        "memories": render_memories,
        "words": render_words,
        "respect": render_respect,
        "intentions": render_intentions,
        "dua": render_dua,
        "goodbye": render_goodbye,
    }
    render_fn = router.get(sec, render_welcome)
    render_fn()


# -----------------------------------------------------------------------------
# 9. Sidebar Component (Permanently Disabled)
# -----------------------------------------------------------------------------
def render_sidebar():
    """Sidebar permanently suppressed to give 100% full-screen immersive view."""
    pass


# -----------------------------------------------------------------------------
# Navigation State Callbacks (Executed BEFORE script execution phase)
# -----------------------------------------------------------------------------
def on_navigate_next(target_id: str):
    """Callback to queue target section and trigger 1.0s forward transition analyzer."""
    st.session_state.pending_section = target_id
    st.session_state.nav_mode = "next"
    st.session_state.app_view = "transition"
    st.session_state.selected_memory = None


def on_navigate_prev(target_id: str):
    """Callback for previous chapter transition with 1.0s reverse analyzer."""
    st.session_state.pending_section = target_id
    st.session_state.nav_mode = "prev"
    st.session_state.app_view = "transition"
    st.session_state.selected_memory = None


def on_navigate_back_to_menu():
    """Callback to trigger 1.0s dedicated analyzer going back to Journey Menu."""
    st.session_state.pending_section = None
    st.session_state.nav_mode = "back_to_menu"
    st.session_state.app_view = "transition"
    st.session_state.selected_memory = None


def on_navigate_start_journey():
    """Callback to trigger 1.5s journey entry analyzer to Journey Menu."""
    st.session_state.pending_section = None
    st.session_state.nav_mode = "journey_start"
    st.session_state.app_view = "transition"
    st.session_state.music_started = True
    st.session_state.music_playing = True
    st.session_state.selected_memory = None


def on_navigate_preview(target_id: str):
    """Callback to transition into focused teaser preview card for next chapter."""
    st.session_state.pending_section = target_id
    st.session_state.app_view = "section_preview"
    st.session_state.selected_memory = None
    st.session_state.selected_respect_plate = None


def on_navigate_section(target_id: str):
    """Alias for forward navigation."""
    on_navigate_next(target_id)


def on_navigate_menu():
    """Alias for returning to journey menu."""
    on_navigate_back_to_menu()


def on_navigate_landing():
    """Callback to return directly to Landing Screen."""
    st.session_state.app_view = "landing"
    st.session_state.active_section = None
    st.session_state.selected_memory = None


def on_reveal_final_words():
    """Callback to open centered spotlight final modal."""
    st.session_state["show_final_words"] = True


def on_close_final_words():
    """Callback to close centered spotlight final modal."""
    st.session_state["show_final_words"] = False


def on_close_respect_plate():
    """Callback to close centered spotlight respect modal."""
    st.session_state["selected_respect_plate"] = None


# -----------------------------------------------------------------------------
# 11. Bottom Navigation Bar (Back to Journey & Next Preview Button)
# -----------------------------------------------------------------------------
def render_chapter_footer(current_id: str):
    """Render clean navigation footer with Back to Journey and Next Preview buttons."""
    chapter_ids = [c["id"] for c in config.CHAPTERS]
    curr_idx = chapter_ids.index(current_id) if current_id in chapter_ids else 0
    next_id = chapter_ids[curr_idx + 1] if curr_idx + 1 < len(chapter_ids) else None
    next_label = None
    if next_id:
        for c in config.CHAPTERS:
            if c["id"] == next_id:
                next_label = c["label"]
                break

    ui("""
    <div class="chapter-footer-divider"></div>
    <div class="chapter-footer-nav-wrap">
    """)

    if next_id and next_label:
        bcol1, bcol2 = st.columns([1, 1], gap="medium")
        with bcol1:
            st.button(
                "← Back to Journey",
                key=f"foot_back_{current_id}",
                type="secondary",
                use_container_width=True,
                on_click=on_navigate_back_to_menu,
            )
        with bcol2:
            st.button(
                f"Next: {next_label} →",
                key=f"foot_next_{current_id}",
                type="primary",
                use_container_width=True,
                on_click=on_navigate_preview,
                args=(next_id,),
            )
    else:
        bcol1, bcol2, bcol3 = st.columns([1, 1.8, 1])
        with bcol2:
            st.button(
                "← Back to Journey",
                key=f"foot_back_{current_id}",
                type="secondary",
                use_container_width=True,
                on_click=on_navigate_back_to_menu,
            )

    ui("</div>")


# -----------------------------------------------------------------------------
# INVISIBLE STREAMLIT BRIDGE DISPATCHER (Zero-latency Programmatic Clicks)
# -----------------------------------------------------------------------------
def render_hidden_bridge_dispatcher():
    """Invisible Streamlit button dispatcher that handles programmatic clicks from JS without reloading the page."""
    with st.container():
        st.markdown(
            """
            <style>
            .st-key-_bridge_landing, .st-key-_bridge_menu, .st-key-_bridge_back_to_menu, .st-key-_bridge_close_final_modal, .st-key-_bridge_close_respect_modal,
            [class*="st-key-_bridge_"],
            div[data-testid="stElementContainer"]:has([class*="st-key-_bridge_"]),
            div[data-testid="stElementContainer"]:has(button[key*="_bridge_"]),
            div[data-testid="stElementContainer"]:has(button[title="bridge_hidden"]),
            div.stButton:has(button[key*="_bridge_"]),
            div.stButton:has(button[title="bridge_hidden"]),
            button[key*="_bridge_"],
            button[title="bridge_hidden"] {
                position: absolute !important;
                top: -9999px !important;
                left: -9999px !important;
                width: 1px !important;
                height: 1px !important;
                padding: 0 !important;
                margin: 0 !important;
                border: none !important;
                opacity: 0 !important;
                pointer-events: auto !important;
                overflow: hidden !important;
                clip: rect(0, 0, 0, 0) !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        c = st.columns(1)[0]
        with c:
            st.button("bridge_go_landing", key="_bridge_landing", help="bridge_hidden", on_click=on_navigate_landing)
            st.button("bridge_go_menu", key="_bridge_menu", help="bridge_hidden", on_click=on_navigate_start_journey)
            st.button("bridge_back_to_menu", key="_bridge_back_to_menu", help="bridge_hidden", on_click=on_navigate_back_to_menu)
            st.button("bridge_close_final_modal", key="_bridge_close_final_modal", help="bridge_hidden", on_click=on_close_final_words)
            st.button("bridge_close_respect_modal", key="_bridge_close_respect_modal", help="bridge_hidden", on_click=on_close_respect_plate)

            for chap in config.CHAPTERS:
                st.button(
                    f"bridge_go_{chap['id']}",
                    key=f"_bridge_{chap['id']}",
                    help="bridge_hidden",
                    on_click=on_navigate_next,
                    args=(chap["id"],),
                )


# -----------------------------------------------------------------------------
# TOP-CENTER FULL MUSIC PLAYER (Mounted ONLY inside Journey & Chapters)
# -----------------------------------------------------------------------------
def render_top_center_music_player():
    """Render full horizontal music player at top-center (Song, Artist, Scrub Bar, Time, Controls)."""
    ui(f"""
    <div class="top-center-music-container">
        <div class="top-center-music-player" id="topCenterMusicPlayer">
            <div class="tc-music-header">
                <div class="tc-music-info">
                    <span class="tc-music-note">🎵</span>
                    <div class="tc-music-titles">
                        <span class="tc-music-title">{config.AUDIO_CONFIG["song_title"]}</span>
                        <span class="tc-music-artist">{config.AUDIO_CONFIG["song_artist"]}</span>
                    </div>
                </div>
                <span class="tc-music-heart" id="tcMusicHeart" title="Favorite">♡</span>
            </div>
            <div class="tc-music-timeline">
                <span class="tc-music-time" id="musicTimeCurrent">00:00</span>
                <div class="tc-music-track" id="musicProgressTrack" title="Click to seek track">
                    <div class="tc-music-fill" id="musicProgressFill" style="width: 0%;"></div>
                    <span class="tc-music-dot" id="musicProgressDot" style="left: 0%;"></span>
                </div>
                <span class="tc-music-time" id="musicTimeTotal">04:58</span>
            </div>
            <div class="tc-music-controls">
                <button class="tc-music-btn" id="musicBtnPrev" title="Rewind 10s">⏮</button>
                <button class="tc-music-playpause" id="musicBtnPlayPause" title="Play / Pause">❚❚</button>
                <button class="tc-music-btn" id="musicBtnNext" title="Forward 10s">⏭</button>
            </div>
        </div>
    </div>
    """)


# -----------------------------------------------------------------------------
# STATE 1 — LANDING / INTRO SCREEN
# -----------------------------------------------------------------------------
def render_landing():
    """Render STATE 1: Pure Cinematic Hero Intro Screen (Zero Audio & Zero Music Player on Landing)."""
    reset_scroll_to_top()
    c = content.HOME_SECTION
    banner_b64 = get_hero_panorama_b64()

    # 1. Initial Splash Overlay (Zero-latency 2.5s dissolve on first load / refresh)
    if not st.session_state.get("initial_splash_done", False):
        render_initial_splash_loader()
        st.session_state["initial_splash_done"] = True
        st.session_state["startup_completed"] = True

    visited_set = st.session_state.get("visited_chapters", set())
    visited_pct = int((len(visited_set) / len(config.CHAPTERS)) * 100)
    hero_pct = max(12, visited_pct)

    # 2. Pure Panoramic Hero Stage (No Music Player on Landing Screen)
    ui(f"""
    <div class="v2-main-wrap landing-page-wrap landing-mount-enter">
        <div class="hero-panoramic-card">
            <img src="data:image/jpeg;base64,{banner_b64}" class="hero-panoramic-bg-img" alt="A Farewell That Stays">
            
            <!-- Atmospheric Layers -->
            <div class="hero-panoramic-gradient-overlay"></div>
            <div class="hero-atmospheric-haze"></div>
            <div class="hero-horizon-sweep"></div>
            
            <!-- Left Typography Overlay -->
            <div class="hero-left-overlay">
                <div class="hero-heart-doodle">♡</div>
                <h1 class="hero-headline">
                    A Farewell<br>
                    <span class="hero-cursive">That Stays</span><br>
                    in the Heart
                </h1>
                <p class="hero-subtitle">
                    Kuch alvida asal mein khatam nahi hotay,<br>
                    wo bas khoobsurat yaadon ki shuruat ban jatay hain.
                </p>
                <div class="hero-action-buttons">
                    <button class="hero-btn-primary hero-cta-button pulsing-cta" id="heroStartJourneyBtn" onclick="window.parent.__farewellStartJourney && window.parent.__farewellStartJourney()">
                        <span class="btn-heart-glyph">♡</span> Start My Journey
                    </button>
                </div>
            </div>

            <!-- Right Floating Memories Collected Stats Card -->
            <div class="hero-floating-stats-card floating-element">
                <div class="stats-card-heart-circle">
                    <span class="stats-card-heart">♡</span>
                </div>
                <div class="stats-card-title">Yaadein Mehfooz</div>
                <div class="stats-card-pct">{hero_pct}% Mukammal</div>
                <div class="stats-card-track">
                    <div class="stats-card-fill" style="width: {hero_pct}%;"></div>
                </div>
                <div class="stats-card-caption">Aage barhein... kuch khoobsurat yaadein ap ki muntazir hain.</div>
                <div class="stats-card-flower">🌸</div>
            </div>
        </div>
    </div>
    """)


# -----------------------------------------------------------------------------
# STATE 2 — MAIN JOURNEY MENU (Central Hub)
# -----------------------------------------------------------------------------
# STATE 2 — MAIN JOURNEY MENU (Central Hub)
# -----------------------------------------------------------------------------
def render_journey_menu():
    """Render STATE 2: Main Journey Menu / Central Hub matching exact reference image."""
    reset_scroll_to_top()
    c = content.HOME_SECTION

    # 1. Top-Center Full Music Player
    render_top_center_music_player()

    # 2. Header
    ui("""
    <div class="v2-main-wrap">
        <div class="journey-menu-header">
            <div class="journey-menu-badge">
                <span style="font-size: 13px; margin-right: 2px;">♡</span> A FAREWELL THAT STAYS
            </div>
            <h1 class="journey-menu-title">Hamari Kahani Ke Safhay</h1>
            <p class="journey-menu-subtitle">Har safha dil se likhi yaadon, sachche alfaaz aur duaon se sajaya gaya hai.</p>
        </div>
    """)

    # 3. Quotation Bar (Horizontal Glowing Dark Glass Strip)
    ui(f"""
        <div class="v2-quote-banner floating-element">
            <div class="v2-quote-left-motif">🌹</div>
            <div class="v2-quote-center-wrap">
                <span class="v2-quote-mark">“</span>
                <span class="v2-quote-text">{c['quote_bar']}</span>
            </div>
            <div class="v2-quote-right-motifs">
                <span class="v2-quote-heart-doodle">♡</span>
                <span class="v2-quote-branch">🌿</span>
                <span class="v2-quote-sparkle">✨</span>
            </div>
        </div>
    """)

    # 4. Chapter Cards Grid (Exact 6+2 Layout with Themed Pastel Keepsake Colors)
    t_home = get_thumbnail_b64("thumb_welcome")
    t_welcome = get_thumbnail_b64("thumb_respect")
    t_memories = get_thumbnail_b64("thumb_memories")
    t_words = get_thumbnail_b64("thumb_words")
    t_respect = get_thumbnail_b64("thumb_respect")
    t_intentions = get_thumbnail_b64("thumb_intentions")
    t_dua = get_thumbnail_b64("thumb_dua")
    t_goodbye = get_thumbnail_b64("thumb_goodbye")

    ui(f"""
        <div class="ref-cards-grid">
            <!-- Card 1: Story Overview -->
            <div class="ref-card ref-theme-1 floating-element" data-chapter="home" onclick="window.parent.__farewellNav('home')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_home}" class="ref-card-thumb" alt="Story Overview">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Story Overview</h3>
                    <p class="ref-card-desc">Hamari kahani ke woh lamhe jo hamesha dil...</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="home">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 2: Welcome -->
            <div class="ref-card ref-theme-2 floating-element" data-chapter="welcome" onclick="window.parent.__farewellNav('welcome')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_welcome}" class="ref-card-thumb" alt="Welcome">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Welcome</h3>
                    <p class="ref-card-desc">Jaane se pehle, ek baar ye khat zaroor parh...</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="welcome">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 3: Memories -->
            <div class="ref-card ref-theme-3 floating-element" data-chapter="memories" onclick="window.parent.__farewellNav('memories')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_memories}" class="ref-card-thumb" alt="Memories">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Memories</h3>
                    <p class="ref-card-desc">Woh khoobsurat lamhe jo waqt ke saath kabhi...</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="memories">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 4: Words From My Heart -->
            <div class="ref-card ref-theme-4 floating-element" data-chapter="words" onclick="window.parent.__farewellNav('words')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_words}" class="ref-card-thumb" alt="Words From My Heart">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Words From My Heart</h3>
                    <p class="ref-card-desc">Woh sachchi baatein jo main ap k saamne keh...</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="words">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 5: Why I Respect You -->
            <div class="ref-card ref-theme-5 floating-element" data-chapter="respect" onclick="window.parent.__farewellNav('respect')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_respect}" class="ref-card-thumb" alt="Why I Respect You">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Why I Respect You</h3>
                    <p class="ref-card-desc">Woh khoobian jin ki wajah se ap ki izzat...</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="respect">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 6: Intentions -->
            <div class="ref-card ref-theme-6 floating-element" data-chapter="intentions" onclick="window.parent.__farewellNav('intentions')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_intentions}" class="ref-card-thumb" alt="Intentions">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Intentions</h3>
                    <p class="ref-card-desc">Meri sachchi duaein aur iradey jo sirf ap ki...</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="intentions">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 7: Dua -->
            <div class="ref-card ref-theme-7 floating-element" data-chapter="dua" onclick="window.parent.__farewellNav('dua')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_dua}" class="ref-card-thumb" alt="Dua">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Dua</h3>
                    <p class="ref-card-desc">Tumhari khushi, sukoon aur kamyabi ke liye dil...</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="dua">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 8: Final Note -->
            <div class="ref-card ref-theme-8 floating-element" data-chapter="goodbye" onclick="window.parent.__farewellNav('goodbye')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_goodbye}" class="ref-card-thumb" alt="Final Note">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Final Note</h3>
                    <p class="ref-card-desc">Ek aakhri baat... mohabbat, izzat aur...</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="goodbye">Open →</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Return to Intro Button -->
        <div style="text-align: center; margin: 2rem 0 3.5rem 0;">
            <button class="bottom-back-intro-btn nav-action-btn floating-element" id="btnBackIntro" data-action="landing" onclick="window.parent.__farewellGoToLanding && window.parent.__farewellGoToLanding()">
                <span style="font-size: 15px; margin-right: 4px;">♡</span> Back to Intro Screen
            </button>
        </div>
    </div>
    """)


# -----------------------------------------------------------------------------
# TWO-STAGE DISCOVERY: RENDER SECTION PREVIEW (Teaser Card)
# -----------------------------------------------------------------------------
def render_section_preview():
    """Render focused single-card teaser preview before opening full chapter interface."""
    reset_scroll_to_top()
    render_top_center_music_player()

    target_id = st.session_state.get("pending_section") or "welcome"

    chap_title = "Upcoming Chapter"
    chap_desc = "Hamari kahani ka agla khoobsurat safha..."
    chap_icon = "✦"
    chap_thumb_key = f"thumb_{target_id}" if target_id != "home" else "thumb_welcome"

    for card in content.HOME_CARDS:
        if card["id"] == target_id:
            chap_title = card["title"]
            chap_desc = card["desc"]
            chap_thumb_key = card.get("thumb", chap_thumb_key)
            break

    for c in config.CHAPTERS:
        if c["id"] == target_id:
            chap_icon = c.get("icon", "✦")
            if not chap_title or chap_title == "Upcoming Chapter":
                chap_title = c["label"]
            break

    thumb_b64 = get_thumbnail_b64(chap_thumb_key)
    if not thumb_b64:
        thumb_b64 = get_thumbnail_b64("thumb_welcome")

    ui(f"""
    <div class="v2-main-wrap section-preview-container feature-section-enter section-floating-enter" key="sec_wrapper_preview" id="sec_wrapper_preview">
        <div class="chapter-eyebrow-badge preview-teaser-badge">✦ UPCOMING CHAPTER ✦</div>
        
        <div class="preview-teaser-card floating-element">
            <div class="preview-teaser-thumb-frame">
                <img src="data:image/png;base64,{thumb_b64}" class="preview-teaser-thumb-img" alt="{chap_title}">
            </div>
            
            <div class="preview-teaser-content">
                <div class="preview-teaser-icon-orb">{chap_icon}</div>
                <h2 class="preview-teaser-title">{chap_title}</h2>
                <p class="preview-teaser-desc">{chap_desc}</p>
            </div>
        </div>
    </div>
    """)

    ui('<div class="section-preview-btn-container">')
    pcol1, pcol2, pcol3 = st.columns([1, 1.2, 1])
    with pcol2:
        st.button(
            "Open →",
            key=f"preview_open_btn_{target_id}",
            type="primary",
            use_container_width=True,
            on_click=on_navigate_next,
            args=(target_id,),
        )

    scol1, scol2, scol3 = st.columns([1, 1.2, 1])
    with scol2:
        st.button(
            "← Back to Chapters Grid",
            key="preview_back_grid_btn",
            type="secondary",
            use_container_width=True,
            on_click=on_navigate_back_to_menu,
        )
    ui('</div>')


# -----------------------------------------------------------------------------
# STATE 3 — SECTION VIEW: HOME / OVERVIEW
# -----------------------------------------------------------------------------
def render_home_overview():
    """Render Story Overview & Reflections Section with luxury romantic editorial card."""
    reset_scroll_to_top()
    ui("""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_home" id="sec_wrapper_home" style="position: relative;">
        <!-- Atmospheric Drifting Embers -->
        <div class="story-starlight-layer">
            <div class="starlight-ember"></div>
            <div class="starlight-ember"></div>
            <div class="starlight-ember"></div>
            <div class="starlight-ember"></div>
        </div>

        <div class="chapter-eyebrow-badge">✦ HAMARI KAHANI KA SAFAR</div>
        <h2 class="chapter-main-title">A Farewell That Stays in the Heart</h2>
        <p class="chapter-subtitle-italic">Kuch alvida asal mein khatam nahi hotay — wo bas khoobsurat yaadon ki shuruat ban jatay hain.</p>
        
        <div class="editorial-story-card floating-element">
            <!-- Decorative Corner Botanical Flourishes -->
            <div class="card-corner-flourish corner-tl">🌸</div>
            <div class="card-corner-flourish corner-tr">🌿</div>
            <div class="card-corner-flourish corner-bl">🌿</div>
            <div class="card-corner-flourish corner-br">🌸</div>
            
            <!-- Faint Background Watermark -->
            <div class="editorial-watermark-decor">”</div>
            
            <!-- Card Top Motif -->
            <div class="story-card-top-motif">
                <div class="story-motif-line"></div>
                <span class="story-motif-heart">♡</span>
                <div class="story-motif-line"></div>
            </div>
            
            <!-- Main Body Paragraphs -->
            <div class="story-body-content">
                <p class="story-paragraph-text">Kuch log sirf zindagi ka hissa nahi bante… wo aadat ban jaate hain.</p>
                <p class="story-paragraph-text">Unki baatein, unki hansi, unka hona — sab kuch itna apna lagne lagta hai ke faasla aane ke baad bhi dil unhein chhor nahi pata.</p>
                <p class="story-paragraph-text">Shayad waqt ke saath sab kuch badal jaye, lekin kuch yaadein aisi hoti hain jo dil khud sambhal kar rakhta hai. Unhein na waqt mita pata hai, na faaslay kam kar pate hain.</p>
                <p class="story-paragraph-text">Is safar mein jo kuch bhi hai, wo bas un jazbaat ka ek chhota sa hissa hai jo shayad alfaaz mein poore kabhi aa hi nahi sakte.</p>
            </div>
            
            <!-- Spotlight Callout Box -->
            <div class="story-climax-quote-box">
                <span class="quote-center-heart">✦ &nbsp; ♡ &nbsp; ✦</span>
                <div class="story-quote-bracket-wrap">
                    <span class="story-quote-large-mark open-mark">“</span>
                    <p class="story-climax-quote-text">
                        Bas itna hai ke tumhari kami shayad waqt ke saath aadat ban jaye…<br>lekin tumhari jagah kabhi koi nahi le sakega.
                    </p>
                    <span class="story-quote-large-mark close-mark">”</span>
                </div>
            </div>
        </div>
    </div>
    """)
    render_chapter_footer("home")


# -----------------------------------------------------------------------------
# CHAPTER 1 — WELCOME
# -----------------------------------------------------------------------------
def render_welcome():
    """Render Chapter 1: Welcome letter with elevated keepsake layout."""
    reset_scroll_to_top()
    c = content.WELCOME_SECTION
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_welcome" id="sec_wrapper_welcome">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="chapter-letter-card floating-element">
            <!-- Decorative Corner Botanical Flourishes -->
            <div class="card-corner-flourish corner-tl">🌸</div>
            <div class="card-corner-flourish corner-tr">🌿</div>
            <div class="card-corner-flourish corner-bl">🌿</div>
            <div class="card-corner-flourish corner-br">🌸</div>

            <!-- Card Top Motif -->
            <div class="story-card-top-motif">
                <div class="story-motif-line"></div>
                <span class="story-motif-heart">♡</span>
                <div class="story-motif-line"></div>
            </div>

            <div class="chapter-letter-body">
                <p>Kabhi kabhi kisi insan ka humari zindagi mein aana itna aam sa lagta hai…<br>lekin aahista aahista wahi insan humari roz ki soch, muskurahat aur yaadon ka hissa ban jata hai.</p>
                <p>Pata hi nahi chalta ke kab uski ek choti si baat bhi dil ko sukoon dene lagti hai, aur kab uski khamoshi bhi mehsoos hone lagti hai.</p>
                <p>Shayad hum har baat keh nahi pate, har ehsaas samjha nahi pate…<br>lekin iska matlab ye nahi hota ke wo ehsaas kam thay.<br>Kuch jazbaat bas dil ke andar reh jaate hain, bina kisi shor ke.</p>
                <p>Aur shayad isi liye ye safar bana hai…<br>taake jo baatein kabhi alfaaz tak nahi aa sakin, wo kam az kam yaadon mein apni jagah bana saken.</p>
            </div>
            
            <!-- Spotlight Nested Callout Box -->
            <div class="story-climax-quote-box">
                <span class="quote-center-heart">✦ &nbsp; ♡ &nbsp; ✦</span>
                <div class="story-quote-bracket-wrap">
                    <span class="story-quote-large-mark open-mark">“</span>
                    <p class="story-climax-quote-text">
                        Agar kabhi meri baaton ki kami mehsoos ho…<br>to bas itna samajh lena ke kuch log door ja kar bhi dil se kabhi door nahi hote.
                    </p>
                    <span class="story-quote-large-mark close-mark">”</span>
                </div>
            </div>
        </div>
    </div>
    """)
    render_chapter_footer("welcome")


# -----------------------------------------------------------------------------
# CHAPTER 2 — MEMORIES
# -----------------------------------------------------------------------------
def render_memories():
    """Render Chapter 2: Memories timeline / cards matching reference image."""
    reset_scroll_to_top()
    c = content.MEMORIES_SECTION
    ui("""
    <div class="v2-chapter-container feature-section-enter memories-page-enter section-floating-enter" key="sec_wrapper_memories" id="sec_wrapper_memories">
        <div class="memories-header-decor">
            <div class="memories-alvida-badge">♥ &nbsp; Alvida... &nbsp; ♥</div>
            <div class="memories-header-flourish">─ &nbsp; ✦ &nbsp; ─</div>
            <p class="memories-poetic-sub">Hamari kahani ke woh lamhe jo mere dil par hamesha ke liye naqsh ho gaye.</p>
        </div>
    """)

    # Check if a memory switch transition loader is in progress
    if st.session_state.get("memory_transition_target") is not None:
        target_idx = st.session_state["memory_transition_target"]
        current_idx = st.session_state.get("selected_memory", 0)
        status_msg = "Moving to next memory..." if target_idx > current_idx else "Moving to previous memory..."
        target_title = c["cards"][target_idx]["category"]
        ui(f"""
        <div class="memory-transition-overlay" id="memoryTransitionOverlay">
            <div class="memory-switch-modal-card">
                <div class="memory-switch-icon-orb">✨</div>
                <div class="memory-switch-status">{status_msg}</div>
                <div class="memory-switch-sub">Opening “{target_title}”...</div>
                <div class="memory-switch-track">
                    <div class="memory-switch-fill"></div>
                </div>
            </div>
        </div>
        """)
        time.sleep(1.25)
        st.session_state["selected_memory"] = target_idx
        st.session_state["memory_transition_target"] = None
        st.rerun()

    idx = st.session_state.get("selected_memory")

    # Mode A: Grid View (8 exact themed memory cards in 2 rows of 4)
    if idx is None:
        decor_arts = [
            '<div class="mem-decor-art">🌹</div>',
            '<div class="mem-decor-art">🌸</div>',
            '<div class="mem-decor-art"></div>',
            '<div class="mem-decor-art">🌹</div>',
            '<div class="mem-decor-art">🌿</div>',
            '<div class="mem-decor-art">🌸</div>',
            '<div class="mem-decor-art">🕊️</div>',
            '<div class="mem-decor-art"></div>',
        ]

        ui('<div class="memories-grid-container">')
        cols1 = st.columns(4, gap="medium")
        for i in range(4):
            mem = c["cards"][i]
            with cols1[i]:
                ui(f"""
                <div class="mem-art-card mem-theme-{i+1} floating-element memory-float-{i+1}">
                    <div class="mem-card-flare"></div>
                    {decor_arts[i]}
                    <div class="mem-art-icon">{mem['icon']}</div>
                    <h4 class="mem-art-title">{mem['category']}</h4>
                </div>
                """)
                if st.button("Open Memory 📖", key=f"mem_btn_{i}", use_container_width=True):
                    st.session_state["selected_memory"] = i
                    st.rerun()

        ui('<div style="height: 1.4rem;"></div>')

        cols2 = st.columns(4, gap="medium")
        for i in range(4, 8):
            mem = c["cards"][i]
            col_idx = i - 4
            with cols2[col_idx]:
                ui(f"""
                <div class="mem-art-card mem-theme-{i+1} floating-element memory-float-{i+1}">
                    <div class="mem-card-flare"></div>
                    {decor_arts[i]}
                    <div class="mem-art-icon">{mem['icon']}</div>
                    <h4 class="mem-art-title">{mem['category']}</h4>
                </div>
                """)
                if st.button("Open Memory 📖", key=f"mem_btn_{i}", use_container_width=True):
                    st.session_state["selected_memory"] = i
                    st.rerun()
        ui('</div>')

    # Mode B: Opened Memory View (High-End Glassmorphism Keepsake UI)
    else:
        mem = c["cards"][idx]
        ts_id = int(time.time() * 1000)
        anim_class = f"mem-slide-{idx}-{ts_id}"
        ui(f"""
        <style>
        .{anim_class} {{
            animation: keepsakeEntrance 700ms cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
            will-change: transform, opacity, filter;
        }}
        </style>
        <div class="memory-detail-wrapper {anim_class}" id="wrap_mem_{idx}">
            <div class="memory-keepsake-card" style="border-left: 4px solid {mem['accent_color']} !important;">
                <div class="memory-watermark-decor">✦</div>
                
                <div class="memory-keepsake-header">
                    <div class="memory-icon-ambient-badge" style="border-color: {mem['accent_color']}66;">{mem['icon']}</div>
                    <div class="memory-keepsake-meta">
                        <div class="memory-counter-badge">✦ MEMORY #{idx + 1} OF {len(c['cards'])}</div>
                        <h3 class="memory-keepsake-title">{mem['category']}</h3>
                    </div>
                </div>
                
                <div class="memory-luminous-divider"></div>
                <p class="memory-story-text">{mem['placeholder']}</p>
            </div>
        </div>
        """)

        mcol1, mcol2, mcol3 = st.columns([1, 1.2, 1])
        with mcol1:
            if idx > 0:
                if st.button("← Previous Memory", key=f"mem_prev_{idx}", use_container_width=True):
                    st.session_state["memory_transition_target"] = idx - 1
                    st.rerun()
        with mcol2:
            if st.button("Close View ×", key=f"mem_close_{idx}", use_container_width=True):
                st.session_state["selected_memory"] = None
                st.session_state["memory_transition_target"] = None
                st.rerun()
        with mcol3:
            if idx < len(c["cards"]) - 1:
                if st.button("Next Memory →", key=f"mem_next_{idx}", type="primary", use_container_width=True):
                    st.session_state["memory_transition_target"] = idx + 1
                    st.rerun()

    ui("</div>")
    render_chapter_footer("memories")


# -----------------------------------------------------------------------------
# CHAPTER 3 — WORDS FROM MY HEART
# -----------------------------------------------------------------------------
def render_words():
    """Render Chapter 3: Words From My Heart intimate letter with elevated keepsake layout."""
    reset_scroll_to_top()
    c = content.WORDS_SECTION
    
    paragraphs_html = "".join([f'<p class="chapter-paragraph-text">{p}</p>' for p in c["paragraphs"]])
    
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_words" id="sec_wrapper_words">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="chapter-letter-card words-letter-card floating-element">
            <!-- Decorative Corner Botanical Flourishes -->
            <div class="card-corner-flourish corner-tl">🌸</div>
            <div class="card-corner-flourish corner-tr">🌿</div>
            <div class="card-corner-flourish corner-bl">🌿</div>
            <div class="card-corner-flourish corner-br">🌸</div>

            <!-- Card Top Motif -->
            <div class="story-card-top-motif">
                <div class="story-motif-line"></div>
                <span class="story-motif-heart">♡</span>
                <div class="story-motif-line"></div>
            </div>

            <div class="chapter-letter-body">
                {paragraphs_html}
            </div>
            
            <!-- Spotlight Nested Callout Box -->
            <div class="story-climax-quote-box">
                <span class="quote-center-heart">✦ &nbsp; ♡ &nbsp; ✦</span>
                <div class="story-quote-bracket-wrap">
                    <span class="story-quote-large-mark open-mark">“</span>
                    <p class="story-climax-quote-text">
                        {c["closing_thought"]}
                    </p>
                    <span class="story-quote-large-mark close-mark">”</span>
                </div>
            </div>
        </div>
    </div>
    """)
    render_chapter_footer("words")


# -----------------------------------------------------------------------------
# CHAPTER 4 — WHY I RESPECT YOU (Crown-Jewel Hero Feature)
# -----------------------------------------------------------------------------
def render_respect():
    """Render Chapter 4: Crown-Jewel Hero Feature with ambient gold/rose glow and Honor Plates."""
    reset_scroll_to_top()
    c = content.RESPECT_SECTION
    plates = c.get("plates", [])

    ui(f"""
    <div class="v2-chapter-container respect-special-section feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_respect" id="sec_wrapper_respect">
        <!-- Ambient Starlight Ember Particles -->
        <div class="respect-starlight-layer">
            <div class="starlight-ember"></div>
            <div class="starlight-ember"></div>
            <div class="starlight-ember"></div>
            <div class="starlight-ember"></div>
        </div>

        <div class="chapter-eyebrow-badge respect-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title respect-gold-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic respect-gold-sub">{c['subtitle']}</p>
    """)

    # 1. Pledge / Honor Plates Grid (Interactive Keepsake Cards)
    if plates:
        cols_row1 = st.columns(2, gap="medium")
        for i in range(min(2, len(plates))):
            plate = plates[i]
            with cols_row1[i]:
                ui(f"""
                <div class="respect-honor-plate floating-element" id="plate_{i}">
                    <div class="respect-plate-header">
                        <span class="respect-plate-tag">{plate['tag']}</span>
                        <div class="respect-crystal-badge">{plate['icon']}</div>
                    </div>
                    <h3 class="respect-plate-title">{plate['title']}</h3>
                    <p class="respect-plate-summary">{plate['summary']}</p>
                    <div class="respect-plate-action">
                        <span>Read Deep Reflection</span> <span>✦</span>
                    </div>
                </div>
                """)
                if st.button(f"Deep Reflection #{i+1} ✦", key=f"respect_btn_{i}", use_container_width=True):
                    st.session_state["selected_respect_plate"] = i
                    st.rerun()

        if len(plates) > 2:
            cols_row2 = st.columns(2, gap="medium")
            for i in range(2, min(4, len(plates))):
                plate = plates[i]
                col_idx = i - 2
                with cols_row2[col_idx]:
                    ui(f"""
                    <div class="respect-honor-plate floating-element" id="plate_{i}">
                        <div class="respect-plate-header">
                            <span class="respect-plate-tag">{plate['tag']}</span>
                            <div class="respect-crystal-badge">{plate['icon']}</div>
                        </div>
                        <h3 class="respect-plate-title">{plate['title']}</h3>
                        <p class="respect-plate-summary">{plate['summary']}</p>
                        <div class="respect-plate-action">
                            <span>Read Deep Reflection</span> <span>✦</span>
                        </div>
                    </div>
                    """)
                    if st.button(f"Deep Reflection #{i+1} ✦", key=f"respect_btn_{i}", use_container_width=True):
                        st.session_state["selected_respect_plate"] = i
                        st.rerun()

    # 2. Deep Reflection Spotlight Modal (Certificate / Keepsake)
    selected_idx = st.session_state.get("selected_respect_plate")
    if selected_idx is not None and 0 <= selected_idx < len(plates):
        plate = plates[selected_idx]
        ui(f"""
        <div class="respect-spotlight-modal-overlay" id="respectSpotlightModalOverlay">
            <div class="respect-spotlight-card finale-modal-floating">
                <div class="respect-spotlight-lantern">{plate['icon']}</div>
                <div class="respect-spotlight-badge">{plate['tag']}</div>
                <h3 class="respect-spotlight-title">{plate['title']}</h3>
                <div class="respect-spotlight-divider"></div>
                <div class="respect-spotlight-body">
                    {plate['detail']}
                </div>
                <div class="respect-spotlight-quote-box">
                    {plate['quote']}
                </div>
                <div style="margin-top: 1.4rem; text-align: center;">
                    <button class="respect-spotlight-close-btn" onclick="window.parent.__farewellCloseRespectModal && window.parent.__farewellCloseRespectModal()">
                        Close Reflection ×
                    </button>
                </div>
            </div>
        </div>
        """)

        # Fallback button for native Streamlit interaction
        rcol1, rcol2, rcol3 = st.columns([1, 1.6, 1])
        with rcol2:
            st.button(
                "Close Reflection ×",
                key="close_respect_plate_btn",
                type="secondary",
                use_container_width=True,
                on_click=on_close_respect_plate,
            )

    # 3. Soulful Signature Affirmation & Wax Seal
    ui(f"""
        <div class="respect-seal-container">
            <div class="respect-golden-banner floating-element">
                “ {c["golden_line"]} ”
            </div>
            <div class="respect-wax-seal-badge floating-element">
                <span class="respect-wax-seal-icon">👑</span>
                <span class="respect-wax-seal-text">{c.get("signature_seal", "Izzat jo alfaaz se nahi, dil ki gehraiyon se di jaati hai.")}</span>
            </div>
            <p class="respect-closing-text">
                {c["closing"]}
            </p>
        </div>
    </div>
    """)
    render_chapter_footer("respect")


# -----------------------------------------------------------------------------
# CHAPTER 5 — INTENTIONS
# -----------------------------------------------------------------------------
def render_intentions():
    """Render Chapter 5: Intentions & Family Respect with locked keepsake design system."""
    reset_scroll_to_top()
    c = content.INTENTIONS_SECTION
    
    cards_html = f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_intentions" id="sec_wrapper_intentions">
        <div class="keepsake-kicker">✦ {c['eyebrow']}</div>
        <h2 class="keepsake-title">{c['title']}</h2>
        <p class="keepsake-subtitle">{c['subtitle']}</p>
        
        <div class="intentions-grid-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; max-width: 760px; margin: 0 auto 20px auto;">
    """
    
    for item in c["intentions"]:
        cards_html += f"""
            <div class="keepsake-nested-box intention-point-card" style="margin: 0;">
                <div class="intention-card-header" style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <span class="intention-icon" style="font-size: 1.25rem;">❤️</span>
                    <h3 class="keepsake-title" style="font-size: 1.2rem; margin: 0; text-align: left;">{item["title"]}</h3>
                </div>
                <p class="keepsake-body-text" style="font-size: 0.98rem; text-align: left; line-height: 1.75;">{item["content"]}</p>
            </div>
        """
        
    cards_html += f"""
        </div>
        
        <div class="keepsake-nested-box intentions-family-card floating-element" style="max-width: 760px; margin: 0 auto; text-align: center; border-color: rgba(251, 191, 36, 0.45);">
            <span class="family-card-icon" style="font-size: 1.8rem; display: block; margin-bottom: 8px;">🏡</span>
            <p class="keepsake-quote-text" style="margin-bottom: 0;">
                “ {c["family_note"]} ”
            </p>
        </div>
    </div>
    """
    ui(cards_html)
    render_chapter_footer("intentions")


# -----------------------------------------------------------------------------
# CHAPTER 6 — DUA
# -----------------------------------------------------------------------------
def render_dua():
    """Render Chapter 6: Prayer & Duas with elevated keepsake layout."""
    reset_scroll_to_top()
    c = content.DUA_SECTION
    
    paragraphs_html = "".join([f'<p class="dua-paragraph-text">{p}</p>' for p in c["paragraphs"]])
    
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_dua" id="sec_wrapper_dua">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="chapter-letter-card dua-prayer-card floating-element">
            <!-- Decorative Corner Botanical Flourishes -->
            <div class="card-corner-flourish corner-tl">🌸</div>
            <div class="card-corner-flourish corner-tr">🌿</div>
            <div class="card-corner-flourish corner-bl">🌿</div>
            <div class="card-corner-flourish corner-br">🌸</div>

            <div class="dua-card-hands-icon">🤲 🤍</div>
            
            <div class="chapter-letter-body">
                {paragraphs_html}
            </div>
            
            <!-- Spotlight Nested Callout Box for Dua Ayah -->
            <div class="story-climax-quote-box dua-ayah-highlight-box">
                <div class="dua-ayah-arabic">{c["closing_ayah"]}</div>
                <div class="dua-ayah-translation">“ {c["closing_meaning"]} ”</div>
            </div>
        </div>
    </div>
    """)
    render_chapter_footer("dua")


# -----------------------------------------------------------------------------
# CHAPTER 7 — FINAL NOTE (Goodbye)
# -----------------------------------------------------------------------------
def render_goodbye():
    """Render Chapter 7: Final Note with interactive reveal and spotlight floating card."""
    reset_scroll_to_top()
    c = content.GOODBYE_SECTION
    
    paragraphs_html = "".join([f'<p class="chapter-paragraph-text">{p}</p>' for p in c["paragraphs"]])
    
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_goodbye" id="sec_wrapper_goodbye">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="final-note-section-wrapper">
            <div class="final-note-bg-content">
                <div class="chapter-letter-card finale-letter-card floating-element">
                    <!-- Decorative Corner Botanical Flourishes -->
                    <div class="card-corner-flourish corner-tl">🌸</div>
                    <div class="card-corner-flourish corner-tr">🌿</div>
                    <div class="card-corner-flourish corner-bl">🌿</div>
                    <div class="card-corner-flourish corner-br">🌸</div>
                    
                    <div class="chapter-letter-body">
                        {paragraphs_html}
                    </div>
                    
                    <!-- Spotlight Nested Callout Box -->
                    <div class="story-climax-quote-box">
                        <span class="quote-center-heart">✦ &nbsp; ♡ &nbsp; ✦</span>
                        <div class="story-quote-bracket-wrap">
                            <span class="story-quote-large-mark open-mark">“</span>
                            <p class="story-climax-quote-text">
                                {c["highlighted_line"]}
                            </p>
                            <span class="story-quote-large-mark close-mark">”</span>
                        </div>
                    </div>
                    
                    <div class="finale-special-monolith" style="margin-top: 24px;">
                        <span class="finale-lantern-icon">🏮</span>
                        <div class="finale-special-text" style="color: #ffffff; font-weight: 600; font-size: 1rem;">
                            {c["final_visual_text"]}
                        </div>
                    </div>
                </div>
            </div>
    """)

    if not st.session_state.get("show_final_words", False):
        fcol1, fcol2, fcol3 = st.columns([1, 1.8, 1])
        with fcol2:
            st.button(
                "Read My Final Words ✉️",
                key="reveal_final_words_btn",
                type="primary",
                use_container_width=True,
                on_click=on_reveal_final_words,
            )
    else:
        # Centered Spotlight Modal Overlay with Deep Backdrop Blur
        ui(f"""
        <div class="final-spotlight-modal-overlay" id="finalSpotlightModalOverlay">
            <div class="final-spotlight-modal-card finale-modal-floating">
                <div class="final-spotlight-lantern">🏮</div>
                <div class="final-spotlight-badge">FROM AWAIS TO ALMAS</div>
                <div class="final-spotlight-divider"></div>
                <div class="final-spotlight-body">
                    {c["absolute_last_line"]}
                </div>
                <div class="final-spotlight-emojis">🌸 &nbsp; 🤍 &nbsp; 🤲</div>
                <div style="margin-top: 1.6rem; text-align: center;">
                    <button class="final-spotlight-close-btn" onclick="window.parent.__farewellCloseFinalModal && window.parent.__farewellCloseFinalModal()">
                        Close Letter ×
                    </button>
                </div>
            </div>
        </div>
        """)

        # Fallback button for native Streamlit interaction
        fcol1, fcol2, fcol3 = st.columns([1, 1.6, 1])
        with fcol2:
            st.button(
                "Close Letter ×",
                key="close_final_words_btn",
                type="secondary",
                use_container_width=True,
                on_click=on_close_final_words,
            )

    ui("""
        </div>
    </div>
    """)
    render_chapter_footer("goodbye")


# -----------------------------------------------------------------------------
# 12. Main Application Controller & Router (4 Mutually Exclusive Views)
# -----------------------------------------------------------------------------
def main():
    """Main state router and layout orchestrator with 4 mutually exclusive views."""
    # 1. State initialization guarded once per session
    if "initial_splash_done" not in st.session_state:
        st.session_state.initial_splash_done = False
    if "startup_completed" not in st.session_state:
        st.session_state.startup_completed = False
    if "app_view" not in st.session_state:
        st.session_state.app_view = "landing"
    if "nav_mode" not in st.session_state:
        st.session_state.nav_mode = "next"
    if "active_section" not in st.session_state:
        st.session_state.active_section = None
    if "show_final_words" not in st.session_state:
        st.session_state.show_final_words = False
    if "selected_memory" not in st.session_state:
        st.session_state.selected_memory = None
    if "selected_respect_plate" not in st.session_state:
        st.session_state.selected_respect_plate = None
    if "memory_transition_target" not in st.session_state:
        st.session_state.memory_transition_target = None
    if "pending_section" not in st.session_state:
        st.session_state.pending_section = None
    if "visited_chapters" not in st.session_state:
        st.session_state.visited_chapters = {"home"}

    # Support URL query parameter routing
    url_view = st.query_params.get("view")
    if url_view in ["landing", "transition", "journey_transition", "section_transition", "journey_menu", "menu", "section"]:
        mapped_view = "journey_menu" if url_view == "menu" else url_view
        if st.session_state.app_view != mapped_view:
            st.session_state.app_view = mapped_view

    url_chap = st.query_params.get("chapter")
    if url_chap and url_chap in [c["id"] for c in config.CHAPTERS]:
        st.session_state.app_view = "section"
        st.session_state.active_section = url_chap

    # 2. Global Styles
    load_styles()

    # 3. TRANSITION ANALYZER GUARDS (Strictly executed BEFORE any view, sidebar, or atmospheric rendering)
    if st.session_state.app_view in ["transition", "section_transition", "journey_transition"]:
        reset_scroll_to_top()
        nav_mode = st.session_state.get("nav_mode", "next")
        if st.session_state.app_view == "journey_transition" and nav_mode == "next":
            nav_mode = "journey_start"

        target_sec = st.session_state.get("pending_section")
        render_dynamic_transition_analyzer(target_id=target_sec, mode=nav_mode)

        duration = 1.5 if nav_mode == "journey_start" else 1.0
        time.sleep(duration)

        if nav_mode in ["back_to_menu", "journey_start"]:
            st.session_state.app_view = "journey_menu"
            st.session_state.active_section = None
        else:
            st.session_state.app_view = "section"
            st.session_state.active_section = target_sec or "welcome"
            if "visited_chapters" in st.session_state and target_sec:
                st.session_state.visited_chapters.add(target_sec)

        st.session_state.pending_section = None
        st.session_state.nav_mode = "next"
        reset_scroll_to_top()
        st.rerun()

    # 5. Top-Level Bridge Navigation Dispatcher
    render_hidden_bridge_dispatcher()

    # 6. Connect JavaScript Audio, 3D WebGL & Navigation Bridge
    app_view = st.session_state.app_view
    active_section = st.session_state.get("active_section") or "home"
    render_cinematic_atmosphere(active_section if app_view == "section" else "home")
    render_sidebar_and_navigation_bridge(app_view, active_section)

    # 7. Main Mutually Exclusive Active Views
    if app_view == "landing":
        render_landing()
    elif app_view in ["journey_menu", "menu"]:
        render_journey_menu()
    elif app_view == "section_preview":
        render_section_preview()
    elif app_view == "section":
        render_section(st.session_state.get("active_section") or "welcome")


if __name__ == "__main__":
    main()
