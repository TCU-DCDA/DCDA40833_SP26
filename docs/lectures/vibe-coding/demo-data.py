# demo-data.py
# Reference script for Live Demo 2: Data Collection & Analysis
# Run in Google Colab (pandas, matplotlib are pre-installed)
#
# This shows the expected output from the vibe coding demo.
# The instructor prompts an AI live; this file is the "answer key."

import pandas as pd
import matplotlib.pyplot as plt

# === DATA COLLECTION ===
# I understand the logic: read_html fetches a webpage and finds all
# <table> elements, returning each one as a DataFrame. The URL points
# to the Wikipedia page listing World Heritage Sites by country.
# It returns a list because a page can have many tables.

url = "https://en.wikipedia.org/wiki/World_Heritage_Sites_by_country"
tables = pd.read_html(url)

# I know what this does but not how: Wikipedia pages have dozens of
# tables (infoboxes, navboxes, etc.). The main data table is usually
# one of the larger ones. You may need to inspect a few indices to
# find the right one. In Colab, just print len(tables) and check
# tables[0].head(), tables[1].head(), etc. until you find it.

df = tables[0]

# === DATA CLEANING ===
# I understand the logic: print the columns and first few rows to
# see what we're working with. Wikipedia column names often have
# footnote markers or multi-level headers that need cleaning.

print(df.columns.tolist())
print(df.head())

# Rename columns to something clean.
# NOTE: The exact column names depend on the current state of the
# Wikipedia page. Check the output above and adjust if needed.
# As of early 2026, the columns include country name and total count.
# If the column names have changed, this is a great live debugging moment.

# === ANALYSIS ===
# I understand the logic: sort by the total number of sites in
# descending order and take the top 10. nlargest is a shortcut
# for sort_values + head.

# Adjust column names below based on what df.columns shows you.
# Common variations: "Total", "Total properties", "Total sites"
country_col = df.columns[0]  # Usually the country name
total_col = df.columns[-1]   # Usually the total count

# Convert total column to numeric (may have footnote markers)
df[total_col] = pd.to_numeric(df[total_col], errors="coerce")

top10 = df.nlargest(10, total_col)

print(top10[[country_col, total_col]])

# === VISUALIZATION (first pass) ===
# I understand the logic: barh makes a horizontal bar chart.
# The y-axis is countries, x-axis is the count. This is the
# "it works but looks generic" version.

plt.figure(figsize=(10, 6))
plt.barh(top10[country_col], top10[total_col])
plt.xlabel("Number of World Heritage Sites")
plt.title("Top 10 Countries by UNESCO World Heritage Sites")
plt.gca().invert_yaxis()  # Highest at top
plt.tight_layout()
plt.show()

# === VISUALIZATION (after iteration) ===
# I understand the logic: same chart with better styling.
# This is what the follow-up prompt produces -- sorted bars,
# a custom color, and cleaner layout.

top10_sorted = top10.sort_values(total_col, ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(
    top10_sorted[country_col],
    top10_sorted[total_col],
    color="#2a9d8f"
)
plt.xlabel("Number of World Heritage Sites")
plt.title("Top 10 Countries by UNESCO World Heritage Sites")
plt.tight_layout()
plt.show()
