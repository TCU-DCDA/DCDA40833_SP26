# Lab 6: Custom Basemap Design & Interactive Hometown Map - Evaluation Rubric

## Overview
This rubric uses an ungrading approach to help you understand expectations and assess your own work. It is structured in two parts: a **Completion Checklist** of required deliverables and **Quality Dimensions** where your work can demonstrate different levels of depth and sophistication. This lab sits at the intersection of creative design and technical implementation — both matter, and the rubric reflects that.

---

## Part 1: Completion Checklist

The following items are required deliverables. They are evaluated on a complete/incomplete basis — all items must be present for the assignment to be considered submitted. These are not areas where "exceeding expectations" applies; they are simply done or not done.

- [ ] **Custom Mapbox basemap published** — A custom style is created in Mapbox Studio from the Blank template with at least 12 individually styled layers/components, published publicly, and the style URL is included in the submission
- [ ] **Hometown locations CSV created** — `hometown_locations.csv` contains at least 10 personally meaningful locations with all required columns (Name, Address, Type, Description, Image_URL) and at least 3 different location types
- [ ] **Python script completed** — A `.py` file that reads the CSV, geocodes addresses via the Mapbox API, creates a Folium map with the custom basemap, adds categorized markers with pop-ups (name, description, image), and saves the result as an HTML file
- [ ] **Interactive map generated** — The final `.html` map file loads the custom basemap, displays all locations with working pop-ups, and uses different marker colors/symbols by location type
- [ ] **Written reflection submitted** — 250–500 word reflection addressing all three prompts (Design Inspiration, Cartographic Challenges, Technical Challenges) submitted as PDF
- [ ] **Portfolio updated** — Interactive map and reflection are added to your portfolio under a Lab 6 section, pushed to GitHub, and live on GitHub Pages
- [ ] **Submitted to D2L** — Mapbox style URL, CSV file, Python script, HTML map, reflection PDF, and GitHub/GitHub Pages links all submitted to the D2L dropbox

---

## Part 2: Quality Dimensions

The following dimensions evaluate the depth and quality of your work. This is where meaningful variation between students occurs, and where you should focus when reflecting on your grade.

---

### 1. Basemap Design & Cartographic Craft

*This evaluates the visual quality, coherence, and intentionality of your custom Mapbox basemap. The question is not whether you're a professional cartographer, but whether you made deliberate design choices and thought carefully about how your map communicates across scales.*

#### Exceeds Expectations
- Basemap has a clear, recognizable visual connection to the stated inspiration source — a viewer could see the relationship without it being explained
- Color palette, typography, and styling work together as a coherent visual system, not a collection of unrelated choices
- Map is thoughtfully designed across zoom levels: features appear and disappear at appropriate scales, labels resize, and the map remains readable from world view to street level
- Goes beyond the minimum 12 layers — adds custom layers, uploaded fonts, or other elements that show creative initiative
- Design choices demonstrate awareness of cartographic principles (visual hierarchy, figure-ground contrast, legibility)

#### Meets Expectations
- Basemap has a visible connection to the inspiration source through color choices and overall aesthetic
- All five required components are present and customized beyond defaults
- Meets the 12-layer minimum with meaningful customization
- Map is functional at multiple zoom levels — not perfect, but no major readability failures
- Design shows evidence of intentional choices rather than arbitrary experimentation

#### Does Not Meet Expectations
- No recognizable connection between the basemap and the stated inspiration
- Components use default or barely modified settings
- Fewer than 12 styled layers, or layers are trivially different from each other
- Map breaks at certain zoom levels (labels collide, features disappear unexpectedly, colors become unreadable)
- Design appears rushed or arbitrary — no evidence of iterative refinement

---

### 2. Dataset Quality & Personal Voice

*This evaluates the thoughtfulness of your location selections and the quality of your descriptions. The dataset is a creative artifact — it tells a story about your relationship with a place.*

#### Exceeds Expectations
- Locations represent a genuinely curated tour — the selection tells a coherent story about the hometown and what makes it meaningful to the student
- Descriptions are personal, specific, and written in an authentic voice — a reader learns something about both the place and the person
- Location types are diverse and show range beyond the obvious (not just 10 restaurants)
- Addresses are accurate and geocode correctly; image URLs work and show relevant images
- CSV is clean, properly formatted, and ready for direct use by the Python script

#### Meets Expectations
- At least 10 locations with at least 3 different types
- Descriptions explain why each place is personally meaningful in 2–3 sentences
- Descriptions are in the student's own words, not copied from Google or Yelp
- Addresses are accurate enough for geocoding; image URLs are functional
- CSV structure matches the required format

#### Does Not Meet Expectations
- Fewer than 10 locations or fewer than 3 types
- Descriptions are generic, impersonal, or clearly copied from external sources
- Locations feel chosen for convenience rather than personal significance
- Multiple addresses fail to geocode or image URLs are broken
- CSV has formatting issues that cause errors in the Python script

---

### 3. Technical Implementation

*This evaluates the quality of your Python code and the resulting interactive map. If you used AI to help generate your code, what matters is whether the final product works correctly and whether you understand what it does.*

#### Exceeds Expectations
- Code is clean, well-organized, and handles edge cases (e.g., failed geocoding, missing data)
- Pop-ups are well-formatted with styled HTML — name, description, and image display attractively
- Marker colors/symbols are meaningfully mapped to location types with a clear visual logic
- Map centers and zooms appropriately to show all locations
- Code includes comments that demonstrate genuine understanding, not just AI-generated boilerplate
- If AI tools were used, the student can articulate what the code does and has made meaningful modifications

#### Meets Expectations
- Code runs without errors and produces a working HTML map
- Custom Mapbox basemap loads correctly (not a default tile set)
- All locations appear as markers with working pop-ups showing name, description, and image
- Different location types are visually distinguishable through color or icon
- Code is commented at a basic level

#### Does Not Meet Expectations
- Code does not run, or produces a broken/incomplete map
- Custom basemap fails to load — map shows default tiles or a blank background
- Markers are missing, pop-ups are broken, or images don't display
- No visual distinction between location types
- Code has no comments and student cannot explain what it does

---

### 4. Reflection Quality

*This evaluates the depth and specificity of your written reflection. The three prompts ask about design, cartography, and code — together they should tell the story of your process and what you learned.*

#### Exceeds Expectations
- **Design Inspiration:** Clearly articulates the connection between the inspiration source and the basemap with specific visual examples — "I used this shade of blue from the film's color palette for water" rather than "I was inspired by the movie"
- **Cartographic Challenges:** Shows genuine engagement with the problem of multi-scale design; discusses specific trade-offs and decisions about what to show or hide at different zoom levels
- **Technical Challenges:** Provides specific, concrete descriptions of coding problems encountered and how they were solved; if AI tools were used, describes the collaboration honestly
- Reflection reads as a thoughtful account of a creative and technical process, not a checklist response
- Includes reference images that clearly connect to the basemap design

#### Meets Expectations
- Addresses all three prompts with adequate detail (250–500 words total)
- Provides specific examples from the actual work rather than speaking in generalities
- Design inspiration section includes reference images
- Technical and cartographic challenges are drawn from real experience, not hypothetical
- Written in the student's own voice

#### Does Not Meet Expectations
- Prompts are addressed superficially or skipped
- Observations are generic and could apply to anyone without having done the assignment
- No reference images included, or images have no clear connection to the basemap
- Reflection reads as AI-generated or as a formulaic response
- Below the minimum word count or significantly padded with filler

---

### 5. Writing Quality & Portfolio Integration

*This evaluates how well the final product is presented and integrated into your portfolio.*

#### Exceeds Expectations
- Writing is clear, engaging, and well-organized across all written components
- Portfolio page presents the interactive map and reflection in a polished, professional layout
- Map is embedded or linked in a way that works seamlessly within the portfolio design
- Page is consistent with the overall portfolio aesthetic and navigation structure
- Demonstrates careful revision and attention to presentation quality

#### Meets Expectations
- Writing is clear and organized; ideas are communicated effectively
- Portfolio page includes the map and reflection with functional formatting
- Page is accessible from the main portfolio navigation
- Few distracting errors in grammar, mechanics, or formatting
- Shows evidence of proofreading

#### Does Not Meet Expectations
- Writing is unclear, disorganized, or difficult to follow
- Portfolio page is missing, broken, or not linked from navigation
- Map doesn't load on the portfolio page or reflection is absent
- Significant errors interfere with communication
- Page appears rushed or unfinished

---

## Self-Assessment Questions

Before submitting, reflect on these questions honestly:

1. **Design Coherence:** Does my basemap have a clear, recognizable connection to my inspiration source? Could someone see the relationship without me explaining it?

2. **Scale Awareness:** Does my map look intentional at different zoom levels, or does it fall apart when zooming in or out?

3. **Data Quality:** Are my location descriptions genuinely personal and meaningful, or are they generic descriptions I could have pulled from Google?

4. **Code Understanding:** If I used AI to generate my Python code, can I explain what each section does? Could I modify it to add a new feature?

5. **Integration:** Do all three components (basemap, data, Python map) work together seamlessly?

6. **Portfolio Quality:** Does this page represent work I would be comfortable showing to a potential employer or graduate program?

---

## Notes on Ungrading Approach

This rubric is designed to help you:
- Understand the difference between completing required deliverables and demonstrating quality in your creative and technical work
- Recognize that this lab rewards both aesthetic intentionality and technical competence — neither alone is sufficient
- Develop skills in cartographic design, data creation, and Python-based web mapping
- Self-assess the coherence and care you brought to a multi-component project

The Completion Checklist ensures all required elements are present. The Quality Dimensions are where you demonstrate growth, creative vision, and technical engagement. When reflecting on your grade, focus on the quality dimensions — that is where the meaningful variation in student work occurs.
