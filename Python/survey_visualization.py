"""
AI Survey Data Visualization and Comparison
Compares quantitative responses from 2025 and 2026 survey data
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Set up paths
data_dir = Path(__file__).parent.parent / "data"
file_2025 = data_dir / "First Day Use of AI Survey (Responses) - 2025.csv"
file_2026 = data_dir / "First Day Use of AI Survey (Responses) - 2026.csv"

# Load data
df_2025 = pd.read_csv(file_2025)
df_2026 = pd.read_csv(file_2026)

# Identify quantitative columns (columns 7 and 8 based on the structure)
# Column names for the quantitative questions
feelings_col = "Which better characterizes your feelings towards AI?"
faculty_col = "In my experience, TCU faculty encourages their students to use AI for their coursework."

# Add year labels
df_2025['Year'] = '2025'
df_2026['Year'] = '2026'

# Print basic info
print("=" * 60)
print("SURVEY DATA SUMMARY")
print("=" * 60)
print(f"\n2025 Respondents: {len(df_2025)}")
print(f"2026 Respondents: {len(df_2026)}")

print(f"\n--- Feelings Towards AI (Scale 1-5) ---")
print(f"2025: Mean = {df_2025[feelings_col].mean():.2f}, Std = {df_2025[feelings_col].std():.2f}")
print(f"2026: Mean = {df_2026[feelings_col].mean():.2f}, Std = {df_2026[feelings_col].std():.2f}")

print(f"\n--- Faculty Encouragement of AI (Scale 1-5) ---")
print(f"2025: Mean = {df_2025[faculty_col].mean():.2f}, Std = {df_2025[faculty_col].std():.2f}")
print(f"2026: Mean = {df_2026[faculty_col].mean():.2f}, Std = {df_2026[faculty_col].std():.2f}")

# Create figure with multiple subplots
fig = plt.figure(figsize=(16, 12))

# Color scheme
color_2025 = '#3498db'  # Blue
color_2026 = '#e74c3c'  # Red

# ============================================================================
# PLOT 1: Side-by-side bar chart - Feelings towards AI
# ============================================================================
ax1 = fig.add_subplot(2, 3, 1)

# Count responses for each rating
feelings_counts_2025 = df_2025[feelings_col].value_counts().sort_index()
feelings_counts_2026 = df_2026[feelings_col].value_counts().sort_index()

# Ensure all ratings 1-5 are represented
all_ratings = range(1, 6)
counts_2025 = [feelings_counts_2025.get(r, 0) for r in all_ratings]
counts_2026 = [feelings_counts_2026.get(r, 0) for r in all_ratings]

x = np.arange(len(all_ratings))
width = 0.35

bars1 = ax1.bar(x - width/2, counts_2025, width, label='2025', color=color_2025, edgecolor='black')
bars2 = ax1.bar(x + width/2, counts_2026, width, label='2026', color=color_2026, edgecolor='black')

ax1.set_xlabel('Rating (1=Negative, 5=Positive)', fontsize=10)
ax1.set_ylabel('Number of Respondents', fontsize=10)
ax1.set_title('Feelings Towards AI\n(Count by Rating)', fontsize=12, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(all_ratings)
ax1.legend()
ax1.set_ylim(0, max(max(counts_2025), max(counts_2026)) * 1.2)

# Add value labels on bars
for bar in bars1:
    height = bar.get_height()
    if height > 0:
        ax1.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
for bar in bars2:
    height = bar.get_height()
    if height > 0:
        ax1.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

# ============================================================================
# PLOT 2: Side-by-side bar chart - Faculty Encouragement
# ============================================================================
ax2 = fig.add_subplot(2, 3, 2)

faculty_counts_2025 = df_2025[faculty_col].value_counts().sort_index()
faculty_counts_2026 = df_2026[faculty_col].value_counts().sort_index()

counts_fac_2025 = [faculty_counts_2025.get(r, 0) for r in all_ratings]
counts_fac_2026 = [faculty_counts_2026.get(r, 0) for r in all_ratings]

bars3 = ax2.bar(x - width/2, counts_fac_2025, width, label='2025', color=color_2025, edgecolor='black')
bars4 = ax2.bar(x + width/2, counts_fac_2026, width, label='2026', color=color_2026, edgecolor='black')

ax2.set_xlabel('Rating (1=Disagree, 5=Agree)', fontsize=10)
ax2.set_ylabel('Number of Respondents', fontsize=10)
ax2.set_title('Faculty Encourages AI Use\n(Count by Rating)', fontsize=12, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(all_ratings)
ax2.legend()
ax2.set_ylim(0, max(max(counts_fac_2025), max(counts_fac_2026)) * 1.2)

for bar in bars3:
    height = bar.get_height()
    if height > 0:
        ax2.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
for bar in bars4:
    height = bar.get_height()
    if height > 0:
        ax4_text = ax2.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

# ============================================================================
# PLOT 3: Mean Comparison Bar Chart
# ============================================================================
ax3 = fig.add_subplot(2, 3, 3)

categories = ['Feelings\nTowards AI', 'Faculty\nEncouragement']
means_2025 = [df_2025[feelings_col].mean(), df_2025[faculty_col].mean()]
means_2026 = [df_2026[feelings_col].mean(), df_2026[faculty_col].mean()]
stds_2025 = [df_2025[feelings_col].std(), df_2025[faculty_col].std()]
stds_2026 = [df_2026[feelings_col].std(), df_2026[faculty_col].std()]

x_cat = np.arange(len(categories))
width_cat = 0.35

bars5 = ax3.bar(x_cat - width_cat/2, means_2025, width_cat, label='2025', color=color_2025, 
                edgecolor='black', yerr=stds_2025, capsize=5)
bars6 = ax3.bar(x_cat + width_cat/2, means_2026, width_cat, label='2026', color=color_2026, 
                edgecolor='black', yerr=stds_2026, capsize=5)

ax3.set_ylabel('Mean Rating', fontsize=10)
ax3.set_title('Mean Ratings Comparison\n(with Standard Deviation)', fontsize=12, fontweight='bold')
ax3.set_xticks(x_cat)
ax3.set_xticklabels(categories)
ax3.legend()
ax3.set_ylim(0, 5.5)
ax3.axhline(y=3, color='gray', linestyle='--', alpha=0.5, label='Neutral (3)')

# Add mean value labels
for bar, mean in zip(bars5, means_2025):
    ax3.annotate(f'{mean:.2f}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')
for bar, mean in zip(bars6, means_2026):
    ax3.annotate(f'{mean:.2f}', xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')

# ============================================================================
# PLOT 4: Distribution Histogram - Feelings (Normalized)
# ============================================================================
ax4 = fig.add_subplot(2, 3, 4)

# Convert to percentages for fair comparison
pct_2025 = [c/len(df_2025)*100 for c in counts_2025]
pct_2026 = [c/len(df_2026)*100 for c in counts_2026]

bars7 = ax4.bar(x - width/2, pct_2025, width, label='2025', color=color_2025, edgecolor='black', alpha=0.8)
bars8 = ax4.bar(x + width/2, pct_2026, width, label='2026', color=color_2026, edgecolor='black', alpha=0.8)

ax4.set_xlabel('Rating (1=Negative, 5=Positive)', fontsize=10)
ax4.set_ylabel('Percentage of Respondents (%)', fontsize=10)
ax4.set_title('Feelings Towards AI\n(Percentage Distribution)', fontsize=12, fontweight='bold')
ax4.set_xticks(x)
ax4.set_xticklabels(all_ratings)
ax4.legend()

for bar in bars7:
    height = bar.get_height()
    if height > 0:
        ax4.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)
for bar in bars8:
    height = bar.get_height()
    if height > 0:
        ax4.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)

# ============================================================================
# PLOT 5: Distribution Histogram - Faculty Encouragement (Normalized)
# ============================================================================
ax5 = fig.add_subplot(2, 3, 5)

pct_fac_2025 = [c/len(df_2025)*100 for c in counts_fac_2025]
pct_fac_2026 = [c/len(df_2026)*100 for c in counts_fac_2026]

bars9 = ax5.bar(x - width/2, pct_fac_2025, width, label='2025', color=color_2025, edgecolor='black', alpha=0.8)
bars10 = ax5.bar(x + width/2, pct_fac_2026, width, label='2026', color=color_2026, edgecolor='black', alpha=0.8)

ax5.set_xlabel('Rating (1=Disagree, 5=Agree)', fontsize=10)
ax5.set_ylabel('Percentage of Respondents (%)', fontsize=10)
ax5.set_title('Faculty Encourages AI Use\n(Percentage Distribution)', fontsize=12, fontweight='bold')
ax5.set_xticks(x)
ax5.set_xticklabels(all_ratings)
ax5.legend()

for bar in bars9:
    height = bar.get_height()
    if height > 0:
        ax5.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)
for bar in bars10:
    height = bar.get_height()
    if height > 0:
        ax5.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)

# ============================================================================
# PLOT 6: Box Plots for Both Variables
# ============================================================================
ax6 = fig.add_subplot(2, 3, 6)

# Prepare data for box plots
box_data = [
    df_2025[feelings_col].dropna().values,
    df_2026[feelings_col].dropna().values,
    df_2025[faculty_col].dropna().values,
    df_2026[faculty_col].dropna().values
]

positions = [1, 2, 4, 5]
bp = ax6.boxplot(box_data, positions=positions, widths=0.6, patch_artist=True)

# Color the boxes
colors_box = [color_2025, color_2026, color_2025, color_2026]
for patch, color in zip(bp['boxes'], colors_box):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax6.set_xticks([1.5, 4.5])
ax6.set_xticklabels(['Feelings Towards AI', 'Faculty Encouragement'], fontsize=10)
ax6.set_ylabel('Rating', fontsize=10)
ax6.set_title('Distribution Comparison (Box Plots)', fontsize=12, fontweight='bold')
ax6.set_ylim(0.5, 5.5)

# Add legend for box plot
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color_2025, alpha=0.7, edgecolor='black', label='2025'),
                   Patch(facecolor=color_2026, alpha=0.7, edgecolor='black', label='2026')]
ax6.legend(handles=legend_elements, loc='upper right')

# Overall title
fig.suptitle('AI Survey Comparison: 2025 vs 2026\n', fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()

# Save figure
output_path = data_dir.parent / "Code" / "survey_comparison_visualization.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"\n✓ Visualization saved to: {output_path}")

plt.show()

# ============================================================================
# ADDITIONAL: Summary Statistics Table
# ============================================================================
print("\n" + "=" * 60)
print("DETAILED STATISTICS")
print("=" * 60)

# Create summary dataframe
summary_data = {
    'Metric': ['n', 'Mean', 'Median', 'Std Dev', 'Min', 'Max'],
    'Feelings 2025': [
        len(df_2025),
        f"{df_2025[feelings_col].mean():.2f}",
        f"{df_2025[feelings_col].median():.1f}",
        f"{df_2025[feelings_col].std():.2f}",
        f"{df_2025[feelings_col].min():.0f}",
        f"{df_2025[feelings_col].max():.0f}"
    ],
    'Feelings 2026': [
        len(df_2026),
        f"{df_2026[feelings_col].mean():.2f}",
        f"{df_2026[feelings_col].median():.1f}",
        f"{df_2026[feelings_col].std():.2f}",
        f"{df_2026[feelings_col].min():.0f}",
        f"{df_2026[feelings_col].max():.0f}"
    ],
    'Faculty 2025': [
        len(df_2025),
        f"{df_2025[faculty_col].mean():.2f}",
        f"{df_2025[faculty_col].median():.1f}",
        f"{df_2025[faculty_col].std():.2f}",
        f"{df_2025[faculty_col].min():.0f}",
        f"{df_2025[faculty_col].max():.0f}"
    ],
    'Faculty 2026': [
        len(df_2026),
        f"{df_2026[faculty_col].mean():.2f}",
        f"{df_2026[faculty_col].median():.1f}",
        f"{df_2026[faculty_col].std():.2f}",
        f"{df_2026[faculty_col].min():.0f}",
        f"{df_2026[faculty_col].max():.0f}"
    ]
}

summary_df = pd.DataFrame(summary_data)
print("\n")
print(summary_df.to_string(index=False))

# Response distribution tables
print("\n" + "-" * 60)
print("RESPONSE DISTRIBUTION: Feelings Towards AI")
print("-" * 60)
dist_feelings = pd.DataFrame({
    'Rating': list(all_ratings),
    '2025 Count': counts_2025,
    '2025 %': [f"{p:.1f}%" for p in pct_2025],
    '2026 Count': counts_2026,
    '2026 %': [f"{p:.1f}%" for p in pct_2026]
})
print(dist_feelings.to_string(index=False))

print("\n" + "-" * 60)
print("RESPONSE DISTRIBUTION: Faculty Encouragement")
print("-" * 60)
dist_faculty = pd.DataFrame({
    'Rating': list(all_ratings),
    '2025 Count': counts_fac_2025,
    '2025 %': [f"{p:.1f}%" for p in pct_fac_2025],
    '2026 Count': counts_fac_2026,
    '2026 %': [f"{p:.1f}%" for p in pct_fac_2026]
})
print(dist_faculty.to_string(index=False))
