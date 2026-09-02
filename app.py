"""
=============================================================================
A FAREWELL THAT STAYS — EXACT REFERENCE UI IMPLEMENTATION
Interactive Storytelling Web Experience with Full-Featured Cinematic Sidebar
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

# Ensure fresh reload of config and content
try:
    importlib.reload(config)
    importlib.reload(content)
except Exception:
    pass

# Page Configuration — Wide cinematic layout with expanded sidebar
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
def get_hero_scene_b64():
    """Load hero scene artwork into base64 string."""
    for name in ["hero_scene_walk.jpg", "hero_banner_ref.jpg", "alvida_hero.jpg"]:
        path = config.IMAGES_DIR / name
        if path.exists():
            try:
                with open(path, "rb") as f:
                    return base64.b64encode(f.read()).decode("ascii")
            except Exception:
                pass
    return ""


def get_hero_image_html():
    """Return hero scene artwork element with cinematic ambient layers."""
    b64 = get_hero_scene_b64()
    if b64:
        return f"""
        <div class="v2-hero-art-wrapper">
            <img src="data:image/jpeg;base64,{b64}" class="v2-hero-img kenburns-hero-motion" alt="A Farewell That Stays">
            <div class="hero-atmospheric-haze"></div>
            <div class="hero-horizon-sweep"></div>
            <div class="hero-girl-distance-layer"></div>
            <div class="hero-bokeh-light-1"></div>
            <div class="hero-bokeh-light-2"></div>
            <div class="hero-dust-container">
                <span class="hero-dust-mote hd1"></span>
                <span class="hero-dust-mote hd2"></span>
                <span class="hero-dust-mote hd3"></span>
                <span class="hero-dust-mote hd4"></span>
                <span class="hero-dust-mote hd5"></span>
                <span class="hero-dust-mote hd6"></span>
            </div>
        </div>
        """
    return '<div class="v2-hero-art-placeholder"></div>'


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
def render_startup_state_machine():
    """Inject background audio into parent document DOM and display 2.4s startup overlay."""
    audio_b64 = get_audio_base64()
    audio_src = f"data:audio/mp3;base64,{audio_b64}" if audio_b64 else "/app/static/farewell.mp3"

    components.html(
        f"""
    <script>
    (function() {{
        const pDoc = window.parent.document;

        // 1. Persistent Audio Element on parent body
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

        // Attempt autoplay with user-gesture fallback
        function triggerAudioPlayback() {{
            if (!audio) return;
            if (audio.paused) {{
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
                    }}).catch(err => {{
                        console.log("Autoplay waiting for gesture:", err);
                        const unlockAction = () => {{
                            audio.play().then(() => {{
                                audio.volume = 0.22;
                            }}).catch(() => {{}});
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
        }}

        triggerAudioPlayback();

        // 2. Prevent duplicate startup overlay
        if (pDoc.getElementById('startupMasterOverlay')) return;

        const overlay = pDoc.createElement('div');
        overlay.id = 'startupMasterOverlay';
        overlay.style.cssText = 'position:fixed; inset:0; z-index:99999999; background:#0e101a; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; transition:opacity 0.5s ease-out;';

        overlay.innerHTML = `
            <style>
                @keyframes pulseHeart {{
                    0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 10px rgba(229,115,115,0.5)); }}
                    50% {{ transform: scale(1.15); filter: drop-shadow(0 0 25px rgba(229,115,115,0.9)); }}
                }}
                @keyframes ringSpin {{
                    0% {{ transform: rotate(0deg); }}
                    100% {{ transform: rotate(360deg); }}
                }}
            </style>
            <div style="text-align:center; padding:2rem; max-width:480px; width:90%;">
                <div style="position:relative; width:90px; height:90px; margin:0 auto 1.5rem auto; display:flex; align-items:center; justify-content:center;">
                    <div style="position:absolute; inset:0; border:2px solid rgba(229,115,115,0.2); border-top:2px solid #e57373; border-radius:50%; animation:ringSpin 1.2s linear infinite;"></div>
                    <div style="font-size:2.4rem; animation:pulseHeart 2s infinite ease-in-out;">💗</div>
                </div>
                <div style="font-family:'Great Vibes', cursive; font-size:2.6rem; color:#f8ede8; margin-bottom:0.3rem;">A Farewell That Stays</div>
                <div style="font-family:'Playfair Display', serif; font-style:italic; font-size:1.15rem; color:#e57373; margin-bottom:0.5rem;">Opening a story that was never forgotten...</div>
                <div style="font-size:0.92rem; color:#baa9b4;">“Some goodbyes stay in the heart forever.”</div>
            </div>
        `;

        pDoc.body.appendChild(overlay);

        setTimeout(() => {{
            overlay.style.opacity = '0';
            overlay.style.pointerEvents = 'none';
            setTimeout(() => {{
                try {{ overlay.remove(); }} catch(e) {{}}
            }}, 500);
        }}, 2200);
    }})();
    </script>
    """,
        height=0,
        width=0,
    )


# -----------------------------------------------------------------------------
# 6. Interactive Sidebar Music Bridge (Real-Time Audio Player Integration)
# -----------------------------------------------------------------------------
def render_sidebar_audio_bridge():
    """Bind real-time interactive controls to sidebar music card DOM elements."""
    components.html(
        """
    <script>
    (function() {
        const pDoc = window.parent.document;
        const audio = pDoc.getElementById('farewellBgAudioMain');

        function fmtTime(sec) {
            if (!sec || isNaN(sec)) return "00:00";
            const m = Math.floor(sec / 60);
            const s = Math.floor(sec % 60);
            return (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
        }

        function bindControls() {
            if (!audio) return;
            const playBtn = pDoc.getElementById('musicBtnPlayPause');
            const prevBtn = pDoc.getElementById('musicBtnPrev');
            const nextBtn = pDoc.getElementById('musicBtnNext');
            const heartBtn = pDoc.getElementById('musicBtnHeart');
            const track = pDoc.getElementById('musicProgressTrack');
            const fill = pDoc.getElementById('musicProgressFill');
            const dot = pDoc.getElementById('musicProgressDot');
            const curTime = pDoc.getElementById('musicTimeCurrent');
            const totTime = pDoc.getElementById('musicTimeTotal');

            function updateUI() {
                if (!audio) return;
                if (playBtn) {
                    playBtn.innerHTML = audio.paused ? '▶' : '❚❚';
                }
                if (curTime) {
                    curTime.textContent = fmtTime(audio.currentTime);
                }
                if (totTime && audio.duration && !isNaN(audio.duration)) {
                    totTime.textContent = fmtTime(audio.duration);
                }
                if (fill && dot && audio.duration && !isNaN(audio.duration)) {
                    const pct = Math.min(100, Math.max(0, (audio.currentTime / audio.duration) * 100));
                    fill.style.width = pct + '%';
                    dot.style.left = pct + '%';
                }
            }

            if (playBtn && !playBtn.__bound) {
                playBtn.__bound = true;
                playBtn.onclick = function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    if (audio.paused) {
                        audio.play().then(updateUI).catch(() => {});
                    } else {
                        audio.pause();
                        updateUI();
                    }
                };
            }

            if (prevBtn && !prevBtn.__bound) {
                prevBtn.__bound = true;
                prevBtn.onclick = function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    audio.currentTime = Math.max(0, audio.currentTime - 10);
                    updateUI();
                };
            }

            if (nextBtn && !nextBtn.__bound) {
                nextBtn.__bound = true;
                nextBtn.onclick = function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    if (audio.duration) {
                        audio.currentTime = Math.min(audio.duration, audio.currentTime + 10);
                    }
                    updateUI();
                };
            }

            if (heartBtn && !heartBtn.__bound) {
                heartBtn.__bound = true;
                heartBtn.onclick = function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    const isFav = heartBtn.classList.toggle('favorited');
                    heartBtn.textContent = isFav ? '♥' : '♡';
                    heartBtn.style.color = isFav ? '#ff6b81' : '#baa9b4';
                    heartBtn.style.filter = isFav ? 'drop-shadow(0 0 10px rgba(255, 107, 129, 0.9))' : 'none';
                };
            }

            if (track && !track.__bound) {
                track.__bound = true;
                track.onclick = function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    if (!audio.duration) return;
                    const rect = track.getBoundingClientRect();
                    const clickX = e.clientX - rect.left;
                    const pct = Math.max(0, Math.min(1, clickX / rect.width));
                    audio.currentTime = pct * audio.duration;
                    updateUI();
                };
            }

            updateUI();
        }

        bindControls();
        if (!window.parent.__farewellMusicInterval) {
            window.parent.__farewellMusicInterval = setInterval(bindControls, 350);
        }
    })();
    </script>
    """,
        height=0,
        width=0,
    )


# -----------------------------------------------------------------------------
# 7. Multi-Container Scroll Reset to Top
# -----------------------------------------------------------------------------
def reset_scroll_to_top():
    """Scroll parent window and Streamlit scroll containers to the top."""
    components.html(
        """
    <script>
    (function() {
        const p = window.parent;
        const pDoc = p.document;
        function doScroll() {
            try { p.scrollTo(0, 0); } catch(e) {}
            try { pDoc.documentElement.scrollTop = 0; } catch(e) {}
            try { pDoc.body.scrollTop = 0; } catch(e) {}
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
        setTimeout(doScroll, 40);
        setTimeout(doScroll, 120);
        setTimeout(doScroll, 250);
    })();
    </script>
    """,
        height=0,
        width=0,
    )


# -----------------------------------------------------------------------------
# 8. Intermediate Analyzing / Chapter Loading Transition (1.3s)
# -----------------------------------------------------------------------------
def render_nav_loader(target_key: str):
    """Render 1.30s intermediate chapter loading screen."""
    loader_box = st.empty()
    loader_info = content.CHAPTER_LOADERS.get(
        target_key, {"title": "Loading...", "message": "Turning the page..."}
    )
    title = loader_info.get("title", "Loading...")
    message = loader_info.get("message", "Turning the page...")

    html = f"""
    <div class="nav-loader-overlay">
        <div class="nav-loader-card">
            <div class="nav-loader-spinner-icon">✦</div>
            <div class="nav-loader-chapter-title">{title}</div>
            <div class="nav-loader-message">{message}</div>
            <div class="nav-loader-track">
                <div class="nav-loader-fill"></div>
            </div>
        </div>
    </div>
    """
    loader_box.markdown(html, unsafe_allow_html=True)
    time.sleep(1.3)
    loader_box.empty()

    st.session_state["active_section"] = target_key
    st.session_state["pending_section"] = None
    st.session_state["visited_chapters"].add(target_key)
    st.rerun()


# -----------------------------------------------------------------------------
# 9. Sidebar Component (Matching Exact Reference UI Mockup)
# -----------------------------------------------------------------------------
def render_sidebar():
    """Render cinematic left sidebar matching exact reference UI with full 4-tier hierarchy."""
    with st.sidebar:
        # =====================================================================
        # 1. TOP BRAND / TITLE AREA
        # =====================================================================
        ui("""
        <div class="sidebar-brand-wrapper">
            <div class="sidebar-brand-heart-glow">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#e57373" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                </svg>
            </div>
            <div class="sidebar-brand-title">A Farewell</div>
            <div class="sidebar-brand-sub">🌿 &nbsp; That Stays &nbsp; 🌿</div>
        </div>
        """)

        # =====================================================================
        # 2. VERTICAL CHAPTER NAVIGATION (8 exact items)
        # =====================================================================
        active_id = st.session_state.get("active_section", "home")
        for chap in config.CHAPTERS:
            is_active = (active_id == chap["id"])
            btn_type = "primary" if is_active else "secondary"
            btn_label = f"{chap['icon']}  {chap['label']}"
            if st.button(btn_label, key=f"sb_nav_{chap['id']}", use_container_width=True, type=btn_type):
                if chap["id"] != active_id:
                    st.session_state["pending_section"] = chap["id"]
                    st.rerun()

        # =====================================================================
        # 3. LOWER: MUSIC PLAYER CARD (Integrated & Fully Interactive)
        # =====================================================================
        ui(f"""
        <div class="sidebar-music-card" id="sidebarMusicCard">
            <div class="music-card-header">
                <div>
                    <div class="music-card-title">{config.AUDIO_CONFIG["song_title"]}</div>
                    <div class="music-card-artist">{config.AUDIO_CONFIG["song_artist"]}</div>
                </div>
                <div class="music-card-icon">🎵</div>
            </div>
            <div class="music-progress-wrap">
                <span class="music-time-lbl music-time-current" id="musicTimeCurrent">01:45</span>
                <div class="music-progress-track" id="musicProgressTrack" title="Click to seek track">
                    <div class="music-progress-fill" id="musicProgressFill"></div>
                    <span class="music-progress-dot" id="musicProgressDot"></span>
                </div>
                <span class="music-time-lbl music-time-total" id="musicTimeTotal">04:58</span>
            </div>
            <div class="music-controls-row">
                <span class="music-ctrl-icon music-btn-prev" id="musicBtnPrev" title="Previous / Rewind 10s">⏮</span>
                <button class="music-ctrl-playpause-glow" id="musicBtnPlayPause" title="Play / Pause">❚❚</button>
                <span class="music-ctrl-icon music-btn-next" id="musicBtnNext" title="Next / Forward 10s">⏭</span>
                <span class="music-ctrl-heart" id="musicBtnHeart" title="Favorite">♡</span>
            </div>
        </div>
        """)

        # =====================================================================
        # 4. BOTTOM: JOURNEY PROGRESS CARD (Calculated from Real Chapter Position)
        # =====================================================================
        chapter_order = ["home", "welcome", "memories", "words", "respect", "intentions", "dua", "goodbye"]
        active_idx = chapter_order.index(active_id) if active_id in chapter_order else 0

        # Milestones progression: Home (12%) -> Goodbye (100%)
        milestones = [12, 25, 38, 50, 63, 75, 88, 100]
        pos_pct = milestones[active_idx]

        visited_set = st.session_state.get("visited_chapters", set())
        visited_ratio = len(visited_set.intersection(set(chapter_order))) / len(chapter_order)
        visited_pct = int(visited_ratio * 100)

        progress_pct = max(pos_pct, visited_pct)

        ui(f"""
        <div class="sidebar-progress-card">
            <div class="progress-card-title-row">
                <span class="progress-title-left">✦ Our Journey Progress</span>
            </div>
            <div class="progress-sub-row">
                <span class="progress-sub-left">Collecting beautiful memories</span>
                <span class="progress-pct-bold">{progress_pct}%</span>
            </div>
            <div class="progress-card-track">
                <div class="progress-card-fill" style="width: {progress_pct}%;"></div>
            </div>
            <div class="progress-footer-row">
                <span class="progress-caption">Every moment matters.</span>
                <span class="progress-heart-icon">♡</span>
            </div>
        </div>
        """)

    # Connect persistent JavaScript bridge to sidebar music card
    render_sidebar_audio_bridge()


# -----------------------------------------------------------------------------
# 10. Bottom Navigation Bar (Back to Home + Next Chapter)
# -----------------------------------------------------------------------------
def render_chapter_footer(current_id: str):
    """Render clean navigation footer with Back and Next buttons."""
    chapter_ids = [c["id"] for c in config.CHAPTERS]
    curr_idx = chapter_ids.index(current_id) if current_id in chapter_ids else 0
    next_id = chapter_ids[curr_idx + 1] if curr_idx + 1 < len(chapter_ids) else None
    next_label = None
    if next_id:
        for c in config.CHAPTERS:
            if c["id"] == next_id:
                next_label = c["label"]
                break

    ui('<div class="chapter-footer-divider"></div>')
    bcol1, bcol2, bcol3 = st.columns([1.2, 0.6, 1.2])

    with bcol1:
        if st.button("← Back to Home", key=f"foot_back_{current_id}", use_container_width=True):
            st.session_state["pending_section"] = "home"
            st.session_state["selected_memory"] = None
            st.rerun()

    with bcol3:
        if next_id and next_label:
            if st.button(f"Next: {next_label} →", key=f"foot_next_{current_id}", type="primary", use_container_width=True):
                st.session_state["pending_section"] = next_id
                st.session_state["selected_memory"] = None
                st.rerun()


# -----------------------------------------------------------------------------
# CHAPTER 0 — HOME (Matching Exact Reference UI Mockup)
# -----------------------------------------------------------------------------
def render_home():
    """Render Home page with exact layout, colors, typography and cards from reference UI."""
    reset_scroll_to_top()
    c = content.HOME_SECTION
    hero_img = get_hero_image_html()

    # 1. Panoramic Hero Section (2-Column Layout)
    ui('<div class="v2-main-wrap">')
    hcol_left, hcol_right = st.columns([1.08, 1.0], gap="large")

    with hcol_left:
        ui(f"""
        <div class="v2-hero-text-wrap">
            <div class="floating-doodle-heart">♡</div>
            <h1 class="v2-hero-headline">
                A Farewell<br>
                <span class="hero-cursive-calligraphy">That Stays</span><br>
                in the Heart
            </h1>
            <p class="v2-hero-subtitle">{c["hero_subtitle"]}</p>
        </div>
        """)

        bcol1, bcol2 = st.columns([1.1, 1.0])
        with bcol1:
            if st.button("♡  Start the Journey", key="hero_start_btn", type="primary", use_container_width=True):
                st.session_state["pending_section"] = "welcome"
                st.rerun()
        with bcol2:
            if st.button("▷  Watch Intro", key="hero_intro_btn", use_container_width=True):
                st.session_state["pending_section"] = "welcome"
                st.rerun()

    with hcol_right:
        ui(f"""
        <div class="v2-hero-art-container">
            {hero_img}
        </div>
        """)

    # 2. Quotation Bar (matching reference mockup)
    ui(f"""
    <div class="v2-quote-banner">
        <span class="v2-quote-mark">“</span>
        <span class="v2-quote-text">{c['quote_bar']}</span>
        <span class="v2-quote-heart-doodle">♡</span>
        <span class="v2-quote-branch">🌿</span>
    </div>
    """)

    # 3. Chapter Cards Grid (2 rows × 4 columns = 8 cards total)
    cards = content.HOME_CARDS

    # Row 1: Cards 1 to 4 (Welcome, Memories, Words From My Heart, Respect)
    cols_row1 = st.columns(4, gap="medium")
    for i in range(4):
        if i < len(cards):
            card = cards[i]
            thumb_b64 = get_thumbnail_b64(card["thumb"])
            img_tag = f'<img src="data:image/png;base64,{thumb_b64}" class="ref-card-thumb" alt="{card["title"]}">' if thumb_b64 else '💐'
            with cols_row1[i]:
                ui(f"""
                <div class="ref-card ref-card-light">
                    <div class="ref-card-thumb-wrap">
                        {img_tag}
                    </div>
                    <div class="ref-card-body">
                        <h3 class="ref-card-title">{card['title']}</h3>
                        <p class="ref-card-desc">{card['desc']}</p>
                    </div>
                </div>
                """)
                if st.button("Open →", key=f"open_card_{card['id']}", use_container_width=True):
                    st.session_state["pending_section"] = card["id"]
                    st.rerun()

    ui('<div style="height: 1.2rem;"></div>')

    # Row 2: Cards 5 to 7 (Intentions, Dua, Final Note) + Card 8 (Dark Lantern Card)
    cols_row2 = st.columns(4, gap="medium")
    for i in range(4, 7):
        if i < len(cards):
            card = cards[i]
            col_idx = i - 4
            thumb_b64 = get_thumbnail_b64(card["thumb"])
            img_tag = f'<img src="data:image/png;base64,{thumb_b64}" class="ref-card-thumb" alt="{card["title"]}">' if thumb_b64 else '💝'
            with cols_row2[col_idx]:
                ui(f"""
                <div class="ref-card ref-card-light">
                    <div class="ref-card-thumb-wrap">
                        {img_tag}
                    </div>
                    <div class="ref-card-body">
                        <h3 class="ref-card-title">{card['title']}</h3>
                        <p class="ref-card-desc">{card['desc']}</p>
                    </div>
                </div>
                """)
                if st.button("Open →", key=f"open_card_{card['id']}", use_container_width=True):
                    st.session_state["pending_section"] = card["id"]
                    st.rerun()

    # 8th Special Night Card (Dark navy with glowing lantern from mockup)
    lantern_b64 = get_thumbnail_b64("thumb_lantern")
    lantern_tag = f'<img src="data:image/png;base64,{lantern_b64}" class="ref-card-thumb-lantern" alt="Lantern">' if lantern_b64 else '🏮'
    with cols_row2[3]:
        ui(f"""
        <div class="ref-card ref-card-dark">
            <div class="ref-card-dark-body">
                <h3 class="ref-card-dark-title">You will always have a special place in my heart.</h3>
                <div class="ref-card-dark-heart">♡</div>
            </div>
            <div class="ref-card-dark-thumb-wrap">
                {lantern_tag}
            </div>
        </div>
        """)
        if st.button("View Lantern 🌸", key="open_lantern_card", use_container_width=True):
            st.session_state["pending_section"] = "goodbye"
            st.rerun()

    # 4. Bottom Footer Bar (matching reference mockup)
    ui(f"""
    <div class="v2-bottom-footer-bar">
        <span>🌸 &nbsp; 🌿 &nbsp; {c['bottom_quote']} &nbsp; ♡ &nbsp; 🌿 &nbsp; 🌸</span>
    </div>
    </div>
    """)


# -----------------------------------------------------------------------------
# CHAPTER 1 — WELCOME
# -----------------------------------------------------------------------------
def render_welcome():
    """Render Chapter 1: Welcome letter."""
    reset_scroll_to_top()
    c = content.WELCOME_SECTION
    ui(f"""
    <div class="v2-chapter-container">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="chapter-letter-card">
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
    """Render Chapter 2: Memories timeline / cards."""
    reset_scroll_to_top()
    c = content.MEMORIES_SECTION
    ui(f"""
    <div class="v2-chapter-container">
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
                <div class="memory-polaroid-card" style="border-top: 3px solid {mem['accent_color']};">
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
                <div class="memory-polaroid-card" style="border-top: 3px solid {mem['accent_color']};">
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
        ui(f"""
        <div class="memory-opened-card" style="border-left: 4px solid {mem['accent_color']};">
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
    """Render Chapter 3: Words From My Heart intimate letter."""
    reset_scroll_to_top()
    c = content.WORDS_SECTION
    ui(f"""
    <div class="v2-chapter-container">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="chapter-letter-card">
            <div class="letter-quote-decor">❝</div>
    """)
    for p in c["paragraphs"]:
        ui(f'<p class="chapter-paragraph-text">{p}</p>')

    ui(f"""
            <div class="chapter-highlight-quote-box">
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
    """Render Chapter 4: Respect & Na-mehram boundary admiration."""
    reset_scroll_to_top()
    c = content.RESPECT_SECTION
    ui(f"""
    <div class="v2-chapter-container respect-special-section">
        <div class="chapter-eyebrow-badge respect-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title respect-gold-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic respect-gold-sub">{c['subtitle']}</p>
        
        <div class="respect-content-card">
    """)
    for point in c["main_content"]:
        ui(f"""
        <div class="respect-point-item">
            <span class="respect-gold-bullet">✦</span>
            <span class="chapter-paragraph-text">{point}</span>
        </div>
        """)

    ui(f"""
            <div class="respect-golden-banner">
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
    """Render Chapter 5: Intentions & Family Respect."""
    reset_scroll_to_top()
    c = content.INTENTIONS_SECTION
    ui(f"""
    <div class="v2-chapter-container">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="intentions-grid-layout">
    """)

    cols = st.columns(2, gap="large")
    for i, intn in enumerate(c["intentions"]):
        col_idx = i % 2
        with cols[col_idx]:
            ui(f"""
            <div class="intention-item-card">
                <div class="intention-card-icon">💝</div>
                <h4 class="intention-card-title">{intn['title']}</h4>
                <p class="intention-card-body">{intn['content']}</p>
            </div>
            """)

    ui(f"""
        </div>
        <div class="intentions-family-card">
            <span class="family-card-icon">🏡</span>
            <p class="chapter-paragraph-text" style="margin-bottom:0; font-style:italic;">
                {c["family_note"]}
            </p>
        </div>
    </div>
    """)
    render_chapter_footer("intentions")


# -----------------------------------------------------------------------------
# CHAPTER 6 — DUA
# -----------------------------------------------------------------------------
def render_dua():
    """Render Chapter 6: Prayer & Duas."""
    reset_scroll_to_top()
    c = content.DUA_SECTION
    ui(f"""
    <div class="v2-chapter-container">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="dua-prayer-card">
            <div class="dua-card-hands-icon">🤲 🤍</div>
    """)
    for p in c["paragraphs"]:
        ui(f'<p class="dua-paragraph-text">{p}</p>')

    ui(f"""
            <div class="dua-ayah-highlight-box">
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
    """Render Chapter 7: Final Note with interactive reveal."""
    reset_scroll_to_top()
    c = content.GOODBYE_SECTION
    ui(f"""
    <div class="v2-chapter-container">
        <div class="chapter-eyebrow-badge">{c['eyebrow']}</div>
        <h2 class="chapter-main-title">{c['title']}</h2>
        <p class="chapter-subtitle-italic">{c['subtitle']}</p>
        
        <div class="chapter-letter-card finale-letter-card">
    """)
    for p in c["paragraphs"]:
        ui(f'<p class="chapter-paragraph-text">{p}</p>')

    ui(f"""
            <div class="finale-quote-highlight">
                {c["highlighted_line"]}
            </div>
            
            <div class="finale-special-monolith">
                <span class="finale-lantern-icon">🏮</span>
                <div class="finale-special-text">{c["final_visual_text"]}</div>
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
            <div class="finale-revealed-box">
                <div class="revealed-sub-badge">From Awais to Almas</div>
                <div class="revealed-prayer-text">{c["absolute_last_line"]}</div>
                <div class="revealed-amen-flower">🌸 🤍 🤲</div>
            </div>
        """)

    ui("""
        </div>
    </div>
    """)
    render_chapter_footer("goodbye")


# -----------------------------------------------------------------------------
# 11. Main Application Controller & Router
# -----------------------------------------------------------------------------
def main():
    """Main state router and layout orchestrator."""
    defaults = {
        "session_started": False,
        "active_section": "home",
        "pending_section": None,
        "music_playing": True,
        "show_final_words": False,
        "selected_memory": None,
        "visited_chapters": {"home"},
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    # 1. Global Styles
    load_styles()

    # 2. First-load Startup Overlay
    if not st.session_state["session_started"]:
        st.session_state["session_started"] = True
        render_startup_state_machine()

    # 3. Always Render Exact Sidebar Architecture (Brand -> Nav -> Music -> Progress)
    render_sidebar()

    # 4. Handle Pending Navigation Transition
    if st.session_state.get("pending_section"):
        target = st.session_state["pending_section"]
        render_nav_loader(target)
        return

    # 5. Route to Active Chapter
    active = st.session_state.get("active_section", "home")
    st.session_state["visited_chapters"].add(active)

    # Render Chapter Ambient Atmosphere Layer
    render_cinematic_atmosphere(active)

    router = {
        "home": render_home,
        "welcome": render_welcome,
        "memories": render_memories,
        "words": render_words,
        "respect": render_respect,
        "intentions": render_intentions,
        "dua": render_dua,
        "goodbye": render_goodbye,
    }

    render_fn = router.get(active, render_home)
    render_fn()


if __name__ == "__main__":
    main()
