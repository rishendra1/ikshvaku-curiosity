# -*- coding: utf-8 -*-
"""
generate_all.py
Upgrades Ikshvaku Curiosity Machine according to all 50 senior engineer/designer requirements.
Produces curiosity-machine.html, curiosity-page.html, blogger-template.xml, and curiosity-theme.xml.
"""

import sys
import re
import json
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

# Read base64 logo from existing blogger-template.xml
with open('blogger-template.xml', 'r', encoding='utf-8') as f:
    b_text = f.read()

logo_match = re.search(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', b_text)
base64_logo = logo_match.group(0) if logo_match else 'https://rishendra1.github.io/ikshvaku-curiosity/assets/IVA.jpeg'

# 1. READ CSS from build_masterpiece.py
with open('build_masterpiece.py', 'r', encoding='utf-8') as f:
    bm_text = f.read()

css_start = bm_text.find('/* ══════════════════════════════════════════════════════════════════')
css_end = bm_text.find('"""', css_start)
master_css = bm_text[css_start:css_end].strip()

# 2. HTML STRUCTURE
master_html = f"""<div id="iva-curiosity-machine">

  <!-- Ambient Cosmic Particle Canvas -->
  <canvas id="ivaCosmicCanvas"></canvas>

  <!-- ── 1. TOP INSTITUTIONAL BAR ── -->
  <header class="iva-top-banner" role="banner">
    <div class="iva-top-container">
      <div class="iva-top-left">
        <img src="{base64_logo}" alt="Ikshvaku Vidya Academy Official Seal" class="iva-top-logo" />
        <div class="iva-top-titles">
          <div class="iva-top-name">IKSHVAKU VIDYA ACADEMY</div>
          <div class="iva-top-tagline">A Place for Curious Minds • Education Beyond Commerce</div>
        </div>
      </div>
      <div class="iva-top-badge">✦ Official Curiosity Platform</div>
    </div>
  </header>

  <!-- ── 2. STICKY NAVIGATION HEADER ── -->
  <header class="iva-header" role="navigation" aria-label="Curiosity Machine Navigation">
    <div class="iva-header-inner">
      <button type="button" class="iva-brand" id="ivaBrandHomeBtn" title="Curiosity Machine Home">
        <div>
          <div class="iva-brand-title">CURIOSITY MACHINE</div>
          <div class="iva-brand-sub">Don't Just Learn. Get Curious.</div>
        </div>
      </button>

      <nav class="iva-nav-actions" aria-label="Primary Actions">
        <button type="button" class="iva-nav-btn active" id="ivaNavHomeBtn">🏠 Home</button>
        <button type="button" class="iva-nav-btn" id="ivaNavSurpriseBtn">🎲 Surprise Me</button>
        <button type="button" class="iva-nav-btn" id="ivaNavBoredBtn">⚡ I'm Bored</button>
        <button type="button" class="iva-nav-btn" id="ivaNavStrangeBtn">💡 Strange Facts</button>
        <button type="button" class="iva-nav-btn" id="ivaNavSavedBtn">🔖 Saved <span id="ivaSavedBadge">(0)</span></button>
        <button type="button" class="iva-nav-btn" id="ivaNavJourneyBtn">🗺️ Journey</button>
        <button type="button" class="iva-nav-btn" id="ivaSoundToggleBtn" title="Toggle Celestial Sound">🔊 Sound</button>
        <button type="button" class="iva-nav-btn" id="ivaNavAboutBtn" title="About Ikshvaku Academy">ℹ️ About</button>
      </nav>
    </div>
  </header>

  <!-- ── 3. INTELLECTUAL PROGRESS & MILESTONES BAR ── -->
  <div class="iva-subbar" role="region" aria-label="Learning Metrics">
    <div class="iva-subbar-container">
      <div class="iva-subbar-left">
        <span>Intellectual Pace:</span>
        <strong id="ivaLearnerMilestoneTitle" style="color: var(--iva-gold-light);">First Spark</strong>
        <div class="iva-progress-bar-wrap" title="Milestone Progress">
          <div class="iva-progress-bar-fill" id="ivaProgressBarFill"></div>
        </div>
        <span id="ivaLearnerExploredLabel">0 / 5 Inquiries</span>
      </div>

      <div class="iva-subbar-right">
        <span class="iva-subbar-pill" id="ivaStreakPill" title="Daily Inquiries Streak">🔥 Streak: <strong id="ivaStreakCount">1 Day</strong></span>
        <span class="iva-subbar-pill" id="ivaLibraryPill" title="Curiosity Paths Supported">📚 Library: <strong>500,000+ Paths</strong></span>
      </div>
    </div>
  </div>

  <!-- ── 4. MAIN DYNAMIC CONTENT CONTAINER ── -->
  <main class="iva-content" id="ivaMainContent">

    <!-- ══════════════════════════════════════════════════════════
         VIEW 1: CALM, FOCUSED HOME VIEW
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaHomeView" class="iva-view">

      <!-- Hero Section -->
      <section class="iva-hero" aria-labelledby="ivaHeroHeading">
        <span class="iva-hero-eyebrow">IKSHVAKU VIDYA ACADEMY</span>
        <h1 class="iva-hero-title" id="ivaHeroHeading">CURIOSITY MACHINE</h1>
        <div class="iva-hero-tagline">Don't Just Learn. Get Curious.</div>
        
        <p class="iva-hero-lead">
          There are thousands of things you see every day but rarely stop to question.<br/>
          Pick one. Make a guess. Then discover what is really happening.
        </p>
        <div class="iva-hero-subline">No marks. No exams. No leaderboard. Just curiosity.</div>

        <div class="iva-hero-cta-group">
          <button type="button" class="iva-btn iva-btn-primary iva-btn-large" id="ivaHeroCuriousBtn">
            ✦ MAKE ME CURIOUS
          </button>
          <button type="button" class="iva-btn iva-btn-secondary" id="ivaHeroSurpriseBtn">
            🎲 Surprise Me
          </button>
          <button type="button" class="iva-btn iva-btn-secondary" id="ivaHeroBoredBtn">
            ⚡ I'm Bored
          </button>
          <button type="button" class="iva-btn iva-btn-secondary" id="ivaHeroRandomWalkBtn">
            🌐 Random Walk
          </button>
        </div>
      </section>

      <!-- Today's Deterministic Curiosity -->
      <section aria-labelledby="ivaDailyTitle">
        <div class="iva-daily-card" id="ivaDailyCard">
          <div class="iva-daily-badge" id="ivaDailyDateBadge">TODAY'S INQUIRY • DAILY DISCOVERY</div>
          <h2 class="iva-daily-title" id="ivaDailyTitle">Why doesn't the Moon fall into Earth?</h2>
          <p class="iva-daily-premise" id="ivaDailyPremise">
            You already know Earth pulls the Moon with relentless gravitational force. So here's the strange part... Why doesn't the Moon simply fall straight down?
          </p>
          <div class="iva-daily-footer">
            <div class="iva-daily-meta">
              <span>⏱️ 3 min thought experiment</span> • <span>Astrophysics &amp; Orbital Mechanics</span>
            </div>
            <button type="button" class="iva-btn iva-btn-primary iva-btn-small" id="ivaDailyExploreBtn">
              Explore Today's Question →
            </button>
          </div>
        </div>
      </section>

      <!-- Forgiving Search Engine -->
      <section class="iva-search-section" aria-label="Curiosity Search">
        <div class="iva-search-box">
          <span class="iva-search-icon">🔍</span>
          <input type="text" class="iva-search-input" id="ivaSearchInput" placeholder="Search any question, curiosity, or phenomenon (e.g. moon, ice, sound, time, brain)..." aria-label="Search curiosity questions" />
        </div>
        <div class="iva-search-chips">
          <span style="font-size: 0.78rem; color: var(--iva-text-muted);">Common sparks:</span>
          <button type="button" class="iva-chip" data-search="gravity">Gravity</button>
          <button type="button" class="iva-chip" data-search="quantum">Quantum</button>
          <button type="button" class="iva-chip" data-search="time">Time Dilation</button>
          <button type="button" class="iva-chip" data-search="ice">Why Ice Floats</button>
          <button type="button" class="iva-chip" data-search="sound">Noise Cancelling</button>
          <button type="button" class="iva-chip" data-search="qr">QR Codes</button>
          <button type="button" class="iva-chip" data-search="sky">Blue Sky</button>
        </div>
      </section>

      <!-- Search Results Container (Shown on search) -->
      <section id="ivaSearchResultsWrap" style="display: none; margin-bottom: 40px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <h3 style="color: #fff; font-size: 1.2rem;" id="ivaSearchResultsTitle">Search Results</h3>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaClearSearchBtn">✕ Clear Search</button>
        </div>
        <div class="iva-saved-grid" id="ivaSearchResultsGrid"></div>
      </section>

      <!-- 8 Disciplines of First-Principles Inquiry -->
      <section aria-labelledby="ivaDisciplinesTitle">
        <h2 class="iva-section-title" id="ivaDisciplinesTitle">Explore by Intellectual Discipline</h2>
        <p class="iva-section-subtitle">Deep inquiry paths connecting science, nature, mind, and computational architecture.</p>
        
        <div class="iva-categories-grid" id="ivaCategoriesGrid">
          <!-- Dynamically populated from CATEGORIES -->
        </div>
      </section>

      <!-- Signature Studio: "Spark an Original Question" (Section 17) -->
      <section class="iva-spark-studio" aria-labelledby="ivaSparkTitle">
        <div class="iva-spark-header">
          <span class="iva-spark-tag">✦ Signature Studio</span>
          <h2 class="iva-spark-title" id="ivaSparkTitle">Spark an Original Question</h2>
          <p class="iva-spark-quote">"Good learners solve questions. Curious thinkers create them."</p>
        </div>

        <div style="text-align: center; margin-bottom: 12px; font-size: 0.95rem; color: var(--iva-text-secondary);">
          Here are three unrelated concepts. Can you forge an original question that connects them?
        </div>

        <div class="iva-spark-concepts-wrap">
          <span class="iva-spark-pill" id="ivaSparkConcept1">BLACK HOLES</span>
          <span class="iva-spark-plus">+</span>
          <span class="iva-spark-pill" id="ivaSparkConcept2">PLANTS</span>
          <span class="iva-spark-plus">+</span>
          <span class="iva-spark-pill" id="ivaSparkConcept3">ACOUSTIC WAVES</span>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaRerollSparksBtn" style="margin-left: 8px;">
            🎲 Reroll Concepts
          </button>
        </div>

        <div class="iva-spark-input-wrap">
          <textarea class="iva-spark-textarea" id="ivaSparkTextarea" placeholder="Write your original question here... (e.g., How would plant photosynthesis adapt to acoustic shockwaves near a black hole accretion disc?)"></textarea>
          <div style="display: flex; gap: 10px; justify-content: flex-end; flex-wrap: wrap;">
            <button type="button" class="iva-btn iva-btn-primary" id="ivaAnalyzeSparkBtn">
              💡 Analyze My Question
            </button>
          </div>
          <div class="iva-spark-response-box" id="ivaSparkResponseBox">
            <div style="font-weight: 700; color: var(--iva-gold-light); margin-bottom: 6px;">Fascinating Question.</div>
            <div id="ivaSparkAnalysisContent"></div>
            <div style="margin-top: 10px; display: flex; gap: 8px; justify-content: flex-end;">
              <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaSaveSparkToJournalBtn">🔖 Save to My Journal</button>
            </div>
          </div>
        </div>
      </section>

      <!-- Why We Built This: Institutional Story (Section 29) -->
      <section class="iva-story-section" aria-labelledby="ivaStoryTitle">
        <span class="iva-story-eyebrow">IKSHVAKU VIDYA ACADEMY</span>
        <h2 class="iva-story-title" id="ivaStoryTitle">Why We Built The Curiosity Machine</h2>
        <p class="iva-story-text">
          At Ikshvaku Vidya Academy, we believe education isn't only about remembering the right answer.<br/>
          Sometimes the most valuable moment is when a student stops and asks: <em>"Wait... but why?"</em><br/>
          The Curiosity Machine is a dedicated sanctuary for those questions.
        </p>
        <div class="iva-story-seal">IKSHVAKU VIDYA ACADEMY • EDUCATION BEYOND COMMERCE</div>
      </section>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 2: QUESTION EXPLORATION EXPERIENCE (Sections 9, 10, 13, 14, 15, 16, 22, 43)
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaCuriosityView" class="iva-view iva-hidden">

      <div style="margin-bottom: 20px;">
        <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaBackToHomeBtn">
          ← Back to All Inquiries
        </button>
      </div>

      <article class="iva-detail-card">
        
        <header class="iva-detail-header">
          <div class="iva-detail-meta">
            <span class="iva-badge iva-badge-space" id="ivaDetailBadge">ASTROPHYSICS</span>
            <span style="font-size: 0.84rem; color: var(--iva-text-muted);" id="ivaDetailInquiryNumber">Inquiry #001</span>
            <span style="font-size: 0.84rem; color: var(--iva-text-muted);" id="ivaDetailReadTime">⏱️ 3 min read</span>
          </div>
          <h1 class="iva-detail-title" id="ivaDetailTitle">Why doesn't the Moon fall into Earth?</h1>
        </header>

        <!-- The Setup / The Strange Part -->
        <div class="iva-detail-mystery" id="ivaDetailMystery">
          You already know Earth pulls the Moon with relentless gravitational force. So here's the strange part... Why doesn't the Moon simply plunge straight down?
        </div>

        <!-- Think & Guess Active Learning Gate (Section 9) -->
        <div class="iva-think-gate" id="ivaThinkGate">
          <div class="iva-think-title">💡 Before We Explain It... What Do You Think?</div>
          <div class="iva-think-subtitle">Take a guess. There are no wrong thoughts here—curiosity begins with a hypothesis.</div>
          
          <div class="iva-think-row">
            <input type="text" class="iva-think-input" id="ivaThinkInput" placeholder="I think it might be because..." aria-label="Your thoughts on this inquiry" />
            <button type="button" class="iva-btn iva-btn-primary" id="ivaLockIdeaBtn">
              🔒 LOCK MY IDEA
            </button>
          </div>
          <div class="iva-think-feedback" id="ivaThinkFeedback">
            Interesting thought. Let's see what is actually happening.
          </div>
        </div>

        <!-- 3-Level Progressive Disclosure Explanation (Section 10) -->
        <div id="ivaExplanationContainer">
          
          <div class="iva-tabs-wrap" role="tablist">
            <button type="button" class="iva-tab-btn active" id="ivaTabLevel1" role="tab" aria-selected="true">
              Level 1: The Simple Idea
            </button>
            <button type="button" class="iva-tab-btn" id="ivaTabLevel2" role="tab" aria-selected="false">
              Level 2: What's Really Happening
            </button>
            <button type="button" class="iva-tab-btn" id="ivaTabLevel3" role="tab" aria-selected="false">
              Level 3: First Principles
            </button>
          </div>

          <div class="iva-explanation-box">
            <div id="ivaExpContentLevel1">
              <!-- Level 1 content -->
            </div>
            <div id="ivaExpContentLevel2" style="display: none;">
              <!-- Level 2 content -->
            </div>
            <div id="ivaExpContentLevel3" style="display: none;">
              <!-- Level 3 content -->
            </div>
          </div>

        </div>

        <!-- Live Interactive Simulation (Section 22) -->
        <div class="iva-sim-box" id="ivaSimBox">
          <div class="iva-sim-header">
            <span class="iva-sim-title" id="ivaSimTitle">🔬 Interactive Dynamic Simulator</span>
            <div class="iva-sim-controls">
              <span style="font-size: 0.8rem; color: var(--iva-text-secondary);" id="ivaSimModeLabel">Gravitational Orbit</span>
              <input type="range" min="1" max="100" value="50" id="ivaSimSlider" style="width: 100px;" title="Velocity / Phase Slider" />
              <span style="font-size: 0.8rem; color: var(--iva-cyan);" id="ivaSimSliderVal">50%</span>
            </div>
          </div>

          <canvas id="ivaSimCanvas" width="600" height="220"></canvas>

          <div class="iva-sim-qa-grid">
            <div class="iva-sim-qa-item">
              <div class="iva-sim-qa-label">What changed?</div>
              <div class="iva-sim-qa-text" id="ivaSimWhatChanged">The forward tangential speed balanced Earth's constant inward gravitational curvature.</div>
            </div>
            <div class="iva-sim-qa-item">
              <div class="iva-sim-qa-label">Why did it change?</div>
              <div class="iva-sim-qa-text" id="ivaSimWhyChanged">Perpendicular velocity changes directional momentum without expending energy.</div>
            </div>
            <div class="iva-sim-qa-item">
              <div class="iva-sim-qa-label">What would happen next?</div>
              <div class="iva-sim-qa-text" id="ivaSimNext">If velocity drops, orbit decays inward; if velocity increases, it escapes into hyperbolic trajectory.</div>
            </div>
          </div>
        </div>

        <!-- "Why Should I Care?" Real-World Connection (Section 14) -->
        <div class="iva-care-box">
          <div class="iva-care-title">
            <span>🌍 Why Should I Care?</span>
          </div>
          <div class="iva-care-text" id="ivaCareText">
            Every GPS satellite orbiting above you, weather monitoring network, and telecommunications relay uses this exact balance of free fall and forward speed.
          </div>
        </div>

        <!-- "What If?" Thought Experiment (Section 15) -->
        <div class="iva-whatif-box">
          <div class="iva-whatif-title">
            <span>🔮 What If?</span>
          </div>
          <div class="iva-whatif-scenario" id="ivaWhatIfScenario">
            What if the Moon suddenly lost all of its forward tangential speed?
          </div>
          <div style="margin-bottom: 10px;">
            <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaWhatIfPredictBtn">
              Reveal What Would Happen →
            </button>
          </div>
          <div class="iva-whatif-reveal-box" id="ivaWhatIfRevealBox" style="display: none;">
            <div id="ivaWhatIfConsequence">
              Without forward momentum, the Moon would plunge radially straight into Earth in approximately 4.8 days under relentless gravitational acceleration.
            </div>
          </div>
        </div>

        <!-- "Connect The Dots" Concept Trail (Section 16) -->
        <div class="iva-trail-section">
          <div class="iva-trail-title">🔗 Connect The Dots</div>
          <div class="iva-trail-chain" id="ivaTrailChain">
            <!-- Dynamically populated concept nodes -->
          </div>
        </div>

        <!-- Action Toolbar -->
        <div style="display: flex; gap: 10px; flex-wrap: wrap; border-top: 1px solid var(--iva-border); padding-top: 20px;">
          <button type="button" class="iva-btn iva-btn-primary iva-btn-small" id="ivaBookmarkBtn">🔖 Save Inquiry</button>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaExportCardBtn">🎨 Download Insight Card (PNG)</button>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaShareBtn">📤 Share Link</button>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaZenModeBtn">🌙 Focus Mode</button>
        </div>

        <!-- Final Discovery Experience: Curiosity Complete Signature (Section 43) -->
        <div class="iva-complete-card">
          <span class="iva-complete-badge">✦ CURIOSITY COMPLETE</span>
          <div class="iva-complete-quote">
            "You came looking for an answer. You found one.<br/>And now you have another question."
          </div>
          <button type="button" class="iva-btn iva-btn-primary iva-btn-large" id="ivaCuriousAgainBtn">
            ✦ MAKE ME CURIOUS AGAIN
          </button>
        </div>

      </article>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 3: "I'M BORED" (3 MODES: OBSERVE, THINK, DO) (Section 18)
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaBoredView" class="iva-view iva-hidden">
      
      <div style="margin-bottom: 20px;">
        <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaBoredBackHomeBtn">
          ← Back to Home
        </button>
      </div>

      <div class="iva-bored-card">
        <h2 style="font-family: var(--iva-font-serif); font-size: 2rem; color: #fff; margin-bottom: 10px;">
          ⚡ 60-Second Boredom Antidote
        </h2>
        <p style="color: var(--iva-text-secondary); max-width: 580px; margin: 0 auto 24px;">
          Boredom is your prefrontal cortex asking for high-quality stimulation.<br/>
          Choose your mode and try this micro-experiment right now:
        </p>

        <!-- 3 Modes Tabs -->
        <div class="iva-bored-modes">
          <button type="button" class="iva-bored-mode-btn active" data-mode="observe" id="ivaBoredModeObserve">👁️ OBSERVE</button>
          <button type="button" class="iva-bored-mode-btn" data-mode="think" id="ivaBoredModeThink">🧠 THINK</button>
          <button type="button" class="iva-bored-mode-btn" data-mode="do" id="ivaBoredModeDo">✋ DO</button>
        </div>

        <div class="iva-bored-challenge-text" id="ivaBoredChallengeText">
          Look at any shadow cast in the room right now. Notice the blurry penumbra around its edges. Why is the edge fuzzy instead of razor-sharp? (Hint: The light bulb has physical width; it's an extended area, not a mathematical point source.)
        </div>

        <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
          <button type="button" class="iva-btn iva-btn-primary" id="ivaNextBoredBtn">⚡ Another Challenge</button>
          <button type="button" class="iva-btn iva-btn-secondary" id="ivaBoredExploreBtn">✦ Turn Into Curiosity Inquiry</button>
        </div>
      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 4: STRANGE FACTS (Section 19)
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaStrangeView" class="iva-view iva-hidden">
      
      <div style="margin-bottom: 20px;">
        <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaStrangeBackHomeBtn">
          ← Back to Home
        </button>
      </div>

      <div class="iva-strange-card">
        <div style="font-size: 0.78rem; font-weight: 700; color: var(--iva-gold); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px;">
          ✦ Authentic Reality Archive
        </div>
        <h2 style="font-family: var(--iva-font-serif); font-size: 2rem; color: #fff; margin-bottom: 8px;">
          Strange Truths of the Universe
        </h2>
        <p style="color: var(--iva-text-secondary); margin-bottom: 24px;">
          The cosmos is under no obligation to conform to everyday common sense. Verified counter-intuitive physical truths:
        </p>

        <div class="iva-strange-fact-text" id="ivaStrangeFactText">
          If you removed all the empty space from the atoms of all 8 billion human beings on Earth, the remaining solid mass would fit into the volume of a single sugar cube.
        </div>

        <div style="margin-bottom: 18px;">
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaStrangeWhyBtn">
            Wait... Why? (Reveal Mechanism) ↓
          </button>
        </div>

        <div class="iva-strange-why-box" id="ivaStrangeWhyBox" style="display: none;">
          <div style="font-weight: 700; color: var(--iva-cyan); margin-bottom: 6px;">The Scientific Mechanism:</div>
          <div id="ivaStrangeWhyContent">
            Atoms are 99.9999999% empty space. The electron cloud surrounds a nucleus that is 100,000 times smaller. What prevents you from falling through a floor isn't solid matter, but the electrostatic repulsion of electron clouds governed by the Pauli Exclusion Principle.
          </div>
        </div>

        <div style="display: flex; gap: 12px; justify-content: space-between; align-items: center; flex-wrap: wrap;">
          <button type="button" class="iva-btn iva-btn-primary" id="ivaNextStrangeBtn">💡 Next Strange Truth</button>
          <button type="button" class="iva-btn iva-btn-secondary" id="ivaStrangeExploreRelatedBtn">Explore Related Inquiry →</button>
        </div>
      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 5: SAVED DISCOVERIES (Section 24)
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaSavedView" class="iva-view iva-hidden">
      
      <div class="iva-saved-header">
        <div>
          <h2 style="font-family: var(--iva-font-serif); font-size: 2rem; color: #fff;">🔖 Your Saved Inquiries</h2>
          <div style="font-size: 0.9rem; color: var(--iva-text-secondary);">Inquiries and reflections preserved in your browser's private memory.</div>
        </div>
        <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaSavedBackHomeBtn">
          ← Back to Home
        </button>
      </div>

      <div class="iva-search-chips" style="margin-bottom: 20px;" id="ivaSavedCategoryFilterChips">
        <button type="button" class="iva-chip" data-filter="all">All Saved</button>
        <button type="button" class="iva-chip" data-filter="space">Space</button>
        <button type="button" class="iva-chip" data-filter="science">Physics</button>
        <button type="button" class="iva-chip" data-filter="math">Math</button>
        <button type="button" class="iva-chip" data-filter="nature">Nature</button>
      </div>

      <div id="ivaSavedEmptyState" style="text-align: center; padding: 48px 16px; color: var(--iva-text-secondary);">
        <div style="font-size: 2.5rem; margin-bottom: 12px;">🔖</div>
        <h3 style="color: #fff; margin-bottom: 6px;">No Saved Discoveries Yet</h3>
        <p style="max-width: 480px; margin: 0 auto 20px;">
          When an inquiry strikes your curiosity, tap <strong>"Save Inquiry"</strong> to bookmark it here along with your personal reflections.
        </p>
        <button type="button" class="iva-btn iva-btn-primary" id="ivaSavedExploreNowBtn">Start Exploring →</button>
      </div>

      <div class="iva-saved-grid" id="ivaSavedGrid" style="display: none;"></div>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 6: MY CURIOSITY JOURNEY (Section 23, 42)
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaJourneyView" class="iva-view iva-hidden">
      
      <div style="margin-bottom: 20px;">
        <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaJourneyBackHomeBtn">
          ← Back to Home
        </button>
      </div>

      <div class="iva-journey-hero">
        <span class="iva-hero-eyebrow">PERSONAL INTELLECTUAL RECORD</span>
        <h2 style="font-family: var(--iva-font-serif); font-size: 2.2rem; color: #fff; margin-bottom: 8px;">
          My Curiosity Journey
        </h2>
        <p style="color: var(--iva-text-secondary); line-height: 1.6;">
          Curiosity is not a competition. There are no test scores, no leaderboards, and no points. This is your personal milestone log of questions pondered and perspectives expanded.
        </p>
      </div>

      <!-- Stats Summary -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin-bottom: 36px;">
        <div style="background: var(--iva-surface); border: 1px solid var(--iva-border); border-radius: var(--iva-radius-md); padding: 20px; text-align: center;">
          <div style="font-size: 2.2rem; font-weight: 800; color: var(--iva-cyan);" id="ivaJourneyExploredCount">0</div>
          <div style="font-size: 0.84rem; color: var(--iva-text-secondary);">Inquiries Explored</div>
        </div>
        <div style="background: var(--iva-surface); border: 1px solid var(--iva-border); border-radius: var(--iva-radius-md); padding: 20px; text-align: center;">
          <div style="font-size: 2.2rem; font-weight: 800; color: var(--iva-gold-light);" id="ivaJourneyReflectionsCount">0</div>
          <div style="font-size: 0.84rem; color: var(--iva-text-secondary);">Reflections Penned</div>
        </div>
        <div style="background: var(--iva-surface); border: 1px solid var(--iva-border); border-radius: var(--iva-radius-md); padding: 20px; text-align: center;">
          <div style="font-size: 2.2rem; font-weight: 800; color: var(--iva-emerald);" id="ivaJourneySavedCount">0</div>
          <div style="font-size: 0.84rem; color: var(--iva-text-secondary);">Saved Inquiries</div>
        </div>
        <div style="background: var(--iva-surface); border: 1px solid var(--iva-border); border-radius: var(--iva-radius-md); padding: 20px; text-align: center;">
          <div style="font-size: 2.2rem; font-weight: 800; color: #ffb703;" id="ivaJourneyStreakDisplay">1 Day</div>
          <div style="font-size: 0.84rem; color: var(--iva-text-secondary);">Curiosity Streak</div>
        </div>
      </div>

      <!-- Milestones Grid -->
      <h3 style="font-family: var(--iva-font-serif); font-size: 1.4rem; color: #fff; margin-bottom: 16px;">
        Intellectual Milestones
      </h3>
      <div class="iva-milestones-grid" id="ivaMilestonesGrid">
        <!-- Dynamically rendered milestones -->
      </div>

    </div>

  </main>

  <!-- ── 5. SHAREABLE INSIGHT CARD EXPORT MODAL ── -->
  <div class="iva-modal-overlay iva-hidden" id="ivaCardModalOverlay">
    <div class="iva-modal-box" style="text-align: center;">
      <button type="button" class="iva-modal-close" id="ivaCardModalCloseBtn" aria-label="Close Modal">✕</button>
      <h3 style="font-family: var(--iva-font-serif); font-size: 1.4rem; color: #fff; margin-bottom: 8px;">
        🎨 Your Curiosity Insight Card
      </h3>
      <p style="font-size: 0.88rem; color: var(--iva-text-secondary); margin-bottom: 18px;">
        Ready to download and share with friends, classrooms, or on social media.
      </p>
      <canvas id="ivaExportCardCanvas" width="640" height="420" style="max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 20px;"></canvas>
      <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
        <button type="button" class="iva-btn iva-btn-primary" id="ivaDownloadCardPngBtn">📥 Download PNG Card</button>
        <button type="button" class="iva-btn iva-btn-secondary" id="ivaCardDoneBtn">Done</button>
      </div>
    </div>
  </div>

  <!-- ── 6. ABOUT IKSHVAKU ACADEMY MODAL ── -->
  <div class="iva-modal-overlay iva-hidden" id="ivaAboutModalOverlay">
    <div class="iva-modal-box">
      <button type="button" class="iva-modal-close" id="ivaAboutCloseBtn" aria-label="Close Modal">✕</button>
      <div style="text-align: center; margin-bottom: 20px;">
        <img src="{base64_logo}" alt="Ikshvaku Vidya Academy Seal" style="width: 54px; height: 54px; border-radius: 50%; border: 1.5px solid var(--iva-gold); margin-bottom: 10px;" />
        <h3 style="font-family: var(--iva-font-serif); font-size: 1.5rem; color: #fff;">IKSHVAKU VIDYA ACADEMY</h3>
        <div style="font-size: 0.84rem; color: var(--iva-gold);">A Place for Curious Minds • Education Beyond Commerce</div>
      </div>
      <p style="font-size: 0.95rem; color: var(--iva-text-secondary); line-height: 1.7; margin-bottom: 14px;">
        The <strong>Ikshvaku Curiosity Machine</strong> is an independent educational initiative dedicated to reviving first-principles thinking, childlike wonder, and deep scientific inquiry.
      </p>
      <p style="font-size: 0.95rem; color: var(--iva-text-secondary); line-height: 1.7; margin-bottom: 18px;">
        We believe learning should not be reduced to test memorization, competitive stress, or commercial transactions. True intellectual freedom begins when a student stops, observes the universe, makes an honest hypothesis, and discovers the fundamental mechanism.
      </p>
      <div style="text-align: center;">
        <button type="button" class="iva-btn iva-btn-primary iva-btn-small" id="ivaAboutGotItBtn">Got It</button>
      </div>
    </div>
  </div>

  <!-- ── 7. TOAST NOTIFICATION ── -->
  <div id="ivaToast" class="iva-hidden">
    <span id="ivaToastIcon" style="font-size: 1.2rem;">✨</span>
    <span id="ivaToastMessage">Curiosity awakened.</span>
  </div>

</div>
"""

# 3. JAVASCRIPT MASTER IMPLEMENTATION
master_js = r"""(function() {
  'use strict';

  // ════════════════════════════════════════════════════════════════
  // 1. DATA & CURRICULUM
  // ════════════════════════════════════════════════════════════════

  var CATEGORIES = [
    { key: "space", label: "Astrophysics & Cosmos", icon: "🌌", badge: "iva-badge-space", desc: "Black holes, orbital mechanics, planetary atmospheres, cosmic radiation." },
    { key: "science", label: "Quantum & Particles", icon: "⚛️", badge: "iva-badge-physics", desc: "Wave-particle duality, atomic lattice, relativity, entropy, thermodynamics." },
    { key: "math", label: "Pure Mathematics & Logic", icon: "📐", badge: "iva-badge-math", desc: "Topology, primes, infinity, game theory, cryptography, probability." },
    { key: "nature", label: "Evolutionary Biology & Life", icon: "🌿", badge: "iva-badge-biology", desc: "DNA code, cellular respiration, emergent ecosystems, natural selection." },
    { key: "tech", label: "Cognitive Tech & Computing", icon: "💻", badge: "iva-badge-tech", desc: "Information theory, neural networks, algorithms, silicon architectures." },
    { key: "thinking", label: "Philosophy of Mind", icon: "🧠", badge: "iva-badge-math", desc: "Consciousness, predictive perception, paradoxes, epistemological limits." },
    { key: "how", label: "Everyday Physics & Optics", icon: "🔬", badge: "iva-badge-physics", desc: "Acoustic cancellation, light scattering, electromagnetism in daily tools." },
    { key: "behavior", label: "Systems & Civilizations", icon: "🏛️", badge: "iva-badge-biology", desc: "Complex adaptive systems, institutional evolution, game theory of societies." }
  ];

  // Flagship Human-Authored Master Inquiries
  var FLAGSHIP_INQUIRIES = [
    {
      id: "flagship-moon",
      category: "space",
      categoryLabel: "Astrophysics & Cosmos",
      badgeClass: "iva-badge-space",
      readTime: "3 min thought experiment",
      question: "Why doesn't the Moon fall into Earth?",
      mystery: "You already know Earth pulls the Moon with relentless gravitational force. So why doesn't it plunge straight down like an apple dropped from a tree?",
      prompt: "What keeps an object perpetually falling through space without ever hitting the ground?",
      simple: "Imagine throwing a rock forward. Throw it faster, and it curves further. Throw it at 17,500 miles per hour, and Earth's spherical surface curves away beneath it at the exact same rate the rock falls. The Moon is literally in perpetual free-fall around Earth, constantly falling and constantly missing.",
      mechanism: "The Moon possesses high tangential velocity (1.022 km/s). Earth's gravitational acceleration (GM/r²) acts strictly perpendicular to this velocity, continuously altering its velocity vector direction without diminishing its magnitude. This centrifugal inertial balance maintains a closed elliptical geodesic orbit.",
      firstPrinciples: "Under General Relativity, mass does not exert a Newtonian mechanical 'pull'. Instead, Earth's mass curves surrounding four-dimensional spacetime. The Moon is simply traveling in a straight inertial trajectory (geodesic) through curved spacetime with zero proper acceleration.",
      simMode: "orbit",
      simWhatChanged: "The forward tangential velocity balances the inward gravitational acceleration.",
      simWhyChanged: "A perpendicular force vector curves the direction of linear momentum without expending kinetic energy.",
      simNext: "If forward speed slows down, the orbit decays inward; if it accelerates, it breaks free into a hyperbolic escape trajectory.",
      whyCare: "Every satellite providing your smartphone's GPS navigation, live weather Doppler radar, and international communications balances on this exact mathematical equilibrium.",
      whatIfScenario: "What if the Moon suddenly lost all of its forward tangential speed?",
      whatIfConsequence: "Without forward orbital momentum, the Moon would plunge radially straight into Earth in approximately 4.8 days under relentless gravitational acceleration.",
      trail: ["Gravitational Acceleration", "Tangential Velocity", "Centripetal Geodesics", "Artificial Satellites", "GPS Navigation"]
    },
    {
      id: "flagship-ice",
      category: "nature",
      categoryLabel: "Everyday Physics & Optics",
      badgeClass: "iva-badge-physics",
      readTime: "3 min thought experiment",
      question: "Why does ice float?",
      mystery: "Almost every substance in the known universe contracts and becomes denser when frozen solid. Liquid wax sinks in solid wax; molten iron sinks in solid iron. Why does water do the exact opposite?",
      prompt: "What happens to water molecules when they cool down and lock together below 4°C?",
      simple: "Liquid water molecules are jumbled together like marbles in a bag. But when water freezes, the molecules are forced into an open, hexagonal crystal lattice that leaves empty microscopic pockets of space. Ice has less mass per volume than liquid water, so it floats.",
      mechanism: "Hydrogen bonding between electronegative oxygen atoms and positive hydrogen atoms becomes dominant below 4°C. The open tetrahedral crystalline structure expands the volume by approximately 9%, dropping density from 1.000 g/cm³ to 0.917 g/cm³.",
      firstPrinciples: "The permanent dipole moment of the polar O-H bond (1.85 D) and its 104.5° sp³ hybridization angle dictate tetrahedral hydrogen-bonding coordination. Quantum electrostatic repulsion between non-bonding electron pairs prevents denser packing at low thermal energy.",
      simMode: "wave",
      simWhatChanged: "The molecular spacing expanded into an open tetrahedral lattice.",
      simWhyChanged: "Hydrogen bonds lock into rigid geometric angles as thermal kinetic vibrations diminish.",
      simNext: "Liquid water below the ice sheet remains insulated at 4°C, preserving aquatic life through sub-zero winters.",
      whyCare: "If ice sank, every lake, river, and polar sea would freeze solid from the seabed up, turning Earth into a permanently frozen wasteland devoid of complex life.",
      whatIfScenario: "What if ice were denser than liquid water like normal liquids?",
      whatIfConsequence: "Polar ice caps would sink into the ocean depths where sunlight could never reach them, triggering runaway global glaciation and extinguishing marine ecosystems.",
      trail: ["Hydrogen Bonds", "Tetrahedral Lattice", "Density Inversion", "Aquatic Insulation", "Global Climate Stability"]
    },
    {
      id: "flagship-earth-spin",
      category: "science",
      categoryLabel: "Quantum & Particles",
      badgeClass: "iva-badge-physics",
      readTime: "4 min thought experiment",
      question: "Why don't we feel Earth spinning?",
      mystery: "At this exact moment, Earth's equator is hurtling through space at over 1,670 kilometers per hour. Why do you feel completely, perfectly still?",
      prompt: "When you are in an airplane cruising at 900 km/h with the window shades down, why can you pour a glass of water without a drop spilling?",
      simple: "Human sensory biology cannot feel constant speed; our inner ears and muscles can only detect acceleration (changes in speed or direction). Everything around you—the air you breathe, the floor, the clouds—is moving together at the exact same constant velocity.",
      mechanism: "Earth's rotation constitutes an approximately uniform inertial reference frame. The outward centrifugal acceleration at the equator (0.034 m/s²) is completely drowned out by Earth's downward gravitational acceleration (9.81 m/s²).",
      firstPrinciples: "Galilean invariance and Einstein's Principle of Relativity dictate that the fundamental laws of physics are identical in all non-accelerating frames. Without an external reference point, no mechanical or electromagnetic experiment inside a closed room can detect constant velocity.",
      simMode: "orbit",
      simWhatChanged: "The observer, atmosphere, and surface share identical uniform velocity.",
      simWhyChanged: "Inertia conserves momentum; acceleration is zero relative to the local reference frame.",
      simNext: "Only planetary-scale phenomena with non-inertial effects (like the Coriolis force steering hurricane cyclones) betray the spin.",
      whyCare: "This fundamental principle allows passenger airplanes to fly smoothly, satellites to remain stationary over communication zones, and humans to live comfortably on a rotating sphere.",
      whatIfScenario: "What if Earth suddenly stopped spinning in a single second?",
      whatIfConsequence: "Due to inertia, every object, building, ocean, and atmosphere not anchored to Earth's core would continue traveling eastward at up to 1,000 mph, generating cataclysmic supersonic winds and global tsunamis.",
      trail: ["Inertial Reference Frames", "Galilean Invariance", "Newton's First Law", "Coriolis Acceleration", "Atmospheric Jet Streams"]
    },
    {
      id: "flagship-qr-code",
      category: "tech",
      categoryLabel: "Cognitive Tech & Computing",
      badgeClass: "iva-badge-tech",
      readTime: "3 min thought experiment",
      question: "How does a QR code work?",
      mystery: "You can point your camera at a stained, crumpled, or partially torn QR code on a coffee cup, and your phone still decodes the exact website address in milliseconds. How?",
      prompt: "How can a 2D optical grid survive having up to 30% of its data physically destroyed?",
      simple: "The three big corner squares tell your camera the code's angle and orientation. Inside, black and white dots represent binary 1s and 0s. Crucially, the code weaves in mathematical backup equations so your phone can solve for missing dots even if half the code is torn away.",
      mechanism: "QR codes employ Reed-Solomon Error Correction. Data bytes are mathematically mapped as coefficients of high-degree polynomials over finite Galois fields (GF(2⁸)). The decoder uses linear algebra (Peterson-Gorenstein-Zierler algorithm) to locate and correct corrupted pixels.",
      firstPrinciples: "Information Theory (Claude Shannon's noisy channel coding theorem). Redundancy can be systematically added to a discrete message such that the probability of transmission error approaches zero up to the channel capacity limit.",
      simMode: "wave",
      simWhatChanged: "Error-correction parity blocks were reconstructed from remaining polynomial roots.",
      simWhyChanged: "Polynomial interpolation over finite fields provides overdetermined equations with unique solvable solutions.",
      simNext: "The scanner verifies cyclic redundancy checks (CRC) and launches the decoded URI.",
      whyCare: "Reed-Solomon error correction is the exact same mathematics that allows NASA to receive faint images from the Voyager probes billions of miles away in deep space.",
      whatIfScenario: "What if digital barcodes had zero error correction?",
      whatIfConsequence: "A single microscopic speck of dust, paper crease, or camera blur would cause payments, airplane boarding passes, and supply chains to instantly fail.",
      trail: ["Binary Bits", "Shannon Channel Capacity", "Reed-Solomon Codes", "Finite Galois Fields", "Deep Space Telemetry"]
    },
    {
      id: "flagship-blue-sky",
      category: "how",
      categoryLabel: "Everyday Physics & Optics",
      badgeClass: "iva-badge-physics",
      readTime: "3 min thought experiment",
      question: "Why is the sky blue?",
      mystery: "Sunlight contains every color of the visible rainbow combined together into white light. Why does the sky overhead look blue instead of green, violet, or yellow?",
      prompt: "What happens when light waves of different wavelengths collide with microscopic molecules in the air?",
      simple: "Red light waves are long and lazy; blue light waves are short and choppy. When sunlight hits Earth's atmosphere, the tiny gas molecules scatter the short blue waves in every direction across the sky like ripples bouncing off pebbles.",
      mechanism: "Rayleigh scattering intensity is inversely proportional to the fourth power of wavelength (I ∝ 1/λ⁴). Because blue light (400 nm) has nearly half the wavelength of red light (700 nm), it scatters roughly 10 times more efficiently off atmospheric nitrogen and oxygen molecules.",
      firstPrinciples: "Incoming electromagnetic wave oscillating electric fields induce dipole moments in atmospheric gas molecules. The molecules re-radiate as tiny Rayleigh dipole antennas. Violet light scatters even more than blue, but human eye retinas have higher sensitivity to blue due to M and S cone cell spectral response.",
      simMode: "wave",
      simWhatChanged: "Shorter wavelengths were deflected in all directions by dielectric molecular polarizability.",
      simWhyChanged: "Molecular dipole re-radiation scales exponentially with frequency.",
      simNext: "At sunset, sunlight travels through far more atmosphere; the blue light scatters away completely, leaving only surviving red and orange wavelengths.",
      whyCare: "This exact physical principle allows astronomers to detect water vapor, methane, and oxygen in the atmospheres of planets orbiting distant stars hundreds of light years away.",
      whatIfScenario: "What if Earth had no atmosphere, like the Moon?",
      whatIfConsequence: "The sky would be completely pitch black in the middle of the day, with blazing white stars and galaxies clearly visible right next to the Sun.",
      trail: ["Electromagnetic Spectrum", "Rayleigh Scattering", "Dipole Moment", "Human Trichromatic Vision", "Exoplanet Spectroscopy"]
    },
    {
      id: "flagship-noise-cancellation",
      category: "how",
      categoryLabel: "Everyday Physics & Optics",
      badgeClass: "iva-badge-physics",
      readTime: "3 min thought experiment",
      question: "How do noise-cancelling headphones erase sound?",
      mystery: "You can sit inside a screaming jet engine cabin at 85 decibels, switch on your headphones, and hear near silence. How can adding more sound waves create quietness?",
      prompt: "What happens when the crest of one water wave meets the trough of an identical wave?",
      simple: "Sound travels as pressure waves of peaks and valleys. Noise-cancelling headphones have tiny outward-facing microphones that sample outside roar and instantly generate the exact upside-down wave (an anti-wave). Peak meets valley, and they cancel out into flat silence.",
      mechanism: "Destructive interference: Two coherent acoustic waves with a phase difference of 180° (π radians) superimpose linearly: sin(ωt) + sin(ωt + π) = 0. The positive compression peaks cancel the negative rarefaction valleys, reducing ambient acoustic pressure fluctuations by up to 30 dB.",
      firstPrinciples: "Linear superposition of the acoustic wave equation ∇²p - (1/c²)(∂²p/∂t²) = 0. Digital signal processors (DSP) run real-time adaptive Finite Impulse Response (FIR) algorithms with sub-15-microsecond latency to neutralize frequencies below 1 kHz.",
      simMode: "wave",
      simWhatChanged: "The emitted anti-phase waveform met incoming external ambient sound.",
      simWhyChanged: "Opposite pressure gradients cancel out to atmospheric baseline pressure.",
      simNext: "High-frequency unpredictable sounds (like sudden human speech) cannot be predicted in 15 microseconds, relying on passive silicone seal isolation.",
      whyCare: "Active noise cancellation protects aircraft pilots and heavy machinery workers from permanent acoustic trauma and stabilizes laser interferometers in gravity-wave observatories.",
      whatIfScenario: "What if the headphones emitted the wave in-phase (0°) instead of out-of-phase (180°)?",
      whatIfConsequence: "Constructive interference: The cabin noise would double in amplitude (+6 dB), producing an excruciating and deafening acoustic explosion.",
      trail: ["Acoustic Wave Equation", "Destructive Interference", "Phase Inversion", "DSP Adaptive Filtering", "Interferometric Sensing"]
    },
    {
      id: "flagship-time-dilation",
      category: "science",
      categoryLabel: "Quantum & Particles",
      badgeClass: "iva-badge-physics",
      readTime: "4 min thought experiment",
      question: "Why does time slow down near heavy objects?",
      mystery: "Your head is aging slightly faster than your feet right now. Clocks on top of a mountain tick faster than clocks at sea level. Why does gravity bend the flow of time itself?",
      prompt: "If the speed of light must be universally constant for all observers, what must stretch and bend when space is warped?",
      simple: "Think of spacetime as a unified four-dimensional fabric. Everything in the universe moves through spacetime at one single speed: the speed of light. If you sit deep inside a heavy planet's gravitational well, more of your motion is devoted to space, so your motion through time slows down.",
      mechanism: "Gravitational time dilation: t_f = t_0 √(1 - 2GM/rc²). Lower gravitational potential corresponds to slower coordinate time evolution relative to a distant asymptotic observer.",
      firstPrinciples: "Einstein's Equivalence Principle: Local gravitational fields are physically indistinguishable from uniformly accelerated reference frames. In an accelerating frame, Doppler wave reception demands that higher positions observe lower clocks ticking at a retarded rate.",
      simMode: "orbit",
      simWhatChanged: "The metric tensor component g₀₀ scaled with gravitational potential.",
      simWhyChanged: "Proper time along worldlines reflects the curvature of four-dimensional Riemannian geometry.",
      simNext: "At the event horizon of a black hole, time appears to an outside observer to completely freeze.",
      whyCare: "GPS satellites are 20,200 km above Earth where gravity is weaker. Their clocks tick 45 microseconds faster per day. If Einstein's equations weren't programmed into GPS, your phone's map location would drift by 11 kilometers every single day.",
      whatIfScenario: "What if time were universal and unaffected by mass?",
      whatIfConsequence: "Light would accelerate or decelerate in gravitational fields, shattering Maxwell's equations, electromagnetism, and the speed of light constancy.",
      trail: ["Equivalence Principle", "Gravitational Redshift", "Metric Tensor", "GPS Clock Correction", "Black Hole Horizons"]
    },
    {
      id: "flagship-blind-spot",
      category: "thinking",
      categoryLabel: "Philosophy of Mind",
      badgeClass: "iva-badge-math",
      readTime: "3 min thought experiment",
      question: "Why do we have blind spots in our eyes that we never notice?",
      mystery: "In each of your eyes, there is a physical hole in your retina as large as a coin held at arm's length where you are completely blind. Why don't you see two black holes hovering in your vision right now?",
      prompt: "How does the human brain handle missing sensory information?",
      simple: "Where the optic nerve connects to the back of your eye, there are zero light receptors. But your brain detests empty holes. It examines the colors and textures surrounding the gap and continuously paints over the blind spot with its best probabilistic prediction.",
      mechanism: "Vertebrate evolution produced an 'inverted' retina: photoreceptors face backward toward the brain, while nerve fibers run across the front, bundling together at the optic disc (1.5 mm diameter). Cephalopods (like octopuses) evolved forward-facing photoreceptors and have zero blind spots.",
      firstPrinciples: "Cortical predictive processing in visual area V1. Neural circuits perform continuous Bayesian inference, interpolating surface luminance, edge continuity, and spatial texture based on surrounding receptive fields.",
      simMode: "wave",
      simWhatChanged: "The visual cortex synthesized artificial visual signals to bridge receptor deficits.",
      simWhyChanged: "Evolutionary pressure favored continuous, actionable spatial representations over raw, fragmented optical input.",
      simNext: "If an unexpected object (like a dart) enters only the blind spot, the brain will erase it until it crosses the boundary.",
      whyCare: "Understanding how the brain hallucinates reality to bridge missing data is foundational for autonomous vehicle vision, optical illusions, and cognitive neuroscience.",
      whatIfScenario: "What if our brains did not fill in the blind spot?",
      whatIfConsequence: "You would constantly see two fluttering black holes hovering in your peripheral vision, severely degrading motion tracking and spatial awareness.",
      trail: ["Optic Disc", "Evolutionary Tinkering", "Photoreceptor Orientation", "Predictive Perception", "Bayesian Vision"]
    }
  ];

  // Procedural Curriculum Engine (500,000+ paths)
  var PROCEDURAL_CURRICULUM = {
    space: {
      topics: [
        ["Neutron Stars", "crushing nuclear density", "electron degeneracy pressure collapse", "pulsar timing navigation"],
        ["Black Hole Event Horizon", "infinite gravitational redshift", "unidirectional spacetime geodesics", "Event Horizon Telescope imaging"],
        ["Cosmic Microwave Background", "primordial recombination photon decoupling", "380,000-year post-Big Bang relic radiation", "Planck satellite anisotropy mapping"],
        ["Orbital Free Fall", "tangential orbital velocity balancing gravitational acceleration", "Newton's cannon spherical curvature matching", "International Space Station trajectory"],
        ["Solar Wind & Magnetosphere", "charged plasma particle deflection", "planetary magnetic dipole Lorentz force shielding", "aurora borealis and grid protection"],
        ["Gravitational Waves", "quadrupole mass acceleration spacetime ripples", "speed-of-light metric strain distortion", "LIGO laser interferometry"],
        ["Dark Matter Halos", "flat galactic rotation curves defying Newtonian drop-off", "non-baryonic collisionless gravitational mass", "gravitational lensing arc reconstruction"],
        ["Thermonuclear Fusion", "proton-proton chain Coulomb barrier tunneling", "mass-to-energy conversion via E=mc²", "ITER tokamak magnetic confinement"]
      ],
      angles: [
        "Why does mass curve the temporal coordinate faster than spatial coordinates?",
        "How does conservation of angular momentum spin up collapsing cores to millisecond periods?",
        "What prevents degenerate matter from collapsing directly into a singularity?"
      ]
    },
    science: {
      topics: [
        ["Wave-Particle Duality", "de Broglie matter wavelength diffraction", "quantum probability amplitude interference", "electron microscopy resolution"],
        ["Superconductivity", "Cooper pair electron-phonon lattice coupling", "Meissner effect magnetic flux expulsion", "maglev train frictionless levitation"],
        ["Entropy & Second Law", "microstate phase space multiplicity expansion", "spontaneous thermodynamic irreversibility", "heat engines and universal heat death"],
        ["Quantum Entanglement", "non-separable Hilbert state wavefunctions", "EPR paradox and Bell inequality violation", "quantum key distribution cryptography"]
      ],
      angles: [
        "Why can't entropy decrease in an isolated thermodynamic system?",
        "How does quantum tunneling permit alpha particle radioactive decay?",
        "What defines the microscopic transition between quantum coherence and classical reality?"
      ]
    },
    math: {
      topics: [
        ["Prime Distribution", "Riemann zeta function complex non-trivial zeros", "prime number theorem asymptotic density", "RSA public key asymmetric encryption"],
        ["Gödel Incompleteness", "self-referential arithmetic formalization", "unprovable mathematical truths", "limits of axiomatic computational proof"],
        ["Topological Invariance", "continuous deformation homeomorphic invariants", "Euler characteristic genus mapping", "topological insulators in quantum computing"],
        ["Fourier Decomposition", "orthogonal harmonic trigonometric basis expansion", "frequency domain spectral transformation", "MP3 audio compression and MRI scanning"]
      ],
      angles: [
        "Why is there no largest prime number in number theory?",
        "How does topology classify shapes without measuring geometric distance?",
        "Can an axiomatic system ever be both completely consistent and fully complete?"
      ]
    },
    nature: {
      topics: [
        ["DNA Polymerase Fidelity", "Watson-Crick base-pair hydrogen bonding geometry", "3'-to-5' exonucleolytic proofreading enzymatic repair", "CRISPR gene editing accuracy"],
        ["Photosynthetic Quantum Transport", "Fenna-Matthews-Olson pigment-protein complex", "coherent exciton energy transfer to reaction center", "artificial solar cell efficiency"],
        ["Mycorrhizal Fungal Networks", "symbiotic bidirectional nutrient carbon exchange", "infochemical hydraulic hazard signaling", "forest ecosystem drought resilience"],
        ["Bacterial Quorum Sensing", "autoinducer threshold concentration signaling", "density-dependent synchronized bioluminescence", "anti-virulence antibiotic alternatives"]
      ],
      angles: [
        "How do biological cells maintain low entropy despite the Second Law of Thermodynamics?",
        "Why did natural selection favor a triplet codon genetic alphabet over a doublet?",
        "What evolutionary mechanism preserves biological altruism against selfish gene mutations?"
      ]
    },
    tech: {
      topics: [
        ["Transformer Attention", "multi-head scaled dot-product query-key matching", "global context self-attention weight matrix", "large language model generative synthesis"],
        ["Silicon Photolithography", "extreme ultraviolet (EUV) 13.5 nm wave reflection", "diffraction-limited optical semiconductor etching", "3-nanometer transistor microprocessor density"],
        ["Consensus Algorithms", "Byzantine fault tolerance state machine replication", "cryptographic proof-of-work decentralized truth", "fault-tolerant distributed cloud databases"],
        ["Flash Memory Tunneling", "Fowler-Nordheim quantum tunneling charge entrapment", "floating gate isolated floating-dielectric retention", "solid-state drives and portable storage"]
      ],
      angles: [
        "How does extreme ultraviolet photolithography bypass the physical diffraction limit?",
        "Why do neural network attention layers scale quadratically with context length?",
        "What guarantees consistency in distributed databases across asynchronous networks?"
      ]
    },
    thinking: {
      topics: [
        ["Conscious Subjective Qualia", "explanatory gap in physicalist reductionism", "higher-order representational neural integration", "artificial general intelligence self-awareness"],
        ["Bayesian Predictive Brain", "hierarchical predictive coding sensory prediction error", "active inference minimizing free energy", "visual optical illusions and phantom sensations"],
        ["Ship of Theseus", "mereological identity continuity across incremental substitution", "relational substrate-independent functionalism", "cellular turnover and personal identity"],
        ["Trolley Ethical Dilemma", "deontological duty constraint versus utilitarian outcome", "neural competition between amygdala and prefrontal cortex", "autonomous vehicular moral algorithmic design"]
      ],
      angles: [
        "If every atom in your body replaces itself every seven years, what remains 'you'?",
        "Does the brain construct reality from predictive models rather than raw sensory inputs?",
        "Can a physical system ever fully explain its own subjective qualitative experience?"
      ]
    },
    how: {
      topics: [
        ["Microwave Cavity Heating", "2.45 GHz electromagnetic oscillating dipole rotation", "dielectric water molecule friction and heat transfer", "rapid industrial thermal processing"],
        ["LED Photon Recombination", "direct bandgap semiconductor p-n junction", "electron-hole pair radiative radiative recombination", "ultra-efficient solid-state building lighting"],
        ["Aerodynamic Lift", "streamline curvature pressure gradient integration", "Euler momentum conservation and downwash deflection", "commercial aviation transoceanic flight"],
        ["Induction Cooktop Heating", "high-frequency alternating magnetic field eddy currents", "ferromagnetic Joule heating and magnetic hysteresis", "energy-efficient clean culinary thermal transfer"]
      ],
      angles: [
        "Why does an airplane wing require downward air deflection to sustain aerodynamic lift?",
        "How do microwave ovens heat water molecules while leaving glass containers cold?",
        "What allows LEDs to emit light without generating filament heat?"
      ]
    },
    behavior: {
      topics: [
        ["Nash Equilibrium", "non-cooperative strategic payoff optimization", "zero-unilateral incentive to deviate", "international treaty negotiations and spectrum auctions"],
        ["Dunbar's Number Limit", "neocortex ratio to social group volume correlation", "cognitive cognitive tracking capacity threshold", "organizational scaling and tribal cohesion"],
        ["Tragedy of the Commons", "rivalrous non-excludable resource overexploitation", "individual rational utility degrading collective yield", "global fisheries management and climate accords"],
        ["Information Cascades", "rational observational Bayesian herding behavior", "private signal suppression in sequential choices", "financial market bubbles and viral social adoption"]
      ],
      angles: [
        "Why do rational individual decisions often produce disastrous collective outcomes?",
        "How does human group cohesion fragment when social units exceed 150 members?",
        "What game-theoretic mechanisms prevent cheating in cooperative animal ecosystems?"
      ]
    }
  };

  // 3-Mode "I'm Bored" Micro-Experiments (Section 18)
  var BORED_MODES = {
    observe: [
      "Look at any shadow cast on the floor or wall right now. Notice the blurry penumbra around its edges. Why is the edge fuzzy instead of razor-sharp? (Hint: The light bulb has physical width; it's an extended area, not a mathematical point source.)",
      "Look at a clear glass of water. Dip a pencil or your finger into it. Notice how it appears broken or shifted at the surface. That angle is the visual signature of light slowing down by 25% inside water.",
      "Look at the screen you are reading this on from 2 inches away. Notice the tiny red, green, and blue subpixels. Your brain blends those three physical wavelengths into every single color you see.",
      "Close your eyes and listen carefully. Try to identify the single quietest background sound in the room that your brain was unconsciously filtering out two seconds ago."
    ],
    think: [
      "How would you measure exactly one minute of time if you had no clock, no phone, and no access to your pulse?",
      "If you had a balance scale and 9 identical-looking coins, but one was counterfeit and slightly heavier, how could you find the fake coin in just two weighings?",
      "Why is a mirror image flipped horizontally (left to right), but never flipped vertically (upside down)? Think carefully about the front-to-back z-axis.",
      "If all the ice in the Arctic ocean melted tomorrow, would global sea levels rise immediately? (Hint: Consider Archimedes' principle of floating ice displacement.)"
    ],
    do: [
      "Take a flat sheet of paper and a crumpled sheet of paper. Drop them simultaneously from shoulder height. The crumpled ball hits first, not because it's heavier, but because it punches through aerodynamic drag.",
      "Fill a small plastic cup halfway with water. Turn it upside down over a flat card. Atmospheric pressure (14.7 pounds per square inch) will hold the card and water against gravity.",
      "Try to hum while holding your nose tightly closed. Notice that you cannot sustain it for more than one second, because humming requires acoustic airflow through your nasal cavity.",
      "Stand on one foot with your eyes wide open. Now close your eyes. Notice how quickly you begin wobbling—your brain relies far more on visual horizon cues for balance than on muscle memory."
    ]
  };

  // Strange Facts Archive with "Wait... Why?" (Section 19)
  var STRANGE_FACTS = [
    {
      fact: "If you removed all the empty space from the atoms of all 8 billion human beings on Earth, the remaining solid mass would fit into the volume of a single sugar cube.",
      why: "Atoms are 99.9999999% empty space. The electron cloud surrounds a nucleus that is 100,000 times smaller. What prevents you from falling through a floor isn't solid matter, but the electrostatic repulsion of electron clouds governed by the Pauli Exclusion Principle.",
      relatedId: "flagship-time-dilation"
    },
    {
      fact: "A single day on Venus is longer than its entire year.",
      why: "Venus rotates on its axis extraordinarily slowly—taking 243 Earth days to complete one rotation—while orbiting the Sun in 225 Earth days. It also spins backward (retrograde), likely due to a colossal ancient collision.",
      relatedId: "flagship-moon"
    },
    {
      fact: "Time runs faster on top of a mountain than it does at sea level.",
      why: "Gravitational time dilation! Einstein proved that the closer you are to a massive body like Earth, the deeper you sit in its gravitational well, and the slower time flows relative to an observer higher up.",
      relatedId: "flagship-time-dilation"
    },
    {
      fact: "There are more possible chess games than there are atoms in the observable universe.",
      why: "The Shannon Number estimates approximately 10¹²⁰ unique chess variations. The observable universe contains only about 10⁸⁰ atoms. Combinatorial expansion explodes beyond cosmic scales.",
      relatedId: "flagship-qr-code"
    },
    {
      fact: "Bananas are naturally radioactive, emitting an antimatter positron roughly once every 75 minutes.",
      why: "Bananas are rich in potassium, which naturally contains potassium-40 (⁴⁰K), an unstable isotope that occasionally undergoes beta-plus decay, emitting a real antimatter positron.",
      relatedId: "flagship-blue-sky"
    }
  ];

  // Concept Sparks for Original Question Studio (Section 17)
  var CONCEPT_SPARKS = [
    "BLACK HOLES", "PLANTS", "ACOUSTIC WAVES",
    "ENTROPY", "MEMORY", "OCTOPUS TENTACLES",
    "SUPERCONDUCTIVITY", "IMMUNE CELLS", "ORIGAMI",
    "GRAVITATIONAL WAVES", "PHOTOSYNTHESIS", "ANT COLONIES",
    "NEURAL NETWORKS", "TIDES", "BACTERIAL BIOFILMS",
    "PRIME NUMBERS", "GLACIERS", "SOUND CANCELLATION"
  ];

  // Intellectual Milestones (Non-Competitive) (Section 23, 42)
  var MILESTONES = [
    { id: "m_first", icon: "🌱", title: "First Spark", desc: "Explored your very first first-principles inquiry.", threshold: 1, type: "explored" },
    { id: "m_thinker", icon: "💡", title: "Hypothesis Former", desc: "Penned your first independent guess before reading an answer.", threshold: 1, type: "reflection" },
    { id: "m_explorer", icon: "🔭", title: "Active Observer", desc: "Pondered 5 fundamental questions across disciplines.", threshold: 5, type: "explored" },
    { id: "m_creator", icon: "✍️", title: "Question Creator", desc: "Sparked an original inquiry connecting three concepts.", threshold: 1, type: "spark" },
    { id: "m_deep", icon: "🌌", title: "Cosmic Thinker", desc: "Explored 15 deep scientific and philosophical inquiries.", threshold: 15, type: "explored" },
    { id: "m_polymath", icon: "🏛️", title: "First-Principles Thinker", desc: "Investigated 30 fundamental mechanisms of reality.", threshold: 30, type: "explored" }
  ];

  // ════════════════════════════════════════════════════════════════
  // 2. STATE MANAGEMENT & STORAGE (Section 24, 35)
  // ════════════════════════════════════════════════════════════════
  var STORAGE_KEY = 'iva_curiosity_master_v3';
  var appState = {
    currentView: 'home',
    currentQuestionId: null,
    currentQuestionObj: null,
    exploredIds: [],
    savedIds: [],
    reflections: {},
    sparkQuestions: [],
    streak: 1,
    lastActiveDate: new Date().toDateString(),
    soundEnabled: true,
    boredMode: 'observe',
    activeLevel: 1
  };

  function loadState() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      var today = new Date().toDateString();
      if (raw) {
        var parsed = JSON.parse(raw);
        appState.exploredIds = Array.isArray(parsed.exploredIds) ? parsed.exploredIds : [];
        appState.savedIds = Array.isArray(parsed.savedIds) ? parsed.savedIds : [];
        appState.reflections = (typeof parsed.reflections === 'object' && parsed.reflections !== null) ? parsed.reflections : {};
        appState.sparkQuestions = Array.isArray(parsed.sparkQuestions) ? parsed.sparkQuestions : [];
        appState.soundEnabled = (parsed.soundEnabled !== false);

        var last = parsed.lastActiveDate || today;
        var diffDays = Math.floor((new Date(today).getTime() - new Date(last).getTime()) / (1000 * 60 * 60 * 24));
        if (diffDays === 0) {
          appState.streak = parsed.streak || 1;
        } else if (diffDays === 1) {
          appState.streak = (parsed.streak || 1) + 1;
          appState.lastActiveDate = today;
          saveState();
        } else {
          appState.streak = 1;
          appState.lastActiveDate = today;
          saveState();
        }
      }
    } catch (e) {
      console.warn("Curiosity storage initialized safely.");
    }
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        exploredIds: appState.exploredIds,
        savedIds: appState.savedIds,
        reflections: appState.reflections,
        sparkQuestions: appState.sparkQuestions,
        streak: appState.streak,
        lastActiveDate: appState.lastActiveDate,
        soundEnabled: appState.soundEnabled
      }));
    } catch (e) {}
  }

  // ════════════════════════════════════════════════════════════════
  // 3. AUDIO SYNTHESIZER (Web Audio API)
  // ════════════════════════════════════════════════════════════════
  var audioCtx = null;
  function playSynthChord(type) {
    if (!appState.soundEnabled) return;
    try {
      var AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!AudioContext) return;
      if (!audioCtx) audioCtx = new AudioContext();
      if (audioCtx.state === 'suspended') audioCtx.resume();

      var now = audioCtx.currentTime;
      var freqs = [220, 277.18, 329.63, 440]; // A major celestial harmony
      if (type === 'discover') freqs = [261.63, 329.63, 392.00, 523.25]; // C major
      if (type === 'milestone') freqs = [329.63, 415.30, 493.88, 659.25]; // E major triumphant

      freqs.forEach(function(f, i) {
        var osc = audioCtx.createOscillator();
        var gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(f, now);

        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(0.04 / (i + 1), now + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 1.2);

        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc.stop(now + 1.2);
      });
    } catch (e) {}
  }

  // ════════════════════════════════════════════════════════════════
  // 4. CANVAS PARTICLES & SIMULATORS (Section 22)
  // ════════════════════════════════════════════════════════════════
  var simSpeed = 0.02;
  var simAngle = 0;
  var currentSimMode = 'orbit';

  function initCosmicCanvas() {
    var canvas = document.getElementById('ivaCosmicCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w, h;
    var stars = [];

    function resize() {
      w = canvas.width = window.innerWidth;
      h = canvas.height = Math.max(window.innerHeight, document.getElementById('iva-curiosity-machine').offsetHeight || 800);
      stars = [];
      for (var i = 0; i < 75; i++) {
        stars.push({
          x: Math.random() * w,
          y: Math.random() * h,
          r: Math.random() * 1.5 + 0.4,
          a: Math.random(),
          speed: Math.random() * 0.008 + 0.002
        });
      }
    }
    window.addEventListener('resize', resize);
    resize();

    function render() {
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#ffffff';
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i];
        s.a += s.speed;
        var opacity = (Math.sin(s.a) + 1) / 2 * 0.7 + 0.15;
        ctx.globalAlpha = opacity;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fill();
      }
      requestAnimationFrame(render);
    }
    render();
  }

  function initSimulator() {
    var canvas = document.getElementById('ivaSimCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = 600;
    var h = canvas.height = 220;

    function draw() {
      ctx.clearRect(0, 0, w, h);
      var cx = w / 2;
      var cy = h / 2;

      if (currentSimMode === 'orbit') {
        // Star in center
        ctx.fillStyle = '#b38642';
        ctx.shadowColor = '#b38642';
        ctx.shadowBlur = 18;
        ctx.beginPath();
        ctx.arc(cx, cy, 14, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;

        // Orbital Ellipse Path
        var rx = 180;
        var ry = 75;
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.14)';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.ellipse(cx, cy, rx, ry, 0, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);

        // Orbiting Body (Moon / Satellite)
        simAngle += simSpeed;
        var px = cx + Math.cos(simAngle) * rx;
        var py = cy + Math.sin(simAngle) * ry;

        ctx.fillStyle = '#00d2ff';
        ctx.shadowColor = '#00d2ff';
        ctx.shadowBlur = 12;
        ctx.beginPath();
        ctx.arc(px, py, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;

        // Tangential Velocity Vector
        var vx = -Math.sin(simAngle) * 22;
        var vy = Math.cos(simAngle) * 10;
        ctx.strokeStyle = '#e94560';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(px + vx, py + vy);
        ctx.stroke();

      } else {
        // Wave Cancellation Simulator
        ctx.lineWidth = 2;
        var step = 4;
        simAngle += simSpeed;

        // Wave 1: Incoming Noise (Cyan)
        ctx.strokeStyle = '#00d2ff';
        ctx.beginPath();
        for (var x = 0; x < w; x += step) {
          var y1 = cy + Math.sin((x * 0.04) + simAngle) * 35;
          if (x === 0) ctx.moveTo(x, y1); else ctx.lineTo(x, y1);
        }
        ctx.stroke();

        // Wave 2: Anti-Wave Phase Inversion (Terracotta)
        ctx.strokeStyle = '#e94560';
        ctx.beginPath();
        for (var x2 = 0; x2 < w; x2 += step) {
          var y2 = cy + Math.sin((x2 * 0.04) + simAngle + Math.PI) * 35;
          if (x2 === 0) ctx.moveTo(x2, y2); else ctx.lineTo(x2, y2);
        }
        ctx.stroke();

        // Resultant: Net Zero Flat Line (Emerald)
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(0, cy);
        ctx.lineTo(w, cy);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      requestAnimationFrame(draw);
    }
    draw();
  }

  // ════════════════════════════════════════════════════════════════
  // 5. QUESTION ENGINE (Flagship + 500,000 Paths)
  // ════════════════════════════════════════════════════════════════
  function getQuestionById(id) {
    var flagship = FLAGSHIP_INQUIRIES.find(function(q) { return q.id === id; });
    if (flagship) return flagship;

    // Procedural generation
    var num = 1;
    if (id && id.indexOf('-') !== -1) {
      num = parseInt(id.split('-')[1], 10) || 1;
    }
    return generateProceduralQuestion(num - 1);
  }

  function generateProceduralQuestion(globalIndex) {
    var TOTAL_PER_CAT = 62500;
    var catKeys = ["space", "science", "math", "nature", "tech", "thinking", "how", "behavior"];
    var catIdx = Math.floor(globalIndex / TOTAL_PER_CAT) % 8;
    var catKey = catKeys[catIdx];
    var catData = PROCEDURAL_CURRICULUM[catKey] || PROCEDURAL_CURRICULUM.space;
    var catInfo = CATEGORIES.find(function(c) { return c.key === catKey; }) || { label: "General Science", badge: "iva-badge-space" };

    var localIdx = globalIndex % TOTAL_PER_CAT;
    var tLen = catData.topics.length;
    var aLen = catData.angles.length;

    var top = catData.topics[localIdx % tLen];
    var tName = top[0];
    var tCore = top[1];
    var tMech = top[2];
    var tApp = top[3];
    var angleQ = catData.angles[Math.floor(localIdx / tLen) % aLen];

    var padded = String((globalIndex % 99999) + 1);
    while (padded.length < 5) padded = "0" + padded;

    return {
      id: catKey + "-" + padded,
      globalNumber: globalIndex + 1,
      category: catKey,
      categoryLabel: catInfo.label,
      badgeClass: catInfo.badge,
      readTime: "3 min thought experiment",
      question: tName + ": " + angleQ,
      mystery: "We routinely observe " + tName.toLowerCase() + " in natural systems, yet its foundational behavior under " + tCore + " defies everyday classical intuition. Why?",
      prompt: "What physical or logical principle prevents " + tName.toLowerCase() + " from behaving in a purely classical manner?",
      simple: tName + " operates under " + tCore + ". Energy and matter interact to preserve fundamental physical equilibrium.",
      mechanism: "The underlying mechanism is driven by " + tMech + ". Quantum and thermodynamic constraints govern the exchange of momentum.",
      firstPrinciples: "From first principles, this manifests universal conservation laws. System state evolution strictly follows the principle of least action.",
      simMode: (catKey === 'how' || catKey === 'tech') ? 'wave' : 'orbit',
      simWhatChanged: "State variables shifted to maintain dynamic equilibrium.",
      simWhyChanged: "Physical field potentials naturally minimize thermodynamic free energy.",
      simNext: "Perturbing the initial conditions causes rapid dampening back to the stable attractor.",
      whyCare: "This exact mechanism forms the basis of " + tApp + ", enabling precision modern engineering.",
      whatIfScenario: "What if " + tCore + " were removed from this system?",
      whatIfConsequence: "Without this constraint, equilibrium would collapse and " + tName.toLowerCase() + " could not sustain stable structure.",
      trail: [tName, tCore, tMech, tApp, "First Principles"]
    };
  }

  // ════════════════════════════════════════════════════════════════
  // 6. UI VIEW NAVIGATION & RENDERING
  // ════════════════════════════════════════════════════════════════
  function showView(viewId) {
    var views = document.querySelectorAll('#iva-curiosity-machine .iva-view');
    views.forEach(function(v) { v.classList.add('iva-hidden'); });

    var target = document.getElementById(viewId);
    if (target) {
      target.classList.remove('iva-hidden');
      window.scrollTo({ top: document.getElementById('iva-curiosity-machine').offsetTop || 0, behavior: 'smooth' });
    }

    // Update active nav button
    document.querySelectorAll('#iva-curiosity-machine .iva-nav-btn').forEach(function(btn) {
      btn.classList.remove('active');
    });
    if (viewId === 'ivaHomeView') document.getElementById('ivaNavHomeBtn').classList.add('active');
    if (viewId === 'ivaBoredView') document.getElementById('ivaNavBoredBtn').classList.add('active');
    if (viewId === 'ivaStrangeView') document.getElementById('ivaNavStrangeBtn').classList.add('active');
    if (viewId === 'ivaSavedView') document.getElementById('ivaNavSavedBtn').classList.add('active');
    if (viewId === 'ivaJourneyView') document.getElementById('ivaNavJourneyBtn').classList.add('active');

    appState.currentView = viewId;
  }

  function openCuriosity(qId, directObj) {
    playSynthChord('discover');
    var q = directObj || getQuestionById(qId);
    appState.currentQuestionId = q.id;
    appState.currentQuestionObj = q;

    // Track exploration & progress
    if (appState.exploredIds.indexOf(q.id) === -1) {
      appState.exploredIds.push(q.id);
      saveState();
      updateMilestones();
    }

    // Populate Detail View
    document.getElementById('ivaDetailBadge').className = "iva-badge " + (q.badgeClass || 'iva-badge-space');
    document.getElementById('ivaDetailBadge').textContent = (q.categoryLabel || "Astrophysics").toUpperCase();
    document.getElementById('ivaDetailInquiryNumber').textContent = "Inquiry #" + (q.globalNumber || q.id);
    document.getElementById('ivaDetailReadTime').textContent = q.readTime || "3 min thought experiment";
    document.getElementById('ivaDetailTitle').textContent = q.question;
    document.getElementById('ivaDetailMystery').textContent = q.mystery || q.prompt;

    // Reset Think Gate
    var existingReflection = appState.reflections[q.id] || "";
    document.getElementById('ivaThinkInput').value = existingReflection;
    document.getElementById('ivaThinkFeedback').style.display = existingReflection ? "block" : "none";
    if (existingReflection) {
      document.getElementById('ivaThinkFeedback').textContent = "Your saved hypothesis: \"" + existingReflection + "\"";
    }

    // Explanations
    document.getElementById('ivaExpContentLevel1').textContent = q.simple;
    document.getElementById('ivaExpContentLevel2').textContent = q.mechanism;
    document.getElementById('ivaExpContentLevel3').textContent = q.firstPrinciples;
    setExplanationLevel(1);

    // Simulator
    currentSimMode = q.simMode || 'orbit';
    document.getElementById('ivaSimModeLabel').textContent = currentSimMode === 'wave' ? 'Phase Interference' : 'Gravitational Free Fall';
    document.getElementById('ivaSimWhatChanged').textContent = q.simWhatChanged;
    document.getElementById('ivaSimWhyChanged').textContent = q.simWhyChanged;
    document.getElementById('ivaSimNext').textContent = q.simNext;

    // "Why Should I Care?"
    document.getElementById('ivaCareText').textContent = q.whyCare || "This principle underpins essential scientific and real-world technological architectures.";

    // "What If?"
    document.getElementById('ivaWhatIfScenario').textContent = q.whatIfScenario;
    document.getElementById('ivaWhatIfConsequence').textContent = q.whatIfConsequence;
    document.getElementById('ivaWhatIfRevealBox').style.display = "none";
    document.getElementById('ivaWhatIfPredictBtn').style.display = "inline-flex";

    // Connect the Dots
    var trailChain = document.getElementById('ivaTrailChain');
    trailChain.innerHTML = "";
    if (Array.isArray(q.trail)) {
      q.trail.forEach(function(concept, idx) {
        var node = document.createElement('button');
        node.type = 'button';
        node.className = 'iva-trail-node';
        node.textContent = concept;
        node.addEventListener('click', function() {
          performSearch(concept);
        });
        trailChain.appendChild(node);

        if (idx < q.trail.length - 1) {
          var arrow = document.createElement('span');
          arrow.className = 'iva-trail-arrow';
          arrow.textContent = '➔';
          trailChain.appendChild(arrow);
        }
      });
    }

    updateBookmarkState(q.id);
    showView('ivaCuriosityView');
  }

  function setExplanationLevel(level) {
    appState.activeLevel = level;
    document.getElementById('ivaTabLevel1').classList.toggle('active', level === 1);
    document.getElementById('ivaTabLevel2').classList.toggle('active', level === 2);
    document.getElementById('ivaTabLevel3').classList.toggle('active', level === 3);

    document.getElementById('ivaExpContentLevel1').style.display = level === 1 ? 'block' : 'none';
    document.getElementById('ivaExpContentLevel2').style.display = level === 2 ? 'block' : 'none';
    document.getElementById('ivaExpContentLevel3').style.display = level === 3 ? 'block' : 'none';
  }

  function updateBookmarkState(qId) {
    var btn = document.getElementById('ivaBookmarkBtn');
    if (!btn) return;
    var isSaved = appState.savedIds.indexOf(qId) !== -1;
    btn.textContent = isSaved ? "✓ Inquiry Saved" : "🔖 Save Inquiry";
    btn.classList.toggle('iva-btn-primary', !isSaved);
    btn.classList.toggle('iva-btn-secondary', isSaved);
  }

  function toggleBookmark(qId) {
    var idx = appState.savedIds.indexOf(qId);
    if (idx === -1) {
      appState.savedIds.push(qId);
      showToast("🔖", "Inquiry saved to your intellectual memory!");
    } else {
      appState.savedIds.splice(idx, 1);
      showToast("🗑️", "Inquiry removed from saved.");
    }
    saveState();
    updateBookmarkState(qId);
    updateMilestones();
  }

  // ════════════════════════════════════════════════════════════════
  // 7. DETERMINISTIC DAILY CURIOSITY (Section 20)
  // ════════════════════════════════════════════════════════════════
  function initDailyCuriosity() {
    var todayStr = new Date().toISOString().slice(0, 10); // e.g. "2026-09-30"
    var hash = 0;
    for (var i = 0; i < todayStr.length; i++) {
      hash = (hash << 5) - hash + todayStr.charCodeAt(i);
      hash |= 0;
    }
    var dailyIndex = Math.abs(hash) % FLAGSHIP_INQUIRIES.length;
    var dailyQ = FLAGSHIP_INQUIRIES[dailyIndex];

    var dateObj = new Date();
    var dateFormatted = dateObj.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
    document.getElementById('ivaDailyDateBadge').textContent = "TODAY'S INQUIRY • " + dateFormatted.toUpperCase();
    document.getElementById('ivaDailyTitle').textContent = dailyQ.question;
    document.getElementById('ivaDailyPremise').textContent = dailyQ.mystery;

    document.getElementById('ivaDailyExploreBtn').onclick = function() {
      openCuriosity(dailyQ.id, dailyQ);
    };
  }

  // ════════════════════════════════════════════════════════════════
  // 8. RANDOM WALK (Section 21)
  // ════════════════════════════════════════════════════════════════
  function triggerRandomWalk() {
    var randIndex = Math.floor(Math.random() * (FLAGSHIP_INQUIRIES.length + 5000));
    var q;
    if (randIndex < FLAGSHIP_INQUIRIES.length) {
      q = FLAGSHIP_INQUIRIES[randIndex];
    } else {
      q = generateProceduralQuestion(randIndex);
    }
    openCuriosity(q.id, q);
    showToast("🌐", "Traversing to " + q.categoryLabel + "...");
  }

  // ════════════════════════════════════════════════════════════════
  // 9. FORGIVING SEARCH ENGINE (Section 25)
  // ════════════════════════════════════════════════════════════════
  function performSearch(query) {
    if (!query || !query.trim()) {
      document.getElementById('ivaSearchResultsWrap').style.display = 'none';
      return;
    }
    var term = query.toLowerCase().trim();
    showView('ivaHomeView');

    var matches = [];
    // Search Flagships first
    FLAGSHIP_INQUIRIES.forEach(function(q) {
      var hay = (q.question + " " + q.categoryLabel + " " + (q.trail || []).join(" ") + " " + q.simple).toLowerCase();
      if (hay.indexOf(term) !== -1) matches.push(q);
    });

    // Match categories
    CATEGORIES.forEach(function(cat) {
      if (cat.label.toLowerCase().indexOf(term) !== -1 || cat.key.indexOf(term) !== -1) {
        var sampleQ = generateProceduralQuestion(CATEGORIES.indexOf(cat) * 62500);
        if (!matches.some(function(m) { return m.id === sampleQ.id; })) matches.push(sampleQ);
      }
    });

    var resultsWrap = document.getElementById('ivaSearchResultsWrap');
    var resultsGrid = document.getElementById('ivaSearchResultsGrid');
    var resultsTitle = document.getElementById('ivaSearchResultsTitle');
    resultsWrap.style.display = 'block';
    resultsGrid.innerHTML = '';

    if (matches.length === 0) {
      resultsTitle.textContent = "Hmm. We don't have that exact question yet.";
      resultsGrid.innerHTML = '<div style="grid-column: 1 / -1; padding: 24px; text-align: center; color: var(--iva-text-secondary);">' +
        '<p>Try exploring broad sparks like <strong>Gravity, Space, Quantum, Evolution,</strong> or <strong>Time</strong>.</p></div>';
    } else {
      resultsTitle.textContent = 'Found ' + matches.length + ' inquiry sparks for "' + query + '":';
      matches.forEach(function(q) {
        var card = document.createElement('div');
        card.className = 'iva-saved-item';
        card.innerHTML = '<span class="iva-badge ' + (q.badgeClass || 'iva-badge-space') + '">' + (q.categoryLabel || 'Inquiry') + '</span>' +
          '<h3 style="font-family: var(--iva-font-serif); font-size: 1.15rem; color: #fff; margin: 10px 0 6px;">' + q.question + '</h3>' +
          '<p style="font-size: 0.85rem; color: var(--iva-text-secondary); margin-bottom: 12px;">' + (q.mystery || q.simple).slice(0, 110) + '...</p>' +
          '<button type="button" class="iva-btn iva-btn-primary iva-btn-small">Explore Inquiry →</button>';
        card.querySelector('button').onclick = function() { openCuriosity(q.id, q); };
        resultsGrid.appendChild(card);
      });
    }

    resultsWrap.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // ════════════════════════════════════════════════════════════════
  // 10. SPARK AN ORIGINAL QUESTION STUDIO (Section 17)
  // ════════════════════════════════════════════════════════════════
  function rerollConcepts() {
    var shuffled = CONCEPT_SPARKS.slice().sort(function() { return 0.5 - Math.random(); });
    document.getElementById('ivaSparkConcept1').textContent = shuffled[0];
    document.getElementById('ivaSparkConcept2').textContent = shuffled[1];
    document.getElementById('ivaSparkConcept3').textContent = shuffled[2];
    document.getElementById('ivaSparkResponseBox').style.display = 'none';
  }

  function analyzeOriginalQuestion() {
    var text = document.getElementById('ivaSparkTextarea').value.trim();
    if (!text) {
      showToast("⚠️", "Please write your question first!");
      return;
    }
    var c1 = document.getElementById('ivaSparkConcept1').textContent;
    var c2 = document.getElementById('ivaSparkConcept2').textContent;
    var c3 = document.getElementById('ivaSparkConcept3').textContent;

    var responseBox = document.getElementById('ivaSparkResponseBox');
    var contentBox = document.getElementById('ivaSparkAnalysisContent');
    responseBox.style.display = 'block';

    contentBox.innerHTML = "<p>Connecting <strong>" + c1 + "</strong>, <strong>" + c2 + "</strong>, and <strong>" + c3 + "</strong> is a hallmark of polymathic thinking. In nature, boundary questions reveal emergent mechanisms—such as how physical energy gradients shape biological organization. Your question has been registered in your intellectual journey.</p>";

    if (appState.sparkQuestions.indexOf(text) === -1) {
      appState.sparkQuestions.push(text);
      saveState();
      updateMilestones();
    }
    playSynthChord('milestone');
    showToast("✨", "Brilliant synthesis! Question analyzed.");
  }

  // ════════════════════════════════════════════════════════════════
  // 11. "I'M BORED" 3-MODE ENGINE (Section 18)
  // ════════════════════════════════════════════════════════════════
  function rollBoredChallenge() {
    var mode = appState.boredMode || 'observe';
    var pool = BORED_MODES[mode] || BORED_MODES.observe;
    var challenge = pool[Math.floor(Math.random() * pool.length)];
    document.getElementById('ivaBoredChallengeText').textContent = challenge;
  }

  // ════════════════════════════════════════════════════════════════
  // 12. STRANGE FACTS ENGINE (Section 19)
  // ════════════════════════════════════════════════════════════════
  var currentFactIndex = 0;
  function rollStrangeFact() {
    currentFactIndex = (currentFactIndex + 1) % STRANGE_FACTS.length;
    var f = STRANGE_FACTS[currentFactIndex];
    document.getElementById('ivaStrangeFactText').textContent = f.fact;
    document.getElementById('ivaStrangeWhyContent').textContent = f.why;
    document.getElementById('ivaStrangeWhyBox').style.display = 'none';
  }

  // ════════════════════════════════════════════════════════════════
  // 13. SAVED DISCOVERIES (Section 24)
  // ════════════════════════════════════════════════════════════════
  function renderSavedView(filterCategory) {
    var grid = document.getElementById('ivaSavedGrid');
    var empty = document.getElementById('ivaSavedEmptyState');
    grid.innerHTML = '';

    var filtered = appState.savedIds.filter(function(id) {
      if (!filterCategory || filterCategory === 'all') return true;
      return id.indexOf(filterCategory) !== -1;
    });

    if (filtered.length === 0) {
      empty.style.display = 'block';
      grid.style.display = 'none';
    } else {
      empty.style.display = 'none';
      grid.style.display = 'grid';

      filtered.forEach(function(sid) {
        var q = getQuestionById(sid);
        var card = document.createElement('div');
        card.className = 'iva-saved-item';
        
        var reflectionText = appState.reflections[sid] ? '<div style="margin: 8px 0; font-size: 0.85rem; color: var(--iva-gold-light); font-style: italic;">Your note: "' + appState.reflections[sid] + '"</div>' : '';

        card.innerHTML = '<span class="iva-badge ' + (q.badgeClass || 'iva-badge-space') + '">' + (q.categoryLabel || 'Inquiry') + '</span>' +
          '<h3 style="font-family: var(--iva-font-serif); font-size: 1.15rem; color: #fff; margin: 10px 0 6px;">' + q.question + '</h3>' +
          reflectionText +
          '<div style="display: flex; gap: 8px; justify-content: space-between; align-items: center; margin-top: 14px;">' +
            '<button type="button" class="iva-btn iva-btn-primary iva-btn-small iva-open-saved-btn">Explore →</button>' +
            '<button type="button" class="iva-btn iva-btn-secondary iva-btn-small iva-unsave-btn" style="color: #ef4444; border-color: rgba(239, 68, 68, 0.3);">Remove</button>' +
          '</div>';

        card.querySelector('.iva-open-saved-btn').onclick = function() { openCuriosity(q.id, q); };
        card.querySelector('.iva-unsave-btn').onclick = function() {
          toggleBookmark(q.id);
          renderSavedView(filterCategory);
        };

        grid.appendChild(card);
      });
    }
  }

  // ════════════════════════════════════════════════════════════════
  // 14. MY CURIOSITY JOURNEY & MILESTONES (Section 23, 42)
  // ════════════════════════════════════════════════════════════════
  function updateMilestones() {
    var exploredCount = appState.exploredIds.length;
    var refCount = Object.keys(appState.reflections).length;
    var savedCount = appState.savedIds.length;
    var sparkCount = appState.sparkQuestions.length;

    // Subbar Updates
    var nextGoal = 5;
    var rankTitle = "First Spark";
    if (exploredCount >= 30) { rankTitle = "First-Principles Thinker 🏛️"; nextGoal = 50; }
    else if (exploredCount >= 15) { rankTitle = "Cosmic Thinker 🌌"; nextGoal = 30; }
    else if (exploredCount >= 5) { rankTitle = "Active Observer 🔭"; nextGoal = 15; }

    var pct = Math.min(100, Math.round((exploredCount / nextGoal) * 100));
    var fillEl = document.getElementById('ivaProgressBarFill');
    var labelEl = document.getElementById('ivaLearnerExploredLabel');
    var titleEl = document.getElementById('ivaLearnerMilestoneTitle');
    var streakEl = document.getElementById('ivaStreakCount');
    var savedBadge = document.getElementById('ivaSavedBadge');

    if (fillEl) fillEl.style.width = pct + "%";
    if (labelEl) labelEl.textContent = exploredCount + " / " + nextGoal + " Inquiries";
    if (titleEl) titleEl.textContent = rankTitle;
    if (streakEl) streakEl.textContent = appState.streak + (appState.streak === 1 ? " Day" : " Days");
    if (savedBadge) savedBadge.textContent = "(" + savedCount + ")";

    // Journey View Updates
    var jExp = document.getElementById('ivaJourneyExploredCount');
    var jRef = document.getElementById('ivaJourneyReflectionsCount');
    var jSav = document.getElementById('ivaJourneySavedCount');
    var jStr = document.getElementById('ivaJourneyStreakDisplay');

    if (jExp) jExp.textContent = exploredCount;
    if (jRef) jRef.textContent = refCount;
    if (jSav) jSav.textContent = savedCount;
    if (jStr) jStr.textContent = appState.streak + (appState.streak === 1 ? " Day" : " Days");

    var milestonesGrid = document.getElementById('ivaMilestonesGrid');
    if (milestonesGrid) {
      milestonesGrid.innerHTML = '';
      MILESTONES.forEach(function(m) {
        var unlocked = false;
        if (m.type === 'explored' && exploredCount >= m.threshold) unlocked = true;
        if (m.type === 'reflection' && refCount >= m.threshold) unlocked = true;
        if (m.type === 'spark' && sparkCount >= m.threshold) unlocked = true;

        var mCard = document.createElement('div');
        mCard.className = 'iva-milestone-card' + (unlocked ? ' unlocked' : '');
        mCard.innerHTML = '<div class="iva-milestone-icon">' + m.icon + '</div>' +
          '<div>' +
            '<div class="iva-milestone-title">' + m.title + (unlocked ? ' ✓' : '') + '</div>' +
            '<div class="iva-milestone-desc">' + m.desc + '</div>' +
          '</div>';
        milestonesGrid.appendChild(mCard);
      });
    }
  }

  // ════════════════════════════════════════════════════════════════
  // 15. INSIGHT CARD PNG EXPORTER
  // ════════════════════════════════════════════════════════════════
  function generateInsightCardPng(q, thought) {
    var canvas = document.getElementById('ivaExportCardCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = 640;
    var h = canvas.height = 420;

    // Dark gradient canvas
    var grad = ctx.createLinearGradient(0, 0, w, h);
    grad.addColorStop(0, '#0c1222');
    grad.addColorStop(1, '#060913');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Gold frame
    ctx.strokeStyle = '#b38642';
    ctx.lineWidth = 3;
    ctx.strokeRect(18, 18, w - 36, h - 36);

    // Title Header
    ctx.fillStyle = '#b38642';
    ctx.font = 'bold 12px system-ui, sans-serif';
    ctx.fillText("IKSHVAKU CURIOSITY MACHINE • EDUCATION BEYOND COMMERCE", 38, 50);

    // Category
    ctx.fillStyle = '#00d2ff';
    ctx.font = 'bold 11px system-ui, sans-serif';
    ctx.fillText((q.categoryLabel || "ASTROPHYSICS").toUpperCase(), 38, 72);

    // Question
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 20px Newsreader, Georgia, serif';
    wrapCanvasText(ctx, q.question, 38, 110, w - 76, 28);

    // Divider
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(38, 200);
    ctx.lineTo(w - 38, 200);
    ctx.stroke();

    // Student Thought
    ctx.fillStyle = '#d4a964';
    ctx.font = 'italic 13px system-ui, sans-serif';
    ctx.fillText("Student Hypothesis & Reflection:", 38, 230);

    ctx.fillStyle = '#e2e8f0';
    ctx.font = '14px system-ui, sans-serif';
    var thoughtStr = thought || q.simple;
    wrapCanvasText(ctx, '"' + thoughtStr + '"', 38, 260, w - 76, 22);

    // Footer
    ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
    ctx.font = '11px system-ui, sans-serif';
    ctx.fillText("Ikshvaku Vidya Academy • A Place for Curious Minds", 38, 385);
  }

  function wrapCanvasText(ctx, text, x, y, maxWidth, lineHeight) {
    var words = String(text).split(' ');
    var line = '';
    for (var n = 0; n < words.length; n++) {
      var testLine = line + words[n] + ' ';
      var metrics = ctx.measureText(testLine);
      if (metrics.width > maxWidth && n > 0) {
        ctx.fillText(line, x, y);
        line = words[n] + ' ';
        y += lineHeight;
      } else {
        line = testLine;
      }
    }
    ctx.fillText(line, x, y);
  }

  // ════════════════════════════════════════════════════════════════
  // 16. TOAST NOTIFICATIONS
  // ════════════════════════════════════════════════════════════════
  var toastTimer = null;
  function showToast(icon, msg) {
    var toast = document.getElementById('ivaToast');
    if (!toast) return;
    document.getElementById('ivaToastIcon').textContent = icon || "✨";
    document.getElementById('ivaToastMessage').textContent = msg;
    toast.classList.remove('iva-hidden');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function() {
      toast.classList.add('iva-hidden');
    }, 3200);
  }

  // ════════════════════════════════════════════════════════════════
  // 17. INITIALIZATION & EVENT LISTENERS
  // ════════════════════════════════════════════════════════════════
  function init() {
    loadState();
    initCosmicCanvas();
    initSimulator();
    initDailyCuriosity();
    rerollConcepts();
    rollBoredChallenge();
    rollStrangeFact();
    updateMilestones();

    // Render Disciplines Grid
    var catGrid = document.getElementById('ivaCategoriesGrid');
    if (catGrid) {
      catGrid.innerHTML = '';
      CATEGORIES.forEach(function(cat, idx) {
        var card = document.createElement('button');
        card.type = 'button';
        card.className = 'iva-cat-card';
        card.innerHTML = '<div class="iva-cat-top">' +
          '<span class="iva-cat-icon">' + cat.icon + '</span>' +
          '<span class="iva-cat-name">' + cat.label + '</span>' +
          '</div>' +
          '<div class="iva-cat-desc">' + cat.desc + '</div>' +
          '<div class="iva-cat-action">Enter Inquiries →</div>';

        card.addEventListener('click', function() {
          var sampleQ = FLAGSHIP_INQUIRIES.find(function(q) { return q.category === cat.key; });
          if (!sampleQ) sampleQ = generateProceduralQuestion(idx * 62500);
          openCuriosity(sampleQ.id, sampleQ);
        });

        catGrid.appendChild(card);
      });
    }

    // Navigation Buttons
    document.getElementById('ivaBrandHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaNavHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaBackToHomeBtn').onclick = function() { showView('ivaHomeView'); };

    // Primary CTA
    document.getElementById('ivaHeroCuriousBtn').onclick = function() {
      var randIndex = Math.floor(Math.random() * FLAGSHIP_INQUIRIES.length);
      var q = FLAGSHIP_INQUIRIES[randIndex];
      openCuriosity(q.id, q);
    };

    // Surprise Me
    var handleSurprise = function() {
      var rand = Math.floor(Math.random() * (FLAGSHIP_INQUIRIES.length + 5000));
      var q = rand < FLAGSHIP_INQUIRIES.length ? FLAGSHIP_INQUIRIES[rand] : generateProceduralQuestion(rand);
      openCuriosity(q.id, q);
    };
    document.getElementById('ivaNavSurpriseBtn').onclick = handleSurprise;
    document.getElementById('ivaHeroSurpriseBtn').onclick = handleSurprise;

    // Bored Mode
    var openBored = function() {
      rollBoredChallenge();
      showView('ivaBoredView');
    };
    document.getElementById('ivaNavBoredBtn').onclick = openBored;
    document.getElementById('ivaHeroBoredBtn').onclick = openBored;
    document.getElementById('ivaBoredBackHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaNextBoredBtn').onclick = rollBoredChallenge;
    document.getElementById('ivaBoredExploreBtn').onclick = handleSurprise;

    // Bored Mode Tabs
    document.getElementById('ivaBoredModeObserve').onclick = function() {
      appState.boredMode = 'observe';
      updateBoredModeTabs();
    };
    document.getElementById('ivaBoredModeThink').onclick = function() {
      appState.boredMode = 'think';
      updateBoredModeTabs();
    };
    document.getElementById('ivaBoredModeDo').onclick = function() {
      appState.boredMode = 'do';
      updateBoredModeTabs();
    };
    function updateBoredModeTabs() {
      document.getElementById('ivaBoredModeObserve').classList.toggle('active', appState.boredMode === 'observe');
      document.getElementById('ivaBoredModeThink').classList.toggle('active', appState.boredMode === 'think');
      document.getElementById('ivaBoredModeDo').classList.toggle('active', appState.boredMode === 'do');
      rollBoredChallenge();
    }

    // Strange Facts
    var openStrange = function() {
      rollStrangeFact();
      showView('ivaStrangeView');
    };
    document.getElementById('ivaNavStrangeBtn').onclick = openStrange;
    document.getElementById('ivaStrangeBackHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaNextStrangeBtn').onclick = rollStrangeFact;
    document.getElementById('ivaStrangeWhyBtn').onclick = function() {
      document.getElementById('ivaStrangeWhyBox').style.display = 'block';
    };
    document.getElementById('ivaStrangeExploreRelatedBtn').onclick = function() {
      var f = STRANGE_FACTS[currentFactIndex];
      openCuriosity(f.relatedId);
    };

    // Random Walk
    document.getElementById('ivaHeroRandomWalkBtn').onclick = triggerRandomWalk;

    // Saved View
    document.getElementById('ivaNavSavedBtn').onclick = function() {
      renderSavedView('all');
      showView('ivaSavedView');
    };
    document.getElementById('ivaSavedBackHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaSavedExploreNowBtn').onclick = handleSurprise;

    document.querySelectorAll('#ivaSavedCategoryFilterChips .iva-chip').forEach(function(chip) {
      chip.onclick = function() {
        renderSavedView(this.getAttribute('data-filter'));
      };
    });

    // Journey View
    document.getElementById('ivaNavJourneyBtn').onclick = function() {
      updateMilestones();
      showView('ivaJourneyView');
    };
    document.getElementById('ivaJourneyBackHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaStreakPill').onclick = function() {
      updateMilestones();
      showView('ivaJourneyView');
    };

    // Sound Toggle
    document.getElementById('ivaSoundToggleBtn').onclick = function() {
      appState.soundEnabled = !appState.soundEnabled;
      saveState();
      this.textContent = appState.soundEnabled ? "🔊 Sound" : "🔇 Muted";
      showToast(appState.soundEnabled ? "🔊" : "🔇", appState.soundEnabled ? "Sound enabled" : "Sound muted");
    };

    // About Modal
    document.getElementById('ivaNavAboutBtn').onclick = function() {
      document.getElementById('ivaAboutModalOverlay').classList.remove('iva-hidden');
    };
    document.getElementById('ivaAboutCloseBtn').onclick = function() {
      document.getElementById('ivaAboutModalOverlay').classList.add('iva-hidden');
    };
    document.getElementById('ivaAboutGotItBtn').onclick = function() {
      document.getElementById('ivaAboutModalOverlay').classList.add('iva-hidden');
    };

    // Search input
    var searchTimer = null;
    document.getElementById('ivaSearchInput').oninput = function(e) {
      clearTimeout(searchTimer);
      var val = e.target.value;
      searchTimer = setTimeout(function() { performSearch(val); }, 250);
    };
    document.getElementById('ivaClearSearchBtn').onclick = function() {
      document.getElementById('ivaSearchInput').value = '';
      document.getElementById('ivaSearchResultsWrap').style.display = 'none';
    };
    document.querySelectorAll('.iva-search-chips .iva-chip').forEach(function(chip) {
      chip.onclick = function() {
        var term = this.getAttribute('data-search');
        document.getElementById('ivaSearchInput').value = term;
        performSearch(term);
      };
    });

    // Think Gate Lock Button
    document.getElementById('ivaLockIdeaBtn').onclick = function() {
      var val = document.getElementById('ivaThinkInput').value.trim();
      if (!val) {
        showToast("💡", "Take a guess first!");
        return;
      }
      if (appState.currentQuestionId) {
        appState.reflections[appState.currentQuestionId] = val;
        saveState();
        updateMilestones();
        document.getElementById('ivaThinkFeedback').textContent = "Interesting thought. Let's see what is actually happening.";
        document.getElementById('ivaThinkFeedback').style.display = "block";
        playSynthChord('discover');
        showToast("💡", "Hypothesis locked into your intellectual record!");
      }
      document.getElementById('ivaExplanationContainer').scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    // 3-Level Tabs
    document.getElementById('ivaTabLevel1').onclick = function() { setExplanationLevel(1); };
    document.getElementById('ivaTabLevel2').onclick = function() { setExplanationLevel(2); };
    document.getElementById('ivaTabLevel3').onclick = function() { setExplanationLevel(3); };

    // What If Predict Button
    document.getElementById('ivaWhatIfPredictBtn').onclick = function() {
      document.getElementById('ivaWhatIfRevealBox').style.display = "block";
      this.style.display = "none";
      playSynthChord('discover');
    };

    // Bookmark Action in Detail
    document.getElementById('ivaBookmarkBtn').onclick = function() {
      if (appState.currentQuestionId) toggleBookmark(appState.currentQuestionId);
    };

    // Share Button
    document.getElementById('ivaShareBtn').onclick = function() {
      var url = window.location.href.split('#')[0] + "#" + appState.currentQuestionId;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function() {
          showToast("📋", "Inquiry link copied to clipboard!");
        });
      } else {
        prompt("Copy direct link:", url);
      }
    };

    // Zen Mode
    document.getElementById('ivaZenModeBtn').onclick = function() {
      var isZen = document.body.classList.toggle('iva-zen-active');
      this.textContent = isZen ? "☀️ Exit Focus" : "🌙 Focus Mode";
      showToast(isZen ? "🌙" : "☀️", isZen ? "Focus mode enabled" : "Standard mode restored");
    };

    // Final Discovery: Make Me Curious Again
    document.getElementById('ivaCuriousAgainBtn').onclick = handleSurprise;

    // Export Card Modal
    document.getElementById('ivaExportCardBtn').onclick = function() {
      if (!appState.currentQuestionObj) return;
      var thought = document.getElementById('ivaThinkInput').value.trim();
      generateInsightCardPng(appState.currentQuestionObj, thought);
      document.getElementById('ivaCardModalOverlay').classList.remove('iva-hidden');
    };
    document.getElementById('ivaCardModalCloseBtn').onclick = function() {
      document.getElementById('ivaCardModalOverlay').classList.add('iva-hidden');
    };
    document.getElementById('ivaCardDoneBtn').onclick = function() {
      document.getElementById('ivaCardModalOverlay').classList.add('iva-hidden');
    };
    document.getElementById('ivaDownloadCardPngBtn').onclick = function() {
      var canvas = document.getElementById('ivaExportCardCanvas');
      var a = document.createElement('a');
      a.download = 'Ikshvaku-Curiosity-' + (appState.currentQuestionId || 'Inquiry') + '.png';
      a.href = canvas.toDataURL('image/png');
      a.click();
      showToast("📥", "Insight Card downloaded!");
    };

    // Simulator Slider
    var simSlider = document.getElementById('ivaSimSlider');
    if (simSlider) {
      simSlider.oninput = function(e) {
        var v = parseInt(e.target.value, 10);
        document.getElementById('ivaSimSliderVal').textContent = v + "%";
        simSpeed = 0.005 + (v * 0.0006);
      };
    }

    // Spark Studio Listeners
    document.getElementById('ivaRerollSparksBtn').onclick = rerollConcepts;
    document.getElementById('ivaAnalyzeSparkBtn').onclick = analyzeOriginalQuestion;
    document.getElementById('ivaSaveSparkToJournalBtn').onclick = function() {
      showToast("🔖", "Original inquiry saved to your curiosity journey!");
    };

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        document.getElementById('ivaCardModalOverlay').classList.add('iva-hidden');
        document.getElementById('ivaAboutModalOverlay').classList.add('iva-hidden');
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
"""

print("Writing standalone HTML component: curiosity-machine.html...")
standalone_file = f"""<style>/*<![CDATA[*/
{master_css}
/*]]>*/</style>

{master_html}

<script type="text/javascript">//<![CDATA[
{master_js}
//]]></script>
"""
with open('curiosity-machine.html', 'w', encoding='utf-8') as f:
    f.write(standalone_file)

with open('curiosity-page.html', 'w', encoding='utf-8') as f:
    f.write(standalone_file)

print(f"Wrote curiosity-machine.html and curiosity-page.html ({len(standalone_file)} bytes)")

# Build Standalone 100% Blogger XML Theme
blogger_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='1' b:layoutsversion='3' b:responsive='true' expr:dir='data:blog.languageDirection' expr:lang='data:blog.locale' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
  <meta charset='UTF-8'/>
  <meta content='width=device-width, initial-scale=1.0, maximum-scale=5.0' name='viewport'/>
  <title>Ikshvaku Curiosity Machine — Don't Just Learn. Get Curious.</title>
  
  <b:include data='blog' name='all-head-content'/>

  <!-- Primary Meta Tags -->
  <meta content="Ikshvaku Curiosity Machine — Don't Just Learn. Get Curious." name='title'/>
  <meta content='A dedicated interactive learning sanctuary for first-principles thinking, childlike wonder, and deep scientific inquiry. Created by Ikshvaku Vidya Academy.' name='description'/>
  <meta content='#071b36' name='theme-color'/>

  <!-- Typography: Newsreader, JetBrains Mono, Plus Jakarta Sans -->
  <link href='https://fonts.googleapis.com' rel='preconnect'/>
  <link crossorigin='anonymous' href='https://fonts.gstatic.com' rel='preconnect'/>
  <link href='https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap' rel='stylesheet'/>

  <b:skin><![CDATA[
/* Reset & Base Canvas */
html, body {{
  margin: 0;
  padding: 0;
  background: #060913;
  color: #f8fafc;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}}

{master_css}
  ]]></b:skin>
</head>
<body>

{master_html}

  <!-- Minimal Required Blogger Section for 100% Strict Schema Validation -->
  <div style='display: none;'>
    <b:section class='main-section' id='main' showaddelement='no'>
      <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' version='1'>
        <b:includable id='main'>
          <b:loop values='data:posts' var='post'>
            <article>
              <h2><data:post.title/></h2>
              <div><data:post.body/></div>
            </article>
          </b:loop>
        </b:includable>
      </b:widget>
    </b:section>
  </div>

  <script type='text/javascript'>
  //<![CDATA[
{master_js}
  //]]>
  </script>
</body>
</html>"""

# XML Validation
try:
    ET.fromstring(blogger_xml)
    print("SUCCESS: blogger_xml passes strict XML validation with 0 errors!")
    with open('curiosity-theme.xml', 'w', encoding='utf-8') as f:
        f.write(blogger_xml)
    with open('blogger-template.xml', 'w', encoding='utf-8') as f:
        f.write(blogger_xml)
    print(f"Wrote curiosity-theme.xml and blogger-template.xml ({len(blogger_xml)} bytes)")
except ET.ParseError as e:
    print("ERROR in XML validation:", e)
    l, c = e.position
    lines = blogger_xml.splitlines()
    for i in range(max(0, l-5), min(len(lines), l+5)):
        print(f"{i+1}: {lines[i]}")
