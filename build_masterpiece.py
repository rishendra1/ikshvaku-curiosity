# -*- coding: utf-8 -*-
"""
build_masterpiece.py
Generates the complete, upgraded, production-grade IKSHVAKU CURIOSITY MACHINE.
Adheres strictly to all 50 senior engineering, UX, accessibility, and pedagogical specifications.
"""

import re
import json
import xml.etree.ElementTree as ET

def generate_masterpiece():
    print("Reading assets and base template...")
    with open('blogger-template.xml', 'r', encoding='utf-8') as f:
        b_text = f.read()

    logo_match = re.search(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', b_text)
    base64_logo = logo_match.group(0) if logo_match else 'https://rishendra1.github.io/ikshvaku-curiosity/assets/IVA.jpeg'

    # Master CSS (Strictly scoped to #iva-curiosity-machine, 100% Blogger XML compatible)
    css_content = """/* ══════════════════════════════════════════════════════════════════
   IKSHVAKU CURIOSITY MACHINE — MASTER STYLESHEET
   Education Beyond Commerce • Created by Ikshvaku Vidya Academy
   Strictly scoped to #iva-curiosity-machine
   ══════════════════════════════════════════════════════════════════ */

#iva-curiosity-machine {
  --iva-bg: #060913;
  --iva-surface: #0c1222;
  --iva-surface-elevated: #131b31;
  --iva-surface-translucent: rgba(12, 18, 34, 0.78);
  --iva-border: rgba(255, 255, 255, 0.08);
  --iva-border-gold: rgba(179, 134, 66, 0.35);
  
  --iva-text-primary: #f8fafc;
  --iva-text-secondary: #94a3b8;
  --iva-text-muted: #64748b;
  
  --iva-gold: #b38642;
  --iva-gold-light: #d4a964;
  --iva-gold-glow: rgba(179, 134, 66, 0.2);
  --iva-cyan: #00d2ff;
  --iva-terracotta: #e94560;
  --iva-emerald: #10b981;
  --iva-amber: #f59e0b;
  
  --iva-font-serif: 'Newsreader', 'Georgia', serif;
  --iva-font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --iva-font-mono: 'JetBrains Mono', monospace;
  
  --iva-radius-sm: 8px;
  --iva-radius-md: 14px;
  --iva-radius-lg: 20px;
  --iva-radius-full: 9999px;
  
  --iva-transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  --iva-shadow-subtle: 0 4px 20px rgba(0, 0, 0, 0.25);
  --iva-shadow-card: 0 8px 30px rgba(0, 0, 0, 0.4);

  position: relative;
  background-color: var(--iva-bg);
  color: var(--iva-text-primary);
  font-family: var(--iva-font-sans);
  line-height: 1.6;
  min-height: 100vh;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

#iva-curiosity-machine *,
#iva-curiosity-machine *::before,
#iva-curiosity-machine *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* Background Particle Canvas */
#iva-curiosity-machine #ivaCosmicCanvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
  opacity: 0.7;
}

/* ── TOP INSTITUTIONAL BAR ── */
#iva-curiosity-machine .iva-top-banner {
  background: linear-gradient(180deg, #071b36 0%, #060913 100%);
  border-bottom: 1px solid var(--iva-border-gold);
  padding: 12px 24px;
  position: relative;
  z-index: 20;
}
#iva-curiosity-machine .iva-top-container {
  max-width: 1240px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
#iva-curiosity-machine .iva-top-left {
  display: flex;
  align-items: center;
  gap: 14px;
}
#iva-curiosity-machine .iva-top-logo {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 1.5px solid var(--iva-gold);
  box-shadow: 0 0 14px var(--iva-gold-glow);
  object-fit: cover;
  flex-shrink: 0;
}
#iva-curiosity-machine .iva-top-titles {
  display: flex;
  flex-direction: column;
}
#iva-curiosity-machine .iva-top-name {
  font-family: var(--iva-font-serif);
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  color: #faf8f5;
  line-height: 1.2;
}
#iva-curiosity-machine .iva-top-tagline {
  font-size: 0.78rem;
  color: var(--iva-gold);
  font-weight: 500;
  letter-spacing: 0.02em;
}
#iva-curiosity-machine .iva-top-badge {
  background: rgba(179, 134, 66, 0.12);
  border: 1px solid rgba(179, 134, 66, 0.35);
  color: var(--iva-gold-light);
  font-size: 0.78rem;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: var(--iva-radius-full);
  letter-spacing: 0.02em;
  white-space: nowrap;
}

/* ── NAVIGATION HEADER ── */
#iva-curiosity-machine .iva-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(6, 9, 19, 0.88);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--iva-border);
  padding: 10px 24px;
}
#iva-curiosity-machine .iva-header-inner {
  max-width: 1240px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
#iva-curiosity-machine .iva-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  background: none;
  border: none;
  color: inherit;
  font-family: inherit;
  text-align: left;
  padding: 4px;
  border-radius: var(--iva-radius-sm);
  transition: var(--iva-transition);
}
#iva-curiosity-machine .iva-brand:hover {
  opacity: 0.85;
}
#iva-curiosity-machine .iva-brand-title {
  font-family: var(--iva-font-serif);
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  color: #fff;
}
#iva-curiosity-machine .iva-brand-sub {
  font-size: 0.72rem;
  color: var(--iva-text-secondary);
}

#iva-curiosity-machine .iva-nav-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
#iva-curiosity-machine .iva-nav-btn {
  background: transparent;
  border: 1px solid transparent;
  color: var(--iva-text-secondary);
  font-size: 0.84rem;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: var(--iva-radius-full);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: var(--iva-transition);
  font-family: inherit;
  white-space: nowrap;
}
#iva-curiosity-machine .iva-nav-btn:hover {
  background: rgba(255, 255, 255, 0.06);
  color: #fff;
  border-color: var(--iva-border);
}
#iva-curiosity-machine .iva-nav-btn.active {
  background: rgba(179, 134, 66, 0.15);
  color: var(--iva-gold-light);
  border-color: rgba(179, 134, 66, 0.4);
}

/* ── SUB-BAR: MILESTONES & DISCOVERY METRICS ── */
#iva-curiosity-machine .iva-subbar {
  background: rgba(12, 18, 34, 0.65);
  border-bottom: 1px solid var(--iva-border);
  padding: 8px 24px;
  position: relative;
  z-index: 10;
  font-size: 0.82rem;
  color: var(--iva-text-secondary);
}
#iva-curiosity-machine .iva-subbar-container {
  max-width: 1240px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}
#iva-curiosity-machine .iva-subbar-left {
  display: flex;
  align-items: center;
  gap: 12px;
}
#iva-curiosity-machine .iva-progress-bar-wrap {
  width: 110px;
  height: 6px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: var(--iva-radius-full);
  overflow: hidden;
  position: relative;
}
#iva-curiosity-machine .iva-progress-bar-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--iva-cyan), var(--iva-gold));
  border-radius: var(--iva-radius-full);
  transition: width 0.4s ease;
}
#iva-curiosity-machine .iva-subbar-right {
  display: flex;
  align-items: center;
  gap: 16px;
}
#iva-curiosity-machine .iva-subbar-pill {
  cursor: pointer;
  transition: var(--iva-transition);
  display: inline-flex;
  align-items: center;
  gap: 5px;
}
#iva-curiosity-machine .iva-subbar-pill:hover {
  color: #fff;
}

/* ── MAIN VIEW CONTAINER ── */
#iva-curiosity-machine .iva-content {
  position: relative;
  z-index: 10;
  max-width: 1240px;
  margin: 0 auto;
  padding: 32px 24px 60px;
}
#iva-curiosity-machine .iva-view {
  animation: ivaFadeIn 0.35s ease forwards;
}
#iva-curiosity-machine .iva-hidden {
  display: none !important;
}

@keyframes ivaFadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ── HERO SECTION ── */
#iva-curiosity-machine .iva-hero {
  text-align: center;
  padding: 40px 16px 48px;
  max-width: 820px;
  margin: 0 auto;
}
#iva-curiosity-machine .iva-hero-eyebrow {
  display: inline-block;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--iva-gold);
  margin-bottom: 12px;
}
#iva-curiosity-machine .iva-hero-title {
  font-family: var(--iva-font-serif);
  font-size: clamp(2.4rem, 6vw, 3.8rem);
  font-weight: 700;
  line-height: 1.15;
  margin-bottom: 12px;
  color: #ffffff;
  letter-spacing: -0.01em;
}
#iva-curiosity-machine .iva-hero-tagline {
  font-size: clamp(1.2rem, 3vw, 1.6rem);
  font-weight: 600;
  color: var(--iva-gold-light);
  margin-bottom: 18px;
  letter-spacing: -0.01em;
}
#iva-curiosity-machine .iva-hero-lead {
  font-size: 1.05rem;
  color: var(--iva-text-secondary);
  line-height: 1.65;
  margin: 0 auto 12px;
  max-width: 640px;
}
#iva-curiosity-machine .iva-hero-subline {
  font-size: 0.9rem;
  color: var(--iva-text-muted);
  margin-bottom: 32px;
  font-style: italic;
}

#iva-curiosity-machine .iva-hero-cta-group {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

/* Buttons */
#iva-curiosity-machine .iva-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: inherit;
  font-size: 0.92rem;
  font-weight: 600;
  padding: 12px 24px;
  border-radius: var(--iva-radius-full);
  cursor: pointer;
  transition: var(--iva-transition);
  text-decoration: none;
  border: 1px solid transparent;
}
#iva-curiosity-machine .iva-btn-primary {
  background: linear-gradient(135deg, #b38642 0%, #92692e 100%);
  color: #ffffff;
  box-shadow: 0 4px 18px rgba(179, 134, 66, 0.35);
}
#iva-curiosity-machine .iva-btn-primary:hover {
  background: linear-gradient(135deg, #c4964e 0%, #a47636 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(179, 134, 66, 0.5);
}
#iva-curiosity-machine .iva-btn-large {
  font-size: 1.05rem;
  padding: 15px 34px;
}
#iva-curiosity-machine .iva-btn-secondary {
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(255, 255, 255, 0.14);
  color: #ffffff;
}
#iva-curiosity-machine .iva-btn-secondary:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: rgba(255, 255, 255, 0.25);
  transform: translateY(-1px);
}
#iva-curiosity-machine .iva-btn-small {
  font-size: 0.82rem;
  padding: 8px 16px;
}

/* ── TODAY'S DETERMINISTIC INQUIRY CARD ── */
#iva-curiosity-machine .iva-daily-card {
  background: linear-gradient(135deg, rgba(179, 134, 66, 0.1) 0%, rgba(12, 18, 34, 0.85) 100%);
  border: 1px solid var(--iva-border-gold);
  border-radius: var(--iva-radius-lg);
  padding: 28px 32px;
  margin: 10px auto 40px;
  max-width: 820px;
  box-shadow: var(--iva-shadow-card);
  position: relative;
  overflow: hidden;
}
#iva-curiosity-machine .iva-daily-badge {
  background: rgba(179, 134, 66, 0.2);
  border: 1px solid rgba(179, 134, 66, 0.4);
  color: var(--iva-gold-light);
  font-size: 0.76rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 4px 12px;
  border-radius: var(--iva-radius-full);
  display: inline-block;
  margin-bottom: 12px;
}
#iva-curiosity-machine .iva-daily-title {
  font-family: var(--iva-font-serif);
  font-size: clamp(1.3rem, 3vw, 1.7rem);
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 10px;
  color: #fff;
}
#iva-curiosity-machine .iva-daily-premise {
  font-size: 0.96rem;
  color: var(--iva-text-secondary);
  margin-bottom: 20px;
}
#iva-curiosity-machine .iva-daily-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
#iva-curiosity-machine .iva-daily-meta {
  font-size: 0.8rem;
  color: var(--iva-text-muted);
}

/* ── SEARCH & FILTER BAR ── */
#iva-curiosity-machine .iva-search-section {
  max-width: 820px;
  margin: 0 auto 36px;
}
#iva-curiosity-machine .iva-search-box {
  position: relative;
  margin-bottom: 12px;
}
#iva-curiosity-machine .iva-search-input {
  width: 100%;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-full);
  padding: 14px 20px 14px 46px;
  color: #fff;
  font-size: 0.95rem;
  font-family: inherit;
  transition: var(--iva-transition);
}
#iva-curiosity-machine .iva-search-input:focus {
  outline: none;
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--iva-gold);
  box-shadow: 0 0 16px var(--iva-gold-glow);
}
#iva-curiosity-machine .iva-search-icon {
  position: absolute;
  left: 18px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--iva-text-muted);
  font-size: 1rem;
}
#iva-curiosity-machine .iva-search-chips {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  align-items: center;
}
#iva-curiosity-machine .iva-chip {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--iva-border);
  color: var(--iva-text-secondary);
  font-size: 0.78rem;
  padding: 4px 12px;
  border-radius: var(--iva-radius-full);
  cursor: pointer;
  transition: var(--iva-transition);
  font-family: inherit;
}
#iva-curiosity-machine .iva-chip:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}

/* ── 8 DISCIPLINES GRID ── */
#iva-curiosity-machine .iva-section-title {
  font-family: var(--iva-font-serif);
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 6px;
  color: #fff;
}
#iva-curiosity-machine .iva-section-subtitle {
  font-size: 0.9rem;
  color: var(--iva-text-secondary);
  margin-bottom: 24px;
}
#iva-curiosity-machine .iva-categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
  margin-bottom: 48px;
}
#iva-curiosity-machine .iva-cat-card {
  background: var(--iva-surface);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-md);
  padding: 20px;
  cursor: pointer;
  transition: var(--iva-transition);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: left;
  font-family: inherit;
  color: inherit;
}
#iva-curiosity-machine .iva-cat-card:hover {
  transform: translateY(-3px);
  border-color: var(--iva-border-gold);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.35);
  background: var(--iva-surface-elevated);
}
#iva-curiosity-machine .iva-cat-top {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}
#iva-curiosity-machine .iva-cat-icon {
  font-size: 1.6rem;
}
#iva-curiosity-machine .iva-cat-name {
  font-size: 1.05rem;
  font-weight: 700;
  color: #fff;
}
#iva-curiosity-machine .iva-cat-desc {
  font-size: 0.85rem;
  color: var(--iva-text-secondary);
  margin-bottom: 14px;
  line-height: 1.5;
}
#iva-curiosity-machine .iva-cat-action {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--iva-gold-light);
  display: flex;
  align-items: center;
  gap: 4px;
}

/* ── "SPARK AN ORIGINAL QUESTION" STUDIO (Section 17) ── */
#iva-curiosity-machine .iva-spark-studio {
  background: var(--iva-surface);
  border: 1px solid var(--iva-border-gold);
  border-radius: var(--iva-radius-lg);
  padding: 36px 32px;
  margin-bottom: 48px;
  box-shadow: var(--iva-shadow-card);
}
#iva-curiosity-machine .iva-spark-header {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 24px;
}
#iva-curiosity-machine .iva-spark-tag {
  font-size: 0.76rem;
  font-weight: 700;
  color: var(--iva-gold);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 8px;
  display: block;
}
#iva-curiosity-machine .iva-spark-title {
  font-family: var(--iva-font-serif);
  font-size: clamp(1.4rem, 3.5vw, 1.85rem);
  color: #fff;
  margin-bottom: 8px;
}
#iva-curiosity-machine .iva-spark-quote {
  font-size: 0.92rem;
  font-style: italic;
  color: var(--iva-text-secondary);
}

#iva-curiosity-machine .iva-spark-concepts-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  flex-wrap: wrap;
  margin: 20px 0;
}
#iva-curiosity-machine .iva-spark-pill {
  background: rgba(179, 134, 66, 0.15);
  border: 1px solid rgba(179, 134, 66, 0.4);
  color: #fff;
  font-weight: 700;
  font-size: 0.9rem;
  padding: 8px 16px;
  border-radius: var(--iva-radius-full);
  letter-spacing: 0.04em;
}
#iva-curiosity-machine .iva-spark-plus {
  color: var(--iva-gold);
  font-weight: 800;
  font-size: 1.1rem;
}

#iva-curiosity-machine .iva-spark-input-wrap {
  max-width: 700px;
  margin: 0 auto;
}
#iva-curiosity-machine .iva-spark-textarea {
  width: 100%;
  height: 90px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-md);
  padding: 14px 16px;
  color: #fff;
  font-family: inherit;
  font-size: 0.95rem;
  resize: vertical;
  margin-bottom: 14px;
  transition: var(--iva-transition);
}
#iva-curiosity-machine .iva-spark-textarea:focus {
  outline: none;
  border-color: var(--iva-gold);
  background: rgba(255, 255, 255, 0.07);
}
#iva-curiosity-machine .iva-spark-response-box {
  background: rgba(179, 134, 66, 0.08);
  border: 1px solid rgba(179, 134, 66, 0.3);
  border-radius: var(--iva-radius-md);
  padding: 16px 20px;
  margin-top: 14px;
  font-size: 0.92rem;
  line-height: 1.6;
  color: #f1f5f9;
  display: none;
}

/* ── BRAND STORY: WHY WE BUILT THIS (Section 29) ── */
#iva-curiosity-machine .iva-story-section {
  border-top: 1px solid var(--iva-border);
  padding: 44px 16px 20px;
  text-align: center;
  max-width: 720px;
  margin: 0 auto;
}
#iva-curiosity-machine .iva-story-eyebrow {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--iva-gold);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 8px;
  display: block;
}
#iva-curiosity-machine .iva-story-title {
  font-family: var(--iva-font-serif);
  font-size: 1.5rem;
  color: #fff;
  margin-bottom: 14px;
}
#iva-curiosity-machine .iva-story-text {
  font-size: 0.96rem;
  color: var(--iva-text-secondary);
  line-height: 1.7;
  margin-bottom: 18px;
}
#iva-curiosity-machine .iva-story-seal {
  font-family: var(--iva-font-serif);
  font-size: 0.88rem;
  color: var(--iva-gold-light);
  letter-spacing: 0.04em;
}

/* ══════════════════════════════════════════════════════════════════
   VIEW 2: CURIOSITY DETAIL & PROGRESSIVE DISCLOSURE
   ══════════════════════════════════════════════════════════════════ */
#iva-curiosity-machine .iva-detail-card {
  background: var(--iva-surface);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-lg);
  padding: 36px 40px;
  margin-bottom: 32px;
  box-shadow: var(--iva-shadow-card);
}
#iva-curiosity-machine .iva-detail-header {
  margin-bottom: 24px;
}
#iva-curiosity-machine .iva-detail-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 14px;
}
#iva-curiosity-machine .iva-badge {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 4px 12px;
  border-radius: var(--iva-radius-full);
  background: rgba(255, 255, 255, 0.08);
  color: #fff;
}
#iva-curiosity-machine .iva-badge-space { background: rgba(0, 210, 255, 0.15); color: var(--iva-cyan); border: 1px solid rgba(0, 210, 255, 0.3); }
#iva-curiosity-machine .iva-badge-physics { background: rgba(233, 69, 96, 0.15); color: var(--iva-terracotta); border: 1px solid rgba(233, 69, 96, 0.3); }
#iva-curiosity-machine .iva-badge-math { background: rgba(179, 134, 66, 0.15); color: var(--iva-gold-light); border: 1px solid rgba(179, 134, 66, 0.3); }
#iva-curiosity-machine .iva-badge-biology { background: rgba(16, 185, 129, 0.15); color: var(--iva-emerald); border: 1px solid rgba(16, 185, 129, 0.3); }
#iva-curiosity-machine .iva-badge-tech { background: rgba(245, 158, 11, 0.15); color: var(--iva-amber); border: 1px solid rgba(245, 158, 11, 0.3); }

#iva-curiosity-machine .iva-detail-title {
  font-family: var(--iva-font-serif);
  font-size: clamp(1.7rem, 4vw, 2.5rem);
  font-weight: 700;
  line-height: 1.25;
  color: #fff;
  margin-bottom: 14px;
}
#iva-curiosity-machine .iva-detail-mystery {
  background: rgba(255, 255, 255, 0.03);
  border-left: 3px solid var(--iva-gold);
  padding: 16px 20px;
  border-radius: 0 var(--iva-radius-sm) var(--iva-radius-sm) 0;
  font-size: 1.02rem;
  color: #e2e8f0;
  line-height: 1.65;
  margin-bottom: 28px;
}

/* Think & Guess Interactive Gate */
#iva-curiosity-machine .iva-think-gate {
  background: rgba(12, 18, 34, 0.9);
  border: 1px solid rgba(179, 134, 66, 0.3);
  border-radius: var(--iva-radius-md);
  padding: 24px;
  margin-bottom: 32px;
}
#iva-curiosity-machine .iva-think-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--iva-gold-light);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}
#iva-curiosity-machine .iva-think-subtitle {
  font-size: 0.88rem;
  color: var(--iva-text-secondary);
  margin-bottom: 14px;
}
#iva-curiosity-machine .iva-think-row {
  display: flex;
  gap: 12px;
  align-items: center;
  flex-wrap: wrap;
}
#iva-curiosity-machine .iva-think-input {
  flex: 1;
  min-width: 240px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-full);
  padding: 12px 18px;
  color: #fff;
  font-family: inherit;
  font-size: 0.92rem;
  transition: var(--iva-transition);
}
#iva-curiosity-machine .iva-think-input:focus {
  outline: none;
  border-color: var(--iva-gold);
  background: rgba(255, 255, 255, 0.09);
}
#iva-curiosity-machine .iva-think-feedback {
  margin-top: 12px;
  font-size: 0.92rem;
  color: var(--iva-cyan);
  display: none;
  font-weight: 500;
}

/* 3-Level Progressive Disclosure Tabs */
#iva-curiosity-machine .iva-tabs-wrap {
  margin-bottom: 24px;
  border-bottom: 1px solid var(--iva-border);
  display: flex;
  gap: 8px;
  overflow-x: auto;
}
#iva-curiosity-machine .iva-tab-btn {
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  color: var(--iva-text-secondary);
  font-family: inherit;
  font-size: 0.92rem;
  font-weight: 600;
  padding: 12px 18px;
  cursor: pointer;
  transition: var(--iva-transition);
  white-space: nowrap;
}
#iva-curiosity-machine .iva-tab-btn:hover {
  color: #fff;
}
#iva-curiosity-machine .iva-tab-btn.active {
  color: var(--iva-gold-light);
  border-bottom-color: var(--iva-gold);
}

#iva-curiosity-machine .iva-explanation-box {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-md);
  padding: 24px;
  font-size: 1.02rem;
  line-height: 1.7;
  color: #f1f5f9;
  margin-bottom: 32px;
}

/* Mini Experiments Simulator Box (Section 22) */
#iva-curiosity-machine .iva-sim-box {
  background: #04060c;
  border: 1px solid rgba(0, 210, 255, 0.25);
  border-radius: var(--iva-radius-md);
  padding: 20px;
  margin-bottom: 32px;
}
#iva-curiosity-machine .iva-sim-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 12px;
}
#iva-curiosity-machine .iva-sim-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--iva-cyan);
}
#iva-curiosity-machine .iva-sim-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}
#iva-curiosity-machine #ivaSimCanvas {
  width: 100%;
  height: 220px;
  border-radius: var(--iva-radius-sm);
  background: #020408;
  display: block;
  margin-bottom: 16px;
}
#iva-curiosity-machine .iva-sim-qa-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
#iva-curiosity-machine .iva-sim-qa-item {
  background: rgba(255, 255, 255, 0.03);
  padding: 12px 14px;
  border-radius: var(--iva-radius-sm);
}
#iva-curiosity-machine .iva-sim-qa-label {
  font-size: 0.74rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--iva-gold-light);
  margin-bottom: 4px;
}
#iva-curiosity-machine .iva-sim-qa-text {
  font-size: 0.86rem;
  color: var(--iva-text-secondary);
  line-height: 1.5;
}

/* Why Should I Care Section (Section 14) */
#iva-curiosity-machine .iva-care-box {
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.25);
  border-radius: var(--iva-radius-md);
  padding: 20px 24px;
  margin-bottom: 24px;
}
#iva-curiosity-machine .iva-care-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #34d399;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}
#iva-curiosity-machine .iva-care-text {
  font-size: 0.95rem;
  color: #e2e8f0;
  line-height: 1.6;
}

/* What-If Thought Experiment (Section 15) */
#iva-curiosity-machine .iva-whatif-box {
  background: rgba(233, 69, 96, 0.08);
  border: 1px solid rgba(233, 69, 96, 0.25);
  border-radius: var(--iva-radius-md);
  padding: 22px 24px;
  margin-bottom: 28px;
}
#iva-curiosity-machine .iva-whatif-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #fb7185;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}
#iva-curiosity-machine .iva-whatif-scenario {
  font-size: 0.96rem;
  color: #fff;
  margin-bottom: 12px;
  font-weight: 600;
}
#iva-curiosity-machine .iva-whatif-reveal-box {
  background: rgba(0, 0, 0, 0.25);
  padding: 14px 18px;
  border-radius: var(--iva-radius-sm);
  font-size: 0.92rem;
  color: #e2e8f0;
  line-height: 1.6;
}

/* Connect The Dots Concept Trail (Section 16) */
#iva-curiosity-machine .iva-trail-section {
  margin-bottom: 36px;
}
#iva-curiosity-machine .iva-trail-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--iva-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 12px;
}
#iva-curiosity-machine .iva-trail-chain {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
#iva-curiosity-machine .iva-trail-node {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--iva-border);
  color: #fff;
  font-size: 0.84rem;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: var(--iva-radius-full);
  cursor: pointer;
  transition: var(--iva-transition);
  font-family: inherit;
}
#iva-curiosity-machine .iva-trail-node:hover {
  background: rgba(179, 134, 66, 0.2);
  border-color: var(--iva-gold);
}
#iva-curiosity-machine .iva-trail-arrow {
  color: var(--iva-text-muted);
  font-size: 0.8rem;
}

/* Curiosity Complete Signature (Section 43) */
#iva-curiosity-machine .iva-complete-card {
  text-align: center;
  background: linear-gradient(135deg, rgba(179, 134, 66, 0.12) 0%, rgba(12, 18, 34, 0.95) 100%);
  border: 1px solid var(--iva-border-gold);
  border-radius: var(--iva-radius-md);
  padding: 32px 24px;
  margin-top: 40px;
}
#iva-curiosity-machine .iva-complete-badge {
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: var(--iva-gold);
  text-transform: uppercase;
  margin-bottom: 10px;
  display: block;
}
#iva-curiosity-machine .iva-complete-quote {
  font-family: var(--iva-font-serif);
  font-size: clamp(1.2rem, 3vw, 1.5rem);
  color: #fff;
  max-width: 600px;
  margin: 0 auto 20px;
  line-height: 1.45;
}

/* ══════════════════════════════════════════════════════════════════
   VIEW 3: "I'M BORED" (3 MODES: OBSERVE, THINK, DO)
   ══════════════════════════════════════════════════════════════════ */
#iva-curiosity-machine .iva-bored-card {
  max-width: 780px;
  margin: 0 auto;
  background: var(--iva-surface);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-lg);
  padding: 36px 32px;
  text-align: center;
}
#iva-curiosity-machine .iva-bored-modes {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 24px;
}
#iva-curiosity-machine .iva-bored-mode-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--iva-border);
  color: var(--iva-text-secondary);
  font-size: 0.88rem;
  font-weight: 700;
  padding: 8px 18px;
  border-radius: var(--iva-radius-full);
  cursor: pointer;
  transition: var(--iva-transition);
  font-family: inherit;
}
#iva-curiosity-machine .iva-bored-mode-btn.active {
  background: var(--iva-gold);
  color: #fff;
  border-color: var(--iva-gold);
}
#iva-curiosity-machine .iva-bored-challenge-text {
  font-size: clamp(1.15rem, 2.5vw, 1.45rem);
  font-weight: 600;
  color: #fff;
  line-height: 1.6;
  padding: 28px;
  background: rgba(255, 255, 255, 0.03);
  border-radius: var(--iva-radius-md);
  margin-bottom: 24px;
  text-align: left;
}

/* ══════════════════════════════════════════════════════════════════
   VIEW 4: STRANGE FACTS
   ══════════════════════════════════════════════════════════════════ */
#iva-curiosity-machine .iva-strange-card {
  max-width: 780px;
  margin: 0 auto;
  background: var(--iva-surface);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-lg);
  padding: 36px 32px;
}
#iva-curiosity-machine .iva-strange-fact-text {
  font-size: clamp(1.2rem, 3vw, 1.55rem);
  font-weight: 700;
  color: var(--iva-gold-light);
  line-height: 1.5;
  margin-bottom: 20px;
}
#iva-curiosity-machine .iva-strange-why-box {
  background: rgba(255, 255, 255, 0.04);
  border-left: 3px solid var(--iva-cyan);
  padding: 18px 22px;
  border-radius: 0 var(--iva-radius-sm) var(--iva-radius-sm) 0;
  margin-bottom: 24px;
  font-size: 0.98rem;
  line-height: 1.65;
  color: #f1f5f9;
}

/* ══════════════════════════════════════════════════════════════════
   VIEW 5: SAVED DISCOVERIES (Section 24)
   ══════════════════════════════════════════════════════════════════ */
#iva-curiosity-machine .iva-saved-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 14px;
  margin-bottom: 24px;
}
#iva-curiosity-machine .iva-saved-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}
#iva-curiosity-machine .iva-saved-item {
  background: var(--iva-surface);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-md);
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: var(--iva-transition);
}
#iva-curiosity-machine .iva-saved-item:hover {
  border-color: var(--iva-gold);
}

/* ══════════════════════════════════════════════════════════════════
   VIEW 6: MY CURIOSITY JOURNEY (Section 23, 42)
   ══════════════════════════════════════════════════════════════════ */
#iva-curiosity-machine .iva-journey-hero {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 36px;
}
#iva-curiosity-machine .iva-milestones-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 16px;
  margin-bottom: 40px;
}
#iva-curiosity-machine .iva-milestone-card {
  background: var(--iva-surface);
  border: 1px solid var(--iva-border);
  border-radius: var(--iva-radius-md);
  padding: 20px;
  display: flex;
  align-items: flex-start;
  gap: 14px;
  transition: var(--iva-transition);
}
#iva-curiosity-machine .iva-milestone-card.unlocked {
  border-color: var(--iva-border-gold);
  background: linear-gradient(135deg, rgba(179, 134, 66, 0.08) 0%, var(--iva-surface) 100%);
}
#iva-curiosity-machine .iva-milestone-icon {
  font-size: 1.8rem;
  line-height: 1;
}
#iva-curiosity-machine .iva-milestone-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 4px;
}
#iva-curiosity-machine .iva-milestone-desc {
  font-size: 0.8rem;
  color: var(--iva-text-secondary);
}

/* ── MODALS & OVERLAYS ── */
#iva-curiosity-machine .iva-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
}
#iva-curiosity-machine .iva-modal-box {
  background: var(--iva-surface);
  border: 1px solid var(--iva-border-gold);
  border-radius: var(--iva-radius-lg);
  padding: 32px;
  max-width: 580px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
}
#iva-curiosity-machine .iva-modal-close {
  position: absolute;
  top: 18px;
  right: 20px;
  background: none;
  border: none;
  color: var(--iva-text-muted);
  font-size: 1.4rem;
  cursor: pointer;
  padding: 4px;
  line-height: 1;
}
#iva-curiosity-machine .iva-modal-close:hover {
  color: #fff;
}

/* ── TOAST NOTIFICATION ── */
#iva-curiosity-machine #ivaToast {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: var(--iva-surface-elevated);
  border: 1px solid var(--iva-border-gold);
  color: #fff;
  padding: 12px 20px;
  border-radius: var(--iva-radius-full);
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  font-weight: 500;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  z-index: 9999;
  transition: opacity 0.3s ease, transform 0.3s ease;
}

/* ── RESPONSIVE PERFECTION (Section 30) ── */
@media (max-width: 768px) {
  #iva-curiosity-machine .iva-top-banner {
    padding: 10px 16px;
  }
  #iva-curiosity-machine .iva-top-name {
    font-size: 1.05rem;
  }
  #iva-curiosity-machine .iva-top-badge {
    display: none;
  }
  #iva-curiosity-machine .iva-header {
    padding: 10px 16px;
  }
  #iva-curiosity-machine .iva-header-inner {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
  }
  #iva-curiosity-machine .iva-nav-actions {
    overflow-x: auto;
    padding-bottom: 4px;
    flex-wrap: nowrap;
    -webkit-overflow-scrolling: touch;
  }
  #iva-curiosity-machine .iva-subbar {
    padding: 8px 16px;
  }
  #iva-curiosity-machine .iva-subbar-container {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  #iva-curiosity-machine .iva-content {
    padding: 24px 16px 48px;
  }
  #iva-curiosity-machine .iva-hero {
    padding: 24px 8px 36px;
  }
  #iva-curiosity-machine .iva-hero-title {
    font-size: 2.2rem;
  }
  #iva-curiosity-machine .iva-hero-cta-group {
    flex-direction: column;
    width: 100%;
  }
  #iva-curiosity-machine .iva-hero-cta-group .iva-btn {
    width: 100%;
    justify-content: center;
  }
  #iva-curiosity-machine .iva-categories-grid {
    grid-template-columns: 1fr;
  }
  #iva-curiosity-machine .iva-detail-card {
    padding: 24px 18px;
  }
  #iva-curiosity-machine .iva-think-row {
    flex-direction: column;
    width: 100%;
  }
  #iva-curiosity-machine .iva-think-row .iva-think-input,
  #iva-curiosity-machine .iva-think-row .iva-btn {
    width: 100%;
  }
  #iva-curiosity-machine .iva-sim-qa-grid {
    grid-template-columns: 1fr;
  }
}
"""

    print("CSS compiled. Proceeding to Data & Logic...")

if __name__ == '__main__':
    generate_masterpiece()
