# TODO - DCDA 40833 Course Site

## High Priority

### Chrome Sidebar Issue (UNRESOLVED)
**Status:** Not working in Chrome, works in Safari/Firefox
**Attempted Fixes:**
- Changed JavaScript selector from `nav a` to `.sidebar nav ul a`
- Added smooth scroll behavior
- Tried `position: sticky` with Chrome-specific fixes (`align-self: start`, `-webkit-sticky`, etc.)
- Switched to `position: fixed` for cross-browser compatibility

**Next Steps to Try:**
1. Check Chrome DevTools Console for JavaScript errors
2. Verify if it's a rendering issue or JavaScript issue
3. Consider if background images or backdrop-filter are causing issues in Chrome
4. Test with Chrome's experimental features disabled
5. Check if z-index stacking is causing visibility issues
6. Verify grid layout is rendering correctly in Chrome Inspector
7. Try simplifying CSS to isolate the problem (remove backdrop-filter, gradients, etc.)
8. Test in Chrome Incognito mode to rule out extension conflicts

**Files Involved:**
- `docs/styles.css` - Main page sidebar styles
- `docs/lab-styles.css` - Lab page sidebar styles
- `docs/index.html` - Main page JavaScript
- `docs/labs/lab01.html - lab06.html` - Lab page JavaScript

---

## Completed This Session

- ✅ Added background images to all lab cards (index.html)
- ✅ Added prominent hero background images to all lab pages (lab01.html - lab06.html)
- ✅ Created CSS overlay system for readability (80% opacity on heroes, 92% on cards)
- ✅ Swapped Labs 5 and 6 (Python Mapping now Lab 5, Vibe Coding now Lab 6)
- ✅ Removed red badge pills from lab hero sections
- ✅ Reduced sidebar spacing for more compact design
- ✅ Added smooth scroll behavior
- ✅ Updated README.md with new docs/ structure and live site info

---

## Future Enhancements

### Lab Content
- [ ] Review Lab 6 (Vibe Coding) content and finalize approach
- [ ] Add portfolio integration guidance to each lab
- [ ] Consider adding example student portfolios

### Design
- [ ] Mobile responsive testing and refinements
- [ ] Add animations/transitions for better UX
- [ ] Consider adding more visual elements to resource cards

### Documentation
- [ ] Add development documentation (how to edit, deploy, etc.)
- [ ] Document color palette and design system
- [ ] Create content editing guide for instructors

---

*Last updated: December 17, 2024*
