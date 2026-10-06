"""YOUZTH CLUB single-page landing website."""

from __future__ import annotations

import base64
from functools import lru_cache
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
HERO_IMAGE = ROOT / "pics" / "YOUZTH CLUBNEW.png"
LOGO_IMAGE = ROOT / "pics" / "logo2.png"
CSS_FILE = ROOT / "styles" / "main.css"
TELEGRAM_URL = "https://t.me/YOUZTH_CLUB"
THEME_CONTROLLER = """
<script>
(() => {
  const storageKey = "youzth-club-theme";
  const root = document.documentElement;
  const media = window.matchMedia("(prefers-color-scheme: dark)");

  const savedTheme = () => {
    try {
      const saved = window.localStorage.getItem(storageKey);
      if (saved === "light" || saved === "dark") return saved;
    } catch (error) {}
    return media.matches ? "dark" : "light";
  };

  const syncToggle = (theme) => {
    const isDark = theme === "dark";
    const label = isDark ? "Switch to light mode" : "Switch to dark mode";
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      button.setAttribute("aria-label", label);
      button.setAttribute("title", label);
      button.setAttribute("aria-pressed", String(isDark));
    });
  };

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    root.style.colorScheme = theme;
    syncToggle(theme);
  };

  if (!window.__youzthThemeControllerInitialized) {
    window.__youzthThemeControllerInitialized = true;
    document.addEventListener("click", (event) => {
      const button = event.target instanceof Element
        ? event.target.closest("[data-theme-toggle]")
        : null;
      if (!button) return;

      const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
      try {
        window.localStorage.setItem(storageKey, nextTheme);
      } catch (error) {}
      applyTheme(nextTheme);
    });

    media.addEventListener("change", (event) => {
      let saved = null;
      try {
        saved = window.localStorage.getItem(storageKey);
      } catch (error) {}
      if (!saved) applyTheme(event.matches ? "dark" : "light");
    });

    const observer = new MutationObserver(() => {
      if (document.querySelector("[data-theme-toggle]")) {
        syncToggle(root.dataset.theme);
        observer.disconnect();
      }
    });
    observer.observe(root, { childList: true, subtree: true });
  }

  applyTheme(savedTheme());

  // Streamlit Cloud places its viewer badge and creator profile beside the app iframe.
  try {
    const hostDocument = window.parent.document;
    if (hostDocument !== document && !hostDocument.getElementById("youzth-hide-streamlit-cloud-ui")) {
      const style = hostDocument.createElement("style");
      style.id = "youzth-hide-streamlit-cloud-ui";
      style.textContent = `
        a[href="https://streamlit.io/cloud"][class*="_viewerBadge_"],
        div[class*="_profileContainer_"]:has(img[data-testid="appCreatorAvatar"]) {
          display: none !important;
        }
      `;
      hostDocument.head.appendChild(style);
    }
  } catch (error) {}
})();
</script>
"""


@lru_cache(maxsize=2)
def image_data_uri(path: Path) -> str:
    """Embed a supplied image without depending on a separate asset server."""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def load_styles() -> None:
    st.markdown(f"<style>{CSS_FILE.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def render_theme_controller() -> None:
    st.html(THEME_CONTROLLER, unsafe_allow_javascript=True)


def render_nav(logo_uri: str) -> None:
    st.markdown(
        f"""
        <nav class="site-nav" aria-label="Main navigation">
          <div class="nav-inner">
            <a class="brand" href="#home" aria-label="YOUZTH CLUB home">
              <span class="brand-mark"><img src="{logo_uri}" alt="" /></span>
              <span class="brand-name">YOUZTH <strong>CLUB</strong></span>
            </a>
            <div class="nav-links">
              <a href="#home">Home</a>
              <a href="#about">About</a>
              <a href="#why-join">Why Join</a>
              <a href="#how-to-join">How to Join</a>
              <a href="#video">Video</a>
            </div>
            <a class="button button-red nav-join" href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">JOIN CLUB <span aria-hidden="true">↗</span></a>
            <button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch to dark mode" title="Switch to dark mode" aria-pressed="false">
              <svg class="theme-icon theme-icon-sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"></path></svg>
              <svg class="theme-icon theme-icon-moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20.4 15.2A8.5 8.5 0 0 1 8.8 3.6 8.5 8.5 0 1 0 20.4 15.2Z"></path></svg>
            </button>
            <details class="mobile-nav">
              <summary aria-label="Open navigation"><span></span><span></span><span></span></summary>
              <div class="mobile-nav-links">
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#why-join">Why Join</a>
                <a href="#how-to-join">How to Join</a>
                <a href="#video">Video</a>
                <a href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">JOIN CLUB</a>
              </div>
            </details>
          </div>
        </nav>
        """,
        unsafe_allow_html=True,
    )


def render_intro(hero_uri: str) -> None:
    st.markdown(
        f"""
          <section class="hero" id="home">
            <div class="section-inner hero-grid">
              <div class="hero-copy">
                <p class="eyebrow"><span class="eyebrow-line"></span> A community for what comes next</p>
                <h1>YOUZTH<br /><span>CLUB<span class="hero-period">.</span></span></h1>
                <p class="hero-lead">Young ideas.<br /><em>Real projects.</em></p>
                <p class="hero-description">We bring young innovators in Uzbekistan together to brainstorm, collaborate, and launch real projects.</p>
                <p class="hero-promise">Want to make a project but don't know how to start? Bring your vision. We'll help you turn it into a first step.</p>
                <div class="hero-actions">
                  <a class="button button-red" href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">JOIN YOUZTH CLUB <span aria-hidden="true">↗</span></a>
                  <a class="button button-outline" href="#video"><span class="play-icon" aria-hidden="true">▶</span> Watch Introduction</a>
                </div>
              </div>
              <div class="hero-art">
                <div class="hero-shape" aria-hidden="true"></div>
                <div class="hero-photo"><img src="{hero_uri}" alt="Colorful YOUZTH CLUB collage artwork" /></div>
                <div class="hero-art-caption"><span class="caption-dot"></span> BRING YOUR VISION</div>
              </div>
            </div>
          </section>

          <section class="value-strip" aria-label="What happens at YOUZTH CLUB">
            <div class="section-inner value-grid">
              <div class="value-item"><span class="value-number">01</span><div><h2>Ideas</h2><p>Turn ideas into something real</p></div></div>
              <div class="value-item"><span class="value-number">02</span><div><h2>Collaboration</h2><p>Build with other young people</p></div></div>
              <div class="value-item"><span class="value-number">03</span><div><h2>Projects</h2><p>Move from discussion to action</p></div></div>
              <div class="value-item"><span class="value-number">04</span><div><h2>Community</h2><p>Meet curious people</p></div></div>
            </div>
          </section>

          <section class="about section-space" id="about">
            <div class="section-inner about-grid">
              <div class="section-copy">
                <p class="section-kicker">01 / About us</p>
                <h2>What is <span>our goal?</span></h2>
                <p class="section-lead">The distance between an idea and a project can feel big. We help make that first step possible.</p>
                <p class="body-copy">Young people have ideas, but often don't know how to bring them into action or where to start. That is exactly why our club exists: to bridge the gap between having an idea and taking action.</p>
                <a class="text-link" href="#how-to-join">See how to join <span aria-hidden="true">↗</span></a>
              </div>
              <div class="process-panel" aria-label="From idea to first step to real project">
                <div class="process-panel-top"><span>THE YOUZTH JOURNEY</span><span class="process-star" aria-hidden="true">✳</span></div>
                <div class="process-step"><span class="process-count">01</span><strong>FROM IDEA</strong><span class="process-arrow" aria-hidden="true">↘</span></div>
                <div class="process-step"><span class="process-count">02</span><strong>TO FIRST STEP</strong><span class="process-arrow" aria-hidden="true">↘</span></div>
                <div class="process-step"><span class="process-count">03</span><strong>TO REAL PROJECT</strong><span class="process-arrow" aria-hidden="true">↗</span></div>
                <p>Start where you are. Build what you imagine.</p>
              </div>
            </div>
          </section>

          <section class="why-section section-space" id="why-join">
            <div class="section-inner">
              <div class="section-heading why-heading">
                <div><p class="section-kicker">02 / Why join</p><h2>Why <span>join us?</span></h2></div>
                <p>By brainstorming and collaborating, we turn big ideas into an actual plan. Young people already have the most valuable thing — curiosity. We help direct it the right way.</p>
              </div>
              <div class="benefit-grid">
                <article class="benefit-card"><span class="benefit-number">01 / THINK</span><h3>Brainstorm</h3><p>Develop your idea with other curious people.</p><span class="benefit-arrow" aria-hidden="true">↗</span></article>
                <article class="benefit-card"><span class="benefit-number">02 / CONNECT</span><h3>Collaborate</h3><p>Meet people with different skills and perspectives.</p><span class="benefit-arrow" aria-hidden="true">↗</span></article>
                <article class="benefit-card"><span class="benefit-number">03 / PLAN</span><h3>Build</h3><p>Turn discussions into an actionable project plan.</p><span class="benefit-arrow" aria-hidden="true">↗</span></article>
                <article class="benefit-card"><span class="benefit-number">04 / BEGIN</span><h3>Launch</h3><p>Take the first real step instead of leaving the idea on paper.</p><span class="benefit-arrow" aria-hidden="true">↗</span></article>
              </div>
            </div>
          </section>
        """,
        unsafe_allow_html=True,
    )


def render_video() -> None:
    with st.container(key="video_section"):
        st.markdown(
            """
            <div class="video-heading" id="video">
              <p class="section-kicker">03 / Get to know us</p>
              <h2>See what YOUZTH<br /><span>CLUB is about.</span></h2>
              <p>Watch our introduction and discover what we're building together.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.video("https://www.youtube.com/watch?v=6KvU_oyD7Eo")


def render_how_to_join() -> None:
    st.markdown(
        f"""
        <section class="how-section section-space" id="how-to-join">
          <div class="section-inner">
            <div class="how-intro">
              <div><p class="section-kicker">04 / Your next step</p><h2>How to <span>join?</span></h2></div>
              <p>YOUZTH CLUB is accessible to everyone. Join our official Telegram channel to enter the community, introduce yourself, and start collaborating.</p>
            </div>
            <div class="join-steps">
              <div class="join-step"><span>01</span><h3>Browse events</h3><p>Enter the YOUZTH CLUB community.</p></div>
              <div class="join-step"><span>02</span><h3>Apply</h3><p>Register for an event.</p></div>
              <div class="join-step"><span>03</span><h3>Start collaborating</h3><p>Meet other young people and turn ideas into real projects.</p></div>
            </div>
            <div class="how-cta"><a class="button button-red" href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">JOIN OUR TELEGRAM <span aria-hidden="true">↗</span></a></div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_footer(logo_uri: str) -> None:
    st.markdown(
        f"""
        <section class="final-cta">
          <div class="section-inner final-cta-inner">
            <div><p class="section-kicker">THE FIRST STEP STARTS HERE</p><h2>Got an idea?<br /><span>Let's make the first step together.</span></h2></div>
            <a class="button button-red" href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">JOIN ON TELEGRAM <span aria-hidden="true">→</span></a>
          </div>
        </section>
        <footer class="site-footer">
          <div class="section-inner footer-main">
            <div class="footer-brand-block">
              <a class="brand" href="#home" aria-label="YOUZTH CLUB home"><span class="brand-mark"><img src="{logo_uri}" alt="" /></span><span class="brand-name">YOUZTH <strong>CLUB</strong></span></a>
              <p>A community where young people in Uzbekistan turn curiosity into action.</p>
            </div>
            <div class="footer-links"><span>EXPLORE</span><a href="#about">About</a><a href="#why-join">Why Join</a><a href="#video">Video</a><a href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">Join Club</a></div>
            <div class="footer-message"><span>BRING YOUR VISION</span><p>We'll help you turn it into a first step.</p></div>
          </div>
          <div class="section-inner footer-bottom"><span>© 2026 YOUZTH CLUB</span><a href="#home">Back to top ↑</a></div>
        </footer>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(page_title="YOUZTH CLUB", page_icon=str(LOGO_IMAGE), layout="wide", initial_sidebar_state="collapsed")
    load_styles()
    render_theme_controller()
    logo_uri = image_data_uri(LOGO_IMAGE)
    render_nav(logo_uri)
    render_intro(image_data_uri(HERO_IMAGE))
    render_video()
    render_how_to_join()
    render_footer(logo_uri)


if __name__ == "__main__":
    main()
