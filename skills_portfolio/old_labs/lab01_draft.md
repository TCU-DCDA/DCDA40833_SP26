# Lab 1: Skills Portfolio Setup — Make It Yours

## Overview

Your **Skills Portfolio** is a website that will grow throughout the semester. Each lab adds a new page showcasing your work, and by the end of the course, you'll have a polished collection demonstrating your DCDA skills.

In this lab, you will:

- Create your own portfolio repository from a provided template
- Customize the template with your personal information
- Make design choices that reflect your style
- Deploy your site live on the web via GitHub Pages

By the end of this lab, you'll have a live, personalized website ready to house your semester's work.

---

## Part 1: Create Your Portfolio Repository

You'll create your own copy of the course portfolio template using GitHub's "Use this template" feature.

1. Go to the template repository: **[DCDA40833-portfolio-template](https://github.com/YOUR-ORG/DCDA40833-portfolio-template)** *(link provided in class)*

2. Click the green **"Use this template"** button → **"Create a new repository"**

3. Configure your new repository:
   - **Owner:** Your GitHub account
   - **Repository name:** `dcda-portfolio` (or similar — lowercase, no spaces)
   - **Description:** Optional, but something like "DCDA 40833 Skills Portfolio"
   - **Visibility:** **Public** (required for free GitHub Pages hosting)

4. Click **"Create repository"**

You now have your own copy of the template in your GitHub account.

---

## Part 2: Clone to Your Computer

Use GitHub Desktop to download your repository so you can edit it locally.

1. Open **GitHub Desktop**
2. **File → Clone Repository**
3. Find your new `dcda-portfolio` repository in the list
4. Choose a local folder (e.g., `Documents/DCDA`)
5. Click **Clone**

Once cloned, click **"Open in Visual Studio Code"** to start editing.

---

## Part 3: Enable GitHub Pages

Before making changes, set up GitHub Pages so your site goes live automatically when you push updates.

1. Go to your repository on GitHub.com
2. Click **Settings** → **Pages** (in the left sidebar)
3. Under "Source," select **Deploy from a branch**
4. Choose **main** branch and **/ (root)** folder
5. Click **Save**

Your site URL will be: `https://yourusername.github.io/dcda-portfolio/`

> ⏳ **Note:** First deployment takes 2-5 minutes. The URL won't work until you push changes. Check **Settings → Pages** for deployment status.

---

## Part 4: Explore the Template

Before editing, take a few minutes to understand what you're working with.

**Open these files in VS Code and look through them:**

| File | Purpose |
|------|---------|
| `index.html` | Your main portfolio page — structure and content |
| `css/styles.css` | All the visual styling — colors, fonts, layout |
| `README.md` | Documentation explaining the template |

**Notice in `index.html`:**
- `<!-- TODO: ... -->` comments mark places for you to add your content
- The page is divided into clear sections: navigation, header, welcome, about, portfolio cards, reflection, footer
- Each section has placeholder text you'll replace

**Notice in `css/styles.css`:**
- The `:root` section at the top defines color variables
- You don't need to understand all the CSS — just know where the colors are defined

---

## Part 5: Make It Yours

Now for the fun part — personalizing your portfolio. Complete the following tasks:

### Task 1: Update Your Name (Required)

Find and replace **"Your Name"** in three locations:

1. **Header section** — the main `<h1>` with your name
2. **Footer section** — the copyright line
3. **Page title** — inside the `<title>` tag in `<head>` (this shows in browser tabs)

Also update:
- The **GitHub link** in the footer with your actual username and repository name

### Task 2: Write Your "About Me" (Required)

Find the About Me section (marked with TODO comments) and replace the placeholder content.

Write authentic responses to:
- **Who I am:** Your name, major, year, and one interesting fact
- **My interests:** What topics, hobbies, or questions excite you?
- **What I hope to learn:** What skills or knowledge do you want from this course?

**Aim for 100-150 words total.** Be genuine — this is your professional introduction.

### Task 3: Customize Your Colors (Required)

Open `css/styles.css` and find the `:root` section near the top (around lines 1-10). You'll see color variables like:

```css
:root {
    --primary-color: #4d1979;
    --secondary-color: #7c3aed;
    --accent-color: #ffd700;
    /* ... more colors ... */
}
```

**Change at least two colors** to create your own palette. Some options:

| Style | Primary | Secondary | Accent |
|-------|---------|-----------|--------|
| TCU Purple (default) | `#4d1979` | `#7c3aed` | `#ffd700` |
| Ocean Blue | `#1e3a5f` | `#3b82f6` | `#06b6d4` |
| Forest Green | `#166534` | `#22c55e` | `#facc15` |
| Warm Coral | `#9f1239` | `#f43f5e` | `#fbbf24` |
| Slate Professional | `#334155` | `#64748b` | `#38bdf8` |

Or use a tool like [Coolors](https://coolors.co/) to generate your own palette.

> 💡 **Tip:** After changing colors, save the file and refresh your browser to see the changes.

### Task 4: Add a Profile Photo (Required)

Add a photo of yourself (or a placeholder image you like) to personalize your portfolio.

1. **Add your image** to the `images/` folder in your project
   - Name it something simple: `profile.jpg` or `headshot.png`
   - Recommended size: 200x200 to 400x400 pixels

2. **Uncomment the image code** in `index.html`:
   - Find the commented-out `<img>` tag in the About section
   - Remove the `<!--` and `-->` surrounding it
   - Update the `src` attribute to match your filename

```html
<!-- Change this: -->
<!-- <img src="images/profile.jpg" alt="Your Name" class="profile-photo"> -->

<!-- To this: -->
<img src="images/profile.jpg" alt="Your Name" class="profile-photo">
```

3. **Update the `alt` text** with your actual name (for accessibility)

### Task 5: Write Your Welcome Message (Required)

Find the Welcome section and replace the placeholder with 2-3 sentences introducing your portfolio.

Consider:
- What will visitors find here?
- What's the purpose of this portfolio?
- What are you hoping to showcase by the end of the semester?

### Task 6: Add Comments to Your Code (Required)

Add HTML comments explaining the changes you made. Comments help us see your understanding and help *you* remember what you did.

**Add at least 5 comments** throughout your `index.html` explaining:
- What content you changed and why
- What sections do (in your own words)
- Any design choices you made

Example:
```html
<!-- I chose this introduction because I want visitors to know
     about my interest in data visualization right away -->
<p>Welcome to my portfolio! I'm excited to explore...</p>
```

---

## Part 6: Commit and Push Your Changes

Once you've made your changes, push them to GitHub so your live site updates.

**In GitHub Desktop:**

1. You'll see all your changed files listed
2. Write a **commit message** describing your changes:
   - Example: "Customize portfolio with personal info and new color scheme"
3. Click **"Commit to main"**
4. Click **"Push origin"**

**Verify your site:**
- Wait 2-3 minutes, then visit your GitHub Pages URL
- Make sure all your changes appear correctly

---

## Part 7: Reflect on Lab 1

Write a reflection about this lab. **This reflection should appear in two places:**

### In Your Portfolio

Update the **Semester Reflection section** at the bottom of your `index.html` with brief responses to:
- What I learned
- Challenges I overcame

You'll expand this section throughout the semester.

### Submitted to D2L

Write a **150-200 word reflection** addressing:

1. **What was new to you?** (GitHub, HTML, CSS, web hosting — or were some familiar?)
2. **What did you find most challenging?** How did you work through it?
3. **What do you want your portfolio to become?** What are you most looking forward to adding as the semester progresses?

---

## Deliverables

Submit to D2L:

1. **Link to your live GitHub Pages site**
   - Example: `https://yourusername.github.io/dcda-portfolio/`

2. **Link to your GitHub repository**
   - Example: `https://github.com/yourusername/dcda-portfolio`

3. **Written reflection (150-200 words)** — as text entry or attached document

**Your portfolio should include:**
- [ ] Your name in header, footer, and page title
- [ ] Personalized "About Me" content (100-150 words)
- [ ] Customized color scheme (at least 2 colors changed)
- [ ] Profile photo added and displaying
- [ ] Welcome message written
- [ ] At least 5 HTML comments explaining your code
- [ ] Reflection started in the Semester Reflection section

---

## Looking Ahead

Your portfolio is now live and personalized — but it's just the beginning. Over the coming weeks, you'll add:

- **Lab 2:** AI Tool Evaluation page
- **Lab 3:** Tufte Visualization Critique
- **Lab 4:** Tableau Interactive Visualization
- **Lab 5:** *(Coming soon)*
- **Lab 6:** Hometown Map with Folium

Each lab builds on this foundation. Keep your portfolio organized, continue refining the design, and document your learning along the way.

By the end of the semester, you'll have a professional showcase of your DCDA skills — something you can share with employers, graduate programs, or anyone you want to impress.

---

## Troubleshooting

**Site not loading?**
- Check Settings → Pages for error messages
- Make sure your repository is Public
- Verify you have an `index.html` file in the root (not in a subfolder)
- Wait a few minutes — GitHub Pages can be slow on first deploy

**Changes not appearing?**
- Did you save your files in VS Code?
- Did you commit AND push in GitHub Desktop?
- Hard refresh your browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)

**Image not showing?**
- Check the filename matches exactly (including capitalization)
- Make sure the image is in the `images/` folder
- Verify the path in your `src` attribute: `images/yourfile.jpg`

**Colors not changing?**
- Make sure you saved `styles.css`
- Check for typos in the hex codes (must start with `#` and have 6 characters)
- Hard refresh your browser to clear the cache
