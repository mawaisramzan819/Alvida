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

# Page Configuration — Wide layout with persistent sidebar
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout=config.PAGE_LAYOUT,
    initial_sidebar_state="expanded",
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
    """Load custom CSS and inject mobile viewport meta."""
    st.markdown(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">',
        unsafe_allow_html=True,
    )
    css_path = config.CSS_DIR / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


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
# 5. Startup State Machine & Audio Engine (DOM Persistent Injection)
# -----------------------------------------------------------------------------
def render_startup_screen():
    """Display the full cinematic starting loader FIRST. Prevents landing page from flashing."""
    audio_b64 = get_audio_base64()
    audio_src = f"data:audio/mp3;base64,{audio_b64}" if audio_b64 else "/app/static/farewell.mp3"

    # 1. Initialize persistent audio element on parent DOM
    components.html(
        f"""
    <script>
    (function() {{
        const pDoc = window.parent.document;

        // Persistent Audio Element on parent body
        let audio = pDoc.getElementById('farewellBgAudioMain');
        if (!audio) {{
            audio = pDoc.createElement('audio');
            audio.id = 'farewellBgAudioMain';
            audio.loop = true;
            audio.preload = 'auto';
            audio.src = '{audio_src}';
            pDoc.body.appendChild(audio);
            window.parent.__farewell_audio = audio;
        }}

        // Trigger autoplay only if user hasn't paused previously
        const isMutedByUser = (localStorage.getItem('farewell_music_paused') === 'true');
        if (audio && audio.paused && !isMutedByUser) {{
            audio.volume = 0;
            let playPromise = audio.play();
            if (playPromise !== undefined) {{
                playPromise.then(() => {{
                    let start = performance.now();
                    function fadeIn() {{
                        let el = performance.now() - start;
                        let frac = Math.min(el / 1500, 1);
                        audio.volume = frac * 0.22;
                        if (frac < 1) requestAnimationFrame(fadeIn);
                    }}
                    requestAnimationFrame(fadeIn);
                }}).catch(() => {{
                    const unlockAction = () => {{
                        if (localStorage.getItem('farewell_music_paused') !== 'true') {{
                            audio.play().then(() => {{
                                audio.volume = 0.22;
                            }}).catch(() => {{}});
                        }}
                        pDoc.removeEventListener('click', unlockAction);
                        pDoc.removeEventListener('touchstart', unlockAction);
                        pDoc.removeEventListener('pointerdown', unlockAction);
                    }};
                    pDoc.addEventListener('click', unlockAction, {{ passive: true }});
                    pDoc.addEventListener('touchstart', unlockAction, {{ passive: true }});
                    pDoc.addEventListener('pointerdown', unlockAction, {{ passive: true }});
                }});
            }}
        }}
    }})();
    </script>
    """,
        height=0,
        width=0,
    )

    # 2. Render Full-Screen Startup Loader UI directly in Streamlit
    loader_box = st.empty()
    loader_html = """
    <div class="startup-loader-overlay">
        <div class="startup-loader-card">
            <div class="startup-loader-icon-wrap">
                <div class="startup-loader-ring"></div>
                <div class="startup-loader-heart">💗</div>
            </div>
            <div class="startup-brand-title">A Farewell That Stays</div>
            <div class="startup-brand-subtitle">Opening a story that was never forgotten...</div>
            <div class="startup-quote-text">“Some goodbyes stay in the heart forever.”</div>
            <div class="startup-progress-track">
                <div class="startup-progress-fill"></div>
            </div>
        </div>
    </div>
    """
    loader_box.markdown(loader_html, unsafe_allow_html=True)
    time.sleep(2.2)
    loader_box.empty()

    st.session_state["startup_completed"] = True
    st.rerun()


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

        // 6. Global Navigation Triggers (Reliable, fast, and no page reload!)
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
            const container = pDoc.querySelector('.v2-main-wrap, .landing-page-wrap');
            if (container) {{ container.classList.add('view-exit'); }}
            window.parent.__farewellResetScroll();
            clickStreamlitBridge('_bridge_menu', 'bridge_go_menu');
        }};

        window.parent.__farewellGoToMenu = function() {{
            window.parent.__farewellStartJourney();
        }};

        window.parent.__farewellGoToLanding = function() {{
            const container = pDoc.querySelector('.v2-chapter-container, .v2-main-wrap');
            if (container) {{ container.classList.add('view-exit'); }}
            window.parent.__farewellResetScroll();
            clickStreamlitBridge('_bridge_landing', 'bridge_go_landing');
        }};

        window.parent.__farewellNav = function(chapterId) {{
            if (!chapterId) return;
            const container = pDoc.querySelector('.v2-chapter-container, .v2-main-wrap');
            if (container) {{ container.classList.add('view-exit'); }}
            window.parent.__farewellResetScroll();
            clickStreamlitBridge(`_bridge_${{chapterId}}`, `bridge_go_${{chapterId}}`);
        }};

        // 7. Global Event Delegation on Parent Document (Intercepts clicks regardless of Streamlit DOM updates)
        if (window.parent.__farewellClickDelegation) {{
            pDoc.removeEventListener('click', window.parent.__farewellClickDelegation, true);
        }}

        window.parent.__farewellClickDelegation = function(e) {{
            const target = e.target;
            if (!target) return;

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

        // 8. Attach audio event listeners
        const audio = window.parent.__farewellGetAudio();
        if (audio) {{
            audio.onplay = () => window.parent.__farewellUpdateMusicUI();
            audio.onpause = () => window.parent.__farewellUpdateMusicUI();
            audio.ontimeupdate = () => window.parent.__farewellUpdateMusicUI();
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
def render_journey_loader():
    """Render the dedicated full-screen Journey Entry transition (rotating animation)."""
    reset_scroll_to_top()
    loader_box = st.empty()
    html = """
    <div class="journey-entry-loader-overlay">
        <div class="journey-entry-loader-card">
            <div class="journey-entry-icon-wrap">
                <div class="journey-entry-ring"></div>
                <div class="journey-entry-heart">✦</div>
            </div>
            <div class="journey-entry-title">Journey Starting...</div>
            <div class="journey-entry-subtitle">Hamara safar shuru ho raha hai...</div>
            <div class="journey-entry-quote">“Kuch alvida asal mein khatam nahi hotay, wo bas khoobsurat yaadon ki shuruat ban jatay hain.”</div>
            <div class="journey-entry-track">
                <div class="journey-entry-fill"></div>
            </div>
        </div>
    </div>
    """
    loader_box.markdown(html, unsafe_allow_html=True)

    # Let the 0.95s rotating entry animation complete fully
    time.sleep(0.95)
    loader_box.empty()

    st.session_state.app_view = "journey_menu"
    st.session_state.active_section = None
    reset_scroll_to_top()
    st.rerun()


def render_section(section_id: str):
    """Render the requested section view with mutually exclusive layout."""
    sec = section_id or "welcome"
    if "visited_chapters" in st.session_state:
        st.session_state.visited_chapters.add(sec)
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
# 9. Sidebar Component (Minimal Branded Header)
# -----------------------------------------------------------------------------
def render_sidebar():
    """Render minimal cinematic left sidebar containing Brand Header."""
    with st.sidebar:
        ui("""
        <div class="sidebar-brand-wrapper" onclick="window.parent.__farewellGoToLanding && window.parent.__farewellGoToLanding()" style="cursor: pointer;" title="Return to Intro Screen">
            <div class="sidebar-brand-heart-glow">
                <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#E96582" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                </svg>
            </div>
            <div class="sidebar-brand-title">A Farewell</div>
            <div class="sidebar-brand-sub">That Stays</div>
            <div class="sidebar-brand-sub-bottom">in the Heart</div>
        </div>
        """)


# -----------------------------------------------------------------------------
# 11. Bottom Navigation Bar (Back to Journey + Next/Prev Chapter)
# -----------------------------------------------------------------------------
def render_chapter_footer(current_id: str):
    """Render clean navigation footer with Back to Journey and Next/Prev buttons."""
    chapter_ids = [c["id"] for c in config.CHAPTERS]
    curr_idx = chapter_ids.index(current_id) if current_id in chapter_ids else 0
    prev_id = chapter_ids[curr_idx - 1] if curr_idx > 0 else None
    next_id = chapter_ids[curr_idx + 1] if curr_idx + 1 < len(chapter_ids) else None

    prev_label = None
    next_label = None
    for c in config.CHAPTERS:
        if c["id"] == prev_id:
            prev_label = c["label"]
        if c["id"] == next_id:
            next_label = c["label"]

    ui('<div class="chapter-footer-divider"></div>')
    bcol1, bcol2, bcol3 = st.columns([1.2, 1.4, 1.2])

    with bcol1:
        if prev_id and prev_label:
            if st.button(f"← Prev: {prev_label}", key=f"foot_prev_{current_id}", use_container_width=True):
                st.session_state.app_view = "section"
                st.session_state.active_section = prev_id
                st.session_state.selected_memory = None
                if "visited_chapters" in st.session_state:
                    st.session_state.visited_chapters.add(prev_id)
                reset_scroll_to_top()
                st.rerun()

    with bcol2:
        if st.button("← Back to Journey", key=f"foot_back_{current_id}", type="secondary", use_container_width=True):
            st.session_state.app_view = "journey_menu"
            st.session_state.active_section = None
            st.session_state.selected_memory = None
            reset_scroll_to_top()
            st.rerun()

    with bcol3:
        if next_id and next_label:
            if st.button(f"Next: {next_label} →", key=f"foot_next_{current_id}", type="primary", use_container_width=True):
                st.session_state.app_view = "section"
                st.session_state.active_section = next_id
                st.session_state.selected_memory = None
                if "visited_chapters" in st.session_state:
                    st.session_state.visited_chapters.add(next_id)
                reset_scroll_to_top()
                st.rerun()


# -----------------------------------------------------------------------------
# INVISIBLE STREAMLIT BRIDGE DISPATCHER (Zero-latency Programmatic Clicks)
# -----------------------------------------------------------------------------
def render_hidden_bridge_dispatcher():
    """Invisible Streamlit button dispatcher that handles programmatic clicks from JS without reloading the page."""
    with st.container():
        st.markdown(
            """
            <style>
            .st-key-_bridge_landing, .st-key-_bridge_menu,
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
            if st.button("bridge_go_landing", key="_bridge_landing", help="bridge_hidden"):
                st.session_state.app_view = "landing"
                st.session_state.active_section = None
                st.session_state.selected_memory = None
                reset_scroll_to_top()
                st.rerun()

            if st.button("bridge_go_menu", key="_bridge_menu", help="bridge_hidden"):
                st.session_state.app_view = "journey_transition"
                st.session_state.active_section = None
                st.session_state.selected_memory = None
                reset_scroll_to_top()
                st.rerun()

            for chap in config.CHAPTERS:
                if st.button(f"bridge_go_{chap['id']}", key=f"_bridge_{chap['id']}", help="bridge_hidden"):
                    st.session_state.app_view = "section"
                    st.session_state.active_section = chap["id"]
                    st.session_state.selected_memory = None
                    if "visited_chapters" in st.session_state:
                        st.session_state.visited_chapters.add(chap["id"])
                    reset_scroll_to_top()
                    st.rerun()


# -----------------------------------------------------------------------------
# TOP-CENTER FULL MUSIC PLAYER
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
                    <div class="tc-music-fill" id="musicProgressFill"></div>
                    <span class="tc-music-dot" id="musicProgressDot"></span>
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
    """Render STATE 1: Pure Cinematic Hero Intro Screen with Top-Center Music Player."""
    reset_scroll_to_top()
    c = content.HOME_SECTION
    banner_b64 = get_hero_panorama_b64()

    visited_set = st.session_state.get("visited_chapters", set())
    visited_pct = int((len(visited_set) / len(config.CHAPTERS)) * 100)
    hero_pct = max(12, visited_pct)

    # 1. Top-Center Full Music Player
    render_top_center_music_player()

    # 2. Cinematic Hero Card
    ui(f"""
    <div class="v2-main-wrap landing-page-wrap">
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
                        <span class="btn-heart-glyph">♡</span> Start the Journey
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
def render_journey_menu():
    """Render STATE 2: Main Journey Menu / Central Hub (Quotation Bar + 8 Compact Cards Grid)."""
    reset_scroll_to_top()
    c = content.HOME_SECTION

    # 1. Top-Center Full Music Player
    render_top_center_music_player()

    # 2. Header
    ui("""
    <div class="v2-main-wrap">
        <div class="journey-menu-header">
            <div class="journey-menu-badge">✦ A FAREWELL THAT STAYS</div>
            <h1 class="journey-menu-title">Hamari Kahani Ke Safhay</h1>
            <p class="journey-menu-subtitle">Har safha dil se likhi yaadon, sachche alfaaz aur duaon se sajjaya gaya hai.</p>
        </div>
    """)

    # 2. Quotation Bar (Horizontal Glowing Dark Glass Strip)
    ui(f"""
        <div class="v2-quote-banner quote-box floating-element">
            <span class="v2-quote-mark">“</span>
            <span class="v2-quote-text">{c['quote_bar']}</span>
            <span class="v2-quote-heart-doodle">♡</span>
            <span class="v2-quote-branch">🌿</span>
        </div>
    """)

    # 3. 2×4 Chapter Cards Grid (8 Compact Primary Navigation Cards)
    t_welcome = get_thumbnail_b64("thumb_welcome")
    t_memories = get_thumbnail_b64("thumb_memories")
    t_words = get_thumbnail_b64("thumb_words")
    t_respect = get_thumbnail_b64("thumb_respect")
    t_intentions = get_thumbnail_b64("thumb_intentions")
    t_dua = get_thumbnail_b64("thumb_dua")
    t_goodbye = get_thumbnail_b64("thumb_goodbye")

    ui(f"""
        <div class="ref-cards-grid">
            <!-- Card 1: Story Overview -->
            <div class="ref-card journey-card ref-card-light memory-card-box feature-card-item floating-element" data-chapter="home" onclick="window.parent.__farewellNav('home')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_welcome}" class="ref-card-thumb" alt="Overview">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Story Overview</h3>
                    <p class="ref-card-desc">Hamari kahani ke woh lamhe jo hamesha dil mein rahein ge.</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="home">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 2: Welcome -->
            <div class="ref-card journey-card ref-card-light memory-card-box feature-card-item floating-element" data-chapter="welcome" onclick="window.parent.__farewellNav('welcome')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_welcome}" class="ref-card-thumb" alt="Welcome">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Welcome</h3>
                    <p class="ref-card-desc">Jaane se pehle, ek baar ye khat zaroor parh lena.</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="welcome">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 3: Memories -->
            <div class="ref-card journey-card ref-card-light memory-card-box feature-card-item floating-element" data-chapter="memories" onclick="window.parent.__farewellNav('memories')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_memories}" class="ref-card-thumb" alt="Memories">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Memories</h3>
                    <p class="ref-card-desc">Woh khoobsurat lamhe jo waqt ke saath kabhi dhundhle nahi honge.</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="memories">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 4: Words From My Heart -->
            <div class="ref-card journey-card ref-card-light memory-card-box feature-card-item floating-element" data-chapter="words" onclick="window.parent.__farewellNav('words')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_words}" class="ref-card-thumb" alt="Words From My Heart">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Words From My Heart</h3>
                    <p class="ref-card-desc">Woh sachchi baatein jo main ap k saamne keh na saka.</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="words">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 5: Why I Respect You -->
            <div class="ref-card journey-card ref-card-light memory-card-box feature-card-item floating-element" data-chapter="respect" onclick="window.parent.__farewellNav('respect')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_respect}" class="ref-card-thumb" alt="Why I Respect You">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Why I Respect You</h3>
                    <p class="ref-card-desc">Woh khoobian jin ki wajah se ap ki izzat hamesha dil mein rahe gi.</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="respect">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 6: Intentions -->
            <div class="ref-card journey-card ref-card-light memory-card-box feature-card-item floating-element" data-chapter="intentions" onclick="window.parent.__farewellNav('intentions')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_intentions}" class="ref-card-thumb" alt="Intentions">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Intentions</h3>
                    <p class="ref-card-desc">Meri sachchi duaein aur iradey jo sirf ap ki khushi ke liye hain.</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="intentions">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 7: Dua -->
            <div class="ref-card journey-card ref-card-light memory-card-box feature-card-item floating-element" data-chapter="dua" onclick="window.parent.__farewellNav('dua')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_dua}" class="ref-card-thumb" alt="Dua">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Dua</h3>
                    <p class="ref-card-desc">Tumhari khushi, sukoon aur kamyabi ke liye dil se dua.</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="dua">Open →</span>
                    </div>
                </div>
            </div>

            <!-- Card 8: Final Note -->
            <div class="ref-card journey-card ref-card-light memory-card-box feature-card-item floating-element" data-chapter="goodbye" onclick="window.parent.__farewellNav('goodbye')">
                <div class="ref-card-thumb-wrap">
                    <img src="data:image/png;base64,{t_goodbye}" class="ref-card-thumb" alt="Final Note">
                </div>
                <div class="ref-card-content">
                    <h3 class="ref-card-title">Final Note</h3>
                    <p class="ref-card-desc">Ek aakhri baat... mohabbat, izzat aur duaon ke saath.</p>
                    <div class="ref-card-btn-row">
                        <span class="ref-card-open-btn" data-chapter="goodbye">Open →</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Return to Intro Button -->
        <div style="text-align: center; margin: 1.5rem 0 2.5rem 0;">
            <button class="bottom-back-btn nav-action-btn floating-element" id="btnBackIntro" data-action="landing" onclick="window.parent.__farewellGoToLanding && window.parent.__farewellGoToLanding()">
                ↺ Back to Intro Screen
            </button>
        </div>

        <!-- Bottom Footer Bar -->
        <div class="v2-bottom-footer-bar quote-box floating-element">
            <span>🌸 &nbsp; 🌿 &nbsp; {c['bottom_quote']} &nbsp; ♡ &nbsp; 🌿 &nbsp; 🌸</span>
        </div>
    </div>
    """)


# -----------------------------------------------------------------------------
# STATE 3 — SECTION VIEW: HOME / OVERVIEW
# -----------------------------------------------------------------------------
def render_home_overview():
    """Render Story Overview & Reflections Section with smooth 3D slide-down."""
    reset_scroll_to_top()
    c = content.HOME_SECTION
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_home" id="sec_wrapper_home">
        <div class="chapter-eyebrow-badge">✦ HAMARI KAHANI KA SAFAR</div>
        <h2 class="chapter-main-title">A Farewell That Stays in the Heart</h2>
        <p class="chapter-subtitle-italic">Kuch alvida asal mein khatam nahi hotay — wo bas khoobsurat yaadon ki shuruat ban jatay hain.</p>
        
        <div class="chapter-letter-card floating-element">
            <div class="chapter-letter-body">
                <p>Kuch log zindagi mein aate hain aur dil par aise naqsh chor jaate hain jo waqt ke saath kabhi nahi mit'te.</p>
                <p>Ye jagah un sabhi khoobsurat yaadon, sachchi seekhon aur be-shart duaon ke liye banayi gayi hai jinhein faaslay kabhi khatam nahi kar sakte.</p>
                <p>Jaise jaise ap is safar ka har safha kholenge, bas itna yaad rakhna ke alvida kisi izzat, qadar aur duaon ka khatma nahi hota.</p>
            </div>
            <div class="chapter-handwritten-note">
                “Faaslay chahe kitne bhi barh jayein, tum meri duaon aur dil mein hamesha raho gi.”
            </div>
        </div>
    </div>
    """)
    render_chapter_footer("home")


# -----------------------------------------------------------------------------
# CHAPTER 1 — WELCOME
# -----------------------------------------------------------------------------
def render_welcome():
    """Render Chapter 1: Welcome letter with smooth 3D slide-down."""
    reset_scroll_to_top()
    c = content.WELCOME_SECTION
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_welcome" id="sec_wrapper_welcome">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="chapter-letter-card floating-element">
    """)
    for p in c["paragraphs"]:
        ui(f'<p class="chapter-paragraph-text">{p}</p>')

    ui(f"""
            <div class="chapter-handwritten-note">“ {c["closing_note"]} ”</div>
        </div>
    </div>
    """)
    render_chapter_footer("welcome")


# -----------------------------------------------------------------------------
# CHAPTER 2 — MEMORIES
# -----------------------------------------------------------------------------
def render_memories():
    """Render Chapter 2: Memories timeline / cards with cinematic entrance & floating cards."""
    reset_scroll_to_top()
    c = content.MEMORIES_SECTION
    ui(f"""
    <div class="v2-chapter-container feature-section-enter memories-page-enter section-floating-enter" key="sec_wrapper_memories" id="sec_wrapper_memories">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
    """)

    idx = st.session_state.get("selected_memory")

    # Mode A: Grid View (8 polaroid cards in 2 rows of 4)
    if idx is None:
        cols1 = st.columns(4, gap="medium")
        for i in range(4):
            mem = c["cards"][i]
            with cols1[i]:
                ui(f"""
                <div class="memory-polaroid-card memory-card-box feature-card-item memory-card-floating floating-element memory-float-{i+1}" style="border-top: 3px solid {mem['accent_color']};">
                    <div class="memory-polaroid-icon">{mem['icon']}</div>
                    <h4 class="memory-polaroid-title">{mem['category']}</h4>
                </div>
                """)
                if st.button("Open Memory ✉️", key=f"mem_btn_{i}", use_container_width=True):
                    st.session_state["selected_memory"] = i
                    st.rerun()

        ui('<div style="height: 1.2rem;"></div>')

        cols2 = st.columns(4, gap="medium")
        for i in range(4, 8):
            mem = c["cards"][i]
            col_idx = i - 4
            with cols2[col_idx]:
                ui(f"""
                <div class="memory-polaroid-card memory-card-box feature-card-item memory-card-floating floating-element memory-float-{i+1}" style="border-top: 3px solid {mem['accent_color']};">
                    <div class="memory-polaroid-icon">{mem['icon']}</div>
                    <h4 class="memory-polaroid-title">{mem['category']}</h4>
                </div>
                """)
                if st.button("Open Memory ✉️", key=f"mem_btn_{i}", use_container_width=True):
                    st.session_state["selected_memory"] = i
                    st.rerun()

    # Mode B: Opened Memory View
    else:
        mem = c["cards"][idx]
        anim_key = f"mem_active_{idx}"
        ui(f"""
        <div class="memory-detail-wrapper" id="wrap_{anim_key}" key="wrap_{anim_key}">
            <div class="memory-opened-card active-memory-card memory-content-fade floating-element" id="{anim_key}" key="{anim_key}" style="border-left: 4px solid {mem['accent_color']};">
                <div class="memory-opened-header">
                    <span class="memory-opened-icon">{mem['icon']}</span>
                    <div>
                        <div class="memory-opened-badge">Memory #{idx + 1} of {len(c['cards'])}</div>
                        <h3 class="memory-opened-title">{mem['category']}</h3>
                    </div>
                </div>
                <div class="memory-opened-divider"></div>
                <p class="memory-opened-body">{mem['placeholder']}</p>
            </div>
        </div>
        """)

        mcol1, mcol2, mcol3 = st.columns([1, 1, 1])
        with mcol1:
            if idx > 0:
                if st.button("← Previous Memory", key="mem_prev", use_container_width=True):
                    st.session_state["selected_memory"] = idx - 1
                    st.rerun()
        with mcol2:
            if st.button("Close View ×", key="mem_close", use_container_width=True):
                st.session_state["selected_memory"] = None
                st.rerun()
        with mcol3:
            if idx < len(c["cards"]) - 1:
                if st.button("Next Memory →", key="mem_next", type="primary", use_container_width=True):
                    st.session_state["selected_memory"] = idx + 1
                    st.rerun()

    ui("</div>")
    render_chapter_footer("memories")


# -----------------------------------------------------------------------------
# CHAPTER 3 — WORDS FROM MY HEART
# -----------------------------------------------------------------------------
def render_words():
    """Render Chapter 3: Words From My Heart intimate letter with smooth 3D slide-down."""
    reset_scroll_to_top()
    c = content.WORDS_SECTION
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_words" id="sec_wrapper_words">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="chapter-letter-card floating-element">
            <div class="letter-quote-decor">❝</div>
    """)
    for p in c["paragraphs"]:
        ui(f'<p class="chapter-paragraph-text">{p}</p>')

    ui(f"""
            <div class="chapter-highlight-quote-box floating-element">
                {c["closing_thought"]}
            </div>
        </div>
    </div>
    """)
    render_chapter_footer("words")


# -----------------------------------------------------------------------------
# CHAPTER 4 — WHY I RESPECT YOU (Special Golden Visual Section)
# -----------------------------------------------------------------------------
def render_respect():
    """Render Chapter 4: Respect & Na-mehram boundary admiration with smooth 3D slide-down."""
    reset_scroll_to_top()
    c = content.RESPECT_SECTION
    ui(f"""
    <div class="v2-chapter-container respect-special-section feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_respect" id="sec_wrapper_respect">
        <div class="chapter-eyebrow-badge respect-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title respect-gold-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic respect-gold-sub">{c['subtitle']}</p>
        
        <div class="respect-content-card floating-element">
    """)
    for point in c["main_content"]:
        ui(f"""
        <div class="respect-point-item">
            <span class="respect-gold-bullet">✦</span>
            <span class="chapter-paragraph-text">{point}</span>
        </div>
        """)

    ui(f"""
            <div class="respect-golden-banner floating-element">
                “ {c["golden_line"]} ”
            </div>
            
            <p class="chapter-paragraph-text" style="text-align:center; font-style:italic; margin-top:2rem;">
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
    """Render Chapter 5: Intentions & Family Respect with dedicated card boxes and pause-on-hover."""
    reset_scroll_to_top()
    c = content.INTENTIONS_SECTION
    
    cards_html = f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_intentions" id="sec_wrapper_intentions">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="intentions-grid-container">
    """
    
    for item in c["intentions"]:
        cards_html += f"""
            <div class="intention-point-card intention-item-card">
                <div class="intention-card-header">
                    <span class="intention-icon">❤️</span>
                    <h3 class="intention-card-title">{item["title"]}</h3>
                </div>
                <p class="intention-card-body">{item["content"]}</p>
            </div>
        """
        
    cards_html += f"""
        </div>
        <div class="intentions-family-card floating-element">
            <span class="family-card-icon">🏡</span>
            <p class="chapter-paragraph-text" style="margin-bottom:0; font-style:italic;">
                {c["family_note"]}
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
    """Render Chapter 6: Prayer & Duas with smooth 3D slide-down."""
    reset_scroll_to_top()
    c = content.DUA_SECTION
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_dua" id="sec_wrapper_dua">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="dua-prayer-card floating-element">
            <div class="dua-card-hands-icon">🤲 🤍</div>
    """)
    for p in c["paragraphs"]:
        ui(f'<p class="dua-paragraph-text">{p}</p>')

    ui(f"""
            <div class="dua-ayah-highlight-box floating-element">
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
    
    paragraphs_html = "".join([f'<p class="chapter-paragraph-text" style="color: #e0d0d8; line-height: 1.7; font-size: 1rem; margin-bottom: 16px;">{p}</p>' for p in c["paragraphs"]])
    
    ui(f"""
    <div class="v2-chapter-container feature-section-enter chapter-page-enter section-floating-enter" key="sec_wrapper_goodbye" id="sec_wrapper_goodbye">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="final-note-section-wrapper">
            <!-- 1. Background Content (Gets blurred on focus) -->
            <div class="final-note-bg-content">
                <div class="chapter-letter-card finale-letter-card">
                    {paragraphs_html}
                    
                    <div class="finale-quote-highlight" style="color: #e2a8b8; font-style: italic; font-size: 0.95rem; margin-bottom: 8px;">
                        {c["highlighted_line"]}
                    </div>
                    
                    <div class="finale-special-monolith">
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
            if st.button("Read My Final Words ✉️", key="reveal_final_words_btn", type="primary", use_container_width=True):
                st.session_state["show_final_words"] = True
                st.rerun()
    else:
        ui(f"""
            <!-- 2. Focused Floating Letter Card -->
            <div class="final-letter-card finale-revealed-box">
                <div class="final-letter-header revealed-sub-badge">From Awais to Almas</div>
                <div class="final-letter-body revealed-prayer-text">{c["absolute_last_line"]}</div>
                <div class="final-letter-emojis revealed-amen-flower">🌸 🤍 🤲</div>
            </div>
        """)

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
    if "app_view" not in st.session_state:
        st.session_state.app_view = "landing"
    if "active_section" not in st.session_state:
        st.session_state.active_section = None
    if "startup_completed" not in st.session_state:
        st.session_state.startup_completed = False
    if "show_final_words" not in st.session_state:
        st.session_state.show_final_words = False
    if "selected_memory" not in st.session_state:
        st.session_state.selected_memory = None
    if "visited_chapters" not in st.session_state:
        st.session_state.visited_chapters = {"home"}

    # Support URL query parameter routing
    url_view = st.query_params.get("view")
    if url_view in ["landing", "journey_transition", "journey_menu", "menu", "section"]:
        mapped_view = "journey_menu" if url_view == "menu" else url_view
        if st.session_state.app_view != mapped_view:
            st.session_state.app_view = mapped_view

    url_chap = st.query_params.get("chapter")
    if url_chap and url_chap in [c["id"] for c in config.CHAPTERS]:
        st.session_state.app_view = "section"
        st.session_state.active_section = url_chap

    # 2. Global Styles
    load_styles()

    # 3. First-load Startup Screen (Display starting loader FIRST, prevent landing page from flashing)
    if not st.session_state.get("startup_completed", False):
        render_startup_screen()
        return

    # 4. Top-Level Bridge Navigation Dispatcher (Evaluated FIRST to prevent waterfall re-renders)
    render_hidden_bridge_dispatcher()

    # 5. Connect JavaScript Audio, 3D WebGL & Navigation Bridge
    app_view = st.session_state.app_view
    active_section = st.session_state.get("active_section") or "home"
    render_cinematic_atmosphere(active_section if app_view == "section" else "home")
    render_sidebar_and_navigation_bridge(app_view, active_section)

    # 6. Sidebar (Mounted ONLY inside the Journey — not on Landing or Journey Transition)
    if app_view in ["journey_menu", "section"]:
        render_sidebar()

    # 7. Strict Mutually Exclusive View Hierarchy
    if app_view == "landing":
        render_landing()
    elif app_view == "journey_transition":
        render_journey_loader()
    elif app_view in ["journey_menu", "menu"]:
        render_journey_menu()
    elif app_view == "section":
        render_section(st.session_state.get("active_section") or "welcome")


if __name__ == "__main__":
    main()
