# Lab 1: Portfolio Setup

**Current Version:** See [docs/labs/lab01.html](../../docs/labs/lab01.html)  
**Due:** January 21, 2026 by 11:30 PM

## Overview

Your **Skills Portfolio** is a website that will grow throughout the semester. Each lab adds a new page showcasing your work, and by the end of the course, you'll have a polished collection demonstrating your DCDA skills.

**Mini-Lecture:** Before starting, view the [GitHub Infrastructure Lecture](../../docs/resources/presentations/github-intro/index.html) to understand why we use these tools.

In this lab, you will:
- Create your own portfolio repository from a provided template
- Customize the template with your personal information
- Make design choices that reflect your style
- Deploy your site live on the web via GitHub Pages

---

## Part 1: Setup Your Tools

### Step 1: Create a GitHub Account
1. Go to [github.com](https://github.com) and click **Sign up**
2. Use your TCU email (for GitHub Education benefits)
3. Choose a **professional username** — this appears in your portfolio URL
4. Verify your email address

### Step 2: Download and Install GitHub Desktop
1. Go to [desktop.github.com](https://desktop.github.com)
2. Download and install for your OS
3. Open GitHub Desktop and sign in with your GitHub account

### Step 3: Download and Install Visual Studio Code
1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download and install for your OS
3. Optional: In GitHub Desktop preferences, set VS Code as external editor

---

## Part 2: Create Your Portfolio Repository

1. Go to the template: [DCDA40833-portfolio-template](https://github.com/TCU-DCDA/DCDA40833-portfolio-template)
2. Click **"Use this template"** → **"Create a new repository"**
3. Configure:
   - **Owner:** Your GitHub account
   - **Repository name:** `dcda-portfolio` (lowercase, no spaces)
   - **Visibility:** **Public** (required for free GitHub Pages)
4. Click **"Create repository"**

---

## Part 3: Clone to Your Computer

1. Open GitHub Desktop
2. **File → Clone Repository**
3. Find your `dcda-portfolio` repository
4. Choose a local folder (e.g., `Documents/DCDA`)
5. Click **Clone**
6. Click **"Open in Visual Studio Code"**

---

## Part 4: Enable GitHub Pages

1. Go to your repository on GitHub.com
2. Click **Settings → Pages**
3. Under "Source," select **Deploy from a branch**
4. Choose **main** branch and **/ (root)** folder
5. Click **Save**

Your site URL: `https://yourusername.github.io/dcda-portfolio/`

**Note:** First deployment takes 2-5 minutes. Check Settings → Pages for status.

---

## Part 5: Explore the Template

Open these files in VS Code:

| File | Purpose |
|------|---------|
| `index.html` | Main homepage — your portfolio landing page |
| `css/styles.css` | All visual styling (colors, fonts, layout) |
| `images/` | Folder for photos and graphics |
| `README.md` | Project documentation (visible on GitHub) |

---

## Part 6: Make It Yours

### Required Personalizations:
1. **Update personal information** in `index.html`:
   - Your name
   - Bio/introduction
   - Contact information or links

2. **Customize visual design** in `css/styles.css`:
   - Colors (background, text, accent colors)
   - Fonts (try Google Fonts)
   - Any layout adjustments you prefer

### Tips:
- Make small changes and preview often
- Keep backups of working code
- Use browser DevTools to experiment (F12 or right-click → Inspect)

---

## Part 7: Commit & Push

### In GitHub Desktop:
1. Review changes in the left panel
2. Write a descriptive commit message (e.g., "Update bio and customize colors")
3. Click **Commit to main**
4. Click **Push origin**

### Verify Deployment:
Visit your GitHub Pages URL to see your changes live (may take 1-2 minutes).

---

## Part 8: Reflect

In your portfolio or as a separate document, briefly reflect:
1. What was most challenging about this setup?
2. What did you learn about GitHub, HTML, or CSS?
3. What design choices did you make and why?

---

## Deliverables

Submit to D2L dropbox:
1. Link to your GitHub repository
2. Link to your live GitHub Pages site

---

## Looking Ahead

Each subsequent lab will ask you to add a new page to this portfolio. By the end of the semester, you'll have a complete showcase of your DCDA skills ready to share with future employers or graduate programs.

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
