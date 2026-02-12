---
theme: default
title: "Vibe Coding: AI-Assisted Development"
info: |
  DCDA · Spring 2026
  Digital Culture & Data Analytics
class: text-center
drawings:
  persist: false
transition: slide-left
routerMode: hash
mdc: true
---

# Vibe Coding: AI-Assisted Development

<div class="mt-4 opacity-70 font-mono text-sm tracking-widest">DCDA · SPRING 2026</div>

<div class="mt-2 opacity-50 text-base">Lab 5 Prep</div>

---

# Day 1: Agenda

<div class="mt-8 space-y-4">
  <div class="flex items-center gap-4 bg-teal-500/10 border border-teal-500/20 rounded-lg p-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">1</span>
    <span class="text-lg">Copilot Orientation</span>
  </div>
  <div class="flex items-center gap-4 bg-teal-500/10 border border-teal-500/20 rounded-lg p-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">2</span>
    <span class="text-lg">The AI Coding Spectrum</span>
  </div>
  <div class="flex items-center gap-4 bg-teal-500/10 border border-teal-500/20 rounded-lg p-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">3</span>
    <span class="text-lg">Save Point</span>
  </div>
  <div class="flex items-center gap-4 bg-teal-500/10 border border-teal-500/20 rounded-lg p-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">4</span>
    <span class="text-lg">Live Demo: Hamburger Nav</span>
  </div>
  <div class="flex items-center gap-4 bg-teal-500/10 border border-teal-500/20 rounded-lg p-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">5</span>
    <span class="text-lg">Work Time</span>
  </div>
</div>

---
layout: center
class: text-center
---

<div class="text-3xl font-bold">Copilot Orientation</div>

<div class="mt-4 text-xl text-teal-400">Let's get familiar with your tools</div>

---

# Copilot in VS Code -- Three Ways to Use It

<div class="mt-6 grid grid-cols-3 gap-6">
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-3">Inline Suggestions</div>
    <div class="text-sm opacity-80 leading-relaxed">Copilot autocompletes as you type. <strong>Tab</strong> to accept, <strong>Esc</strong> to dismiss.</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-3">Copilot Chat Panel</div>
    <div class="text-sm opacity-80 leading-relaxed"><strong>Cmd+Shift+I</strong> (Mac) / <strong>Ctrl+Shift+I</strong> (Windows) for full conversations.</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-3">Inline Chat</div>
    <div class="text-sm opacity-80 leading-relaxed"><strong>Cmd+I</strong> / <strong>Ctrl+I</strong> to ask a question right in your code.</div>
  </div>
</div>

<div class="mt-8 bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-3 rounded-r text-base">
For this lab, <strong>Copilot Chat</strong> is your main tool. Inline suggestions are nice, but vibe coding means describing what you want in chat and reviewing what comes back.
</div>

---

# Switching Models

<div class="mt-8 text-lg leading-relaxed">

Copilot Pro gives you access to **multiple AI models.**

</div>

<div class="mt-6 space-y-3 text-lg">
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Claude, ChatGPT, Gemini, and others</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>You can switch models in the chat panel</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Try different models on the same prompt to see how responses differ</span>
  </div>
</div>

---
layout: center
class: text-center
---

<div class="text-3xl font-bold">The AI Coding Spectrum</div>

<div class="mt-4 text-lg opacity-70">Not all AI-assisted coding is the same</div>

---

# Four Levels

<div class="mt-6 grid grid-cols-2 gap-6">
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">1. Fundamentals First</div>
    <div class="text-sm opacity-80"><strong>YOU</strong> write all the code. AI explains errors and answers questions.</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">2. Collaborative</div>
    <div class="text-sm opacity-80"><strong>YOU</strong> design the logic. AI helps implement it.</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">3. Vibe Coding</div>
    <div class="text-sm opacity-80"><strong>YOU</strong> describe the outcome. AI generates the code.</div>
  </div>
  <div class="bg-amber-500/10 border border-amber-500/20 rounded-lg p-6">
    <div class="text-amber-400 font-semibold text-lg mb-2">4. Full Automation</div>
    <div class="text-sm opacity-80"><strong>YOU</strong> have minimal involvement. AI is a black box.</div>
  </div>
</div>

---

# Where Should You Be?

<div class="mt-8 text-lg leading-relaxed">

Discussion:

</div>

<div class="mt-4 space-y-3 text-lg">
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Where on this spectrum have you been operating?</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Where should you be for this class?</span>
  </div>
</div>

<div class="mt-8 bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
  <div class="text-teal-400 font-semibold mb-2">Key Point</div>
  <div class="text-base opacity-80">It depends on the task, your familiarity, and what you're trying to learn. The spectrum isn't a ladder -- moving "up" isn't always better.</div>
</div>

---
layout: center
class: text-center
---

<div class="text-2xl font-bold max-w-2xl mx-auto leading-relaxed">
You must be able to <span class="text-teal-400">read</span>, <span class="text-teal-400">explain</span>, and <span class="text-teal-400">modify</span> any code you use.
</div>

<div class="mt-6 text-lg opacity-60">
Regardless of who -- or what -- wrote it.
</div>

---

# Save Point

<div class="mt-4 text-xl text-teal-400 italic">
Before you touch any code, let's create a save point.
</div>

<div class="mt-6 text-lg leading-relaxed">

Steps in GitHub Desktop:

</div>

<div class="mt-4 space-y-4">
  <div class="flex items-start gap-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">1</span>
    <span class="text-lg">Make sure all changes are checked</span>
  </div>
  <div class="flex items-start gap-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">2</span>
    <span class="text-lg">Summary: <strong>"Save before Lab 5 experiments"</strong></span>
  </div>
  <div class="flex items-start gap-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">3</span>
    <span class="text-lg">Click <strong>Commit to main</strong></span>
  </div>
  <div class="flex items-start gap-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">4</span>
    <span class="text-lg"><strong>Push origin</strong></span>
  </div>
</div>

<div class="mt-6 bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-3 rounded-r text-base">
If anything breaks during your experiments, you can always go back to this commit.
</div>

---
layout: center
class: text-center
---

<div class="text-3xl font-bold">Live Demo</div>

<div class="mt-4 text-xl text-teal-400">Vibe Coding a Hamburger Nav Menu</div>

<div class="mt-6 text-lg opacity-60">Watch the process, not just the product</div>

---

# Step 1 -- Plan First

<div class="mt-6 text-lg leading-relaxed">

Before touching AI, think about what you need:

</div>

<div class="mt-4 space-y-3 text-lg">
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>A button (hamburger icon) visible only on mobile</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>A nav list that collapses/expands</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>A media query breakpoint</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>JavaScript to toggle the menu</span>
  </div>
</div>

<div class="mt-8 bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-3 rounded-r text-base">
Sketch the components before you prompt.
</div>

---

# Step 2 -- Craft the Prompt

<div class="mt-6 grid grid-cols-2 gap-6">
  <div class="bg-amber-500/10 border border-amber-500/20 rounded-lg p-6">
    <div class="text-amber-400 font-semibold text-lg mb-3">Bad Prompt</div>
    <div class="text-sm opacity-80 italic">"make my site responsive"</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-3">Good Prompt</div>
    <div class="text-sm opacity-80 italic">"Add a hamburger menu to my HTML portfolio. The nav should collapse into a hamburger icon on screens under 768px. Use vanilla JavaScript, no frameworks. Here's my current HTML: [paste code]"</div>
  </div>
</div>

<div class="mt-8 text-lg leading-relaxed">

What makes the good prompt better? **Context**, **specificity**, **constraints**.

</div>

---

# Step 3 -- Review the Output

<div class="mt-8 space-y-5 text-lg leading-relaxed">

<div class="flex items-start gap-3">
  <span class="text-teal-400 mt-1">→</span>
  <span>Read every line the AI gives you</span>
</div>

<div class="flex items-start gap-3">
  <span class="text-teal-400 mt-1">→</span>
  <span>Don't just check <strong>"does it work?"</strong></span>
</div>

<div class="flex items-start gap-3">
  <span class="text-teal-400 mt-1">→</span>
  <span>Ask: <strong>"Do I understand it?"</strong></span>
</div>

</div>

<div class="mt-8 text-lg">

This is where the Understanding Spectrum comes in.

</div>

---

# The Understanding Spectrum

<div class="mt-6 space-y-4">
  <div class="flex items-start gap-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">1</span>
    <div>
      <div class="text-lg font-semibold">"I wrote this"</div>
      <div class="text-sm opacity-70">You understand it fully. Brief comment is fine.</div>
    </div>
  </div>
  <div class="flex items-start gap-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">2</span>
    <div>
      <div class="text-lg font-semibold">"I understand the logic"</div>
      <div class="text-sm opacity-70">You get what it does and why, even if you couldn't write it from scratch. Explain in your own words.</div>
    </div>
  </div>
  <div class="flex items-start gap-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">3</span>
    <div>
      <div class="text-lg font-semibold">"I know what it does but not how"</div>
      <div class="text-sm opacity-70">You see the input/output but the mechanism is unclear. Flag it honestly.</div>
    </div>
  </div>
  <div class="flex items-start gap-4">
    <span class="bg-teal-500/20 text-teal-400 rounded-full w-8 h-8 flex items-center justify-center font-bold shrink-0">4</span>
    <div>
      <div class="text-lg font-semibold">"I don't understand this"</div>
      <div class="text-sm opacity-70">That's okay to say. Try to figure it out and document what you learned.</div>
    </div>
  </div>
</div>

<div class="mt-6 bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-3 rounded-r text-base">
Your comments are a record of your understanding -- not a performance.
</div>

---

# Good vs. Bad Comments

<div class="mt-6 grid grid-cols-2 gap-6">
  <div class="bg-amber-500/10 border border-amber-500/20 rounded-lg p-6">
    <div class="text-amber-400 font-semibold text-lg mb-3">Bad Comment</div>
    <div class="text-sm opacity-80 font-mono leading-relaxed">
      // toggle menu<br>
      function toggleMenu() { ... }
    </div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-3">Good Comment</div>
    <div class="text-sm opacity-80 font-mono leading-relaxed">
      // When hamburger is clicked, toggle<br>
      // 'active' class on the nav. This<br>
      // triggers the CSS transform to slide<br>
      // the menu in from the right. I<br>
      // understand the classList.toggle<br>
      // method but had to look up how the<br>
      // CSS transition works.
    </div>
  </div>
</div>

---

# Step 4 -- Test and Refine

<div class="mt-8 space-y-5 text-lg leading-relaxed">

<div class="flex items-start gap-3">
  <span class="text-teal-400 mt-1">→</span>
  <span>Does it actually work?</span>
</div>

<div class="flex items-start gap-3">
  <span class="text-teal-400 mt-1">→</span>
  <span>Resize the browser -- does it break?</span>
</div>

<div class="flex items-start gap-3">
  <span class="text-teal-400 mt-1">→</span>
  <span>Go back to AI: <strong>"The menu doesn't close when I click a link"</strong></span>
</div>

<div class="flex items-start gap-3">
  <span class="text-teal-400 mt-1">→</span>
  <span>Or fix it yourself</span>
</div>

</div>

---

# Choosing Your Experiments

<div class="mt-6 text-lg leading-relaxed">

You need at least **two experiments** from three options:

</div>

<div class="mt-6 grid grid-cols-3 gap-6">
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">A: Portfolio Enhancement</div>
    <div class="text-sm opacity-80">Add a feature to your HTML/CSS/JS portfolio</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">B: Python in Colab</div>
    <div class="text-sm opacity-80">Use AI to help write Python for data analysis</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">C: Debug with AI</div>
    <div class="text-sm opacity-80">Use AI to diagnose and fix broken code</div>
  </div>
</div>

<div class="mt-6 space-y-3 text-lg">
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Difficulty labels are there to help you self-select</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>A simple, well-understood feature <strong>beats</strong> a complex one you can't explain</span>
  </div>
</div>

---

# Experiment B Note

<div class="mt-6 text-lg leading-relaxed">

Python experiments use **Google Colab** -- no installation needed.

</div>

<div class="mt-4 space-y-3 text-lg">
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span><strong>colab.research.google.com</strong></span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>pandas, matplotlib, etc. are pre-installed</span>
  </div>
</div>

<div class="mt-8 bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-3 rounded-r text-base">
If Python makes you nervous, this might be the best experiment to try -- using AI to help with something you're not fully comfortable with is where vibe coding gets interesting.
</div>

---

# Work Time

<div class="mt-8 text-xl text-teal-400 italic">
Pick your experiments and start working.
</div>

<div class="mt-8 space-y-3 text-lg">
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Save your prompts and AI responses as you go</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Commit and push often</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>I'm here -- ask questions early</span>
  </div>
</div>

---
layout: center
class: text-center
---

<div class="text-3xl font-bold">Day 2</div>

<div class="mt-4 text-xl text-teal-400">Work Time + Reflection Prep</div>

---

# Check-in

<div class="mt-8 text-xl text-teal-400 italic">
Where are you? What's stuck?
</div>

<div class="mt-8 text-lg leading-relaxed">

Common issues we'll address.

</div>

---

# Work Time

<div class="mt-6 text-lg leading-relaxed">

Continue your experiments. Questions to ask yourself as you work:

</div>

<div class="mt-6 space-y-3 text-lg">
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Am I commenting honestly or performatively?</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Am I scope-creeping?</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Have I been saving my prompts?</span>
  </div>
</div>

---
layout: center
class: text-center
---

<div class="text-3xl font-bold">Reflection Preview</div>

<div class="mt-4 text-xl text-teal-400">The reflection is where the real learning shows up</div>

---

# What We're Looking For

<div class="mt-6 text-lg leading-relaxed">

**400-600 words**, your own voice, **no AI**.

</div>

<div class="mt-6 text-lg">

Three areas:

</div>

<div class="mt-4 grid grid-cols-3 gap-6">
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">Technical Understanding</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">Process Evaluation</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-2">Ethical & Pedagogical</div>
  </div>
</div>

<div class="mt-8 bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-3 rounded-r text-base">
This isn't a summary of what you did -- it's critical thinking about how it went.
</div>

---

# Strong vs. Generic Reflection

<div class="mt-6 grid grid-cols-2 gap-6">
  <div class="bg-amber-500/10 border border-amber-500/20 rounded-lg p-6">
    <div class="text-amber-400 font-semibold text-lg mb-3">Generic</div>
    <div class="text-sm opacity-80 italic leading-relaxed">"AI was helpful for generating code quickly. It saved me time and the code worked. I think AI is a useful tool that should be used responsibly."</div>
  </div>
  <div class="bg-teal-500/10 border border-teal-500/20 rounded-lg p-6">
    <div class="text-teal-400 font-semibold text-lg mb-3">Strong</div>
    <div class="text-sm opacity-80 italic leading-relaxed">"When I asked Copilot to build a dark mode toggle, the JavaScript worked immediately but the CSS variables it chose had poor contrast ratios I wouldn't have caught without testing. This showed me that 'working code' and 'good code' aren't the same thing -- AI optimizes for function, not necessarily for the user experience details that matter."</div>
  </div>
</div>

---

# Before You Submit

<div class="mt-8 space-y-4 text-lg">
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>Portfolio updated with <strong>lab05.html</strong> page</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>GitHub Pages site displays correctly</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>D2L submission: reflection, commented code, prompts, AI output, links</span>
  </div>
  <div class="flex items-start gap-3">
    <span class="text-teal-400 mt-1">→</span>
    <span>If you used Colab: download <strong>.ipynb</strong> + datasets, add to repo, link from portfolio</span>
  </div>
</div>

---
layout: center
class: text-center
---

<div class="text-lg opacity-80 max-w-2xl mx-auto">
The question isn't "Should I use AI?"
</div>

<div class="mt-8 text-2xl font-semibold text-teal-400">
It's "How do I use AI while staying in the driver's seat?"
</div>
