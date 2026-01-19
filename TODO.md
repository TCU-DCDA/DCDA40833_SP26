# TODO - DCDA 40833 Senior Capstone (Spring 2026)

**Last Updated:** January 2026

---

## High Priority

### Chrome Sidebar Issue ⚠️
**Status:** UNRESOLVED — Works in Safari/Firefox, not Chrome

**Attempted Fixes:**
- Changed JavaScript selector from `nav a` to `.sidebar nav ul a`
- Added smooth scroll behavior
- Tried `position: sticky` with Chrome-specific fixes (`align-self: start`, `-webkit-sticky`)
- Switched to `position: fixed` for cross-browser compatibility

**Debugging Steps to Try:**
1. Check Chrome DevTools Console for JavaScript errors
2. Verify if it's a rendering issue or JavaScript issue
3. Test with `backdrop-filter` disabled (known Chrome quirks)
4. Check z-index stacking and grid layout in Chrome Inspector
5. Simplify CSS to isolate the problem (remove gradients, effects)
6. Test in Chrome Incognito mode to rule out extension conflicts
7. Test with Chrome experimental features disabled

**Files Involved:**
- `docs/styles.css` — Main page sidebar styles
- `docs/lab-styles.css` — Lab page sidebar styles
- `docs/index.html` — Main page JavaScript
- `docs/labs/lab01.html - lab06.html` — Lab page JavaScript

---

## Medium Priority

### Lab Content Review
- [ ] Review Lab 6 (Vibe Coding) content and finalize approach
  - Pedagogical placement as portfolio polish/capstone
  - Relationship to Lab 2 (AI evaluation framework)
  - Confirm: standalone deep dive vs. distributed AI integration
- [ ] Add portfolio integration guidance to each lab
- [ ] Consider adding example student portfolios

### Website Enhancements
- [ ] Mobile responsive testing across devices
- [ ] Add animations/transitions for improved UX
- [ ] Test search functionality thoroughly
- [ ] Add accessibility features (ARIA labels, keyboard navigation)
- [ ] Test hero image loading performance

### Documentation
- [ ] Create development/editing guide for instructors
- [ ] Document color palette and design system (Mazda Soul Red #C1272D)
- [ ] Create student-facing schedule/calendar
- [ ] Consider "getting started" guide for students

### GitHub Workflow
- [ ] Clean up tracked files per .gitignore
- [ ] Consider GitHub Actions for automated checks
- [ ] Student repo template creation

---

## Low Priority / Future Considerations

### AI Integration Strategy
- Lab 2 establishes evaluation framework
- Current approach: minimal AI early, increase as fundamentals solidify
- Revisit as AI tools evolve

### Portfolio Iterative Approach
- Each lab adds to portfolio (6 pages total)
- Consider: portfolio rubric or checklist for students

### Semester Project Bridge
- No explicit "project prep" lab currently
- Consider scaffolding between skills (Labs 1-6) and project proposal

---

## Completed ✓

### Course Website - DEPLOYED
**URL:** https://tcu-dcda.github.io/DCDA40833_SP26/

- ✅ Searchable resource hub (Labs, Portfolio, Projects, Reflections)
- ✅ All 6 lab instruction pages converted to HTML
- ✅ Mazda Soul Red theme with sidebar navigation
- ✅ AI-generated hero images for each lab (abstract tech minimalism)
- ✅ Background images on lab cards with gradient overlays
- ✅ Smooth scroll behavior and active nav states

### Lab Organization - FINALIZED
| Lab | Title | Portfolio Page |
|-----|-------|----------------|
| 1 | Portfolio Setup (GitHub, HTML/CSS) | `index.html` |
| 2 | AI Tool Evaluation (evergreen framework) | `ai-evaluation.html` |
| 3 | Tufte Critique (visualization analysis) | `tufte-critique.html` |
| 4 | Tableau Visualization (Tableau Public) | `tableau-visualization.html` |
| 5 | Python Mapping (Folium/GeoPy) | `hometown-map.html` |
| 6 | Vibe Coding (AI-assisted development) | TBD |

*Rationale: Students gain Python fundamentals before AI-assisted capstone*

### Lab Consistency Updates
- ✅ Portfolio integration with specific HTML page names
- ✅ Consistent GitHub workflow (push repo, verify Pages)
- ✅ Standard submission format (GH repo + Pages links to D2L)
- ✅ Word count minimums for reflections
- ✅ Removed legacy D2L "submit to folder" language
- ✅ Removed pair work options for consistency
- ✅ Professional HTML instruction pages with sidebar nav
- ✅ Visual enrichment with background imagery

---

## Questions for Reflection

1. Does the Lab 5→6 progression (Python→AI-assisted) achieve the right pedagogical flow?
2. Is the resource website design effective for student navigation?
3. Do students need more structured project prep time between labs and semester project?
4. Is the portfolio-building approach clear enough in each lab?
5. What's the right balance between guided exercises and student autonomy?
6. Should we add more visual examples or student work samples to the site?

---

*This file consolidates project tracking formerly split across TODO.md and NEXT_STEPS.md*
