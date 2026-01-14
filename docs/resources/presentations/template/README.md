# DCDA Presentation Template

A Reveal.js-based presentation template using the **Soul Red** theme aligned with the main course site.

## Quick Start

1. Copy `index.html` to your presentation folder
2. Replace the sample slides with your content
3. Open in browser to present

## Features

- **Keyboard Navigation**: Arrow keys, Space, Escape
- **Touch Support**: Swipe on mobile devices  
- **Slide Numbers**: Current/Total display
- **Code Highlighting**: Syntax highlighting with Monokai theme
- **Speaker Notes**: Press `S` to open speaker view
- **Overview Mode**: Press `Esc` or `O` for slide overview
- **Fullscreen**: Press `F` for fullscreen
- **PDF Export**: Add `?print-pdf` to URL, then print

## Slide Types & Components

### Title Slide
```html
<section class="title-slide">
    <h1>Title</h1>
    <h3>Subtitle</h3>
    <p class="author">Course • Info</p>
</section>
```

### Section Divider
```html
<section class="section-divider">
    <h2>New Section</h2>
    <p>Section description</p>
</section>
```

### Two-Column Layout
```html
<section>
    <h2>Title</h2>
    <div class="two-column">
        <div class="column">Left content</div>
        <div class="column">Right content</div>
    </div>
</section>
```

### Comparison (Before/After)
```html
<div class="comparison">
    <div class="comparison-box bad">
        <h4>❌ Before</h4>
        <ul><li>Problem</li></ul>
    </div>
    <div class="comparison-box good">
        <h4>✅ After</h4>
        <ul><li>Solution</li></ul>
    </div>
</div>
```

### Key Insight Box
```html
<div class="key-insight">
    <p><strong>Key Insight:</strong> Important takeaway</p>
</div>
```

### Definition Box
```html
<div class="definition-box">
    <h4>Term</h4>
    <p>Definition of the term</p>
</div>
```

### Steps/Workflow
```html
<div class="steps">
    <div class="step">
        <span class="step-number">1</span>
        <div class="step-content">
            <h4>Step Title</h4>
            <p>Description</p>
        </div>
    </div>
</div>
```

### Code Block with Line Numbers
```html
<pre><code class="language-html" data-trim data-line-numbers>
Your code here
</code></pre>
```

### Progressive Reveal (Fragments)
```html
<p class="fragment fade-in">Appears first</p>
<p class="fragment fade-in">Appears second</p>
```

### Vertical Slides (Sub-sections)
```html
<section>
    <section>Main slide</section>
    <section>Sub-slide 1</section>
    <section>Sub-slide 2</section>
</section>
```

### Speaker Notes
```html
<section>
    <h2>Slide Title</h2>
    <aside class="notes">
        These notes only appear in speaker view (press S)
    </aside>
</section>
```

## Color Palette

| Variable | Value | Usage |
|----------|-------|-------|
| `--soul-red` | #C1272D | Primary accent |
| `--soul-red-light` | #FF6B75 | Highlights, links |
| `--soul-red-dark` | #8B1C1F | Dark accent |
| `--charcoal` | #0f0f0f | Background |
| `--text-primary` | #ffffff | Main text |
| `--text-secondary` | #d0d0d0 | Secondary text |

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| → / Space | Next slide |
| ← | Previous slide |
| ↓ | Next vertical slide |
| ↑ | Previous vertical slide |
| Esc / O | Overview mode |
| S | Speaker notes |
| F | Fullscreen |
| B | Blackout screen |
| Home | First slide |
| End | Last slide |

## Configuration Options

Edit the `Reveal.initialize()` call in your HTML:

```javascript
Reveal.initialize({
    hash: true,              // Enable URL hash
    slideNumber: 'c/t',      // Current/Total
    controls: true,          // Show navigation arrows
    progress: true,          // Show progress bar
    center: true,            // Center slides vertically
    transition: 'slide',     // none/fade/slide/convex/concave/zoom
    transitionSpeed: 'default'
});
```

## File Structure

```
template/
├── index.html          # Main presentation file
├── css/
│   └── soul-red-theme.css  # Custom theme
├── images/             # Slide images
└── README.md           # This file
```

## Converting Existing Presentations

To migrate an existing presentation:

1. Copy slide content into `<section>` elements
2. Apply appropriate classes (`title-slide`, `section-divider`, etc.)
3. Convert custom CSS to use Soul Red variables
4. Test navigation and code highlighting
