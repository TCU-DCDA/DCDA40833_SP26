# Vibe Coding -- Instructor Outline

Two-session prep for Lab 5 (Vibe Coding). Glanceable reference for running class.

- Students have VS Code + GitHub Copilot Pro (GitHub Education)
- They use GitHub Desktop, not CLI
- Prior Python experience but many are anxious about it
- Ungrading model -- students argue for their grade based on quality of work
- Lab has three experiments: A (portfolio enhancement), B (Python in Colab), C (debugging with AI)
- Students must complete at least two experiments
- Understanding Spectrum for commenting: I wrote this / I understand the logic / I know what it does but not how / I don't understand this

---

# DAY 1: Intro + Demo

---

## Copilot Orientation

- Have students open VS Code
- Walk through three ways to use Copilot:
  - **Inline suggestions** -- autocomplete as you type, Tab to accept, Esc to dismiss
  - **Copilot Chat panel** -- Cmd+Shift+I (Mac) / Ctrl+Shift+I (Windows) -- full conversations
  - **Inline chat** -- Cmd+I / Ctrl+I -- quick question right in code
- Show how to switch models in the chat panel (Claude, GPT-4o, Gemini, etc.)
- Key message: **"For this lab, Copilot Chat is your main tool. Describe what you want, review what comes back."**

> Transition: "Now that you know the tools, let's talk about the different ways people use them."

---

## The AI Coding Spectrum

- Walk through four levels using a concrete example (dark mode toggle):
  - **Fundamentals First** -- You write the CSS and JS; ask AI "why isn't my class toggle working?"
  - **Collaborative** -- You sketch the approach; AI writes the implementation
  - **Vibe Coding** -- You say "add dark mode to my site" and review what comes back
  - **Full Automation** -- You paste AI output, it works, you move on without reading it
- Discussion prompt: **"Where on this spectrum have you been operating? Where should you be?"**
- Key point: the spectrum isn't a ladder -- moving "up" isn't always better
- Key point: it depends on the task, your familiarity, and what you're trying to learn
- Nail the rule: **"You must be able to read, explain, and modify any code you use."**

> Transition: "Before we start experimenting, let's create a safety net."

---

## Save Point

- Everyone opens GitHub Desktop together
- Walk them through: check all changes, summary "Save before Lab 5 experiments", Commit to main, Push origin
- **"This is your save point. If anything breaks, you can go back to this commit on GitHub and grab the working version of any file."**
- Quick mention: to recover, go to your repo on GitHub.com, click the file, click History, grab the old version

> Transition: "Now let's see what vibe coding actually looks like."

---

## Live Demo: Hamburger Nav Menu

Reference materials: `demo-before.html` and `demo-after.html` in this folder.

### Step 1 -- Plan First

- Open `demo-before.html` -- show the basic portfolio with a horizontal nav
- Ask: "What do we need to make this work on mobile?"
- Sketch on board or list: hamburger button, collapsible nav, media query, JS toggle
- **"Always plan before you prompt."**

### Step 2 -- Craft the Prompt

- Show a bad prompt: "make my site responsive"
- Show a good prompt: "Add a hamburger menu to my HTML portfolio. The nav should collapse into a hamburger icon on screens under 768px. Use vanilla JavaScript, no frameworks. Here's my current HTML: [paste]"
- Ask students: **"What makes the second prompt better?"** (context, specificity, constraints)

### Step 3 -- Review the Output

- Open `demo-after.html` -- walk through the AI's response line by line
- This is the teaching moment: model how to read code you didn't write
- Point out the Understanding Spectrum comments in the demo file
- Show examples of each level:
  - "I wrote this" -- brief, confident
  - "I understand the logic" -- explains in own words
  - "I know what it does but not how" -- flags the CSS transform
  - "I don't understand this" -- flags aria-expanded, documents what they learned
- **"Your comments are a record of your understanding, not a performance."**
- Ask: **"What's the difference between these comments and just writing '// toggle menu' above everything?"**

### Step 4 -- Test and Refine

- Open in browser, resize window, show the hamburger working
- Find or introduce a bug: "The menu doesn't close when I click a link"
- Show two options: go back to AI and ask for a fix, OR fix it yourself
- Either way, you need to understand the fix

### Step 5 -- Good vs. Bad Comments Side by Side

- Bad: `// toggle menu` above `toggleMenu()`
- Good: `// When hamburger is clicked, toggle 'active' class on the nav. This triggers the CSS transform to slide the menu in from the right. I understand classList.toggle but had to look up how the CSS transition works.`

> Transition: "That was a front-end example. Let's do the same thing with data."

---

## Live Demo 2: Data Collection & Analysis

Reference material: `demo-data.py` in this folder. Run this in **Google Colab** (colab.research.google.com).

### Step 1 -- Plan First

- Pose the question: **"Which countries have the most UNESCO World Heritage Sites?"**
- Ask students: "What do we need to answer this?"
- List on board: a data source, a way to read it into Python, some filtering, a chart
- **"Same rule: plan before you prompt."**

### Step 2 -- Craft the Prompt

- Open a new Colab notebook
- Show a bad prompt: "analyze some data for me"
- Show a good prompt: "Use pandas to scrape the Wikipedia table of World Heritage Sites by country. Show me the top 10 countries by total number of sites. Then create a horizontal bar chart with matplotlib."
- Ask: **"Why is this better?"** (names the library, names the source, specifies "top 10," specifies chart type)

### Step 3 -- Review the Output

- Paste the AI's response into a Colab cell and run it
- Walk through the code line by line:
  - `pd.read_html(url)` -- **"One line scrapes an entire table from a webpage."** Pause here. This is the hook.
  - It returns a list of DataFrames -- ask: **"Why a list? Wikipedia pages have many tables."** Show how `[0]` or indexing selects the right one.
  - Column names may be messy (multi-level headers, footnote markers) -- **"This is what real data looks like."**
  - `nlargest()` or `sort_values()` + `head()` for top 10
  - `plt.barh()` for the chart
- If column names or table structure have changed since you last tested, that's fine -- model debugging live: **"The AI wrote code for the table structure it expected. The real table is slightly different. That's normal."**
- Key message: **"With data code, you can check if the output is correct by looking at it. You know how many World Heritage Sites Italy has -- does the chart match?"**

### Step 4 -- Iterate

- The first chart probably looks generic. Ask the AI to improve it:
  - "Sort the bars so the country with the most sites is at the top. Add a title. Use a color that isn't the default blue."
- Show the before/after
- **"Small, specific follow-up prompts beat rewriting the whole thing."**
- Point out: this is the same cycle. Plan → prompt → review → iterate. Works for HTML, works for data.

### Step 5 -- Quick Understanding Spectrum Check

- Point to a line: `pd.read_html(url)` -- **"Where would you put this on the spectrum?"**
  - Most students: "I know what it does but not how" -- that's honest and fine
- Point to `plt.barh()` -- same question
- **"You'd comment these the same way you commented the hamburger CSS."**

> Transition: "You've now seen vibe coding for front-end and for data. Time to try it yourself."

---

## Experiment Selection + Work Time

- Overview of the three experiments:
  - **Experiment A** -- Portfolio enhancement -- HTML/CSS/JS in VS Code. Options listed in lab.
  - **Experiment B** -- Python in Google Colab (colab.research.google.com) -- no installation needed. Difficulty labels on options. **"If Python makes you nervous, this might be the best one to try -- using AI to help with something you're uncomfortable with is exactly what makes this interesting."**
  - **Experiment C** -- Debug with AI -- starter bugs provided in the lab. Try to find the bug yourself first, then compare with AI.
- Remind: at least two experiments
- Remind: **save your prompts and AI responses as you go** -- you need them for submission
- Students start working. Circulate. Watch for:
  - Students who are stuck choosing
  - Students who are scope-creeping (steer toward simpler)
  - Students who accepted AI output without reading it
  - Colab questions from Python-anxious students

---

# DAY 2: Work Time + Reflection Prep

---

## Check-in

- Quick pulse: **"Where are you? What's stuck?"**
- Address common issues from Day 1
- If many students are stuck on the same thing, do a quick whole-class walkthrough

---

## Work Time

- Students continue experiments. Circulate and check:
  - Are comments honest or performative?
  - Are Python/Colab students stuck?
  - Is anyone scope-creeping? Steer them back.
  - Has anyone not been saving prompts? Remind them now.

---

## Reflection Preview

- Reference: `reflection-examples.md` in this folder
- Show the generic example first. Ask: **"What's wrong with this?"**
  - Vague, could apply to anyone, no specific examples, says the "right things" without conviction
- Show the strong example. Ask: **"What makes this better?"**
  - Specific references to actual work, honest about gaps, identifies tension, personal voice
- Key reminders:
  - 400-600 words
  - **Your own voice -- no AI**
  - The self-assessment questions in the lab are a good starting point
  - Connect your reflection to your Understanding Spectrum comments -- you can point to specific moments
- Submission checklist:
  - Portfolio with lab05.html on GitHub Pages
  - D2L: reflection (PDF/Word), commented code (or .ipynb + datasets for Colab), prompts, AI output examples, GitHub Pages URL + repo URL
- **"A simple experiment you understand deeply will make a much better reflection than a complex one you can't explain."**

---

# NOTES

---

## If students haven't applied for GitHub Education yet

- They need to start NOW -- 7-14 business days for approval
- Pre-application checklist is in the lab page (GitHub Education Setup section)
- In the meantime, they can use ChatGPT, Claude, or any other AI tool for the experiments

## Recovery from broken portfolio

- Go to repo on GitHub.com
- Click the file that broke
- Click History
- Find the "Save before Lab 5 experiments" commit
- Click the commit, copy the old file content
- Paste back into VS Code, save, commit, push

## Common student questions

- **"Can I do all three experiments?"** -- Yes, but two is the minimum. Quality over quantity.
- **"Does my Experiment B code need to be in my portfolio repo?"** -- Yes. Download the .ipynb and any datasets, add them to your repo, and link from your lab05.html page.
- **"What if the AI-generated code is already perfect?"** -- Look more closely. Is the code accessible? Is it efficient? Are variable names clear? Does it handle edge cases? "Perfect" usually just means "it runs."
- **"Can I use ChatGPT instead of Copilot?"** -- Yes, any AI tool is fine. The lab is about the process, not the specific tool.
