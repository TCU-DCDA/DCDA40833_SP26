---
theme: default
title: GitHub as Infrastructure
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

# GitHub as Infrastructure

<div class="mt-2 opacity-70 text-xl">Version Control · Backup · Hosting</div>

<div class="mt-4 opacity-70 font-mono text-sm tracking-widest">DCDA · SPRING 2026</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# The Problem We're Solving

<div class="space-y-2 text-sm">

### ❌ Before GitHub

- Lost files ("my laptop died")
- Version chaos (`final_v2_REAL_final.html`)
- No collaboration history
- Manual file hosting
- Breaking changes with no undo

</div>

::right::

<div class="space-y-2 text-sm">

### ✅ With GitHub

- Cloud backup (automatic)
- Clear version history
- Tracked changes & authors
- Free web hosting
- Time machine for your code

</div>

<div class="bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-2 rounded-r mt-6 text-sm">
  <strong>Key Insight:</strong> GitHub solves three problems at once — tracking changes, preserving work, and sharing publicly.
</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Role #1: Version Control

<span class="opacity-70">The Time Machine for Your Code</span>

Tracks **every change** to your code with timestamps, descriptions, and author information.

<div class="bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-2 rounded-r mt-4 text-sm">
  <strong>Why it matters:</strong>
  <ul class="mt-1">
    <li>See who changed what, when, and why</li>
    <li>Revert to any previous version</li>
    <li>Compare versions side-by-side</li>
  </ul>
</div>

::right::

```bash
# Every commit is a snapshot
commit 3a2f1b9
Author: you@email.com
Date: Jan 14, 2026

    Add navigation bar

commit 2c8e4d1
Author: you@email.com
Date: Jan 13, 2026

    Initial homepage structure
```

---

# Role #2: Backup

<span class="opacity-70">The Safety Net</span>

<div class="grid grid-cols-3 gap-6 mt-8">

<div class="bg-teal-500/10 rounded-xl p-6 text-center">
  <div class="text-3xl mb-3">💻</div>
  <h4 class="font-bold">Your Computer</h4>
  <p class="text-sm mt-2 opacity-70">Work locally on your HTML, CSS, and files</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-6 text-center">
  <div class="text-3xl mb-3">☁️</div>
  <h4 class="font-bold">GitHub Cloud</h4>
  <p class="text-sm mt-2 opacity-70">Automatic backup with complete history</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-6 text-center">
  <div class="text-3xl mb-3">🔄</div>
  <h4 class="font-bold">Recovery</h4>
  <p class="text-sm mt-2 opacity-70">Laptop breaks? Clone repository to new machine</p>
</div>

</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Role #3: Web Hosting

<span class="opacity-70">The Public Stage — GitHub Pages</span>

Turns your repository into a **live website** accessible to anyone with the URL.

GitHub reads your HTML/CSS files and serves them as a functioning website — no server configuration needed.

::right::

<div class="bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-2 rounded-r text-sm">
  <strong>Benefits:</strong>
  <ul class="mt-1">
    <li><strong>Free hosting</strong> (no server costs)</li>
    <li><strong>Custom URL:</strong> <code>username.github.io/project</code></li>
    <li><strong>Automatic updates</strong> when you push</li>
    <li><strong>HTTPS security</strong> built-in</li>
  </ul>
</div>

---

# The Complete Workflow

<div class="grid grid-cols-5 gap-4 mt-8 text-center">

<div class="bg-teal-500/10 rounded-xl p-4">
  <div class="text-2xl font-bold text-teal-400 mb-2">1</div>
  <h4 class="font-bold text-sm">Create Locally</h4>
  <p class="text-xs mt-1 opacity-70">Write HTML, CSS, add images</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-4">
  <div class="text-2xl font-bold text-teal-400 mb-2">2</div>
  <h4 class="font-bold text-sm">Review Changes</h4>
  <p class="text-xs mt-1 opacity-70">GitHub Desktop shows what you modified</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-4">
  <div class="text-2xl font-bold text-teal-400 mb-2">3</div>
  <h4 class="font-bold text-sm">Commit</h4>
  <p class="text-xs mt-1 opacity-70">Add message & click "Commit to main"</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-4">
  <div class="text-2xl font-bold text-teal-400 mb-2">4</div>
  <h4 class="font-bold text-sm">Push to Origin</h4>
  <p class="text-xs mt-1 opacity-70">Click "Push origin" → uploads to cloud</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-4">
  <div class="text-2xl font-bold text-teal-400 mb-2">5</div>
  <h4 class="font-bold text-sm">Live on Web</h4>
  <p class="text-xs mt-1 opacity-70">GitHub Pages publishes automatically</p>
</div>

</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# GitHub Desktop

<span class="opacity-70">Your Visual Toolkit</span>

<div class="space-y-3 text-sm">

- **📝 Changes Tab** — View file changes with visual diffs
- **💬 Commit Message** — Describe your changes clearly
- **✅ Commit to Main** — Save snapshot locally

</div>

::right::

<div class="space-y-3 text-sm">

- **⬆️ Push Origin** — Upload to GitHub cloud
- **⬇️ Fetch/Pull Origin** — Download latest changes
- **📜 History Tab** — View all previous commits

</div>

<div class="bg-amber-500/10 border-l-3 border-amber-400 pl-4 py-2 rounded-r mt-6 text-sm">
  ⚠️ <strong>Remember:</strong> Always fetch/pull before you commit and push to avoid conflicts!
</div>

---

# How GitHub Pages Works

<div class="grid grid-cols-3 gap-6 mt-8">

<div class="bg-teal-500/10 rounded-xl p-6 text-center">
  <div class="text-3xl mb-3">📁</div>
  <h4 class="font-bold">Your Repository Structure</h4>
  <p class="text-sm mt-2 opacity-70">HTML files, CSS, images organized in folders</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-6 text-center">
  <div class="text-3xl mb-3">⚙️</div>
  <h4 class="font-bold">GitHub Pages Activation</h4>
  <p class="text-sm mt-2 opacity-70">Configure which branch and folder to publish</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-6 text-center">
  <div class="text-3xl mb-3">🌐</div>
  <h4 class="font-bold">Live Website</h4>
  <p class="text-sm mt-2 opacity-70"><code>https://yourusername.github.io/project</code></p>
</div>

</div>

<div class="bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-2 rounded-r mt-6 text-sm">
  <strong>The Magic:</strong> Every time you push changes, GitHub automatically rebuilds your site (1–2 minutes).
</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Role #4: Collaboration & Transparency

<div class="text-sm space-y-1">

- **Transparency:** Anyone can see your code
- **Attribution:** Changes tied to authors
- **Discussion:** Issues & pull requests
- **Forking:** Others can build on your work

</div>

::right::

<div class="text-sm space-y-1">

### Real-World Examples

- 📚 Open educational resources
- 🔬 Reproducible research
- 🌐 Community documentation
- 🎨 Collaborative projects

</div>

<div class="bg-blue-500/10 border-l-3 border-blue-400 pl-4 py-2 rounded-r mt-6 text-sm">
  📝 <strong>Critical Question:</strong> When code is visible to everyone, who gets credit? How does this change academic attribution?
</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Public vs Private

<span class="opacity-70">Know the Boundaries</span>

<div class="text-sm">

### 🔒 Never Commit

- Passwords
- API keys
- Personal data
- Sensitive information
- Private notes

</div>

::right::

<div class="text-sm">

### 🌐 Always Commit

- HTML/CSS code
- Documentation
- Public images
- Project files
- Portfolio work

</div>

<div class="bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-2 rounded-r mt-6 text-sm">
  GitHub makes your code <strong>public by default</strong>. This is a feature, not a bug — but it requires conscious decision-making about digital boundaries.
</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Common Pitfalls & Solutions

<div class="text-sm space-y-4">

<div class="bg-red-500/10 rounded-lg p-3">
  <strong>❌ "Changes aren't showing"</strong><br/>
  ✅ Check if you pushed · Wait 1–2 min · Hard refresh browser
</div>

<div class="bg-red-500/10 rounded-lg p-3">
  <strong>❌ "Merge conflicts"</strong><br/>
  ✅ Always fetch before making changes · Don't edit on GitHub.com
</div>

</div>

::right::

<div class="text-sm space-y-4">

<div class="bg-red-500/10 rounded-lg p-3">
  <strong>❌ "Site shows 404"</strong><br/>
  ✅ Ensure <code>index.html</code> exists · Check Pages settings
</div>

<div class="bg-red-500/10 rounded-lg p-3">
  <strong>❌ "Committed sensitive data"</strong><br/>
  ✅ Delete file, commit, push · Change exposed passwords immediately
</div>

</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Best Practices

<div class="text-sm">

### ✅ Do This

- **Commit often** with clear messages
- **Use README.md** to document
- **Organize files** in folders
- **Test locally** before committing
- **Fetch origin** regularly

</div>

::right::

<div class="text-sm">

### ❌ Avoid This

- Committing passwords or API keys
- Vague messages: "fixed stuff"
- Large files (>100MB)
- Editing directly on GitHub.com
- Messy file structures

</div>

<div class="bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-2 rounded-r mt-6 text-sm">
  Your GitHub repository is both your <strong>backup</strong> and your <strong>public portfolio</strong> — treat it professionally.
</div>

---

# The Complete Development Cycle

<div class="grid grid-cols-4 gap-6 mt-8 text-center">

<div class="bg-teal-500/10 rounded-xl p-6">
  <div class="text-3xl mb-3">🎨</div>
  <h4 class="font-bold">Design & Code</h4>
  <p class="text-sm mt-2 opacity-70">Create HTML structure and CSS styling locally</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-6">
  <div class="text-3xl mb-3">💾</div>
  <h4 class="font-bold">Version Control</h4>
  <p class="text-sm mt-2 opacity-70">Review → Commit with meaningful message</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-6">
  <div class="text-3xl mb-3">☁️</div>
  <h4 class="font-bold">Backup</h4>
  <p class="text-sm mt-2 opacity-70">Push to GitHub cloud</p>
</div>

<div class="bg-teal-500/10 rounded-xl p-6">
  <div class="text-3xl mb-3">🌐</div>
  <h4 class="font-bold">Publish</h4>
  <p class="text-sm mt-2 opacity-70">GitHub Pages makes it live</p>
</div>

</div>

<div class="bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-2 rounded-r mt-6 text-sm">
  <strong>This is infrastructure:</strong> The technical systems that make digital culture possible.
</div>

---
layout: two-cols
layoutClass: gap-8 items-center
---

# Resources & Next Steps

<div class="text-sm">

### 📚 Documentation

- [GitHub Desktop Docs](https://docs.github.com/en/desktop)
- [GitHub Pages Guide](https://docs.github.com/en/pages)
- [Download GitHub Desktop](https://desktop.github.com/)

</div>

::right::

<div class="text-sm">

### 🛠️ Practice

- Create your first repository
- Make commits with good messages
- Enable GitHub Pages
- Share your live URL!

</div>

---
layout: center
class: text-center
---

# Questions?

<div class="mt-6 text-left inline-block text-sm">

**GitHub's Four Roles:**

- 🔄 **Version Control** — Track every change
- ☁️ **Backup** — Safe in the cloud
- 🌐 **Hosting** — Live website with Pages
- 👥 **Collaboration** — Public, transparent, citable

</div>

<div class="bg-teal-500/10 border-l-3 border-teal-400 pl-4 py-2 rounded-r mt-6 text-sm">
  GitHub isn't just a tool — it's the <strong>foundation</strong> that enables collaborative, versioned, public code.
</div>

<div class="mt-6 opacity-70 text-sm">Next: Setting up your portfolio repository</div>
