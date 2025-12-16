# Lab 1: Skills Portfolio Setup — GitHub, HTML & CSS Foundations

## Overview

In this lab, you will set up the foundation for your **Skills Portfolio** — a website that will grow throughout the semester as you add artifacts from each lab assignment. By the end of this lab, you will have:

- A GitHub account and repository
- A live website hosted on GitHub Pages
- A basic HTML/CSS structure ready for future content

---

## Part 1: GitHub Setup

### Create a GitHub Account

1. Go to [github.com](https://github.com) and sign up for a free account
2. Use your TCU email or personal email (your choice)
3. Choose a professional username — this will be visible in your portfolio URL

### Create Your Repository

1. Click the **+** icon (top right) → **New repository**
2. Name it: `dcda40833-portfolio` (or similar — lowercase, no spaces)
3. Set to **Public** (required for GitHub Pages free hosting)
4. Check **Add a README file**
5. Click **Create repository**

### Enable GitHub Pages

1. In your repo, go to **Settings** → **Pages** (left sidebar)
2. Under "Source," select **Deploy from a branch**
3. Choose **main** branch and **/ (root)** folder
4. Click **Save**
5. Your live URL will be: `https://yourusername.github.io/dcda40833-portfolio/`

> ⚠️ **Note:** The URL won't work until you push an `index.html` file. First-time deployment can take 5-10 minutes. If your site doesn't appear, check **Settings → Pages** for status or error messages.

---

## Part 2: Tools & Local Setup

### Install VS Code

1. Download [Visual Studio Code](https://code.visualstudio.com/)
2. Install and open it
3. This will be your code editor for HTML, CSS, and other files throughout the course

### Install GitHub Desktop

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Sign in with your GitHub account
3. Clone your repository: **File → Clone Repository** → select your repo
4. Choose a local folder (e.g., `Documents/DCDA`)

> 💡 **Tip:** In GitHub Desktop, click **Repository → Open in Visual Studio Code** to quickly open your project.

### The Git Workflow (GitHub Desktop)

Whenever you make changes:

1. **Save** your files in VS Code
2. Open **GitHub Desktop** — it automatically detects changes
3. Write a **commit message** describing what you changed
4. Click **Commit to main**
5. Click **Push origin** to upload to GitHub

Your live site will update automatically within a few minutes.

> 📚 **Want to learn more about Git?** See [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)

---

## Part 3: HTML & CSS Foundations

### Key Concepts (Reference)

This section summarizes what we'll cover in class. Use it as a reference.

**HTML** (structure):
- Elements: `<html>`, `<head>`, `<body>`, `<h1>`-`<h6>`, `<p>`, `<a>`, `<img>`, `<div>`, `<section>`
- Attributes: `class`, `id`, `href`, `src`, `alt`

**CSS** (style):
- Selectors: element (`p`), class (`.classname`), id (`#idname`)
- Box model: margin, border, padding, content
- Common properties: `color`, `background-color`, `font-family`, `font-size`, `margin`, `padding`, `width`, `height`

> 📚 **Self-study resources:**
> - [MDN HTML Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
> - [MDN CSS Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
> - [W3Schools HTML Tutorial](https://www.w3schools.com/html/)
> - [W3Schools CSS Tutorial](https://www.w3schools.com/css/)

---

## Part 4: Build Your Portfolio Structure

### Create Your Files

1. Open your repository folder in VS Code (**File → Open Folder** or use GitHub Desktop's **Open in Visual Studio Code**)
2. Create the following structure:

```
dcda40833-portfolio/
├── index.html
├── css/
│   └── style.css
└── images/
    └── (your images go here)
```

**In VS Code:**
- Click the **New File** icon to create `index.html`
- Click the **New Folder** icon to create `css` and `images` folders
- Inside `css`, create `style.css`
- The `images` folder can stay empty for now

### Starter Template

**index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name | DCDA Portfolio</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>Your Name</h1>
        <nav>
            <a href="#about">About</a>
            <a href="#portfolio">Portfolio</a>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>Write a brief introduction about yourself here. What's your major? What are your interests? What do you hope to do after graduation?</p>
        </section>

        <section id="portfolio">
            <h2>Portfolio</h2>
            
            <!-- Lab 1 will go here -->
            <article class="lab-entry">
                <h3>Lab 1: Portfolio Setup</h3>
                <p>Description of what you learned and accomplished...</p>
            </article>

            <!-- Future labs will be added here -->
            <article class="lab-entry">
                <h3>Lab 2: Coming Soon</h3>
            </article>

            <article class="lab-entry">
                <h3>Lab 3: Coming Soon</h3>
            </article>

            <article class="lab-entry">
                <h3>Lab 4: Coming Soon</h3>
            </article>

            <article class="lab-entry">
                <h3>Lab 5: Coming Soon</h3>
            </article>

            <article class="lab-entry">
                <h3>Lab 6: Coming Soon</h3>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 Your Name | TCU DCDA</p>
    </footer>
</body>
</html>
```

**css/style.css:**
```css
/* Base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Georgia, 'Times New Roman', serif;
    line-height: 1.6;
    color: #333;
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
}

/* Header */
header {
    text-align: center;
    padding: 40px 0;
    border-bottom: 1px solid #ddd;
    margin-bottom: 40px;
}

header h1 {
    margin-bottom: 10px;
}

nav a {
    margin: 0 15px;
    color: #4a1a7a; /* TCU purple */
    text-decoration: none;
}

nav a:hover {
    text-decoration: underline;
}

/* Main content */
section {
    margin-bottom: 60px;
}

h2 {
    color: #4a1a7a;
    margin-bottom: 20px;
    border-bottom: 2px solid #4a1a7a;
    padding-bottom: 10px;
}

/* Lab entries */
.lab-entry {
    background: #f9f9f9;
    padding: 20px;
    margin-bottom: 20px;
    border-left: 4px solid #4a1a7a;
}

.lab-entry h3 {
    margin-bottom: 10px;
}

/* Footer */
footer {
    text-align: center;
    padding: 20px 0;
    border-top: 1px solid #ddd;
    margin-top: 40px;
    color: #666;
}
```

### Personalize It

At minimum, update:
1. Your name (in `<title>`, `<h1>`, and `<footer>`)
2. About Me section content
3. Colors, fonts, or layout to make it your own

---

## Part 5: Add Comments

Add HTML and CSS comments to explain your code. This helps you learn and helps us assess your understanding.

**HTML comments:** `<!-- This is a comment -->`

**CSS comments:** `/* This is a comment */`

Example:
```html
<!-- Navigation links - these jump to sections on the page -->
<nav>
    <a href="#about">About</a>
    <a href="#portfolio">Portfolio</a>
</nav>
```

**Err on the side of over-commenting.** The more you explain, the better we can see your understanding.

---

## Deliverables

Submit to D2L:

1. **Link to your live GitHub Pages site** (e.g., `https://yourusername.github.io/dcda40833-portfolio/`)

2. **Link to your GitHub repository** (e.g., `https://github.com/yourusername/dcda40833-portfolio`)

3. **Your site should include:**
   - Personalized About Me section
   - Placeholder sections for Labs 2-6
   - HTML and CSS comments explaining your code

4. **Written Reflection (150-200 words)** — Submit as a separate document or text entry addressing:
   - What was new to you in this lab (GitHub, HTML, CSS, or all three)?
   - What did you find most challenging, and how did you work through it?
   - What aspects of your portfolio are you most looking forward to developing as the semester progresses?

---

## Looking Ahead

Each subsequent lab will add to this portfolio. You'll document what you learned, embed visualizations, link to artifacts, and continuously refine the design. By the end of the semester, you'll have a polished showcase of your DCDA skills.
