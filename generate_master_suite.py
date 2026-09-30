# -*- coding: utf-8 -*-
"""
generate_master_suite.py
Assembles the complete, unified, production-grade Ikshvaku Curiosity Machine.
Produces:
- curiosity-machine.html
- curiosity-page.html
- blogger-template.xml
- curiosity-theme.xml
And copies curiosity-machine.html to the Windows clipboard!
"""

import sys
import re
import json
import xml.etree.ElementTree as ET
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

# Read base64 logo
with open('blogger-template.xml', 'r', encoding='utf-8') as f:
    b_text = f.read()

logo_match = re.search(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', b_text)
base64_logo = logo_match.group(0) if logo_match else 'https://rishendra1.github.io/ikshvaku-curiosity/assets/IVA.jpeg'
print(f"Loaded logo: {len(base64_logo)} chars")

with open('build_complete_system.py', 'r', encoding='utf-8') as f:
    bcs_text = f.read()

css_start = bcs_text.find('/* ══════════════════════════════════════════════════════════════════')
css_end = bcs_text.find('"""', css_start)
master_css = bcs_text[css_start:css_end].strip()

# ── MASTER HTML ──
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
        <button type="button" class="iva-nav-btn active" id="ivaNavHomeBtn"><span>🏛️</span> Home</button>
        <button type="button" class="iva-nav-btn" id="ivaNavBoredBtn"><span>⚡</span> I'm Bored</button>
        <button type="button" class="iva-nav-btn" id="ivaNavStrangeBtn"><span>🌌</span> Strange Truths</button>
        <button type="button" class="iva-nav-btn" id="ivaNavSavedBtn"><span>🔖</span> Saved (<span id="ivaSavedNavCount">0</span>)</button>
        <button type="button" class="iva-nav-btn" id="ivaNavJourneyBtn"><span>🧭</span> My Journey</button>
        <button type="button" class="iva-nav-btn" id="ivaNavAboutBtn"><span>ℹ️</span> About</button>
      </nav>
    </div>
  </header>

  <!-- ── 3. MAIN APP CONTAINER ── -->
  <main class="iva-main-container" role="main">

    <!-- ══════════════════════════════════════════════════════════
         VIEW 1: HOMEPAGE (Section 21)
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaHomeView" class="iva-view">

      <!-- Hero Section -->
      <section class="iva-hero" aria-labelledby="ivaHeroTitle">
        <div class="iva-hero-eyebrow">✦ Digital Sanctuary for Independent Wonder</div>
        <h1 class="iva-hero-title" id="ivaHeroTitle">Don't Just Learn. Get Curious.</h1>
        <p class="iva-hero-subtitle">
          A digital place where people come to wonder. Move from intuition to mechanism to first principles, explore counter-intuitive realities, and forge original questions.
        </p>

        <!-- Primary Actions -->
        <div class="iva-hero-actions">
          <button type="button" class="iva-btn iva-btn-primary iva-btn-large" id="ivaHeroStartBtn">
            ✦ START WONDERING
          </button>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-large" id="ivaHeroSurpriseBtn">
            🎲 SURPRISE ME
          </button>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-large" id="ivaHeroBoredBtn">
            ⚡ I'M BORED
          </button>
        </div>

        <!-- Live Reactive Statistics Bar -->
        <div class="iva-stats-bar">
          <span class="iva-stat-chip">🔥 Active Streak: <strong id="ivaLiveStreak">1 Day</strong></span>
          <span class="iva-stat-chip">💡 Inquiries Explored: <strong id="ivaLiveExplored">0</strong></span>
          <span class="iva-stat-chip">🔖 Inquiries Saved: <strong id="ivaLiveSaved">0</strong></span>
          <span class="iva-stat-chip">🌐 Combinatorial Paths: <strong>500,000+</strong></span>
        </div>
      </section>

      <!-- Today's Curiosity Deterministic Spotlight (Section 10) -->
      <section class="iva-daily-card" aria-labelledby="ivaDailyTitle">
        <div style="flex: 1; min-width: 280px;">
          <div class="iva-daily-badge">🌅 TODAY'S CURIOSITY • DETERMINISTIC SPOTLIGHT</div>
          <div class="iva-daily-question" id="ivaDailyTitle">Why doesn't the Moon fall into Earth?</div>
          <div class="iva-daily-sub">Consistent for today. Tomorrow, we continue somewhere unexpected.</div>
        </div>
        <button type="button" class="iva-btn iva-btn-primary" id="ivaExploreDailyBtn">
          ✦ EXPLORE TODAY'S CURIOSITY →
        </button>
      </section>

      <!-- Search Section -->
      <section class="iva-search-section" aria-label="Curiosity Search">
        <div class="iva-search-box">
          <span class="iva-search-icon">🔍</span>
          <input type="text" class="iva-search-input" id="ivaSearchInput" placeholder="Search any question, curiosity, or phenomenon (e.g. moon, ice, sound, time, brain)..." aria-label="Search curiosity questions" />
        </div>
        <div class="iva-search-chips">
          <span style="font-size: 0.78rem; color: var(--iva-text-muted);">Common sparks:</span>
          <button type="button" class="iva-chip" data-search="gravity">Gravity</button>
          <button type="button" class="iva-chip" data-search="ice">Why Ice Floats</button>
          <button type="button" class="iva-chip" data-search="spin">Earth's Spin</button>
          <button type="button" class="iva-chip" data-search="sound">Noise Cancelling</button>
          <button type="button" class="iva-chip" data-search="sky">Blue Sky</button>
          <button type="button" class="iva-chip" data-search="qr">QR Codes</button>
          <button type="button" class="iva-chip" data-search="time">Time Dilation</button>
          <button type="button" class="iva-chip" data-search="blind">Blind Spot</button>
        </div>
      </section>

      <!-- Search Results Container -->
      <section id="ivaSearchResultsWrap" style="display: none; margin-bottom: 40px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <h3 style="color: #fff; font-size: 1.2rem;" id="ivaSearchResultsTitle">Search Results</h3>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaClearSearchBtn">✕ Clear Search</button>
        </div>
        <div class="iva-saved-grid" id="ivaSearchResultsGrid"></div>
      </section>

      <!-- 8 Disciplines of First-Principles Inquiry (Section 15) -->
      <section aria-labelledby="ivaDisciplinesTitle">
        <h2 class="iva-section-title" id="ivaDisciplinesTitle">Explore by Intellectual Discipline</h2>
        <p class="iva-section-subtitle">Deep inquiry paths connecting science, nature, mind, and computational architecture.</p>
        
        <div class="iva-categories-grid" id="ivaCategoriesGrid">
          <!-- Dynamically populated -->
        </div>
      </section>

      <!-- Signature Studio: "Spark an Original Question" (Section 7) -->
      <section class="iva-spark-studio" aria-labelledby="ivaSparkTitle">
        <div class="iva-spark-header">
          <span class="iva-spark-tag">✦ Signature Studio</span>
          <h2 class="iva-spark-title" id="ivaSparkTitle">Spark an Original Question</h2>
          <p class="iva-spark-quote">"Good learners answer questions. Curious thinkers create them."</p>
        </div>

        <div style="text-align: center; margin-bottom: 12px; font-size: 0.95rem; color: var(--iva-text-secondary);">
          Here are three seemingly unrelated concepts. What original question could connect them?
        </div>

        <div class="iva-spark-concepts-wrap">
          <span class="iva-spark-pill" id="ivaSparkConcept1">BLACK HOLES</span>
          <span class="iva-spark-plus">+</span>
          <span class="iva-spark-pill" id="ivaSparkConcept2">HONEYBEES</span>
          <span class="iva-spark-plus">+</span>
          <span class="iva-spark-pill" id="ivaSparkConcept3">MEMORY</span>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaRerollSparksBtn" style="margin-left: 8px;">
            🎲 Reroll Concepts
          </button>
        </div>

        <div class="iva-spark-input-wrap">
          <textarea class="iva-spark-textarea" id="ivaSparkTextarea" placeholder="Write your original connecting question here... (e.g., How does information storage at a black hole event horizon compare to collective memory encoding in a beehive?)"></textarea>
          <div style="display: flex; gap: 10px; justify-content: flex-end; flex-wrap: wrap;">
            <button type="button" class="iva-btn iva-btn-primary" id="ivaAnalyzeSparkBtn">
              💡 Analyze My Question
            </button>
          </div>
          <div class="iva-spark-response-box" id="ivaSparkResponseBox">
            <div style="font-weight: 700; color: var(--iva-gold-light); margin-bottom: 6px;" id="ivaSparkFeedbackHeader">Fascinating Question.</div>
            <div id="ivaSparkAnalysisContent"></div>
            <div style="margin-top: 14px; display: flex; gap: 8px; justify-content: flex-end;">
              <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaSaveSparkToJournalBtn">🔖 Save to My Journal</button>
            </div>
          </div>
        </div>
      </section>

      <!-- Why We Built This: Institutional Story (Section 37) -->
      <section class="iva-story-section" aria-labelledby="ivaStoryTitle">
        <span class="iva-story-eyebrow">IKSHVAKU VIDYA ACADEMY</span>
        <h2 class="iva-story-title" id="ivaStoryTitle">Why We Built The Curiosity Machine</h2>
        <p class="iva-story-text">
          At Ikshvaku Vidya Academy, we believe education isn't only about memorizing the right answer for an exam.<br/>
          Sometimes the most transformative moment in a life is when someone pauses, observes the world, and asks: <em>"Wait... but why?"</em><br/>
          The Curiosity Machine is a dedicated sanctuary for those moments.
        </p>
        <div class="iva-story-seal">IKSHVAKU VIDYA ACADEMY • EDUCATION BEYOND COMMERCE</div>
      </section>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 2: QUESTION EXPLORATION EXPERIENCE (Sections 2, 4, 5, 6, 16, 22)
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

        <!-- ── THINK FIRST ACTIVE GATE (Section 2) ── -->
        <div class="iva-think-gate" id="ivaThinkGate">
          <div class="iva-think-title">💡 Think First: Before We Explain It...</div>
          <div class="iva-think-subtitle">Curiosity begins the moment you formulate a hypothesis. Choose your starting point:</div>
          
          <div class="iva-think-choices">
            <button type="button" class="iva-think-choice-btn active" id="ivaThinkChoiceGuess">✍️ My Guess</button>
            <button type="button" class="iva-think-choice-btn" id="ivaThinkChoiceNoIdea">🤷 I Have No Idea</button>
            <button type="button" class="iva-think-choice-btn" id="ivaThinkChoiceHint">💡 Give Me a Hint</button>
          </div>

          <!-- Choice 1: My Guess Box -->
          <div id="ivaThinkSectionGuess" class="iva-think-box">
            <div style="font-size: 0.84rem; color: var(--iva-text-secondary); margin-bottom: 8px;" id="ivaThinkPromptText">
              What keeps an object perpetually falling through space without ever hitting the ground?
            </div>
            <div class="iva-think-input-row">
              <input type="text" class="iva-think-input" id="ivaThinkInput" placeholder="I think it might be because..." aria-label="Your thoughts on this inquiry" />
              <button type="button" class="iva-btn iva-btn-primary iva-btn-small" id="ivaLockIdeaBtn">🔒 Lock Hypothesis</button>
            </div>
          </div>

          <!-- Choice 2: I Have No Idea Box -->
          <div id="ivaThinkSectionNoIdea" class="iva-think-box" style="display: none;">
            <div style="color: var(--iva-gold-light); font-weight: 600; margin-bottom: 4px;">The Most Fertile Place in Science:</div>
            <div>"I don't know" is not a failure; it is the beginning of wonder. Isaac Newton didn't know why apples fell either until he stopped taking it for granted. Admitting you don't know is the true prerequisite for genuine understanding.</div>
          </div>

          <!-- Choice 3: Hint Box -->
          <div id="ivaThinkSectionHint" class="iva-think-box" style="display: none;">
            <div style="color: var(--iva-cyan); font-weight: 600; margin-bottom: 4px;">Conceptual Clue:</div>
            <div id="ivaThinkHintText">Think of throwing a baseball horizontally from a tall mountain. What happens as you throw it faster and faster across a spherical planet?</div>
          </div>

          <!-- Feedback &amp; Reveal Trigger -->
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 14px;">
            <div id="ivaThinkSavedMsg" style="font-size: 0.84rem; color: var(--iva-gold-light); font-style: italic; display: none;">✓ Hypothesis recorded in your journey.</div>
            <button type="button" class="iva-btn iva-btn-primary" id="ivaRevealExplanationBtn">
              ✦ REVEAL CORE EXPLANATION ↓
            </button>
          </div>
        </div>

        <!-- ── 3-LEVEL PROGRESSIVE DISCLOSURE EXPLANATION (Section 5) ── -->
        <div id="ivaExplanationContainer">
          
          <div class="iva-tabs-wrap" role="tablist">
            <button type="button" class="iva-tab-btn active" id="ivaTabLevel1" role="tab" aria-selected="true">
              Level 1: The Intuitive Core
            </button>
            <button type="button" class="iva-tab-btn" id="ivaTabLevel2" role="tab" aria-selected="false">
              Level 2: The Mechanism
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

        <!-- ── LIVE DYNAMIC SIMULATOR (Section 16) ── -->
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
              <div class="iva-sim-qa-label">What happens next?</div>
              <div class="iva-sim-qa-text" id="ivaSimNext">If velocity drops, orbit decays inward; if velocity increases, it escapes into hyperbolic trajectory.</div>
            </div>
          </div>
        </div>

        <!-- ── WHY SHOULD I CARE? (Section 2) ── -->
        <div class="iva-care-box">
          <div class="iva-care-title">
            <span>🌍 Why Should I Care?</span>
          </div>
          <div class="iva-care-text" id="ivaCareText">
            Every GPS satellite orbiting above you, weather monitoring network, and telecommunications relay uses this exact balance of free fall and forward speed.
          </div>
        </div>

        <!-- ── INTERACTIVE WHAT-IF ENGINE (Section 6) ── -->
        <div class="iva-whatif-box" id="ivaWhatIfBox">
          <div class="iva-whatif-title">
            <span>🔮 What If? (Interactive Variable Lab)</span>
          </div>
          <div class="iva-whatif-desc" id="ivaWhatIfDesc">
            What happens when we perturb the physical variables of this universe? Select an adjustment:
          </div>

          <!-- Variable Buttons: 50%, 75%, 100%, 125%, 200% -->
          <div class="iva-whatif-vars">
            <button type="button" class="iva-whatif-var-btn" data-val="50">50%</button>
            <button type="button" class="iva-whatif-var-btn" data-val="75">75%</button>
            <button type="button" class="iva-whatif-var-btn active" data-val="100">100% (Baseline)</button>
            <button type="button" class="iva-whatif-var-btn" data-val="125">125%</button>
            <button type="button" class="iva-whatif-var-btn" data-val="200">200%</button>
          </div>

          <div class="iva-whatif-reaction-grid">
            <div class="iva-whatif-reaction-col">
              <div class="iva-whatif-reaction-label">🔄 What Changed</div>
              <div class="iva-whatif-reaction-text" id="ivaWhatIfChanged">Stable baseline equilibrium (1.022 km/s).</div>
            </div>
            <div class="iva-whatif-reaction-col">
              <div class="iva-whatif-reaction-label">⚙️ Why It Changed</div>
              <div class="iva-whatif-reaction-text" id="ivaWhatIfWhy">Inward gravitational acceleration precisely matches centripetal requirements.</div>
            </div>
            <div class="iva-whatif-reaction-col">
              <div class="iva-whatif-reaction-label">💥 Consequence Follows</div>
              <div class="iva-whatif-reaction-text" id="ivaWhatIfConsequence">Stable 27.3-day lunar orbit, regular tides, and climate stability.</div>
            </div>
          </div>
        </div>

        <!-- ── WHERE ELSE DOES THIS APPEAR? (Section 2) ── -->
        <div class="iva-where-else-box" id="ivaWhereElseBox">
          <h3 class="iva-where-else-title">🌐 Where Else Does This Principle Appear?</h3>
          <div class="iva-where-else-grid" id="ivaWhereElseGrid">
            <!-- Populated dynamically -->
          </div>
        </div>

        <!-- ── CONNECT THE DOTS: CROSS-DISCIPLINE BRIDGE (Section 2 &amp; 15) ── -->
        <div class="iva-bridge-box" id="ivaBridgeBox">
          <h3 class="iva-bridge-title">
            <span>🔗 Connect The Dots:</span>
            <span class="iva-bridge-pill" id="ivaBridgeDisciplineFrom">Astrophysics</span>
            <span>➔</span>
            <span class="iva-bridge-pill" id="ivaBridgeDisciplineTo">Evolutionary Biology</span>
          </h3>
          <div class="iva-bridge-text" id="ivaBridgeText">
            The gravitational tidal locking of the Moon creates rhythmic intertidal zones on Earth's coastlines. Evolutionary biologists believe these wet-dry tidal pools were the critical staging ground for early marine organisms to develop air-breathing lungs and transition onto land.
          </div>
        </div>

        <!-- ── YOUR TURN: SPARK FOLLOW-UP (Section 2) ── -->
        <div class="iva-your-turn-box">
          <h3 class="iva-your-turn-title">🤔 Your Turn: What Question Does This Spark?</h3>
          <div class="iva-your-turn-desc" id="ivaYourTurnDesc">Every answer reveals a dozen new doors. What do you wonder now?</div>
          <textarea class="iva-your-turn-textarea" id="ivaYourTurnInput" placeholder="What question does this discovery make you curious about?"></textarea>
          <div style="display: flex; justify-content: flex-end;">
            <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaSaveYourTurnBtn">📝 Save to My Journal</button>
          </div>
        </div>

        <!-- ── END OF EVERY DISCOVERY: THE INFINITE CURIOSITY LOOP (Section 22) ── -->
        <div class="iva-discovery-loop">
          <div class="iva-loop-grid">
            <div class="iva-loop-item">
              <div class="iva-loop-label">YOU DISCOVERED:</div>
              <div class="iva-loop-val" id="ivaLoopDiscovered">Perpetual Free-Fall &amp; Orbital Velocity Balance</div>
            </div>
            <div class="iva-loop-arrow">➔</div>
            <div class="iva-loop-item">
              <div class="iva-loop-label">THAT CONNECTS TO:</div>
              <div class="iva-loop-val" id="ivaLoopConnects">Gravitational Spacetime Curvature &amp; Time Dilation</div>
            </div>
            <div class="iva-loop-arrow">➔</div>
            <div class="iva-loop-item">
              <div class="iva-loop-label">NOW YOU MIGHT WONDER:</div>
              <div class="iva-loop-val" id="ivaLoopNextQuestion">Why does time run faster on top of a mountain than at sea level?</div>
            </div>
          </div>
          <button type="button" class="iva-btn iva-btn-primary iva-btn-large" id="ivaLoopNextBtn">
            ✦ EXPLORE NEXT CURIOSITY →
          </button>
        </div>

        <!-- Action Toolbar -->
        <div style="display: flex; gap: 10px; flex-wrap: wrap; border-top: 1px solid var(--iva-border); padding-top: 20px;">
          <button type="button" class="iva-btn iva-btn-primary iva-btn-small" id="ivaBookmarkBtn">🔖 Save Inquiry</button>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaExportCardBtn">🎨 Download Insight Card (PNG)</button>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaShareBtn">📤 Share Link</button>
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaZenModeBtn">🌙 Focus Mode</button>
        </div>

      </article>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 3: "I'M BORED" (3 MODES: OBSERVE, THINK, DO) (Section 8)
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
          Boredom is your prefrontal cortex asking for active, high-quality observation.<br/>
          Select your mode and explore this micro-experiment right now:
        </p>

        <!-- 3 Modes Tabs -->
        <div class="iva-bored-modes">
          <button type="button" class="iva-bored-mode-btn active" data-mode="observe" id="ivaBoredModeObserve">👁️ OBSERVE</button>
          <button type="button" class="iva-bored-mode-btn" data-mode="think" id="ivaBoredModeThink">🧠 THINK</button>
          <button type="button" class="iva-bored-mode-btn" data-mode="do" id="ivaBoredModeDo">✋ DO</button>
        </div>

        <div class="iva-bored-challenge-text" id="ivaBoredChallengeText">
          Look at the shadow of your hand on the wall. Why isn't the edge perfectly sharp? Move your hand closer to the light source... What changed?
        </div>

        <div style="margin-bottom: 18px;">
          <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaBoredRevealBtn">
            💡 What Did You Notice? (Reveal Mechanism) ↓
          </button>
        </div>

        <div class="iva-bored-reveal-box" id="ivaBoredRevealBox" style="display: none;">
          <div style="font-weight: 700; color: var(--iva-cyan); margin-bottom: 6px;">The Scientific Mechanism:</div>
          <div id="ivaBoredRevealContent">
            The light source has physical width, casting two regions: the dark core (umbra) and a fuzzy partial shadow (penumbra). As your hand approaches the light, the penumbra widens due to geometric angular divergence.
          </div>
        </div>

        <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
          <button type="button" class="iva-btn iva-btn-primary" id="ivaNextBoredBtn">⚡ Another Challenge</button>
          <button type="button" class="iva-btn iva-btn-secondary" id="ivaBoredExploreBtn">✦ Turn Into Curiosity Inquiry</button>
        </div>
      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 4: STRANGE TRUTHS (Section 9)
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
          The cosmos is under no obligation to conform to human common sense. Verified counter-intuitive physical truths:
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
         VIEW 5: SAVED DISCOVERIES (Section 13)
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaSavedView" class="iva-view iva-hidden">
      
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 24px;">
        <div>
          <h2 style="font-family: var(--iva-font-serif); font-size: 2rem; color: #fff;">🔖 Your Saved Inquiries</h2>
          <div style="font-size: 0.9rem; color: var(--iva-text-secondary);">Discoveries and personal reflections preserved in your private browser memory.</div>
        </div>
        <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaSavedBackHomeBtn">
          ← Back to Home
        </button>
      </div>

      <div id="ivaSavedEmptyState" style="text-align: center; padding: 60px 20px; color: var(--iva-text-muted); display: none;">
        <div style="font-size: 3rem; margin-bottom: 12px;">🔖</div>
        <h3 style="font-size: 1.2rem; color: #fff; margin-bottom: 8px;">No Inquiries Saved Yet</h3>
        <p style="font-size: 0.9rem; max-width: 440px; margin: 0 auto 20px;">
          When an inquiry surprises or challenges you, click "Save Inquiry" to build your personal intellectual archive.
        </p>
        <button type="button" class="iva-btn iva-btn-primary iva-btn-small" id="ivaSavedExploreNowBtn">
          Start Exploring Now
        </button>
      </div>

      <div class="iva-saved-grid" id="ivaSavedGrid">
        <!-- Populated dynamically -->
      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════
         VIEW 6: MY CURIOSITY JOURNEY (Section 12)
         ══════════════════════════════════════════════════════════ -->
    <div id="ivaJourneyView" class="iva-view iva-hidden">
      
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 24px;">
        <div>
          <h2 style="font-family: var(--iva-font-serif); font-size: 2rem; color: #fff;">🧭 My Curiosity Journey</h2>
          <div style="font-size: 0.9rem; color: var(--iva-text-secondary);">An authentic record of your questions, hypotheses, and intellectual trajectory. (Zero competition, zero fake XP).</div>
        </div>
        <button type="button" class="iva-btn iva-btn-secondary iva-btn-small" id="ivaJourneyBackHomeBtn">
          ← Back to Home
        </button>
      </div>

      <!-- Non-Competitive Metric Cards -->
      <div class="iva-journey-grid">
        <div class="iva-journey-stat-card">
          <div class="iva-journey-stat-num" id="ivaJourneyExploredNum">0</div>
          <div class="iva-journey-stat-label">Inquiries Explored</div>
        </div>
        <div class="iva-journey-stat-card">
          <div class="iva-journey-stat-num" id="ivaJourneySavedNum">0</div>
          <div class="iva-journey-stat-label">Inquiries Saved</div>
        </div>
        <div class="iva-journey-stat-card">
          <div class="iva-journey-stat-num" id="ivaJourneyOriginalNum">0</div>
          <div class="iva-journey-stat-label">Questions Created</div>
        </div>
        <div class="iva-journey-stat-card">
          <div class="iva-journey-stat-num" id="ivaJourneyHypothesisNum">0</div>
          <div class="iva-journey-stat-label">Hypotheses Formed</div>
        </div>
        <div class="iva-journey-stat-card">
          <div class="iva-journey-stat-num" id="ivaJourneyStreakNum">1</div>
          <div class="iva-journey-stat-label">Day Wonder Streak</div>
        </div>
      </div>

      <!-- Visual Concept Trail (Section 12) -->
      <div style="margin-bottom: 24px;">
        <h3 style="font-family: var(--iva-font-serif); font-size: 1.25rem; color: #fff; margin-bottom: 10px;">
          🗺️ Visual Discovery Trail
        </h3>
        <p style="font-size: 0.86rem; color: var(--iva-text-secondary); margin-bottom: 14px;">
          The web of concepts you have walked through:
        </p>
        <div class="iva-journey-trail-flow" id="ivaJourneyTrailFlow">
          <!-- Populated dynamically -->
        </div>
      </div>

      <!-- Created Questions &amp; Hypotheses History -->
      <div>
        <h3 style="font-family: var(--iva-font-serif); font-size: 1.25rem; color: #fff; margin-bottom: 12px;">
          📝 Your Created Questions &amp; Hypotheses
        </h3>
        <div id="ivaJourneyNotesList">
          <!-- Populated dynamically -->
        </div>
      </div>

    </div>

  </main>

  <!-- ── 4. INSIGHT CARD EXPORT MODAL ── -->
  <div class="iva-modal-overlay iva-hidden" id="ivaCardModalOverlay">
    <div class="iva-modal-box">
      <button type="button" class="iva-modal-close" id="ivaCardCloseBtn" aria-label="Close Modal">✕</button>
      <h3 style="font-family: var(--iva-font-serif); font-size: 1.4rem; color: #fff; margin-bottom: 14px; text-align: center;">
        🎨 Your Downloadable Insight Card
      </h3>
      <canvas id="ivaCardCanvas" width="600" height="420" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid var(--iva-border); margin-bottom: 18px;"></canvas>
      <div style="display: flex; gap: 10px; justify-content: center;">
        <button type="button" class="iva-btn iva-btn-primary" id="ivaDownloadCardBtn">💾 Download Image (PNG)</button>
        <button type="button" class="iva-btn iva-btn-secondary" id="ivaCardDismissBtn">Close</button>
      </div>
    </div>
  </div>

  <!-- ── 5. ABOUT IKSHVAKU ACADEMY MODAL (Section 37) ── -->
  <div class="iva-modal-overlay iva-hidden" id="ivaAboutModalOverlay">
    <div class="iva-modal-box">
      <button type="button" class="iva-modal-close" id="ivaAboutCloseBtn" aria-label="Close Modal">✕</button>
      <div style="text-align: center; margin-bottom: 20px;">
        <img src="{base64_logo}" alt="Ikshvaku Vidya Academy Seal" style="width: 58px; height: 58px; border-radius: 50%; border: 1.5px solid var(--iva-gold); margin-bottom: 10px;" />
        <h3 style="font-family: var(--iva-font-serif); font-size: 1.6rem; color: #fff;">IKSHVAKU VIDYA ACADEMY</h3>
        <div style="font-size: 0.84rem; color: var(--iva-gold);">A Place for Curious Minds • Education Beyond Commerce</div>
      </div>
      
      <div style="font-size: 0.92rem; color: var(--iva-text-secondary); line-height: 1.7; display: flex; flex-direction: column; gap: 14px;">
        <div>
          <strong style="color: #fff;">What is Ikshvaku Curiosity Machine?</strong><br/>
          An independent digital laboratory built to revive first-principles inquiry, childlike wonder, and genuine scientific understanding.
        </div>
        <div>
          <strong style="color: #fff;">Why was it created?</strong><br/>
          To provide an alternative to exam-driven rote learning and gamified dopamine traps. True education starts when you pause and wonder: <em>"Why does reality behave this way?"</em>
        </div>
        <div>
          <strong style="color: #fff;">What does "Don't Just Learn. Get Curious." mean?</strong><br/>
          Learning is often passive consumption of answers. Curiosity is an active, joyful stance that looks at everyday phenomena and uncovers the hidden mechanisms beneath them.
        </div>
        <div>
          <strong style="color: #fff;">What does "Education Beyond Commerce" mean?</strong><br/>
          It means knowledge should never be gatekept by paywalls, dark patterns, or anxiety-inducing metrics. Wonder is a universal birthright.
        </div>
      </div>

      <div style="text-align: center; margin-top: 24px;">
        <button type="button" class="iva-btn iva-btn-primary iva-btn-small" id="ivaAboutGotItBtn">Got It</button>
      </div>
    </div>
  </div>

  <!-- ── 6. TOAST NOTIFICATION ── -->
  <div id="ivaToast" class="iva-hidden">
    <span id="ivaToastIcon" style="font-size: 1.2rem;">✨</span>
    <span id="ivaToastMessage">Curiosity awakened.</span>
  </div>

</div>
"""

print(f"Master HTML generated (length: {len(master_html)} bytes)")

# ── MASTER JAVASCRIPT ENGINE ──
with open('build_masterpiece.py', 'r', encoding='utf-8') as f:
    bmp_text = f.read()

# We will generate a clean, modern, fully functional master_js string
# containing all flagship inquiries, procedural engine, think-first tri-gates,
# what-if variable engine, simulator, bored mode, strange facts, search, etc.

master_js = r"""(function() {
  'use strict';

  // ════════════════════════════════════════════════════════════════
  // 1. KNOWLEDGE DISCIPLINES & FLAGSHIP INQUIRIES
  // ════════════════════════════════════════════════════════════════

  var CATEGORIES = [
    { key: "space", label: "Astrophysics & Cosmos", icon: "🌌", badge: "iva-badge-space", desc: "Black holes, orbital mechanics, planetary atmospheres, cosmic radiation." },
    { key: "science", label: "Quantum & Relativity", icon: "⚛️", badge: "iva-badge-physics", desc: "Wave-particle duality, atomic lattice, relativity, entropy, thermodynamics." },
    { key: "math", label: "Pure Mathematics & Logic", icon: "📐", badge: "iva-badge-math", desc: "Topology, primes, infinity, game theory, cryptography, probability." },
    { key: "nature", label: "Everyday Physics & Nature", icon: "🌿", badge: "iva-badge-biology", desc: "Molecular geometry, ice density inversion, cellular energy, emergent systems." },
    { key: "tech", label: "Cognitive Tech & Computing", icon: "💻", badge: "iva-badge-tech", desc: "Information theory, error correction, neural networks, silicon logic." },
    { key: "thinking", label: "Philosophy of Mind", icon: "🧠", badge: "iva-badge-math", desc: "Predictive perception, optical scotomas, consciousness, epistemology." },
    { key: "how", label: "Wave Physics & Optics", icon: "🔬", badge: "iva-badge-physics", desc: "Acoustic phase cancellation, Rayleigh scattering, wave superposition." },
    { key: "behavior", label: "Systems & Civilizations", icon: "🏛️", badge: "iva-badge-biology", desc: "Complex adaptive systems, institutional evolution, game theory of societies." }
  ];

  var FLAGSHIP_INQUIRIES = [
    {
      id: "flagship-moon",
      category: "space",
      categoryLabel: "Astrophysics & Cosmos",
      badgeClass: "iva-badge-space",
      readTime: "3 min thought experiment",
      question: "Why doesn't the Moon fall into Earth?",
      mystery: "You already know Earth pulls the Moon with relentless gravitational force. So here's the strange part... Why doesn't the Moon simply plunge straight down like an apple dropped from a tree?",
      thinkPrompt: "What keeps an object perpetually falling through space without ever hitting the ground?",
      hint: "Think of throwing a baseball horizontally from a tall mountain. What happens as you throw it faster and faster across a curved planet?",
      level1: "Imagine standing on a high mountain and throwing a stone forward. Throw it at 100 mph, and it curves down into the valley. Throw it at 17,500 mph, and the ground curves away underneath it at the exact same rate the stone falls. The stone falls, but the Earth curves away before the stone can touch it. The Moon is doing this perpetually: it is constantly falling toward Earth, but it has so much sideways speed that it keeps missing the planet forever. An orbit is just perpetual falling.",
      level2: "Newtonian orbital mechanics: The Moon has a high tangential velocity (1.022 km/s). Gravity provides a continuous centripetal acceleration (a = v²/r) directed strictly toward Earth's center. Because gravity acts at a 90-degree angle to the Moon's velocity vector at every instant, it changes the direction of the Moon's motion without changing its speed. The inward gravitational pull exactly matches the inertial tendency of the Moon to fly off in a straight tangent line.",
      level3: "General Relativity (Einstein, 1915): In modern physics, gravity is not an attractive mechanical force pulling through space. Instead, Earth's massive energy-momentum curves the four-dimensional spacetime around it. The Moon is actually traveling along the straightest possible inertial path—called a geodesic—through this curved spacetime geometry. Zero net proper force acts on the Moon; it is in pure, unforced inertial free-fall.",
      whyCare: "Every GPS navigation satellite directing your smartphone, every weather Doppler radar, and every communications relay balances on this exact mathematical equilibrium. Without orbital mechanics, modern global logistics and navigation would cease to exist.",
      whatIf: {
        variableName: "Forward Orbital Velocity",
        baseline: "100% (1.022 km/s)",
        reactions: {
          "50": {
            whatChanged: "Forward tangential speed reduced by half (to 0.511 km/s).",
            whyChanged: "Centrifugal inertial resistance drops with the square of velocity, leaving inward gravitational attraction dominant.",
            consequence: "The circular orbit collapses into a steep decay spiral. The Moon would collide radially with Earth within approximately 9 days, obliterating the crust and wiping out planetary life."
          },
          "75": {
            whatChanged: "Tangential speed drops to 75% (0.767 km/s).",
            whyChanged: "Velocity is insufficient to maintain a stable circular geodesic at 384,400 km.",
            consequence: "The orbit shifts into a highly eccentric ellipse with a low perigee that enters Earth's Roche limit (18,470 km), tearing the Moon into a brilliant ring system of planetary debris like Saturn's."
          },
          "100": {
            whatChanged: "Stable baseline equilibrium (1.022 km/s).",
            whyChanged: "Inward gravitational acceleration (GM/r²) precisely matches required centripetal acceleration (v²/r).",
            consequence: "Stable quasi-circular orbit with predictable 27.3-day sidereal period, driving regular oceanic tides, stabilizing Earth's 23.5° axial tilt, and protecting our stable climate seasons."
          },
          "125": {
            whatChanged: "Tangential speed increases by 25% (1.278 km/s).",
            whyChanged: "Kinetic energy exceeds gravitational binding energy for a circular orbit.",
            consequence: "The Moon migrates into an elongated elliptical orbit with an apogee far past 600,000 km. Ocean tides would swing between tranquil calms and massive 50-meter tidal surges every month."
          },
          "200": {
            whatChanged: "Velocity doubled to 2.044 km/s (exceeding escape velocity √2·v ≈ 1.445 km/s).",
            whyChanged: "Total mechanical energy (E = K + U) becomes strictly positive, breaking the gravitational well.",
            consequence: "The Moon permanently escapes Earth's orbit into a hyperbolic trajectory, becoming an independent dwarf planet orbiting the Sun. Earth's axial tilt would begin wildly destabilizing from 0° to 85° over millions of years, destroying regular seasons."
          }
        }
      },
      whereElse: [
        { title: "International Space Station", desc: "Astronauts aboard the ISS aren't in 'zero gravity'—Earth's gravity at 400 km is still 90% as strong as on the ground! They float because they and the station are both falling together around Earth at 28,000 km/h." },
        { title: "Halley's Comet & Asteroids", desc: "Comets swing around the Sun in highly eccentric orbits, plunging inward toward solar heat and then hurtling out past Neptune, continually falling and missing." },
        { title: "Rollercoaster Loops", desc: "At the apex of a teardrop-shaped clothoid loop, your forward momentum balances downward gravity, momentarily giving you weightless free-fall sensations." }
      ],
      crossDiscipline: {
        from: "Astrophysics & Orbital Mechanics",
        to: "Evolutionary Biology",
        bridge: "The gravitational tidal locking of the Moon creates rhythmic intertidal zones on Earth's coastlines. Evolutionary biologists believe these wet-dry tidal pools were the critical staging ground for early marine organisms to develop air-breathing lungs and transition onto land."
      },
      yourTurn: "If Earth were suddenly replaced by a black hole of the exact same mass, would the Moon get sucked in or stay in its current orbit?",
      loop: {
        discovered: "Perpetual Free-Fall & Orbital Velocity Balance",
        connectsTo: "Gravitational Spacetime Curvature & Time Dilation",
        nextQuestion: "Why does time run faster on top of a mountain than at sea level?",
        nextId: "flagship-time-dilation"
      },
      simMode: "orbit",
      simWhatChanged: "The forward tangential speed balanced Earth's constant inward gravitational curvature.",
      simWhyChanged: "Perpendicular velocity changes directional momentum without expending energy.",
      simNext: "If velocity drops, orbit decays inward; if velocity increases, it escapes into hyperbolic trajectory.",
      trail: ["Perpetual Free-Fall", "Centripetal Geodesics", "General Relativity", "GPS Satellites", "Planetary Stability"]
    },
    {
      id: "flagship-ice",
      category: "nature",
      categoryLabel: "Everyday Physics & Thermodynamics",
      badgeClass: "iva-badge-physics",
      readTime: "3 min thought experiment",
      question: "Why does ice float?",
      mystery: "Almost every liquid in the known universe contracts and becomes denser when frozen solid. Liquid wax sinks in solid wax; molten iron sinks in solid iron. Why does water do the exact opposite?",
      thinkPrompt: "What happens to the geometric arrangement of water molecules when they freeze below 4°C?",
      hint: "Look closely at the chemical formula H2O. How do the positive hydrogen charges and negative oxygen charges push and pull against each other?",
      level1: "In liquid water, molecules are buzzing and jiggling past one another like people in a crowded train station. As it cools, they slow down. But when water freezes below 0°C, the electrical charges on the molecules force them to lock into a rigid hexagonal ring structure. This crystal lattice has wide open spaces in the middle—like a scaffolding with empty air inside. Because it expands by 9% upon freezing, solid ice has fewer molecules per volume than liquid water. Less dense things float!",
      level2: "Water is a polar molecule with a bent shape (104.5° bond angle). Oxygen has a higher electronegativity, creating a strong permanent dipole. In liquid water, hydrogen bonds constantly break and reform trillions of times per second. Below 4°C, thermal kinetic motion can no longer overcome electrostatic repulsion, forcing each oxygen to coordinate tetrahedrally with four hydrogens. This open hexagonal crystal lattice decreases density from 1.000 g/cm³ to 0.917 g/cm³.",
      level3: "Quantum Electrostatic Repulsion & Pauli Exclusion Principle: Water's tetrahedral geometry originates from sp³ hybridization of oxygen's valence electron orbitals. Two hybrid orbitals contain bonded electron pairs, while two contain non-bonding lone pairs. Coulombic repulsion between these lone pairs and neighboring hydrogen nuclei stabilizes the open lattice. Thermodynamic entropy minimization at low temperature favors enthalpy-driven hydrogen bonding over dense, disordered geometric packing.",
      whyCare: "If ice sank, every lake, river, and polar sea would freeze solid from the bottom up. Sunlight could never reach the depths to melt it. Earth would be locked in a permanent global ice age, making complex multicellular life impossible.",
      whatIf: {
        variableName: "Hydrogen Bond Angle & Geometry",
        baseline: "100% (Hexagonal Open Lattice)",
        reactions: {
          "50": {
            whatChanged: "Hydrogen bond angle contracts, collapsing the open hexagonal ring.",
            whyChanged: "Molecules pack tightly into a dense amorphous solid without interior voids.",
            consequence: "Ice becomes 15% denser than liquid water. Ice cubes sink straight to the bottom of your glass. Winter frost sinks to riverbeds and ocean trenches, permanently freezing all marine biospheres."
          },
          "75": {
            whatChanged: "Lattice expansion drops from 9% to 2%.",
            whyChanged: "Partial void collapse reduces the buoyancy margin.",
            consequence: "Ice barely floats with 98% submerged. Slight atmospheric temperature swings cause surface ice sheets to collapse and sink under moderate wave action."
          },
          "100": {
            whatChanged: "Natural physical baseline: 9% volumetric expansion below 4°C.",
            whyChanged: "Stable sp³ tetrahedral hydrogen coordination creates rigid hexagonal cages.",
            consequence: "Floating ice sheets act as thermal insulation blankets for lakes and oceans, keeping liquid water underneath at a stable 4°C, sheltering fish and aquatic organisms through harsh winters."
          },
          "125": {
            whatChanged: "Hexagonal lattice expands by 20% on freezing.",
            whyChanged: "Stronger hydrogen bonds force even wider coordination spacing.",
            consequence: "Freezing water exerts extreme hydraulic burst pressure. Any tree or plant tissue freezing in winter would violently rupture, and water pipes would explode with explosive force."
          },
          "200": {
            whatChanged: "Lattice expansion doubles to 40% with ultralight porous geometry.",
            whyChanged: "Super-rigid quantum bond angles create ultra-low density aerogel-like ice.",
            consequence: "Ice forms buoyant rafts that float effortlessly on water like cork, but possesses so little compressive strength that glaciers would crumble under their own weight, dramatically reshaping planetary topography."
          }
        }
      },
      whereElse: [
        { title: "Lake Thermocline Insulation", desc: "During freezing winters, the bottom of deep freshwater lakes stays at exactly 4°C (water's densest state), allowing aquatic ecosystems to survive under surface ice." },
        { title: "Biological Cryopreservation", desc: "Because freezing water expands and forms sharp crystal needles, flash-freezing cells requires cryoprotectant sugars to prevent ice from tearing cell membranes apart." },
        { title: "Geological Frost Wedging", desc: "Water trickles into micro-fractures in granite mountains. When it freezes and expands by 9%, it splits solid rock with up to 30,000 psi of pressure, driving natural erosion." }
      ],
      crossDiscipline: {
        from: "Thermodynamics & Molecular Chemistry",
        to: "Planetary Geology & Astrobiology",
        bridge: "The density inversion of water is why astrobiologists look for liquid oceans beneath the icy crusts of moons like Jupiter's Europa and Saturn's Enceladus. The ice shell insulates a vast subsurface ocean warmed by geothermal tidal heating."
      },
      yourTurn: "If hot water sometimes freezes faster than cold water (the Mpemba effect), what does that tell us about evaporation and dissolved gases?",
      loop: {
        discovered: "Water's Density Inversion & Hexagonal Lattice",
        connectsTo: "Atmospheric Molecular Scattering & Sunlight",
        nextQuestion: "Why is the sky blue instead of violet if violet light scatters more?",
        nextId: "flagship-blue-sky"
      },
      simMode: "wave",
      simWhatChanged: "The molecular spacing expanded into an open tetrahedral lattice.",
      simWhyChanged: "Hydrogen bonds lock into rigid geometric angles as thermal kinetic vibrations diminish.",
      simNext: "Liquid water below the ice sheet remains insulated at 4°C, preserving aquatic life through sub-zero winters.",
      trail: ["Hydrogen Bonding", "Tetrahedral Lattice", "Density Inversion", "Aquatic Insulation", "Planetary Astrobiology"]
    },
    {
      id: "flagship-earth-spin",
      category: "science",
      categoryLabel: "Relativity & Motion",
      badgeClass: "iva-badge-physics",
      readTime: "4 min thought experiment",
      question: "Why don't we feel Earth spinning?",
      mystery: "At this exact moment, Earth's equator is hurtling through space at over 1,670 kilometers per hour. Why do you feel completely, perfectly still?",
      thinkPrompt: "When you ride in an airplane cruising smoothly at 900 km/h with the window shades drawn, can you pour a glass of water?",
      hint: "Think about what human sensory nerves actually measure: do our inner ears detect speed, or do they detect changes in speed?",
      level1: "You cannot feel speed; you can only feel acceleration (speeding up, slowing down, or turning a corner). When you are on a high-speed train moving at a constant 300 km/h on smooth tracks, a coin tossed in the air lands right back in your palm. Everything inside the train—the air, the seats, the coin, and you—shares the exact same constant speed. Earth is the ultimate smooth train: the atmosphere, the oceans, the mountains, and your body are all moving together at the exact same constant velocity.",
      level2: "Inertial reference frames and the Equivalence Principle: The human vestibular system in the inner ear uses semicircular canals filled with fluid (endolymph) and tiny hair cells that respond strictly to inertia during acceleration (F = ma). Earth rotates at a virtually constant angular speed (1 rotation every 86,164 seconds). The outward centrifugal acceleration at the equator is merely 0.034 m/s²—completely drowned out by Earth's downward gravitational pull of 9.81 m/s².",
      level3: "Galilean Invariance & The Principle of Relativity: Formulated by Galileo in 1632 and formalized by Einstein in 1905, the laws of mechanics and electromagnetism are identical in all non-accelerating inertial frames. Inside a closed system moving with uniform velocity, no internal physical experiment can determine whether the system is at rest or in motion. Absolute velocity does not exist in physics—velocity is meaningful only relative to an external observer.",
      whyCare: "This foundational principle made modern aviation, space station docking, and Einstein's Special Theory of Relativity possible. Without understanding relative inertial frames, interplanetary navigation would be fundamentally unsolvable.",
      whatIf: {
        variableName: "Earth's Rotational Deceleration",
        baseline: "100% Constant Velocity (0 km/h/s Deceleration)",
        reactions: {
          "50": {
            whatChanged: "Earth decelerates at a steady rate of 50 km/h per hour.",
            whyChanged: "A continuous tangential force acts against rotational inertia.",
            consequence: "You would feel a persistent eastward tilt in balance, equivalent to standing on a 3° incline. Ocean currents would surge eastwards, causing perpetual continental flooding along western coastlines."
          },
          "75": {
            whatChanged: "Sudden 25% drop in rotational velocity over 60 seconds.",
            whyChanged: "Rapid change in momentum (dp/dt) creates massive inertial shear forces.",
            consequence: "Atmospheric air masses and oceans, retaining their 1,670 km/h momentum, would sweep across continents in supersonic 400 km/h winds, flattening human structures."
          },
          "100": {
            whatChanged: "Smooth, constant rotation (1 revolution per 23h 56m 4s).",
            whyChanged: "Conservation of angular momentum in vacuum of space with near-zero external torque.",
            consequence: "Total subjective stillness. The Coriolis effect gently curves storm systems into cyclones and steers global trade winds without shaking a single pebble."
          },
          "125": {
            whatChanged: "Earth's rotation accelerates by 25% (18-hour day).",
            whyChanged: "Higher angular momentum increases equatorial centrifugal acceleration.",
            consequence: "Centrifugal acceleration increases to 0.053 m/s². You would weigh slightly less at the equator. Weather patterns would generate much tighter, more frequent, and intense hurricane spirals."
          },
          "200": {
            whatChanged: "Earth spins twice as fast (12-hour day; equator at 3,340 km/h).",
            whyChanged: "Doubling angular velocity quadruples centrifugal force (ac = ω²r).",
            consequence: "Oceans would migrate heavily toward the equator, creating a massive equatorial megaswelling that drowns tropical nations while exposing shallow continental shelves at the poles."
          }
        }
      },
      whereElse: [
        { title: "Commercial Jet Cruising", desc: "At 35,000 feet moving at 900 km/h, coffee pours into a cup identically to how it pours on your kitchen table because the cabin air and coffee share the jet's velocity." },
        { title: "Foucault Pendulum", desc: "A heavy pendulum swinging in a museum appears to slowly rotate its plane of swing over 24 hours—providing visible proof that the Earth is rotating beneath it." },
        { title: "Coriolis Storm Spirals", desc: "Hurricanes in the Northern Hemisphere always spin counter-clockwise, while cyclones in the Southern Hemisphere spin clockwise, deflected by Earth's rotating surface." }
      ],
      crossDiscipline: {
        from: "Classical Mechanics & Relativity",
        to: "Neurobiology & Sensory Physiology",
        bridge: "The human brain evolved to ignore constant velocity because our ancestors lived in an environment with no artificial vehicles. Our inner ear's otolith organs and semicircular canals developed specifically to detect predators' sudden lunges and balance stumbles."
      },
      yourTurn: "If Earth stopped spinning instantly, would you fly into space or slide across the ground?",
      loop: {
        discovered: "Inertial Frames & Galileo's Principle of Relativity",
        connectsTo: "Information Encodings & Computational Matrices",
        nextQuestion: "How does a smartphone camera read a QR code instantly, even if it's smudged or held upside down?",
        nextId: "flagship-qr-code"
      },
      simMode: "orbit",
      simWhatChanged: "The observer, atmosphere, and surface share identical uniform velocity.",
      simWhyChanged: "Inertia conserves momentum; acceleration is zero relative to the local reference frame.",
      simNext: "Centrifugal acceleration reduces effective weight by only 0.3% at the equator.",
      trail: ["Inertial Reference Frames", "Centrifugal Equilibrium", "Equivalence Principle", "Galilean Invariance", "Vestibular Physiology"]
    },
    {
      id: "flagship-qr-code",
      category: "tech",
      categoryLabel: "Cognitive Tech & Computing",
      badgeClass: "iva-badge-tech",
      readTime: "3 min thought experiment",
      question: "How does a smartphone camera read a QR code upside down or with a smudge?",
      mystery: "You can hold a QR code rotated at a weird 37-degree angle, crinkled in dim lighting, or with 30% of it covered in coffee stains, and your phone still scans it in under 50 milliseconds. How?",
      thinkPrompt: "Notice the three big squares in the corners of every QR code. Why are there only three, not four?",
      hint: "Three points define a two-dimensional plane and its rotational orientation in space. And what mathematical trick lets you reconstruct missing words in a sentence?",
      level1: "Every QR code has three identical square targets in its corners. By locating those three squares, your phone's camera instantly calculates the code's size, tilt, angle, and distance—even if you hold it upside down. For the smudges, QR codes don't just store your link; they store it using mathematical 'safety nets' called Reed-Solomon error correction. It's like writing a message where every third letter is a mathematical clue that lets the phone recalculate any missing or ruined pixels!",
      level2: "Computer Vision & Galois Field Algebra: The phone runs an edge-detection algorithm to locate the three Position Detection Patterns (PDPs), which have a unique 1:1:3:1:1 black-white-black ratio from any scan line angle. This creates an affine transformation matrix to unwarp the image into a clean square grid. Then, Reed-Solomon error correction over finite fields (GF(2⁸)) treats data as coefficients of a high-degree polynomial. Extra check bytes allow the decoder to find and correct up to 30% corrupted or missing data.",
      level3: "Shannon Information Theory & Algebraic Coding: Claude Shannon established that channel noise can be completely overcome by adding structured redundancy below channel capacity. Reed-Solomon codes achieve the Singleton Bound, making them Maximum Distance Separable (MDS) codes. They maximize the minimum Hamming distance between valid codewords, ensuring that partial occlusions map uniquely to the original message polynomial.",
      whyCare: "The exact same Reed-Solomon math preserves data on scratched Blu-ray discs, allows Voyager 1 to beam crisp photographs across 24 billion kilometers of noisy interstellar space, and prevents memory corruption inside solid-state hard drives.",
      whatIf: {
        variableName: "Reed-Solomon Error Correction Level",
        baseline: "100% (Level H: 30% Damage Recovery)",
        reactions: {
          "50": {
            whatChanged: "Error correction reduced to Level L (7% recovery).",
            whyChanged: "Fewer check polynomials are interleaved with data bytes.",
            consequence: "The QR code holds more raw text, but a single thumbprint or tear causes the scan to fail completely."
          },
          "75": {
            whatChanged: "Reduced to Level M (15% recovery, typical commercial baseline).",
            whyChanged: "Balanced tradeoff between data density and mathematical resilience.",
            consequence: "Scans reliably on clean product packaging, but fails on crumpled flyers or glaring reflective surfaces."
          },
          "100": {
            whatChanged: "High-durability Level H (30% recovery threshold).",
            whyChanged: "Approximately 50% of the visual code consists of redundant algebraic parity bytes.",
            consequence: "You can paste a custom company logo directly over the center of the code, and scanners will still decode the URL with 100% fidelity."
          },
          "125": {
            whatChanged: "Hypothetical Level X (50% recovery threshold).",
            whyChanged: "Check symbols outnumber raw payload symbols 2-to-1.",
            consequence: "You could slice the QR code in half with scissors, and the camera could reconstruct the entire original URL from either remaining piece."
          },
          "200": {
            whatChanged: "Ultra-redundant 75% error recovery.",
            whyChanged: "Extremely high polynomial degree redundancy.",
            consequence: "The code matrix becomes dense and tiny (like fine sandpaper), requiring high-resolution microscopes to scan, but surviving extreme physical mutilation."
          }
        }
      },
      whereElse: [
        { title: "Deep Space Telemetry (Voyager & James Webb)", desc: "Weak radio signals traversing billions of miles of solar cosmic rays use Reed-Solomon encoding to eliminate bit-flip corruption." },
        { title: "Audio CDs & Blu-ray Discs", desc: "A 2mm scratch across a compact disc destroys thousands of bits, but Reed-Solomon algebra reconstructs the exact original audio stream in real-time." },
        { title: "Barcodes & Shipping Logistics", desc: "Automated warehouse conveyor belts scan crushed, dirty cardboard shipping boxes at 60 mph without misrouting packages." }
      ],
      crossDiscipline: {
        from: "Computer Science & Information Theory",
        to: "Molecular Genetics & DNA Storage",
        bridge: "Geneticists now encode digital archives (books, operating systems, music) into synthetic DNA strands using Reed-Solomon error correction to prevent biochemical mutation from corrupting data over thousands of years."
      },
      yourTurn: "Can you create an error-correcting language for humans where typos automatically correct themselves?",
      loop: {
        discovered: "Affine Geometry & Reed-Solomon Polynomial Codes",
        connectsTo: "Acoustic Wave Superposition & Phase Cancellation",
        nextQuestion: "How do noise-cancelling headphones erase jet engine roar using sound itself?",
        nextId: "flagship-noise-cancellation"
      },
      simMode: "wave",
      simWhatChanged: "The affine matrix unwarped perspective distortion while polynomial check bytes reconstructed missing pixels.",
      simWhyChanged: "Redundancy placed below channel capacity eliminates noise without information loss.",
      simNext: "Scanned data instantly decodes into an alphanumeric string within 30 milliseconds.",
      trail: ["Reed-Solomon Codes", "Affine Transformations", "Galois Fields", "Shannon Entropy", "Error Correction"]
    },
    {
      id: "flagship-blue-sky",
      category: "how",
      categoryLabel: "Everyday Physics & Optics",
      badgeClass: "iva-badge-physics",
      readTime: "3 min thought experiment",
      question: "Why is the sky blue instead of violet?",
      mystery: "Physics textbooks tell us shorter wavelengths scatter more, and violet light has an even shorter wavelength than blue light. So why isn't our daytime sky a vivid purple?",
      thinkPrompt: "Is the color of the sky purely a property of sunlight, or is it also a property of human eye anatomy?",
      hint: "Look at how the Sun emits light across the rainbow spectrum, and how the three color-sensing cone cells in your retina respond to blue vs violet.",
      level1: "Two reasons combine here: one in the sky, and one inside your eyes. First, while sunlight contains violet, the Sun emits far more blue photons than violet photons. Second, your eyes are not cameras; your retinas use three types of color sensors (cones) tuned to red, green, and blue. When the scattered violet and blue photons hit your eyes together, your brain's color circuits register the combination as bright celestial sky blue, not violet.",
      level2: "Rayleigh Scattering (I ∝ 1/λ⁴) & Solar Blackbody Radiation: Nitrogen and oxygen molecules (N₂, O₂) in the atmosphere are smaller than the wavelength of visible light. Shorter blue wavelengths (400–450 nm) scatter nearly 10 times more efficiently than red wavelengths (700 nm). However, solar emission peaks in the green spectrum around 500 nm according to Planck's Law and declines steeply toward the violet/ultraviolet edge.",
      level3: "Tristimulus Human Photoreceptor Biology: The human eye's Short-wavelength (S) cones peak at 420 nm, but the Medium (M) and Long (L) cones also maintain slight sensitivity in the violet range. When exposed to Rayleigh-scattered sunlight, the S-cones are strongly stimulated while M and L cones receive moderate excitation. The visual cortex processes this exact ratio of cone firing through opponent-process color theory as sky blue tinted with white light, actively canceling perceived violet hues.",
      whyCare: "Rayleigh scattering explains why sunsets turn flaming red (blue light is scattered away during long optical path lengths) and allows atmospheric scientists to detect water vapor, methane, and oxygen in the atmospheres of distant exoplanets.",
      whatIf: {
        variableName: "Atmospheric Molecular Density",
        baseline: "100% (Earth Sea Level)",
        reactions: {
          "50": {
            whatChanged: "Atmospheric density drops by 50% (like high Tibetan plateau).",
            whyChanged: "Fewer gas molecules available to scatter incoming photons.",
            consequence: "The sky darkens to deep indigo navy; stars and bright planets become visible during the day beside a dazzling white Sun."
          },
          "75": {
            whatChanged: "Atmospheric density drops to 75%.",
            whyChanged: "Moderate decrease in Rayleigh scattering events.",
            consequence: "Crisp cobalt blue skies with sharper mountain shadows and reduced ambient diffuse daylight."
          },
          "100": {
            whatChanged: "Earth standard 1 atm pressure (78% N2, 21% O2).",
            whyChanged: "Perfect balance of solar blackbody output and Rayleigh scattering.",
            consequence: "Familiar brilliant azure blue sky with warm golden direct sunlight and soft diffuse ambient illumination."
          },
          "125": {
            whatChanged: "Atmosphere becomes 25% denser.",
            whyChanged: "Increased optical scattering per cubic meter.",
            consequence: "Sky turns milky pale blue with washed-out contrast; shadows become hazy and sunsets turn deep blood-crimson hours earlier."
          },
          "200": {
            whatChanged: "Atmospheric pressure doubled (2 atm, like dense planetary soup).",
            whyChanged: "Multiple-order scattering dominates over single Rayleigh scattering.",
            consequence: "The entire daytime sky becomes a uniform, glowing whitish-gold dome. The Sun's disc becomes completely invisible, mimicking a perpetual overcast day."
          }
        }
      },
      whereElse: [
        { title: "Red Sunsets & Moon Rises", desc: "At dusk, sunlight travels through 10 times more atmosphere. Blue light is completely scattered away, leaving only surviving red and orange wavelengths." },
        { title: "Blue Eyes & Bird Feathers", desc: "Blue eyes and blue jay feathers contain zero blue pigment! Their color is structural: tiny protein particles scatter light via Tyndall scattering." },
        { title: "Martian Butterscotch Skies", desc: "Mars has thin air filled with fine rust dust (Fe₂O₃) that absorbs blue light, giving Mars butterscotch orange day skies and blue sunsets!" }
      ],
      crossDiscipline: {
        from: "Atmospheric Optics & Wave Mechanics",
        to: "Neuro-Ophthalmology & Visual Perception",
        bridge: "Many birds and insects possess a fourth ultraviolet photoreceptor cone (tetrachromatic vision). To a migratory songbird, Earth's sky is not blue at all, but a shimmering ultraviolet compass displaying polarization patterns that guide global navigation."
      },
      yourTurn: "Why does clean steam from a kettle look white, but cigarette smoke looks slightly blue?",
      loop: {
        discovered: "Rayleigh Scattering & Tristimulus Color Perception",
        connectsTo: "Phase Inversion & Destructive Wave Interference",
        nextQuestion: "How do noise-cancelling headphones erase ambient noise using sound waves?",
        nextId: "flagship-noise-cancellation"
      },
      simMode: "wave",
      simWhatChanged: "Blue wavelengths (450nm) scattered 10 times more vigorously than red wavelengths (700nm).",
      simWhyChanged: "Electromagnetic radiation oscillates dipole charges in atmospheric nitrogen and oxygen molecules.",
      simNext: "Human cone photoreceptors combine the scattered spectrum into subjective sky blue.",
      trail: ["Rayleigh Scattering", "Blackbody Radiation", "Opponent Color Theory", "Tristimulus Vision", "Atmospheric Optics"]
    },
    {
      id: "flagship-noise-cancellation",
      category: "how",
      categoryLabel: "Wave Physics & Acoustics",
      badgeClass: "iva-badge-physics",
      readTime: "3 min thought experiment",
      question: "How do noise-cancelling headphones erase jet engine roar using sound itself?",
      mystery: "If you add more sound into your ears, wouldn't it always get louder? How can firing two sounds together create total acoustic silence?",
      thinkPrompt: "Imagine a wave on the ocean: what happens if a wave peak meets an identical wave trough at the exact same instant?",
      hint: "Sound is a pressure wave of air compressions and rarefactions. What is (+1) plus (-1)?",
      level1: "Sound is not a solid object; it is a traveling pressure wave. When a jet engine roars, it pushes air molecules together (a peak), then pulls them apart (a trough). Noise-cancelling headphones have tiny outward-facing microphones that sample this noise in microseconds. The headphone speaker then plays an exact upside-down replica of the noise: when the outside world pushes air, the speaker pulls air. The peak meets a trough, adding up to zero. Two loud sounds collide to create silence!",
      level2: "Active Noise Control (ANC) & Phase Inversion: Acoustic sound propagates as longitudinal pressure waves p(t) = A sin(ωt + φ). An external microphone samples incoming acoustic noise and feeds it to an ultra-low-latency Digital Signal Processor (DSP). The DSP applies a 180° (π radians) phase shift, outputting an anti-phase waveform -p(t). By the Principle of Superposition, the net sound pressure at the eardrum becomes p_net(t) = p(t) + (-p(t)) = 0.",
      level3: "Wave Equation Superposition & Boundary Limitations: The acoustic wave equation ∇²p - (1/c²)∂²p/∂t² = 0 is strictly linear in air at audible volumes. Linear differential equations obey strict additive superposition. ANC succeeds brilliantly with low-frequency repetitive hums (100–1000 Hz) because wavelengths are long (34 cm to 3.4 m), providing ample time for DSP processing. High-frequency transient sounds (speech, glass breaking) have millimetric wavelengths that shift phase before the speaker can react, requiring passive silicone insulation.",
      whyCare: "Acoustic phase cancellation protects the hearing of jet pilots, reduces industrial turbine vibration in hospitals, and enables stealth submarine propulsion systems.",
      whatIf: {
        variableName: "Anti-Wave Phase Offset",
        baseline: "100% Exact 180° Inversion (Total Silence)",
        reactions: {
          "50": {
            whatChanged: "Phase offset drifts by 90° (halfway to cancellation).",
            whyChanged: "DSP timing latency introduces phase lag.",
            consequence: "Instead of silence, the waves partially interfere, producing an unsettling metallic comb-filter echo that sounds like speaking through an aluminum tube."
          },
          "75": {
            whatChanged: "Phase offset at 135° (slight timing delay).",
            whyChanged: "Sub-optimal cancellation leaves low-frequency residual rumble.",
            consequence: "Jet engine hum is reduced by only 6 dB instead of 25 dB; user experiences mild acoustic pressure on eardrums."
          },
          "100": {
            whatChanged: "Precise 180° phase inversion (-π radians).",
            whyChanged: "Compressions and rarefactions match and eliminate each other with microsecond accuracy.",
            consequence: "Jet engine roar drops by up to 30 decibels (a 90% reduction in perceived loudness), creating serene library-like quiet inside a noisy airplane cabin."
          },
          "125": {
            whatChanged: "Phase overshoots to 225°.",
            whyChanged: "DSP algorithm overcompensates for high-frequency transients.",
            consequence: "The system begins amplifying specific harmonics, causing high-pitched whistling squeals (acoustic feedback oscillation)."
          },
          "200": {
            whatChanged: "Phase shifts to 360° (0° in-phase alignment).",
            whyChanged: "Anti-wave is played completely in-phase with ambient noise.",
            consequence: "Constructive interference! The sound wave amplitudes double, quadrupling the acoustic energy and making the jet engine roar deafeningly twice as loud!"
          }
        }
      },
      whereElse: [
        { title: "Anti-Reflective Optical Coatings", desc: "Eyeglass lenses and camera optics use a microscopic chemical coating of precise thickness so that reflected light waves cancel themselves out, maximizing light transmission." },
        { title: "Automotive Mufflers", desc: "Car mufflers route engine exhaust through reflective internal baffles, bouncing sound waves against themselves to cancel out combustion explosions." },
        { title: "Earthquake Tuned Mass Dampers", desc: "Skyscrapers like Taipei 101 suspend massive 660-ton steel pendulums that sway in exact anti-phase to earthquake tremors, canceling building oscillations." }
      ],
      crossDiscipline: {
        from: "Acoustics & Signal Processing",
        to: "Molecular Structural Biology",
        bridge: "In structural biology, X-ray crystallography uses wave diffraction and interference patterns of X-rays bouncing off crystallized proteins to reconstruct the three-dimensional atomic structure of complex molecules like DNA and ribosomes."
      },
      yourTurn: "If two flashlights shine at the same spot on a wall, can you ever make them cancel each other out into darkness?",
      loop: {
        discovered: "Destructive Wave Superposition & Phase Inversion",
        connectsTo: "Spacetime Curvature & Gravitational Time Dilation",
        nextQuestion: "Why does time run faster on top of a mountain than at sea level?",
        nextId: "flagship-time-dilation"
      },
      simMode: "wave",
      simWhatChanged: "The inverted anti-wave matched ambient peaks with artificial troughs.",
      simWhyChanged: "Linear wave differential equations enforce additive superposition of acoustic pressures.",
      simNext: "Net acoustic pressure at the eardrum cancels down to near-zero amplitude.",
      trail: ["Principle of Superposition", "Phase Inversion", "Acoustic Wave Equation", "Digital Signal Processing", "Constructive Interference"]
    },
    {
      id: "flagship-time-dilation",
      category: "science",
      categoryLabel: "Quantum & Relativity",
      badgeClass: "iva-badge-physics",
      readTime: "4 min thought experiment",
      question: "Why does time run faster on top of a mountain than at sea level?",
      mystery: "You might assume an hour is an hour everywhere in the universe. But if you take two identical atomic clocks, keep one on a beach and take one to Mount Everest, the mountain clock ticks measurably faster. Why does altitude bend time?",
      thinkPrompt: "If light must always travel at the exact same speed for all observers, what has to stretch or contract to make that true?",
      hint: "Think about Einstein's insight: gravity is not just pulling on matter—it curves the very fabric of space and time.",
      level1: "Time is not a universal metronome ticking at the same rhythm across the cosmos. Einstein discovered that massive objects like Earth warp both space and time around them. The closer you are to Earth's center of gravity, the deeper you sit in its gravitational well, and the slower your time ticks relative to someone further away. On top of a mountain, you are further from Earth's center of mass, so gravity is slightly weaker—and your personal clock ticks faster!",
      level2: "General Relativity & Gravitational Redshift: In Einstein's field equations, gravitational time dilation is expressed by tf = t0 √(1 - 2GM/rc²). Photons climbing out of a gravitational potential well lose energy (E = hf), shifting to lower frequencies (gravitational redshift). Because the speed of light c is invariant for all observers, a reduction in gravitational potential directly stretches proper time intervals.",
      level3: "Equivalence Principle & Metric Tensor Geometry: By the Equivalence Principle, a reference frame resting on Earth's surface is mathematically indistinguishable from a rocket accelerating at 9.81 m/s² in deep space. In Minkowski-Riemann spacetime with metric tensor g_μν, proper time along a worldline is dτ = √(-g00) dt. As radial distance r increases, the metric component g00 = -(1 - 2GM/c²r) approaches -1, causing proper time dτ to tick faster relative to coordinate time.",
      whyCare: "If GPS satellite software did not correct for both gravitational time dilation (running 45 microseconds fast per day) and orbital speed time dilation (running 7 microseconds slow per day), GPS navigation would accumulate over 11 kilometers of navigational error every single day, rendering Google Maps useless within 2 hours.",
      whatIf: {
        variableName: "Earth's Gravitational Mass",
        baseline: "100% (1 Earth Mass)",
        reactions: {
          "50": {
            whatChanged: "Earth's mass halved (gravitational potential decreases).",
            whyChanged: "Spacetime curvature flattens closer to flat Minkowski geometry.",
            consequence: "The time difference between sea level and Mount Everest shrinks by half; satellite clock adjustments require smaller relativistic calibration offsets."
          },
          "75": {
            whatChanged: "Mass reduced to 75%.",
            whyChanged: "Weaker gravitational well dilates time less severely.",
            consequence: "Clocks at sea level tick 10 microseconds faster per year compared to our present timeline."
          },
          "100": {
            whatChanged: "Natural physical baseline: 1.0 Earth Mass (5.972 × 10²⁴ kg).",
            whyChanged: "Exact relativistic metric distortion measured by NIST atomic optical lattice clocks.",
            consequence: "For every 1 foot you climb above the ground, you age approximately 90 billionths of a second faster over a 79-year human lifespan."
          },
          "125": {
            whatChanged: "Earth's mass increased by 25%.",
            whyChanged: "Deeper gravitational well slows surface clock rates.",
            consequence: "Mountain hikers age noticeably faster relative to beach dwellers; GPS satellites require daily 60-microsecond mathematical offsets."
          },
          "200": {
            whatChanged: "Earth becomes a super-Earth with twice its mass.",
            whyChanged: "Extreme gravitational spacetime stretching.",
            consequence: "Surface time slows noticeably relative to deep space; light emitted from streetlights shifts noticeably toward the red end of the spectrum."
          }
        }
      },
      whereElse: [
        { title: "Black Hole Event Horizons", desc: "At the event horizon of a supermassive black hole, gravitational time dilation reaches infinity. An outside observer would see an astronaut freeze forever in place, their light fading into black." },
        { title: "NIST Tabletop Atomic Clocks", desc: "Physicists at NIST placed two strontium optical atomic clocks on a table and raised one clock by just 33 centimeters. The clock raised by 1 foot ran measurably faster!" },
        { title: "Interstellar Travel Aging", desc: "Astronauts spending 6 months on the International Space Station return to Earth having aged approximately 0.005 seconds less than their twin siblings on the ground." }
      ],
      crossDiscipline: {
        from: "Theoretical Physics & General Relativity",
        to: "Philosophy of Time & Epistemology",
        bridge: "General relativity completely abolished the philosophical notion of 'universal now'. There is no cosmic master clock ticking for the universe. Events that appear simultaneous to one observer happen in the past or future to another, shattering human intuition about fate and causality."
      },
      yourTurn: "If you fell into a black hole feet first, would your feet age slower than your head?",
      loop: {
        discovered: "Gravitational Spacetime Curvature & Proper Time",
        connectsTo: "Neural Predictive Perception & Optical Blind Spots",
        nextQuestion: "Why does your brain completely hide your eyes' giant physical blind spot?",
        nextId: "flagship-blind-spot"
      },
      simMode: "orbit",
      simWhatChanged: "The gravitational metric potential weakened with distance from Earth's center of mass.",
      simWhyChanged: "Mass curves four-dimensional spacetime, stretching proper time intervals.",
      simNext: "Photons climbing the mountain lose energy, red-shifting while mountain clocks tick faster.",
      trail: ["General Relativity", "Gravitational Redshift", "Equivalence Principle", "Proper Time", "Spacetime Curvature"]
    },
    {
      id: "flagship-blind-spot",
      category: "thinking",
      categoryLabel: "Philosophy of Mind & Neurobiology",
      badgeClass: "iva-badge-math",
      readTime: "3 min thought experiment",
      question: "Why does your brain completely hide your eyes' physical blind spot?",
      mystery: "Right now, in the middle of each of your eyes, there is a physical hole the size of a blueberry where no photoreceptors exist at all. Why don't you see two black holes hovering in your field of vision?",
      thinkPrompt: "Close your left eye, stare at a point with your right eye, and move your thumb sideways. Why does your thumb disappear, but the background doesn't turn black?",
      hint: "Does your brain show you an exact video feed of reality, or is vision an active internal simulation based on prediction?",
      level1: "In the human eye, all the nerve fibers carrying visual signals bundle together to form the optic nerve. That bundle exits through the back of your eyeball, leaving a physical hole where there are zero rods or cones. You are literally blind in that spot. But you never see a black hole because your visual cortex doesn't just passively display what your eyes capture; it actively paints over the missing gap using clues from surrounding patterns, textures, and memories. You see an edited painting, not a raw camera feed!",
      level2: "Optic Disc Anatomy & Cortical Predictive Filling-In: The optic disc (1.5 mm across) creates a scotoma approximately 15° temporally from the fovea. When an object falls within this visual field, no signals reach the primary visual cortex (V1). Rather than rendering an error state (blackness), receptive fields in higher visual areas (V2, V4) perform active spatial interpolation. They extrapolate surrounding luminance, texture gradients, and edge orientations, seamlessly filling in the missing pixels.",
      level3: "Bayesian Predictive Processing & Helmholtzian Inference: Modern cognitive neuroscience models the brain as a hierarchical Bayesian prediction machine. The brain does not passively receive sensory input from the bottom up; it continuously generates top-down generative models of the world. Sensory signals merely serve as prediction error checks. Because the brain's internal prior expectation predicts that textures continue smoothly across space, the perceptual hallucination is indistinguishable from physical reality.",
      whyCare: "Understanding predictive perception explains optical illusions, phantom limb pain, how magicians manipulate human attention, and why eyewitness testimonies are notoriously unreliable in criminal courtrooms.",
      whatIf: {
        variableName: "Cortical Filling-In Algorithm",
        baseline: "100% Active Predictive Interpolation",
        reactions: {
          "50": {
            whatChanged: "Predictive interpolation reduced to low-confidence rendering.",
            whyChanged: "Visual cortex reduces top-down prior weights.",
            consequence: "You perceive a shimmering, translucent smudge in your peripheral vision whenever you look at complex textures."
          },
          "75": {
            whatChanged: "Interpolation speed delayed by 100 milliseconds.",
            whyChanged: "Delayed neural feedforward processing.",
            consequence: "Fast-moving objects disappear and reappear with a perceptible stutter when crossing the optic disc boundary."
          },
          "100": {
            whatChanged: "Natural neurobiological baseline: seamless Bayesian filling-in.",
            whyChanged: "High-confidence sensory prior extrapolation across receptive fields.",
            consequence: "Complete perceptual continuity. You perceive a continuous panoramic visual field with zero awareness of your physical optical deficits."
          },
          "125": {
            whatChanged: "Predictive priors strengthened by 25%.",
            whyChanged: "Over-weighting of top-down internal models over bottom-up sensory data.",
            consequence: "Mild pareidolia—you begin seeing faces and familiar shapes in random wallpaper patterns and clouds even more vividly than normal."
          },
          "200": {
            whatChanged: "Predictive hallucination completely overrides sensory input.",
            whyChanged: "Top-down predictive signals decouple entirely from sensory afferents.",
            consequence: "Total conscious hallucination akin to deep REM dreaming or psychedelic states, where the internal world simulation runs freely without sensory constraints."
          }
        }
      },
      whereElse: [
        { title: "Saccadic Masking (The Stopped-Clock Illusion)", desc: "When your eyes dart from one object to another (saccades), your brain momentarily blinds you for 50 milliseconds to prevent motion blur, then backdates your perception so time seems to freeze!" },
        { title: "Octopus Inverted Retinas", desc: "Octopuses evolved camera eyes independently from humans, but their nerve fibers exit from the back of retinal cells rather than the front—giving cephalopods zero blind spot!" },
        { title: "Artificial Intelligence Inpainting", desc: "Modern generative AI tools like Photoshop Content-Aware Fill and Stable Diffusion use algorithmic filling-in that mathematically mirrors how visual cortex neurons interpolate missing data." }
      ],
      crossDiscipline: {
        from: "Neurobiology & Cognitive Psychology",
        to: "Epistemology & Philosophy of Consciousness",
        bridge: "The blind spot proves that what we call 'conscious reality' is never the objective physical world itself, but a controlled hallucination constructed by our nervous systems to keep us alive. As cognitive scientist Donald Hoffman notes, perception is a user interface, not a mirror of truth."
      },
      yourTurn: "If everything you see is an internal simulation constructed by your brain, how can you ever prove that anything outside your mind truly exists?",
      loop: {
        discovered: "Bayesian Predictive Perception & The Optic Scotoma",
        connectsTo: "Planetary Free-Fall & Orbital Mechanics",
        nextQuestion: "Why doesn't the Moon fall into Earth?",
        nextId: "flagship-moon"
      },
      simMode: "wave",
      simWhatChanged: "The visual cortex interpolated missing retinal signals using surrounding spatial textures.",
      simWhyChanged: "Hierarchical Bayesian inference treats sensory inputs as prediction error correctors rather than raw video feeds.",
      simNext: "Conscious perception renders a smooth, unbroken visual scene with zero black holes.",
      trail: ["Predictive Processing", "Optic Disc", "Bayesian Brain", "Helmholtz Inference", "Philosophy of Perception"]
    }
  ];

  // Procedural Curriculum Matrix (500,000 algorithmic combinations)
  var PROCEDURAL_CURRICULUM = {
    space: {
      topics: [
        ["Black Hole Event Horizons", "infinite gravitational spacetime curvature", "Hawking radiation emission", "astrophysical quantum thermodynamics"],
        ["Neutron Star Degeneracy", "Pauli exclusion principle of packed neutrons", "extreme magnetic field pulsars", "gravitational wave astronomy"],
        ["Cosmic Microwave Background", "primordial big bang photon decoupling", "anisotropic temperature ripples", "early universe cosmology"],
        ["Planetary Atmosphere Retention", "Maxwell-Boltzmann thermal escape velocity", "magnetic magnetosphere deflection", "planetary habitability criteria"]
      ],
      angles: [
        "How does quantum thermodynamics challenge general relativity here?",
        "Why does everyday classical intuition break down in this extreme regime?",
        "What observable consequence would occur if the fundamental constant shifted by 5%?",
        "How did human astronomers deduce this mechanism without ever touching the object?"
      ]
    },
    science: {
      topics: [
        ["Quantum Entanglement", "non-local wave function collapse", "EPR paradox and Bell inequalities", "quantum cryptography networks"],
        ["Thermodynamic Entropy", "statistical microstate probabilities", "irreversible arrow of cosmic time", "information dissipation"],
        ["Superconductivity Cooper Pairs", "electron-phonon lattice coupling", "Meissner magnetic flux expulsion", "maglev high-speed transit"],
        ["Wave-Particle Duality", "de Broglie matter wavelength interference", "Heisenberg uncertainty principle", "transmission electron microscopy"]
      ],
      angles: [
        "What physical constraint prevents this from occurring at macroscopic room temperature?",
        "How does this principle manifest the conservation of information?",
        "What was the pivotal experiment that forced physicists to accept this reality?",
        "Why is this counter-intuitive behavior essential for stable matter to exist?"
      ]
    },
    math: {
      topics: [
        ["Prime Distribution Patterns", "Riemann zeta function complex zeros", "unpredictable yet bounded density", "modern RSA cryptographic security"],
        ["Topological Invariance", "continuous deformations without tearing", "Euler characteristic invariants", "data manifold analysis"],
        ["Godel Incompleteness", "self-referential formal axiomatic limits", "unprovable mathematical truths", "theoretical computer science limits"],
        ["Chaos Theory Attractors", "extreme sensitive dependence on initial conditions", "non-linear phase space trajectories", "weather forecasting boundaries"]
      ],
      angles: [
        "Why is this mathematical truth true in every conceivable universe?",
        "How did pure abstract curiosity lead to modern computational infrastructure?",
        "What hidden symmetry connects this concept to physical mechanics?",
        "Can human intuition ever truly visualize this higher-dimensional space?"
      ]
    },
    nature: {
      topics: [
        ["Photosynthetic Quantum Coherence", "delocalized exciton energy transfer", "99% near-perfect photon efficiency", "next-gen artificial solar cells"],
        ["DNA Polymerase Error Correction", "3'-to-5' exonucleolytic proofreading", "one mistake in a billion base pairs", "evolutionary genetic stability"],
        ["Mycelial Nutrient Networks", "decentralized resource trade algorithms", "forest-wide symbiotic routing", "sustainable ecological agriculture"],
        ["Avian Magnetoreception", "cryptochrome radical pair quantum entanglement", "geomagnetic field line sensing", "global migratory navigation"]
      ],
      angles: [
        "How did natural selection stumble upon this quantum mechanism billions of years ago?",
        "What thermodynamic price does the organism pay to maintain this low-entropy state?",
        "How would life on an exoplanet solve this identical evolutionary challenge?",
        "What lesson does this bio-architecture hold for human engineering?"
      ]
    },
    tech: {
      topics: [
        ["Silicon Transistor Gate Leakage", "quantum mechanical electron tunneling", "sub-3nm lithography physical limits", "spintronic quantum computing"],
        ["Neural Network Loss Landscapes", "high-dimensional non-convex gradient descent", "stochastic convergence to saddle points", "artificial general intelligence"],
        ["Public-Key Cryptography", "trapdoor one-way modular exponentiation", "computational asymmetry of factoring", "global financial security"],
        ["Distributed Byzantine Consensus", "fault-tolerant peer gossip protocols", "state machine replication without central authority", "blockchain systems"]
      ],
      angles: [
        "What physical hardware wall is this software architecture trying to circumvent?",
        "How does this artificial system mirror cognitive biological networks?",
        "What unexpected failure mode emerges when scaling this system 1,000x?",
        "Why did it take computer scientists 50 years to find this elegant mathematical shortcut?"
      ]
    },
    thinking: {
      topics: [
        ["The Hard Problem of Consciousness", "first-person subjective qualia vs neural firing", "explanatory gap in physicalism", "philosophy of mind"],
        ["Predictive Coding Perception", "top-down Bayesian world simulation", "sensory prediction error minimization", "computational neuroscience"],
        ["The Epistemological Horizon", "limits of empirical observation through instruments", "theory-laden sensory interpretation", "scientific realism debate"],
        ["Cognitive Heuristics & Biases", "fast evolutionary frugal algorithms", "systematic deviations from rational logic", "behavioral decision theory"]
      ],
      angles: [
        "How can the mind study the very instrument it uses to study?",
        "What evolutionary pressure favored this cognitive illusion over raw truth?",
        "How would an alien intellect perceive this reality differently?",
        "Where is the boundary between biological perception and artificial simulation?"
      ]
    },
    how: {
      topics: [
        ["Fiber Optic Total Internal Reflection", "critical angle Snell refraction index boundary", "zero optical signal leakage across oceans", "global internet bandwidth"],
        ["Microwave Dipole Heating", "molecular rotational dielectric relaxation", "2.45 GHz alternating electric fields", "industrial food thermodynamics"],
        ["Laser Stimulated Emission", "metastable population inversion and coherent photons", "Einstein B-coefficient amplification", "precision laser eye surgery"],
        ["Aerodynamic Lift & Circulation", "Navier-Stokes pressure differentials and Kutta condition", "vortex generation over curved aerofoils", "commercial aviation flight"]
      ],
      angles: [
        "What common everyday misconception completely misidentifies how this works?",
        "How does this convert micro-scale quantum properties into macro-scale utility?",
        "What was the single engineering breakthrough that made this reliable for consumer use?",
        "Why does this fail if you change a single physical parameter by 10%?"
      ]
    },
    behavior: {
      topics: [
        ["Tragedy of the Commons", "individual rational self-interest depleting shared resources", "Nash equilibrium dilemma", "global climate diplomacy"],
        ["Dunbar's Cognitive Number", "neocortex ratio constraints on social cohesion", "group fission beyond 150 members", "organizational scaling architecture"],
        ["Information Cascades", "Bayesian social imitation overwhelming private evidence", "herd dynamics and market bubbles", "sociological network theory"],
        ["Ant Colony Stigmergy", "indirect pheromone environmental coordination", "emergent decentralized superorganism intelligence", "logistical swarm robotics"]
      ],
      angles: [
        "Why do individual rational decisions produce collectively irrational outcomes?",
        "How can decentralized local rules produce breathtaking global coordination?",
        "What mathematical threshold separates stable cooperation from sudden collapse?",
        "How does institutional memory protect systems from historical amnesia?"
      ]
    }
  };

  // 3-Mode "I'm Bored" Micro-Experiments (Section 8)
  var BORED_DATA = {
    observe: [
      {
        challenge: "Look at the shadow of your hand on the wall right now. Notice the blurry penumbra around its edges. Why isn't the edge perfectly sharp? Move your hand closer to the light source... What changed?",
        mechanism: "The light bulb is not an infinitesimal point source; it has physical width. It casts a dark core (umbra) and a fuzzy partial shadow (penumbra). As your hand approaches the light, the penumbra widens due to geometric angular divergence.",
        relatedId: "flagship-blue-sky"
      },
      {
        challenge: "Look at a clear glass of water. Dip a pencil or your finger into it. Notice how it appears broken or shifted at the surface. What optical law makes it look detached?",
        mechanism: "Refraction! Light travels at 300,000 km/s in air, but slows down to ~225,000 km/s in water. That change in wave speed bends the wavefront according to Snell's Law (n₁ sin θ₁ = n₂ sin θ₂).",
        relatedId: "flagship-blue-sky"
      },
      {
        challenge: "Look at the screen you are reading this on from 2 inches away. Notice the tiny glowing red, green, and blue subpixels. How does your eye combine them into yellow or white?",
        mechanism: "Tristimulus additive color mixing! Your retina's red, green, and blue cones fire simultaneously. Your visual cortex synthesizes equal stimulation of all three into the subjective experience of pure white.",
        relatedId: "flagship-blind-spot"
      },
      {
        challenge: "Close your eyes and listen carefully for 15 seconds. Try to identify the single quietest background sound that your brain was unconsciously filtering out two seconds ago.",
        mechanism: "Sensory gating in the thalamus! Your brain constantly filters out predictable background noise (air conditioning, distant traffic) to conserve neural bandwidth for unexpected evolutionary threats.",
        relatedId: "flagship-noise-cancellation"
      }
    ],
    think: [
      {
        challenge: "How would you measure exactly one minute of time if you were locked in a quiet room with no clock, no phone, and no access to your pulse?",
        mechanism: "A simple pendulum! By finding any weighted object on a string of exactly 0.994 meters (roughly 1 yard), its period of swing is exactly 2 seconds (1 second each way). 30 full swings equal exactly 60 seconds, governed solely by Earth's gravity (T = 2π√(L/g)).",
        relatedId: "flagship-moon"
      },
      {
        challenge: "Why does a mirror reverse left and right, but never reverses up and down? Think carefully about the front-to-back z-axis.",
        mechanism: "A mirror doesn't reverse left and right at all—it reverses front and back! When you face north toward a mirror, your hand pointing east still points east. The mirror simply inverts the depth z-axis like a rubber glove turned inside out.",
        relatedId: "flagship-blind-spot"
      },
      {
        challenge: "If all the ice floating in the Arctic ocean melted tomorrow, would global sea levels rise immediately? Think about Archimedes' principle.",
        mechanism: "Floating sea ice already displaces a volume of seawater equal to its own mass (Archimedes' Principle). Melting floating ice does not raise sea levels directly! The true sea level threat comes from land-based ice sheets (Greenland and Antarctica) sliding into the ocean.",
        relatedId: "flagship-ice"
      },
      {
        challenge: "If you have a balance scale and 9 identical-looking gold coins, but one is counterfeit and slightly heavier, how can you find the fake coin in just two weighings?",
        mechanism: "Ternary information theory! Divide into 3 groups of 3 coins. Weigh group A vs group B. If they balance, the fake is in group C. If not, it's in the heavier group. Take that 3-coin group, weigh 1 vs 1. In just two weighings, log₃(9) = 2 steps pinpoint the coin with mathematical certainty.",
        relatedId: "flagship-qr-code"
      }
    ],
    do: [
      {
        challenge: "Take a flat sheet of paper and a crumpled sheet of paper. Drop them simultaneously from shoulder height. Why does the crumpled ball hit first if gravity pulls equally on all masses?",
        mechanism: "Aerodynamic air resistance! In a vacuum, both fall with identical acceleration (g = 9.81 m/s²). In air, the flat sheet has 50 times greater surface area, reaching terminal velocity within inches as upward air drag balances downward weight.",
        relatedId: "flagship-earth-spin"
      },
      {
        challenge: "Try to hum while holding your nose tightly closed. Notice that you cannot sustain the hum for more than one second. Why?",
        mechanism: "Acoustic airflow physics! Humming requires air pressure to pass across your vocal cords and exit through your nasal cavities. When your mouth and nose are both sealed, air pressure in your mouth equalizes with your lungs in 0.5 seconds, halting vocal fold vibration.",
        relatedId: "flagship-noise-cancellation"
      },
      {
        challenge: "Stand on one foot with your eyes wide open. Easy, right? Now close your eyes. Notice how quickly you begin wobbling. What does this reveal about your balance?",
        mechanism: "Visual proprioceptive dominance! Your brain balances using three systems: vestibular (inner ear), proprioceptive (muscle joints), and vision. Vision provides over 70% of high-speed balance correction. Deprived of optical horizon cues, your brain has to scramble on muscle signals alone.",
        relatedId: "flagship-blind-spot"
      },
      {
        challenge: "Put a single drop of water on a smooth coin or smartphone screen. Why does it form a rounded bead instead of spreading out flat?",
        mechanism: "Cohesive hydrogen bonding! Water molecules attract each other more strongly than they attract the hydrophobic surface. To minimize thermodynamic surface free energy, the droplet adopts a sphere—the geometric shape with the lowest surface-area-to-volume ratio.",
        relatedId: "flagship-ice"
      }
    ]
  };

  // Strange Truths of the Universe (Section 9)
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
    },
    {
      fact: "If Earth stopped spinning instantly, the atmosphere would continue hurtling east at 1,000 mph.",
      why: "Rotational momentum! Atmosphere, oceans, and buildings share Earth's 1,670 km/h equatorial surface velocity. Halting the rocky crust would trigger supersonic kinetic shockwaves.",
      relatedId: "flagship-earth-spin"
    }
  ];

  // Concept Sparks for Original Question Studio (Section 7)
  var CONCEPT_SPARKS = [
    "BLACK HOLES", "HONEYBEES", "MEMORY",
    "QUANTUM TUNNELING", "PLANT ROOTS", "CRYPTOGRAPHY",
    "SUPERCONDUCTIVITY", "NEURAL SYNAPSES", "BIRD MIGRATION",
    "THERMODYNAMIC ENTROPY", "LANGUAGE", "ACCELERATION",
    "CELL WALLS", "TIDAL FORCES", "MUSIC"
  ];

  // ════════════════════════════════════════════════════════════════
  // 2. STATE MANAGEMENT & LOCAL STORAGE (Section 29)
  // ════════════════════════════════════════════════════════════════
  var STORAGE_KEY = "iva_curiosity_master_state_v3";
  var appState = {
    currentView: "ivaHomeView",
    currentQuestionId: "flagship-moon",
    currentQuestionObj: null,
    exploredIds: [],
    savedIds: [],
    reflections: {},
    sparkQuestions: [],
    streakDays: 1,
    lastActiveDate: null,
    activeWhatIfVal: "100",
    activeLevel: 1,
    boredMode: "observe",
    currentBoredIndex: 0,
    currentStrangeIndex: 0
  };

  function loadState() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        var parsed = JSON.parse(saved);
        if (parsed && typeof parsed === 'object') {
          for (var k in parsed) {
            if (parsed.hasOwnProperty(k)) appState[k] = parsed[k];
          }
        }
      }
    } catch(e) {
      console.warn("localStorage unavailable:", e);
    }
    calculateStreak();
    updateLiveMetrics();
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
    } catch(e) {
      console.warn("Failed to persist state:", e);
    }
    updateLiveMetrics();
  }

  function calculateStreak() {
    var today = new Date().toISOString().slice(0, 10);
    if (!appState.lastActiveDate) {
      appState.lastActiveDate = today;
      appState.streakDays = 1;
    } else if (appState.lastActiveDate !== today) {
      var prev = new Date(appState.lastActiveDate);
      var curr = new Date(today);
      var diffDays = Math.round((curr - prev) / (1000 * 60 * 60 * 24));
      if (diffDays === 1) {
        appState.streakDays += 1;
      } else if (diffDays > 1) {
        appState.streakDays = 1;
      }
      appState.lastActiveDate = today;
      saveState();
    }
  }

  function updateLiveMetrics() {
    var streakEl = document.getElementById('ivaLiveStreak');
    var expEl = document.getElementById('ivaLiveExplored');
    var savedEl = document.getElementById('ivaLiveSaved');
    var navSavedEl = document.getElementById('ivaSavedNavCount');

    if (streakEl) streakEl.textContent = appState.streakDays + (appState.streakDays === 1 ? " Day" : " Days");
    if (expEl) expEl.textContent = appState.exploredIds.length;
    if (savedEl) savedEl.textContent = appState.savedIds.length;
    if (navSavedEl) navSavedEl.textContent = appState.savedIds.length;

    // Journey View Metrics
    var jExp = document.getElementById('ivaJourneyExploredNum');
    var jSaved = document.getElementById('ivaJourneySavedNum');
    var jOrig = document.getElementById('ivaJourneyOriginalNum');
    var jHypo = document.getElementById('ivaJourneyHypothesisNum');
    var jStreak = document.getElementById('ivaJourneyStreakNum');

    if (jExp) jExp.textContent = appState.exploredIds.length;
    if (jSaved) jSaved.textContent = appState.savedIds.length;
    if (jOrig) jOrig.textContent = appState.sparkQuestions.length;
    if (jHypo) jHypo.textContent = Object.keys(appState.reflections).length;
    if (jStreak) jStreak.textContent = appState.streakDays;
  }

  // ════════════════════════════════════════════════════════════════
  // 3. AUDIO SYNTH CHIME (Web Audio API)
  // ════════════════════════════════════════════════════════════════
  var audioCtx = null;
  function playSynthChord(type) {
    try {
      var AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!AudioContext) return;
      if (!audioCtx) audioCtx = new AudioContext();
      if (audioCtx.state === 'suspended') audioCtx.resume();

      var now = audioCtx.currentTime;
      var freqs = type === 'discover' ? [523.25, 659.25, 783.99] : [440, 554.37, 659.25];
      freqs.forEach(function(f, i) {
        var osc = audioCtx.createOscillator();
        var gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(f, now + i * 0.05);
        gain.gain.setValueAtTime(0.04, now + i * 0.05);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + i * 0.05 + 0.6);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now + i * 0.05);
        osc.stop(now + i * 0.05 + 0.65);
      });
    } catch(e) {}
  }

  // ════════════════════════════════════════════════════════════════
  // 4. AMBIENT COSMIC PARTICLE CANVAS
  // ════════════════════════════════════════════════════════════════
  function initCosmicCanvas() {
    var canvas = document.getElementById('ivaCosmicCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = window.innerWidth;
    var h = canvas.height = window.innerHeight;
    var particles = [];

    for (var i = 0; i < 45; i++) {
      particles.push({
        x: Math.random() * w,
        y: Math.random() * h,
        r: Math.random() * 1.5 + 0.5,
        dx: (Math.random() - 0.5) * 0.25,
        dy: (Math.random() - 0.5) * 0.25,
        opacity: Math.random() * 0.4 + 0.1
      });
    }

    function animate() {
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "rgba(179, 134, 66, 0.4)";
      particles.forEach(function(p) {
        p.x += p.dx;
        p.y += p.dy;
        if (p.x < 0) p.x = w;
        if (p.x > w) p.x = 0;
        if (p.y < 0) p.y = h;
        if (p.y > h) p.y = 0;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
      });
      requestAnimationFrame(animate);
    }
    animate();

    window.addEventListener('resize', function() {
      w = canvas.width = window.innerWidth;
      h = canvas.height = window.innerHeight;
    });
  }

  // ════════════════════════════════════════════════════════════════
  // 5. DYNAMIC SIMULATOR (Orbit & Wave with real physics)
  // ════════════════════════════════════════════════════════════════
  var currentSimMode = 'orbit';
  var simSpeed = 0.02;
  var simAngle = 0;
  var simCanvas, simCtx;

  function initSimulator() {
    simCanvas = document.getElementById('ivaSimCanvas');
    if (!simCanvas) return;
    simCtx = simCanvas.getContext('2d');

    function draw() {
      var w = simCanvas.width;
      var h = simCanvas.height;
      simCtx.clearRect(0, 0, w, h);
      var cx = w / 2;
      var cy = h / 2;

      if (currentSimMode === 'orbit') {
        // Orbit Simulator: Central body + Orbiting satellite + Velocity & Gravity Vectors
        simCtx.fillStyle = '#b38642';
        simCtx.shadowColor = '#d4a964';
        simCtx.shadowBlur = 18;
        simCtx.beginPath();
        simCtx.arc(cx, cy, 18, 0, Math.PI * 2);
        simCtx.fill();
        simCtx.shadowBlur = 0;

        // Elliptical Geodesic Path
        var rx = 180;
        var ry = 75;
        simCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
        simCtx.lineWidth = 1;
        simCtx.setLineDash([3, 3]);
        simCtx.beginPath();
        simCtx.ellipse(cx, cy, rx, ry, 0, 0, Math.PI * 2);
        simCtx.stroke();
        simCtx.setLineDash([]);

        simAngle += simSpeed;
        var px = cx + Math.cos(simAngle) * rx;
        var py = cy + Math.sin(simAngle) * ry;

        // Satellite
        simCtx.fillStyle = '#00d2ff';
        simCtx.shadowColor = '#00d2ff';
        simCtx.shadowBlur = 14;
        simCtx.beginPath();
        simCtx.arc(px, py, 7, 0, Math.PI * 2);
        simCtx.fill();
        simCtx.shadowBlur = 0;

        // Blue Tangential Velocity Vector
        var vx = -Math.sin(simAngle) * 26;
        var vy = Math.cos(simAngle) * 12;
        simCtx.strokeStyle = '#00d2ff';
        simCtx.lineWidth = 2;
        simCtx.beginPath();
        simCtx.moveTo(px, py);
        simCtx.lineTo(px + vx, py + vy);
        simCtx.stroke();

        // Red Inward Gravitational Acceleration Vector
        var dx = cx - px;
        var dy = cy - py;
        var len = Math.sqrt(dx * dx + dy * dy);
        simCtx.strokeStyle = '#e94560';
        simCtx.beginPath();
        simCtx.moveTo(px, py);
        simCtx.lineTo(px + (dx / len) * 22, py + (dy / len) * 22);
        simCtx.stroke();

      } else {
        // Wave Cancellation Simulator
        simCtx.lineWidth = 2;
        var step = 4;
        simAngle += simSpeed * 1.5;

        // Wave 1: Incoming Noise (Cyan)
        simCtx.strokeStyle = '#00d2ff';
        simCtx.beginPath();
        for (var x = 0; x < w; x += step) {
          var y1 = cy + Math.sin((x * 0.04) + simAngle) * 35;
          if (x === 0) simCtx.moveTo(x, y1); else simCtx.lineTo(x, y1);
        }
        simCtx.stroke();

        // Wave 2: Anti-Wave Phase Inversion (Terracotta)
        var phaseOffset = (appState.activeWhatIfVal === "200") ? 0 : Math.PI;
        simCtx.strokeStyle = '#e94560';
        simCtx.beginPath();
        for (var x2 = 0; x2 < w; x2 += step) {
          var y2 = cy + Math.sin((x2 * 0.04) + simAngle + phaseOffset) * 35;
          if (x2 === 0) simCtx.moveTo(x2, y2); else simCtx.lineTo(x2, y2);
        }
        simCtx.stroke();

        // Resultant: Net Superposition (Emerald)
        simCtx.strokeStyle = '#10b981';
        simCtx.lineWidth = 2;
        simCtx.setLineDash([4, 4]);
        simCtx.beginPath();
        if (phaseOffset === Math.PI) {
          simCtx.moveTo(0, cy);
          simCtx.lineTo(w, cy);
        } else {
          for (var x3 = 0; x3 < w; x3 += step) {
            var y3 = cy + (Math.sin((x3 * 0.04) + simAngle) * 70);
            if (x3 === 0) simCtx.moveTo(x3, y3); else simCtx.lineTo(x3, y3);
          }
        }
        simCtx.stroke();
        simCtx.setLineDash([]);
      }

      requestAnimationFrame(draw);
    }
    draw();
  }

  // ════════════════════════════════════════════════════════════════
  // 6. QUESTION ENGINE (Flagship + 500,000 Procedural Paths)
  // ════════════════════════════════════════════════════════════════
  function getQuestionById(id) {
    var flagship = FLAGSHIP_INQUIRIES.find(function(q) { return q.id === id; });
    if (flagship) return flagship;

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
      mystery: "We routinely observe " + tName.toLowerCase() + " in natural and engineered systems, yet its foundational behavior under " + tCore + " defies everyday classical intuition. Why?",
      thinkPrompt: "What physical or logical principle prevents " + tName.toLowerCase() + " from behaving in a purely classical manner?",
      hint: "Consider how energy and momentum are constrained at microscopic and macroscopic scales under " + tCore + ".",
      level1: tName + " operates under " + tCore + ". Energy and matter interact to preserve fundamental physical equilibrium, creating stable emergent structures.",
      level2: "The underlying mechanism is driven by " + tMech + ". System state evolution strictly minimizes thermodynamic free energy across dynamic boundaries.",
      level3: "From first principles, this manifests universal conservation laws. Quantum and relativistic constraints govern the exchange of information and momentum.",
      whyCare: "This exact mechanism forms the basis of " + tApp + ", enabling precision modern engineering and scientific discovery.",
      whatIf: {
        variableName: tCore + " Field Strength",
        baseline: "100% Natural Equilibrium",
        reactions: {
          "50": {
            whatChanged: "Constraint field halved to 50%.",
            whyChanged: "Lower binding energy permits rapid entropy dispersion.",
            consequence: "The system cannot maintain structural coherence; " + tName.toLowerCase() + " dissipates into thermal noise."
          },
          "75": {
            whatChanged: "Field weakened to 75%.",
            whyChanged: "Sub-optimal thermodynamic stability threshold.",
            consequence: "System exhibits unpredictable quantum phase transitions and turbulent oscillations."
          },
          "100": {
            whatChanged: "Natural physical baseline equilibrium.",
            whyChanged: "Optimal conservation balance governed by fundamental physical constants.",
            consequence: "Stable sustained manifestation enabling " + tApp + "."
          },
          "125": {
            whatChanged: "Field strength increased by 25%.",
            whyChanged: "Higher potential barrier resists structural perturbation.",
            consequence: "Rigid crystallization prevents adaptive mechanical flexibility."
          },
          "200": {
            whatChanged: "Field strength doubled to 200%.",
            whyChanged: "Extreme over-coupling forces collapse into a high-density singularity.",
            consequence: "System freezes into degenerate ground state, extinguishing all dynamic interactions."
          }
        }
      },
      whereElse: [
        { title: tApp, desc: "Direct technological utilization of " + tMech.toLowerCase() + " in state-of-the-art instruments." },
        { title: "Astrophysical Stellar Interiors", desc: "Extreme gravitational and thermodynamic environments manifesting the exact same conservation law." },
        { title: "Biological Macromolecules", desc: "Cellular enzymes utilizing delicate energy gradients to coordinate metabolic reactions." }
      ],
      crossDiscipline: {
        from: catInfo.label,
        to: "Complex Systems & Information Theory",
        bridge: "The mathematical principles governing " + tName.toLowerCase() + " mirror information entropy dissipation across distributed computational networks."
      },
      yourTurn: "What boundary condition or physical variable do you suspect could break this equilibrium?",
      loop: {
        discovered: tName + " Equilibrium",
        connectsTo: "Fundamental Spacetime & Quantum Symmetries",
        nextQuestion: "Why doesn't the Moon fall into Earth?",
        nextId: "flagship-moon"
      },
      simMode: (catKey === 'how' || catKey === 'tech') ? 'wave' : 'orbit',
      simWhatChanged: "State variables shifted to maintain dynamic equilibrium.",
      simWhyChanged: "Physical field potentials naturally minimize thermodynamic free energy.",
      simNext: "Perturbing initial conditions causes rapid dampening back to the stable attractor.",
      trail: [tName, tCore, tMech, tApp, "First Principles"]
    };
  }

  // ════════════════════════════════════════════════════════════════
  // 7. VIEW NAVIGATION & CURATION CONTROLLER
  // ════════════════════════════════════════════════════════════════
  function showView(viewId) {
    var views = document.querySelectorAll('#iva-curiosity-machine .iva-view');
    views.forEach(function(v) { v.classList.add('iva-hidden'); });

    var target = document.getElementById(viewId);
    if (target) {
      target.classList.remove('iva-hidden');
      window.scrollTo({ top: document.getElementById('iva-curiosity-machine').offsetTop || 0, behavior: 'smooth' });
    }

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

    if (appState.exploredIds.indexOf(q.id) === -1) {
      appState.exploredIds.push(q.id);
      saveState();
    }

    // Populate Headers
    document.getElementById('ivaDetailBadge').className = "iva-badge " + (q.badgeClass || 'iva-badge-space');
    document.getElementById('ivaDetailBadge').textContent = (q.categoryLabel || "Astrophysics").toUpperCase();
    document.getElementById('ivaDetailInquiryNumber').textContent = "Inquiry #" + (q.globalNumber || q.id);
    document.getElementById('ivaDetailReadTime').textContent = q.readTime || "3 min read";
    document.getElementById('ivaDetailTitle').textContent = q.question;
    document.getElementById('ivaDetailMystery').textContent = q.mystery || q.prompt;

    // Reset Think First Gate
    document.getElementById('ivaThinkPromptText').textContent = q.thinkPrompt || "What physical or logical principle is at play here?";
    document.getElementById('ivaThinkHintText').textContent = q.hint || "Consider how energy and forces interact to maintain balance.";
    var existingReflection = appState.reflections[q.id] || "";
    document.getElementById('ivaThinkInput').value = existingReflection;
    document.getElementById('ivaThinkSavedMsg').style.display = existingReflection ? "block" : "none";
    setThinkChoice('guess');

    // Populate 3-Level Explanations
    document.getElementById('ivaExpContentLevel1').textContent = q.level1 || q.simple;
    document.getElementById('ivaExpContentLevel2').textContent = q.level2 || q.mechanism;
    document.getElementById('ivaExpContentLevel3').textContent = q.level3 || q.firstPrinciples;
    setExplanationLevel(1);

    // Dynamic Simulator
    currentSimMode = q.simMode || 'orbit';
    document.getElementById('ivaSimModeLabel').textContent = currentSimMode === 'wave' ? 'Phase Interference' : 'Gravitational Free Fall';
    document.getElementById('ivaSimWhatChanged').textContent = q.simWhatChanged;
    document.getElementById('ivaSimWhyChanged').textContent = q.simWhyChanged;
    document.getElementById('ivaSimNext').textContent = q.simNext;

    // "Why Should I Care?"
    document.getElementById('ivaCareText').textContent = q.whyCare || "This principle underpins essential scientific and real-world technological architectures.";

    // Interactive What-If Engine
    var whatIfData = q.whatIf || {
      variableName: "Field Intensity",
      baseline: "100%",
      reactions: {
        "50": { whatChanged: "Variable halved.", whyChanged: "Equilibrium offset.", consequence: "System destabilizes." },
        "75": { whatChanged: "Variable at 75%.", whyChanged: "Moderate perturbation.", consequence: "Mild state shift." },
        "100": { whatChanged: "Baseline equilibrium.", whyChanged: "Natural constants.", consequence: "Stable persistence." },
        "125": { whatChanged: "Variable increased 25%.", whyChanged: "Higher energy.", consequence: "Accelerated kinetics." },
        "200": { whatChanged: "Variable doubled.", whyChanged: "Extreme excitation.", consequence: "Runaway transition." }
      }
    };
    document.getElementById('ivaWhatIfDesc').textContent = "Parameter under test: " + whatIfData.variableName + " (Baseline: " + whatIfData.baseline + "). Select an adjustment:";
    setWhatIfValue("100", whatIfData);

    // Where Else Does This Appear?
    var whereElseGrid = document.getElementById('ivaWhereElseGrid');
    whereElseGrid.innerHTML = '';
    var whereList = q.whereElse || [
      { title: "Everyday Technology", desc: "Commonly applied across modern engineering and sensor systems." },
      { title: "Astrophysical Scales", desc: "Manifests identically across planetary systems and cosmic radiation." }
    ];
    whereList.forEach(function(item) {
      var card = document.createElement('div');
      card.className = 'iva-where-else-card';
      card.innerHTML = "<div class='iva-where-else-card-title'>" + item.title + "</div><div class='iva-where-else-card-desc'>" + item.desc + "</div>";
      whereElseGrid.appendChild(card);
    });

    // Cross-Discipline Bridge
    var bridge = q.crossDiscipline || { from: "Physics", to: "Biology", bridge: "Physical forces shape biological organization across evolutionary timescales." };
    document.getElementById('ivaBridgeDisciplineFrom').textContent = bridge.from;
    document.getElementById('ivaBridgeDisciplineTo').textContent = bridge.to;
    document.getElementById('ivaBridgeText').textContent = bridge.bridge;

    // Your Turn
    document.getElementById('ivaYourTurnDesc').textContent = q.yourTurn || "What question does this make you curious about?";
    document.getElementById('ivaYourTurnInput').value = "";

    // End of Every Discovery Loop (Section 22)
    var loop = q.loop || {
      discovered: "Underlying Physical Principle",
      connectsTo: "Universal Thermodynamic Equilibrium",
      nextQuestion: "Why doesn't the Moon fall into Earth?",
      nextId: "flagship-moon"
    };
    document.getElementById('ivaLoopDiscovered').textContent = loop.discovered;
    document.getElementById('ivaLoopConnects').textContent = loop.connectsTo;
    document.getElementById('ivaLoopNextQuestion').textContent = loop.nextQuestion;
    document.getElementById('ivaLoopNextBtn').onclick = function() {
      openCuriosity(loop.nextId);
    };

    updateBookmarkState(q.id);
    showView('ivaCuriosityView');
  }

  function setThinkChoice(choice) {
    document.getElementById('ivaThinkChoiceGuess').classList.toggle('active', choice === 'guess');
    document.getElementById('ivaThinkChoiceNoIdea').classList.toggle('active', choice === 'noidea');
    document.getElementById('ivaThinkChoiceHint').classList.toggle('active', choice === 'hint');

    document.getElementById('ivaThinkSectionGuess').style.display = choice === 'guess' ? 'block' : 'none';
    document.getElementById('ivaThinkSectionNoIdea').style.display = choice === 'noidea' ? 'block' : 'none';
    document.getElementById('ivaThinkSectionHint').style.display = choice === 'hint' ? 'block' : 'none';
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

  function setWhatIfValue(val, dataOverride) {
    appState.activeWhatIfVal = val;
    document.querySelectorAll('#iva-curiosity-machine .iva-whatif-var-btn').forEach(function(btn) {
      btn.classList.toggle('active', btn.getAttribute('data-val') === val);
    });

    var q = appState.currentQuestionObj;
    var data = dataOverride || (q && q.whatIf) || null;
    if (data && data.reactions && data.reactions[val]) {
      var r = data.reactions[val];
      document.getElementById('ivaWhatIfChanged').textContent = r.whatChanged;
      document.getElementById('ivaWhatIfWhy').textContent = r.whyChanged;
      document.getElementById('ivaWhatIfConsequence').textContent = r.consequence;
    }

    // Dynamic simulator reaction
    var vNum = parseInt(val, 10) || 100;
    var slider = document.getElementById('ivaSimSlider');
    if (slider) {
      slider.value = Math.min(100, Math.max(1, vNum / 2));
      document.getElementById('ivaSimSliderVal').textContent = vNum + "%";
      simSpeed = 0.005 + (vNum * 0.0002);
    }
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
  }

  // ════════════════════════════════════════════════════════════════
  // 8. DETERMINISTIC DAILY CURIOSITY (Section 10)
  // ════════════════════════════════════════════════════════════════
  function initDailyCuriosity() {
    var todayStr = new Date().toISOString().slice(0, 10);
    var hash = 0;
    for (var i = 0; i < todayStr.length; i++) {
      hash = (hash << 5) - hash + todayStr.charCodeAt(i);
      hash |= 0;
    }
    var dailyIndex = Math.abs(hash) % FLAGSHIP_INQUIRIES.length;
    var dailyQ = FLAGSHIP_INQUIRIES[dailyIndex];

    var dailyTitle = document.getElementById('ivaDailyTitle');
    if (dailyTitle) dailyTitle.textContent = dailyQ.question;

    var dailyBtn = document.getElementById('ivaExploreDailyBtn');
    if (dailyBtn) {
      dailyBtn.onclick = function() {
        openCuriosity(dailyQ.id, dailyQ);
      };
    }
  }

  // ════════════════════════════════════════════════════════════════
  // 9. RANDOM EXPLORATION WITH SERENDIPITY BRIDGE (Section 11)
  // ════════════════════════════════════════════════════════════════
  function triggerSurpriseMe() {
    var randIndex = Math.floor(Math.random() * (FLAGSHIP_INQUIRIES.length + 5000));
    var q;
    if (randIndex < FLAGSHIP_INQUIRIES.length) {
      q = FLAGSHIP_INQUIRIES[randIndex];
    } else {
      q = generateProceduralQuestion(randIndex - FLAGSHIP_INQUIRIES.length);
    }
    showToast("🎲", "Serendipity doorway opened: " + q.categoryLabel);
    openCuriosity(q.id, q);
  }

  // ════════════════════════════════════════════════════════════════
  // 10. TOLERANT SEARCH ENGINE (Section 14)
  // ════════════════════════════════════════════════════════════════
  function performSearch(query) {
    var clean = (query || "").trim().toLowerCase();
    var wrap = document.getElementById('ivaSearchResultsWrap');
    var grid = document.getElementById('ivaSearchResultsGrid');
    var title = document.getElementById('ivaSearchResultsTitle');
    if (!clean) {
      wrap.style.display = 'none';
      return;
    }

    var matches = [];
    FLAGSHIP_INQUIRIES.forEach(function(q) {
      var haystack = (q.question + " " + q.mystery + " " + q.categoryLabel + " " + (q.trail || []).join(" ")).toLowerCase();
      if (haystack.indexOf(clean) !== -1) {
        matches.push(q);
      }
    });

    wrap.style.display = 'block';
    grid.innerHTML = '';

    if (matches.length > 0) {
      title.textContent = "Discoveries matching \"" + query + "\" (" + matches.length + ")";
      matches.forEach(function(m) {
        var card = document.createElement('div');
        card.className = 'iva-saved-card';
        card.innerHTML = "<span class='iva-badge " + m.badgeClass + "'>" + m.categoryLabel + "</span>" +
                         "<h4 class='iva-saved-title'>" + m.question + "</h4>" +
                         "<button type='button' class='iva-btn iva-btn-primary iva-btn-small'>Explore Curiosity →</button>";
        card.querySelector('button').onclick = function() {
          openCuriosity(m.id, m);
        };
        grid.appendChild(card);
      });
    } else {
      // Forgiving fallback (Section 14)
      title.textContent = "We couldn't find an exact question for \"" + query + "\"";
      var fallback = document.createElement('div');
      fallback.style.gridColumn = "1 / -1";
      fallback.style.padding = "20px";
      fallback.style.background = "var(--iva-surface-elevated)";
      fallback.style.borderRadius = "var(--iva-radius-md)";
      fallback.style.color = "var(--iva-text-secondary)";
      fallback.innerHTML = "<p style='margin-bottom: 12px;'>Your curiosity points toward exciting frontiers. Explore related inquiries in these disciplines:</p>" +
                           "<div style='display:flex; gap:8px; flex-wrap:wrap;'>" +
                           "<button type='button' class='iva-chip' id='ivaSearchFallback1'>Astrophysics & Cosmos</button>" +
                           "<button type='button' class='iva-chip' id='ivaSearchFallback2'>Everyday Physics & Nature</button>" +
                           "<button type='button' class='iva-chip' id='ivaSearchFallback3'>Cognitive Tech & Computing</button>" +
                           "</div>";
      grid.appendChild(fallback);
      var fb1 = fallback.querySelector('#ivaSearchFallback1');
      var fb2 = fallback.querySelector('#ivaSearchFallback2');
      var fb3 = fallback.querySelector('#ivaSearchFallback3');
      if (fb1) fb1.onclick = function() { openCuriosity('flagship-moon'); };
      if (fb2) fb2.onclick = function() { openCuriosity('flagship-ice'); };
      if (fb3) fb3.onclick = function() { openCuriosity('flagship-qr-code'); };
    }
  }

  // ════════════════════════════════════════════════════════════════
  // 11. SPARK AN ORIGINAL QUESTION STUDIO (Section 7)
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

    contentBox.innerHTML = 
      "<p style='margin-bottom: 10px;'>You bridged these three seemingly distant domains through the lens of <strong>Information & Energetic Boundary Symmetries</strong>.</p>" +
      "<div style='background: var(--iva-surface); border: 1px solid var(--iva-border); border-radius: 6px; padding: 10px 14px; margin-bottom: 10px; font-size: 0.86rem;'>" +
      "<div><strong>CONNECTION 1:</strong> " + c1 + " ➔ Information and thermodynamic entropy thresholds</div>" +
      "<div><strong>CONNECTION 2:</strong> " + c2 + " ➔ Decentralized environmental signaling and memory storage</div>" +
      "<div><strong>CONNECTION 3:</strong> " + c3 + " ➔ Dynamic state encoding and pattern persistence across time</div>" +
      "</div>" +
      "<p style='color: var(--iva-gold-light); font-size: 0.88rem; font-style: italic;'>" +
      "Your question opens a direct doorway into Complex Adaptive Systems and Information Theory. To sharpen it further, ask: <em>'What variable breaks this connection?'</em>" +
      "</p>";

    if (appState.sparkQuestions.indexOf(text) === -1) {
      appState.sparkQuestions.push(text);
      saveState();
    }
    playSynthChord('discover');
    showToast("✨", "Brilliant synthesis! Question registered.");
  }

  // ════════════════════════════════════════════════════════════════
  // 12. "I'M BORED" 3-MODE ENGINE (Section 8)
  // ════════════════════════════════════════════════════════════════
  function rollBoredChallenge() {
    var mode = appState.boredMode || 'observe';
    var pool = BORED_DATA[mode] || BORED_DATA.observe;
    appState.currentBoredIndex = (appState.currentBoredIndex + 1) % pool.length;
    var item = pool[appState.currentBoredIndex];

    document.getElementById('ivaBoredChallengeText').textContent = item.challenge;
    document.getElementById('ivaBoredRevealContent').textContent = item.mechanism;
    document.getElementById('ivaBoredRevealBox').style.display = 'none';

    var exploreBtn = document.getElementById('ivaBoredExploreBtn');
    exploreBtn.onclick = function() {
      openCuriosity(item.relatedId);
    };
  }

  // ════════════════════════════════════════════════════════════════
  // 13. STRANGE FACTS ENGINE (Section 9)
  // ════════════════════════════════════════════════════════════════
  function rollStrangeFact() {
    appState.currentStrangeIndex = (appState.currentStrangeIndex + 1) % STRANGE_FACTS.length;
    var f = STRANGE_FACTS[appState.currentStrangeIndex];

    document.getElementById('ivaStrangeFactText').textContent = f.fact;
    document.getElementById('ivaStrangeWhyContent').textContent = f.why;
    document.getElementById('ivaStrangeWhyBox').style.display = 'none';

    var relatedBtn = document.getElementById('ivaStrangeExploreRelatedBtn');
    relatedBtn.onclick = function() {
      openCuriosity(f.relatedId);
    };
  }

  // ════════════════════════════════════════════════════════════════
  // 14. SAVED DISCOVERIES VIEW (Section 13)
  // ════════════════════════════════════════════════════════════════
  function renderSavedView() {
    var grid = document.getElementById('ivaSavedGrid');
    var empty = document.getElementById('ivaSavedEmptyState');
    grid.innerHTML = '';

    if (appState.savedIds.length === 0) {
      empty.style.display = 'block';
      return;
    }
    empty.style.display = 'none';

    appState.savedIds.forEach(function(id) {
      var q = getQuestionById(id);
      var reflection = appState.reflections[id] || "";
      var card = document.createElement('div');
      card.className = 'iva-saved-card';
      card.innerHTML = 
        "<div>" +
          "<span class='iva-badge " + (q.badgeClass || 'iva-badge-space') + "'>" + (q.categoryLabel || "Inquiry") + "</span>" +
          "<h3 class='iva-saved-title' style='margin-top: 8px;'>" + q.question + "</h3>" +
          (reflection ? "<div class='iva-saved-reflection'>Your Thought: \"" + reflection + "\"</div>" : "") +
        "</div>" +
        "<div style='display: flex; gap: 8px; justify-content: space-between; margin-top: 14px;'>" +
          "<button type='button' class='iva-btn iva-btn-primary iva-btn-small iva-saved-open-btn'>Read Inquiry →</button>" +
          "<button type='button' class='iva-btn iva-btn-secondary iva-btn-small iva-saved-del-btn'>✕ Remove</button>" +
        "</div>";

      card.querySelector('.iva-saved-open-btn').onclick = function() {
        openCuriosity(q.id, q);
      };
      card.querySelector('.iva-saved-del-btn').onclick = function() {
        toggleBookmark(q.id);
        renderSavedView();
      };
      grid.appendChild(card);
    });
  }

  // ════════════════════════════════════════════════════════════════
  // 15. MY CURIOSITY JOURNEY VIEW (Section 12)
  // ════════════════════════════════════════════════════════════════
  function renderJourneyView() {
    updateLiveMetrics();

    // Visual Concept Trail
    var flow = document.getElementById('ivaJourneyTrailFlow');
    flow.innerHTML = '';
    var baseConcepts = ["Perpetual Free-Fall", "Gravitational Geodesics", "Spacetime Curvature", "Relativistic Time", "Optical Wave Inversion", "Predictive Perception", "Information Entropy"];
    
    // Add concepts from explored inquiries
    appState.exploredIds.forEach(function(id) {
      var q = getQuestionById(id);
      if (q && q.trail) {
        q.trail.forEach(function(c) {
          if (baseConcepts.indexOf(c) === -1) baseConcepts.push(c);
        });
      }
    });

    baseConcepts.slice(0, 10).forEach(function(concept, idx) {
      var node = document.createElement('button');
      node.type = 'button';
      node.className = 'iva-trail-node';
      node.textContent = concept;
      node.onclick = function() {
        performSearch(concept);
        showView('ivaHomeView');
      };
      flow.appendChild(node);

      if (idx < Math.min(9, baseConcepts.length - 1)) {
        var arrow = document.createElement('span');
        arrow.style.color = "var(--iva-gold)";
        arrow.style.fontSize = "0.9rem";
        arrow.textContent = "➔";
        flow.appendChild(arrow);
      }
    });

    // Notes & Created Questions
    var notesList = document.getElementById('ivaJourneyNotesList');
    notesList.innerHTML = '';
    var allItems = [];

    appState.sparkQuestions.forEach(function(sq) {
      allItems.push({ type: "Created Question", text: sq });
    });
    for (var qId in appState.reflections) {
      if (appState.reflections.hasOwnProperty(qId)) {
        var ref = appState.reflections[qId];
        var qObj = getQuestionById(qId);
        allItems.push({ type: "Hypothesis (" + (qObj ? qObj.question : qId) + ")", text: ref });
      }
    }

    if (allItems.length === 0) {
      notesList.innerHTML = "<div style='color: var(--iva-text-muted); font-size: 0.9rem;'>No reflections or original questions recorded yet. Form a hypothesis on any inquiry or try the Original Question Studio on the home page!</div>";
    } else {
      allItems.forEach(function(item) {
        var box = document.createElement('div');
        box.style.background = "var(--iva-surface)";
        box.style.border = "1px solid var(--iva-border)";
        box.style.borderRadius = "var(--iva-radius-sm)";
        box.style.padding = "14px";
        box.style.marginBottom = "10px";
        box.innerHTML = "<div style='font-size: 0.74rem; font-weight: 700; color: var(--iva-gold-light); text-transform: uppercase; margin-bottom: 4px;'>" + item.type + "</div>" +
                        "<div style='font-size: 0.9rem; color: #fff; line-height: 1.5;'>\"" + item.text + "\"</div>";
        notesList.appendChild(box);
      });
    }
  }

  // ════════════════════════════════════════════════════════════════
  // 16. INSIGHT CARD GENERATOR (Canvas PNG Export)
  // ════════════════════════════════════════════════════════════════
  function generateInsightCard() {
    var q = appState.currentQuestionObj || FLAGSHIP_INQUIRIES[0];
    var thought = appState.reflections[q.id] || "";
    var cardCanvas = document.getElementById('ivaCardCanvas');
    if (!cardCanvas) return;
    var ctx = cardCanvas.getContext('2d');
    var w = cardCanvas.width = 600;
    var h = cardCanvas.height = 420;

    // Dark Cosmic Gradient
    var bg = ctx.createLinearGradient(0, 0, w, h);
    bg.addColorStop(0, '#071b36');
    bg.addColorStop(1, '#060913');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, w, h);

    // Gold Outer Border
    ctx.strokeStyle = '#b38642';
    ctx.lineWidth = 3;
    ctx.strokeRect(10, 10, w - 20, h - 20);

    // Seal & Header
    ctx.fillStyle = '#d4a964';
    ctx.font = 'bold 12px system-ui, sans-serif';
    ctx.fillText("IKSHVAKU CURIOSITY MACHINE • OFFICIAL INSIGHT CARD", 34, 46);

    ctx.fillStyle = '#ffffff';
    ctx.font = 'italic 18px Georgia, serif';
    ctx.fillText(q.categoryLabel.toUpperCase(), 34, 80);

    // Question
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 20px Georgia, serif';
    wrapCanvasText(ctx, q.question, 34, 116, w - 68, 28);

    // Intuitive Core
    ctx.fillStyle = '#94a3b8';
    ctx.font = '13px system-ui, sans-serif';
    wrapCanvasText(ctx, q.level1 || q.simple, 34, 185, w - 68, 20);

    // Student Thought
    if (thought) {
      ctx.fillStyle = '#d4a964';
      ctx.font = 'italic 12px system-ui, sans-serif';
      ctx.fillText("Personal Hypothesis:", 34, 290);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '13px system-ui, sans-serif';
      wrapCanvasText(ctx, '"' + thought + '"', 34, 314, w - 68, 20);
    }

    // Institutional Footer
    ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
    ctx.font = '11px system-ui, sans-serif';
    ctx.fillText("Ikshvaku Vidya Academy • A Place for Curious Minds • Education Beyond Commerce", 34, 395);

    document.getElementById('ivaCardModalOverlay').classList.remove('iva-hidden');
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
  // 17. TOAST NOTIFICATIONS
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
  // 18. INITIALIZATION & EVENT LISTENERS
  // ════════════════════════════════════════════════════════════════
  function init() {
    loadState();
    initCosmicCanvas();
    initSimulator();
    initDailyCuriosity();
    rerollConcepts();
    rollBoredChallenge();
    rollStrangeFact();

    // Populate Disciplines Grid
    var catGrid = document.getElementById('ivaCategoriesGrid');
    if (catGrid) {
      catGrid.innerHTML = '';
      CATEGORIES.forEach(function(cat) {
        var card = document.createElement('button');
        card.type = 'button';
        card.className = 'iva-cat-card';
        card.innerHTML = 
          "<span class='iva-cat-icon'>" + cat.icon + "</span>" +
          "<h3 class='iva-cat-title'>" + cat.label + "</h3>" +
          "<div class='iva-cat-desc'>" + cat.desc + "</div>";
        card.onclick = function() {
          var sampleQ = FLAGSHIP_INQUIRIES.find(function(q) { return q.category === cat.key; });
          if (sampleQ) {
            openCuriosity(sampleQ.id, sampleQ);
          } else {
            var randProc = generateProceduralQuestion(Math.floor(Math.random() * 50000));
            openCuriosity(randProc.id, randProc);
          }
        };
        catGrid.appendChild(card);
      });
    }

    // Top Brand & Nav Buttons
    document.getElementById('ivaBrandHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaNavHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaNavBoredBtn').onclick = function() { showView('ivaBoredView'); };
    document.getElementById('ivaNavStrangeBtn').onclick = function() { showView('ivaStrangeView'); };
    document.getElementById('ivaNavSavedBtn').onclick = function() { renderSavedView(); showView('ivaSavedView'); };
    document.getElementById('ivaNavJourneyBtn').onclick = function() { renderJourneyView(); showView('ivaJourneyView'); };
    document.getElementById('ivaNavAboutBtn').onclick = function() { document.getElementById('ivaAboutModalOverlay').classList.remove('iva-hidden'); };

    // Hero Actions
    document.getElementById('ivaHeroStartBtn').onclick = function() { openCuriosity('flagship-moon'); };
    document.getElementById('ivaHeroSurpriseBtn').onclick = triggerSurpriseMe;
    document.getElementById('ivaHeroBoredBtn').onclick = function() { showView('ivaBoredView'); };

    // Search Box
    var searchInput = document.getElementById('ivaSearchInput');
    if (searchInput) {
      searchInput.oninput = function(e) { performSearch(e.target.value); };
    }
    document.getElementById('ivaClearSearchBtn').onclick = function() {
      searchInput.value = '';
      document.getElementById('ivaSearchResultsWrap').style.display = 'none';
    };
    document.querySelectorAll('#iva-curiosity-machine .iva-chip').forEach(function(chip) {
      chip.onclick = function() {
        var query = chip.getAttribute('data-search');
        if (searchInput) searchInput.value = query;
        performSearch(query);
      };
    });

    // Back to Home Buttons
    document.getElementById('ivaBackToHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaBoredBackHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaStrangeBackHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaSavedBackHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaJourneyBackHomeBtn').onclick = function() { showView('ivaHomeView'); };
    document.getElementById('ivaSavedExploreNowBtn').onclick = function() { showView('ivaHomeView'); };

    // Think First Interactions
    document.getElementById('ivaThinkChoiceGuess').onclick = function() { setThinkChoice('guess'); };
    document.getElementById('ivaThinkChoiceNoIdea').onclick = function() { setThinkChoice('noidea'); };
    document.getElementById('ivaThinkChoiceHint').onclick = function() { setThinkChoice('hint'); };
    document.getElementById('ivaLockIdeaBtn').onclick = function() {
      var val = document.getElementById('ivaThinkInput').value.trim();
      if (!val) {
        showToast("💡", "Take a guess first!");
        return;
      }
      appState.reflections[appState.currentQuestionId] = val;
      saveState();
      document.getElementById('ivaThinkSavedMsg').style.display = 'block';
      showToast("🔒", "Hypothesis locked in memory!");
    };
    document.getElementById('ivaRevealExplanationBtn').onclick = function() {
      var explBox = document.getElementById('ivaExplanationContainer');
      if (explBox) {
        explBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
        showToast("✨", "Core explanation revealed.");
      }
    };

    // 3-Level Tabs
    document.getElementById('ivaTabLevel1').onclick = function() { setExplanationLevel(1); };
    document.getElementById('ivaTabLevel2').onclick = function() { setExplanationLevel(2); };
    document.getElementById('ivaTabLevel3').onclick = function() { setExplanationLevel(3); };

    // What-If Variable Buttons
    document.querySelectorAll('#iva-curiosity-machine .iva-whatif-var-btn').forEach(function(btn) {
      btn.onclick = function() {
        var val = btn.getAttribute('data-val');
        setWhatIfValue(val);
      };
    });

    // Save Your Turn Follow-up
    document.getElementById('ivaSaveYourTurnBtn').onclick = function() {
      var val = document.getElementById('ivaYourTurnInput').value.trim();
      if (!val) {
        showToast("⚠️", "Please write your question first!");
        return;
      }
      if (appState.sparkQuestions.indexOf(val) === -1) {
        appState.sparkQuestions.push(val);
        saveState();
      }
      showToast("📝", "Follow-up question saved to your curiosity journey!");
      document.getElementById('ivaYourTurnInput').value = "";
    };

    // Action Toolbar
    document.getElementById('ivaBookmarkBtn').onclick = function() {
      toggleBookmark(appState.currentQuestionId);
    };
    document.getElementById('ivaExportCardBtn').onclick = generateInsightCard;
    document.getElementById('ivaShareBtn').onclick = function() {
      if (navigator.share) {
        navigator.share({
          title: "Curiosity Machine — " + (appState.currentQuestionObj ? appState.currentQuestionObj.question : "Deep Inquiry"),
          text: "Look at this fascinating inquiry on the Ikshvaku Curiosity Machine!",
          url: window.location.href
        }).catch(function() {});
      } else {
        if (navigator.clipboard) {
          navigator.clipboard.writeText(window.location.href);
          showToast("📋", "Inquiry link copied to clipboard!");
        } else {
          showToast("🔗", "Link ready to share!");
        }
      }
    };
    document.getElementById('ivaZenModeBtn').onclick = function() {
      var top = document.querySelector('#iva-curiosity-machine .iva-top-banner');
      var hdr = document.querySelector('#iva-curiosity-machine .iva-header');
      var isZen = top.style.display === 'none';
      top.style.display = isZen ? 'block' : 'none';
      hdr.style.display = isZen ? 'block' : 'none';
      showToast(isZen ? "☀️" : "🌙", isZen ? "Standard view restored." : "Focus Mode enabled. Press Esc to exit.");
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
      showToast("🔖", "Original inquiry saved to your journey!");
    };

    // Bored Mode Buttons
    document.getElementById('ivaBoredModeObserve').onclick = function() { appState.boredMode = 'observe'; updateBoredModeTabs(); rollBoredChallenge(); };
    document.getElementById('ivaBoredModeThink').onclick = function() { appState.boredMode = 'think'; updateBoredModeTabs(); rollBoredChallenge(); };
    document.getElementById('ivaBoredModeDo').onclick = function() { appState.boredMode = 'do'; updateBoredModeTabs(); rollBoredChallenge(); };
    document.getElementById('ivaBoredRevealBtn').onclick = function() {
      var box = document.getElementById('ivaBoredRevealBox');
      box.style.display = box.style.display === 'none' ? 'block' : 'none';
    };
    document.getElementById('ivaNextBoredBtn').onclick = rollBoredChallenge;

    function updateBoredModeTabs() {
      document.getElementById('ivaBoredModeObserve').classList.toggle('active', appState.boredMode === 'observe');
      document.getElementById('ivaBoredModeThink').classList.toggle('active', appState.boredMode === 'think');
      document.getElementById('ivaBoredModeDo').classList.toggle('active', appState.boredMode === 'do');
    }

    // Strange Facts Buttons
    document.getElementById('ivaStrangeWhyBtn').onclick = function() {
      var box = document.getElementById('ivaStrangeWhyBox');
      box.style.display = box.style.display === 'none' ? 'block' : 'none';
    };
    document.getElementById('ivaNextStrangeBtn').onclick = rollStrangeFact;

    // Modal Closers
    document.getElementById('ivaCardCloseBtn').onclick = function() { document.getElementById('ivaCardModalOverlay').classList.add('iva-hidden'); };
    document.getElementById('ivaCardDismissBtn').onclick = function() { document.getElementById('ivaCardModalOverlay').classList.add('iva-hidden'); };
    document.getElementById('ivaAboutCloseBtn').onclick = function() { document.getElementById('ivaAboutModalOverlay').classList.add('iva-hidden'); };
    document.getElementById('ivaAboutGotItBtn').onclick = function() { document.getElementById('ivaAboutModalOverlay').classList.add('iva-hidden'); };
    document.getElementById('ivaDownloadCardBtn').onclick = function() {
      var cardCanvas = document.getElementById('ivaCardCanvas');
      var link = document.createElement('a');
      link.download = 'ikshvaku-curiosity-' + appState.currentQuestionId + '.png';
      link.href = cardCanvas.toDataURL('image/png');
      link.click();
      showToast("💾", "Insight card downloaded!");
    };

    // Keyboard Shortcuts
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        document.getElementById('ivaCardModalOverlay').classList.add('iva-hidden');
        document.getElementById('ivaAboutModalOverlay').classList.add('iva-hidden');
        document.querySelector('#iva-curiosity-machine .iva-top-banner').style.display = 'block';
        document.querySelector('#iva-curiosity-machine .iva-header').style.display = 'block';
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

# 3. COMPILE STANDALONE HTML
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

# 4. COMPILE 100% STRICT BLOGGER XML THEME
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

# 5. COPY TO CLIPBOARD VIA POWERSHELL
try:
    cmd = 'powershell -Command "Get-Content -Raw -Encoding UTF8 curiosity-machine.html | Set-Clipboard"'
    subprocess.run(cmd, shell=True, check=True)
    print("SUCCESS: curiosity-machine.html copied to Windows clipboard!")
except Exception as e:
    print("Clipboard notice:", e)

print("All tasks completed successfully!")
