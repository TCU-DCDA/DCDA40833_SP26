# Lab 6: Creating an Interactive Map of Your Hometown

## Preparation

Complete the Lab 6 training notebook to refresh and/or learn the skills needed for this lab:

- **Training Notebook:** [DCDA_Capstone_Python_mapping_2025_V3.ipynb](lab06_materials/DCDA_Capstone_Python_mapping_2025_V3.ipynb)
- **Sample Data:** [lab06_materials/Lab_6_data/](lab06_materials/Lab_6_data/)

The training covers geocoding with GeoPy, creating point maps with Folium, custom basemaps, and exporting maps as HTML.

---

## Task

Create an interactive online map of your hometown. The map should:

- Use a **custom basemap** (create one on [mapbox.com](https://mapbox.com), or use pre-made options from Folium, ESRI, CartoDB, or other sources)
- Include **point-markers for at least 10 locations** unique to your hometown (parks, mom-and-pop restaurants, your church, school, etc.)
- **Do not include** your actual house or other private information
- Think of it as highlighting places for someone visiting your hometown for the first time, or places meaningful to you personally

You will need to create a `.csv` file with those locations to either:
1. Geocode using the Nominatim geocoding service, or
2. Plot using lat/long coordinates you include yourself

The map must have **pop-ups** (tooltips) that include:
- Placename
- Description
- Image URL (when possible)

### CSV Format

| Loc_ID | PlaceName | Address | City | State | Zip | Lat | Lon | About | Image_Url |
|--------|-----------|---------|------|-------|-----|-----|-----|-------|-----------|
| 1 | Example Place | 123 Main St | Yourtown | TX | 76109 | 32.7555 | -97.3308 | Description here | https://... |

---

## Deliverables

Submit a folder to the Lab 6 assignment folder containing:

1. **The map** saved as a `.html` webpage
2. **A PDF reflection** that includes:
   - Link to your Google Colab notebook
     - *Sharing settings:* Share → General access → Anyone with the link → Viewer
   - Answers to the following prompts:
     1. What elements of this exercise were most challenging for you, and why?
     2. How do you see yourself using web-mapping in your final project?
     3. How do you see yourself using web-mapping in your professional life post-graduation?
