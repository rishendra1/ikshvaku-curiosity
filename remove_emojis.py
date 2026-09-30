# -*- coding: utf-8 -*-
"""
remove_emojis.py
Cleans all distracting, childish emojis from generate_master_suite.py
Restores a prestigious, calm, academic aesthetic (like MIT, Nature, CERN).
"""

import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('generate_master_suite.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Emoji removal mappings
replacements = [
    # Navigation
    ('<span>🏛️</span> Home', 'Home'),
    ('<span>⚡</span> I\'m Bored', 'I\'m Bored'),
    ('<span>🌌</span> Strange Truths', 'Strange Truths'),
    ('<span>🔖</span> Saved', 'Saved'),
    ('<span>🧭</span> My Journey', 'My Journey'),
    ('<span>ℹ️</span> About', 'About'),

    # Hero
    ('🎲 SURPRISE ME', 'SURPRISE ME'),
    ('⚡ I\'M BORED', 'I\'M BORED'),
    ('🔥 Active Streak:', 'Active Streak:'),
    ('💡 Inquiries Explored:', 'Inquiries Explored:'),
    ('🔖 Inquiries Saved:', 'Inquiries Saved:'),
    ('🌐 Combinatorial Paths:', 'Combinatorial Paths:'),
    ('🌅 TODAY\'S CURIOSITY', 'TODAY\'S CURIOSITY'),
    ('🔍', ''),

    # Spark Studio
    ('🎲 Reroll Concepts', 'Reroll Concepts'),
    ('💡 Analyze My Question', 'Analyze Question'),
    ('🔖 Save to My Journal', 'Save to Journal'),
    ('🔖 Save to My Journey', 'Save to Journey'),

    # Inquiry View
    ('⏱️ 3 min read', '3 min read'),
    ('⏱️ 4 min read', '4 min read'),
    ('⏱️ 3 min thought experiment', '3 min thought experiment'),
    ('⏱️ 4 min thought experiment', '4 min thought experiment'),
    ('💡 Think First: Before We Explain It...', 'Think First: Before We Explain It'),
    ('✍️ My Guess', 'My Guess'),
    ('🤷 I Have No Idea', 'I Don\'t Know'),
    ('💡 Give Me a Hint', 'Give Me a Hint'),
    ('🔒 Lock Hypothesis', 'Lock Hypothesis'),
    ('🔒 Lock My Hypothesis', 'Lock Hypothesis'),
    ('🔒 LOCK MY IDEA', 'LOCK HYPOTHESIS'),
    ('🔬 Interactive Dynamic Simulator', 'Interactive Dynamic Simulator'),
    ('🌍 Why Should I Care?', 'Why Should I Care?'),
    ('🔮 What If? (Interactive Variable Lab)', 'What If? (Interactive Variable Lab)'),
    ('🔮 What If?', 'What If?'),
    ('🔄 What Changed', 'What Changed'),
    ('⚙️ Why It Changed', 'Why It Changed'),
    ('💥 Consequence Follows', 'Consequence Follows'),
    ('🌐 Where Else Does This Appear?', 'Where Else Does This Appear?'),
    ('🔗 Connect The Dots:', 'Connect The Dots:'),
    ('🤔 Your Turn: What Question Does This Spark?', 'Your Turn: What Question Does This Spark?'),
    ('📝 Save to My Journal', 'Save to Journal'),
    ('🔖 Save Inquiry', 'Save Inquiry'),
    ('✓ Inquiry Saved', 'Saved'),
    ('🎨 Download Insight Card (PNG)', 'Download Insight Card (PNG)'),
    ('🎨 Your Downloadable Insight Card', 'Your Downloadable Insight Card'),
    ('💾 Download Image (PNG)', 'Download Image (PNG)'),
    ('📤 Share Link', 'Share Link'),
    ('🌙 Focus Mode', 'Focus Mode'),

    # Bored View
    ('⚡ 60-Second Boredom Antidote', '60-Second Boredom Antidote'),
    ('👁️ OBSERVE', 'OBSERVE'),
    ('🧠 THINK', 'THINK'),
    ('✋ DO', 'DO'),
    ('💡 What Did You Notice? (Reveal Mechanism) ↓', 'What Did You Notice? (Reveal Mechanism) ↓'),
    ('⚡ Another Challenge', 'Another Challenge'),
    ('✦ Turn Into Curiosity Inquiry', 'Explore Deep Inquiry'),

    # Strange Facts
    ('💡 Next Strange Truth', 'Next Strange Truth'),

    # Saved & Journey
    ('🔖 Your Saved Inquiries', 'Saved Inquiries'),
    ('<div style="font-size: 3rem; margin-bottom: 12px;">🔖</div>', ''),
    ('🧭 My Curiosity Journey', 'My Curiosity Journey'),
    ('🗺️ Visual Discovery Trail', 'Visual Discovery Trail'),
    ('📝 Your Created Questions & Hypotheses', 'Your Created Questions & Hypotheses'),

    # Category Icons in JS
    ('{ key: "space", label: "Astrophysics & Cosmos", icon: "🌌"', '{ key: "space", label: "Astrophysics & Cosmos", icon: "01"'),
    ('{ key: "science", label: "Quantum & Relativity", icon: "⚛️"', '{ key: "science", label: "Quantum & Relativity", icon: "02"'),
    ('{ key: "math", label: "Pure Mathematics & Logic", icon: "📐"', '{ key: "math", label: "Pure Mathematics & Logic", icon: "03"'),
    ('{ key: "nature", label: "Everyday Physics & Nature", icon: "🌿"', '{ key: "nature", label: "Everyday Physics & Nature", icon: "04"'),
    ('{ key: "tech", label: "Cognitive Tech & Computing", icon: "💻"', '{ key: "tech", label: "Cognitive Tech & Computing", icon: "05"'),
    ('{ key: "thinking", label: "Philosophy of Mind", icon: "🧠"', '{ key: "thinking", label: "Philosophy of Mind", icon: "06"'),
    ('{ key: "how", label: "Wave Physics & Optics", icon: "🔬"', '{ key: "how", label: "Wave Physics & Optics", icon: "07"'),
    ('{ key: "behavior", label: "Systems & Civilizations", icon: "🏛️"', '{ key: "behavior", label: "Systems & Civilizations", icon: "08"'),

    # Toasts in JS
    ('showToast("🔖"', 'showToast(""'),
    ('showToast("🗑️"', 'showToast(""'),
    ('showToast("🎲"', 'showToast(""'),
    ('showToast("💡"', 'showToast(""'),
    ('showToast("🔒"', 'showToast(""'),
    ('showToast("✨"', 'showToast(""'),
    ('showToast("💾"', 'showToast(""'),
    ('showToast("⚠️"', 'showToast(""'),
    ('showToast("📋"', 'showToast(""'),
    ('showToast("🔗"', 'showToast(""'),
    ('showToast("📝"', 'showToast(""'),
    ('showToast(isZen ? "☀️" : "🌙"', 'showToast(""')
]

for src, dst in replacements:
    text = text.replace(src, dst)

# Remove any remaining standalone emojis from text strings
emojis_to_clean = ['🏛️', '⚡', '🌌', '🔖', '🧭', 'ℹ️', '✍️', '🤷', '💡', '🔬', '🔮', '🌐', '🔗', '🤔', '👁️', '🧠', '✋', '🎲', '🔥', '🌅', '🎨', '📤', '🌙', '💾', '📋', '📐', '💻', '🌿', '⚛️', '⚙️', '💥', '🔄', '🔍', '🔒', '🗑️', '🗺️', '✨']
for em in emojis_to_clean:
    text = text.replace(em, '')

with open('generate_master_suite.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cleaned emojis from generate_master_suite.py!")
