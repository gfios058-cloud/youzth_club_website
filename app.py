"""YOUZTH CLUB single-page landing website."""

from __future__ import annotations

import base64
import re
import sqlite3
from functools import lru_cache
from pathlib import Path

import streamlit as st

from applications import Application, save_application


ROOT = Path(__file__).resolve().parent
HERO_IMAGE = ROOT / "pics" / "YOUZTH CLUBNEW.png"
LOGO_IMAGE = ROOT / "pics" / "logo.png"
CSS_FILE = ROOT / "styles" / "main.css"
TELEGRAM_URL = "https://t.me/YOUZTH_CLUB"


@lru_cache(maxsize=2)
def image_data_uri(path: Path) -> str:
    """Embed a supplied image without depending on a separate asset server."""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def load_styles() -> None:
    st.markdown(f"<style>{CSS_FILE.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


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
            <a class="button button-red nav-apply" href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">Apply to Join <span aria-hidden="true">↗</span></a>
            <details class="mobile-nav">
              <summary aria-label="Open navigation"><span></span><span></span><span></span></summary>
              <div class="mobile-nav-links">
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#why-join">Why Join</a>
                <a href="#how-to-join">How to Join</a>
                <a href="#video">Video</a>
                <a href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">Apply to Join</a>
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
                  <a class="button button-red" href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">Apply to Join <span aria-hidden="true">↗</span></a>
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
              <p>YOUZTH CLUB is accessible to everyone. Click “Apply to Join” to open our official Telegram channel and connect with the community. We're happy to welcome you.</p>
            </div>
            <div class="join-steps">
              <div class="join-step"><span>01</span><h3>Apply</h3><p>Open the official Telegram channel.</p></div>
              <div class="join-step"><span>02</span><h3>Tell us about yourself</h3><p>Share what interests you and what you want to create.</p></div>
              <div class="join-step"><span>03</span><h3>Join the community</h3><p>Take your next step with other young people.</p></div>
            </div>
            <div class="how-cta"><a class="button button-red" href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">Apply to Join <span aria-hidden="true">↗</span></a></div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_application() -> None:
    with st.container(key="application_section"):
        st.markdown(
            """
            <div class="application-heading">
              <p class="section-kicker">05 / Make your move</p>
              <h2>Ready to turn your<br /><span>idea into action?</span></h2>
              <p>Join YOUZTH CLUB and start building with us.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("join_form", clear_on_submit=False, border=False):
            name_column, age_column = st.columns(2)
            with name_column:
                full_name = st.text_input("Full name *", placeholder="Your full name")
            with age_column:
                age_text = st.text_input("Age *", placeholder="Your age", max_chars=3)

            city_column, email_column = st.columns(2)
            with city_column:
                city = st.text_input("City *", placeholder="Where are you based?")
            with email_column:
                email = st.text_input("Email *", placeholder="you@example.com")

            telegram_column, idea_column = st.columns(2)
            with telegram_column:
                telegram = st.text_input("Telegram username", placeholder="@username (optional)")
            with idea_column:
                has_project_idea = st.selectbox(
                    "Do you already have a project idea? *",
                    ["Choose an answer", "Yes", "Not yet", "I'm exploring"],
                )
            interests = st.text_input("What are you interested in? *", placeholder="Your interests or skills")
            message = st.text_area(
                "Why do you want to join? *",
                placeholder="Tell us a little about what you want to explore or build.",
                height=116,
            )
            submitted = st.form_submit_button("SEND APPLICATION  ↗", use_container_width=True)

        if submitted:
            required_text = [full_name, city, interests, email, message]
            if not all(value.strip() for value in required_text) or not age_text.strip() or has_project_idea == "Choose an answer":
                st.error("Please complete all required fields before submitting.")
            elif not age_text.strip().isdigit() or not 1 <= int(age_text.strip()) <= 120:
                st.error("Please enter an age between 1 and 120.")
            elif not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email.strip()):
                st.error("Please enter a valid email address.")
            else:
                application: Application = {
                    "full_name": full_name.strip(),
                    "age": int(age_text.strip()),
                    "city": city.strip(),
                    "email": email.strip(),
                    "telegram": telegram.strip(),
                    "interests": interests.strip(),
                    "has_project_idea": has_project_idea,
                    "message": message.strip(),
                }
                try:
                    save_application(application)
                except (OSError, sqlite3.Error):
                    st.error("We couldn't save your application. Please try again later.")
                else:
                    st.success("Thank you for applying! Your application has been saved.")

        st.markdown(
            '<p class="application-note">Your application is saved on this site’s server for the club to review.</p>',
            unsafe_allow_html=True,
        )


def render_footer(logo_uri: str) -> None:
    st.markdown(
        f"""
        <section class="final-cta">
          <div class="section-inner final-cta-inner">
            <div><p class="section-kicker">THE FIRST STEP STARTS HERE</p><h2>Got an idea?<br /><span>Let's make the first step together.</span></h2></div>
            <a class="button button-red" href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">Apply to Join <span aria-hidden="true">↗</span></a>
          </div>
        </section>
        <footer class="site-footer">
          <div class="section-inner footer-main">
            <div class="footer-brand-block">
              <a class="brand" href="#home" aria-label="YOUZTH CLUB home"><span class="brand-mark"><img src="{logo_uri}" alt="" /></span><span class="brand-name">YOUZTH <strong>CLUB</strong></span></a>
              <p>A community where young people in Uzbekistan turn curiosity into action.</p>
            </div>
            <div class="footer-links"><span>EXPLORE</span><a href="#about">About</a><a href="#why-join">Why Join</a><a href="#video">Video</a><a href="{TELEGRAM_URL}" target="_blank" rel="noopener noreferrer">Apply</a></div>
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
    logo_uri = image_data_uri(LOGO_IMAGE)
    render_nav(logo_uri)
    render_intro(image_data_uri(HERO_IMAGE))
    render_video()
    render_how_to_join()
    render_application()
    render_footer(logo_uri)


if __name__ == "__main__":
    main()
