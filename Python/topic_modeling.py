"""
Topic Modeling for AI Survey Qualitative Responses
Compares topics from 2025 and 2026 survey data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import re
from collections import Counter

# NLP imports
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation, NMF
import warnings
warnings.filterwarnings('ignore')

# Set up paths
data_dir = Path(__file__).parent.parent / "data"
file_2025 = data_dir / "First Day Use of AI Survey (Responses) - 2025.csv"
file_2026 = data_dir / "First Day Use of AI Survey (Responses) - 2026.csv"

# Load data
df_2025 = pd.read_csv(file_2025)
df_2026 = pd.read_csv(file_2026)

# Define qualitative columns (excluding coding experience question)
qualitative_cols = [
    "To your best understanding, what is AI? How does AI work? How would you explain what it is to an alien?",
    "How and when do you use AI?",
    "Do you have any fears about AI?",
    "How do you see AI benefiting and/or threatening the rest of your studies and/or early careers?",
    "What controversies are you aware of surrounding the creation, development, current applications, and/or future applications of AI technologies? List as many as come to mind.",
    "What should the instructors of our class know about students' attitudes toward AI that might not otherwise be apparent?",
    "In your opinion, what are the most constructive ways faculty and students can develop a shared understanding of AI's role in our coursework and lives? Put another way, what's your advice to the four course instructors about how to best approach and discuss AI with you, their students?"
]

# Short names for display
col_short_names = {
    qualitative_cols[0]: "What is AI?",
    qualitative_cols[1]: "How/When Use AI?",
    qualitative_cols[2]: "Fears about AI?",
    qualitative_cols[3]: "Benefits/Threats?",
    qualitative_cols[4]: "Controversies?",
    qualitative_cols[5]: "Student Attitudes?",
    qualitative_cols[6]: "Advice for Faculty?"
}

# Custom stopwords relevant to this survey
custom_stopwords = [
    'ai', 'artificial', 'intelligence', 'use', 'used', 'using', 'think', 'know',
    'like', 'just', 'really', 'also', 'would', 'could', 'dont', 'im', 'ive',
    'thats', 'its', 'thing', 'things', 'something', 'lot', 'much', 'many',
    'way', 'ways', 'make', 'made', 'get', 'got', 'going', 'go', 'come',
    'want', 'need', 'sure', 'able', 'feel', 'believe', 'see', 'one', 'well'
]

def preprocess_text(text):
    """Clean and preprocess text for topic modeling."""
    if pd.isna(text):
        return ""
    text = str(text).lower()
    # Remove special characters but keep spaces
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

def get_top_words_per_topic(model, feature_names, n_top_words=10):
    """Extract top words for each topic from the model."""
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        topics.append(top_words)
    return topics

def run_topic_modeling(texts, n_topics=5, method='lda', n_top_words=10):
    """Run topic modeling on a list of texts."""
    # Preprocess
    processed_texts = [preprocess_text(t) for t in texts]
    processed_texts = [t for t in processed_texts if len(t) > 10]  # Filter very short texts
    
    if len(processed_texts) < 3:
        return None, None, None
    
    # Vectorize
    if method == 'lda':
        vectorizer = CountVectorizer(
            max_df=0.95, 
            min_df=2, 
            stop_words='english',
            max_features=1000
        )
    else:  # NMF
        vectorizer = TfidfVectorizer(
            max_df=0.95, 
            min_df=2, 
            stop_words='english',
            max_features=1000
        )
    
    # Add custom stopwords
    if vectorizer.stop_words is None:
        vectorizer.stop_words = custom_stopwords
    else:
        vectorizer.stop_words = list(vectorizer.stop_words) + custom_stopwords
    
    try:
        doc_term_matrix = vectorizer.fit_transform(processed_texts)
    except ValueError:
        return None, None, None
    
    feature_names = vectorizer.get_feature_names_out()
    
    # Fit model
    if method == 'lda':
        model = LatentDirichletAllocation(
            n_components=n_topics,
            random_state=42,
            max_iter=20
        )
    else:
        model = NMF(
            n_components=n_topics,
            random_state=42,
            max_iter=200
        )
    
    model.fit(doc_term_matrix)
    topics = get_top_words_per_topic(model, feature_names, n_top_words)
    
    return model, topics, doc_term_matrix

def get_word_frequencies(texts, top_n=20):
    """Get word frequencies from a list of texts."""
    all_words = []
    for text in texts:
        processed = preprocess_text(text)
        words = processed.split()
        # Filter stopwords
        from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
        words = [w for w in words if w not in ENGLISH_STOP_WORDS 
                 and w not in custom_stopwords 
                 and len(w) > 2]
        all_words.extend(words)
    
    return Counter(all_words).most_common(top_n)

def plot_word_frequencies(freq_2025, freq_2026, title, ax):
    """Plot side-by-side word frequency comparison."""
    # Get all unique words
    words_2025 = dict(freq_2025)
    words_2026 = dict(freq_2026)
    
    # Get top words from both years
    all_words = list(set(list(words_2025.keys())[:15] + list(words_2026.keys())[:15]))[:15]
    
    counts_2025 = [words_2025.get(w, 0) for w in all_words]
    counts_2026 = [words_2026.get(w, 0) for w in all_words]
    
    x = np.arange(len(all_words))
    width = 0.35
    
    ax.barh(x - width/2, counts_2025, width, label='2025', color='#3498db', edgecolor='black')
    ax.barh(x + width/2, counts_2026, width, label='2026', color='#e74c3c', edgecolor='black')
    
    ax.set_yticks(x)
    ax.set_yticklabels(all_words, fontsize=9)
    ax.set_xlabel('Frequency')
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.legend(loc='lower right')
    ax.invert_yaxis()

# ============================================================================
# MAIN ANALYSIS
# ============================================================================

print("=" * 70)
print("TOPIC MODELING: AI SURVEY QUALITATIVE RESPONSES")
print("=" * 70)

# ============================================================================
# PART 1: Word Frequency Analysis by Question
# ============================================================================
print("\n" + "=" * 70)
print("PART 1: TOP WORD FREQUENCIES BY QUESTION")
print("=" * 70)

# Create figure for word frequencies
n_questions = len(qualitative_cols)
fig1, axes1 = plt.subplots(3, 3, figsize=(18, 14))
axes1 = axes1.flatten()

for i, col in enumerate(qualitative_cols):
    short_name = col_short_names[col]
    print(f"\n--- {short_name} ---")
    
    texts_2025 = df_2025[col].dropna().tolist()
    texts_2026 = df_2026[col].dropna().tolist()
    
    freq_2025 = get_word_frequencies(texts_2025, top_n=15)
    freq_2026 = get_word_frequencies(texts_2026, top_n=15)
    
    print(f"2025 Top Words: {[w for w, c in freq_2025[:10]]}")
    print(f"2026 Top Words: {[w for w, c in freq_2026[:10]]}")
    
    if i < len(axes1):
        plot_word_frequencies(freq_2025, freq_2026, short_name, axes1[i])

# Hide unused subplots
for j in range(len(qualitative_cols), len(axes1)):
    axes1[j].axis('off')

# Add note about what was excluded
axes1[-1].text(0.5, 0.5, "Note: Coding experience\nquestion excluded\nfrom analysis", 
               ha='center', va='center', fontsize=12, style='italic',
               transform=axes1[-1].transAxes)
axes1[-1].axis('off')

fig1.suptitle('Word Frequency Comparison by Survey Question: 2025 vs 2026\n', 
              fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig1.savefig(data_dir.parent / "Code" / "word_frequencies_by_question.png", 
             dpi=150, bbox_inches='tight', facecolor='white')
print(f"\n✓ Word frequency visualization saved")

# ============================================================================
# PART 2: Combined Topic Modeling (All Text)
# ============================================================================
print("\n" + "=" * 70)
print("PART 2: TOPIC MODELING (ALL QUALITATIVE RESPONSES COMBINED)")
print("=" * 70)

# Combine all qualitative text for each year
def combine_all_text(df, cols):
    all_text = []
    for _, row in df.iterrows():
        combined = ' '.join([str(row[col]) for col in cols if pd.notna(row[col])])
        all_text.append(combined)
    return all_text

all_text_2025 = combine_all_text(df_2025, qualitative_cols)
all_text_2026 = combine_all_text(df_2026, qualitative_cols)

# Run LDA topic modeling
n_topics = 4

print(f"\n--- 2025 Topics (LDA, {n_topics} topics) ---")
model_2025, topics_2025, dtm_2025 = run_topic_modeling(all_text_2025, n_topics=n_topics)
if topics_2025:
    for i, topic in enumerate(topics_2025):
        print(f"Topic {i+1}: {', '.join(topic)}")

print(f"\n--- 2026 Topics (LDA, {n_topics} topics) ---")
model_2026, topics_2026, dtm_2026 = run_topic_modeling(all_text_2026, n_topics=n_topics)
if topics_2026:
    for i, topic in enumerate(topics_2026):
        print(f"Topic {i+1}: {', '.join(topic)}")

# ============================================================================
# PART 3: Topic Visualization
# ============================================================================

fig2, axes2 = plt.subplots(2, 2, figsize=(14, 10))

# Plot topics for 2025
if topics_2025:
    for i in range(min(2, len(topics_2025))):
        ax = axes2[0, i]
        words = topics_2025[i][:8]
        weights = model_2025.components_[i]
        top_indices = model_2025.components_[i].argsort()[:-9:-1]
        top_weights = [model_2025.components_[i][idx] for idx in top_indices]
        
        # Normalize weights for display
        top_weights = np.array(top_weights) / max(top_weights)
        
        y_pos = np.arange(len(words))
        ax.barh(y_pos, top_weights, color='#3498db', edgecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words, fontsize=10)
        ax.invert_yaxis()
        ax.set_xlabel('Relative Weight')
        ax.set_title(f'2025 - Topic {i+1}', fontsize=12, fontweight='bold')

# Plot topics for 2026
if topics_2026:
    for i in range(min(2, len(topics_2026))):
        ax = axes2[1, i]
        words = topics_2026[i][:8]
        top_indices = model_2026.components_[i].argsort()[:-9:-1]
        top_weights = [model_2026.components_[i][idx] for idx in top_indices]
        
        # Normalize weights for display
        top_weights = np.array(top_weights) / max(top_weights)
        
        y_pos = np.arange(len(words))
        ax.barh(y_pos, top_weights, color='#e74c3c', edgecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words, fontsize=10)
        ax.invert_yaxis()
        ax.set_xlabel('Relative Weight')
        ax.set_title(f'2026 - Topic {i+1}', fontsize=12, fontweight='bold')

fig2.suptitle('LDA Topic Modeling Results: 2025 vs 2026\n(Top 2 Topics Shown)', 
              fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig2.savefig(data_dir.parent / "Code" / "topic_modeling_results.png", 
             dpi=150, bbox_inches='tight', facecolor='white')
print(f"\n✓ Topic modeling visualization saved")

# ============================================================================
# PART 4: Question-Specific Topic Modeling
# ============================================================================
print("\n" + "=" * 70)
print("PART 3: QUESTION-SPECIFIC TOPIC ANALYSIS")
print("=" * 70)

# Focus on key questions with more detailed analysis
key_questions = [
    qualitative_cols[2],  # Fears about AI
    qualitative_cols[3],  # Benefits/Threats
    qualitative_cols[4],  # Controversies
]

fig3, axes3 = plt.subplots(2, 3, figsize=(16, 10))

for q_idx, col in enumerate(key_questions):
    short_name = col_short_names[col]
    print(f"\n--- {short_name} ---")
    
    texts_2025 = df_2025[col].dropna().tolist()
    texts_2026 = df_2026[col].dropna().tolist()
    
    # Topic model for each year
    _, topics_q_2025, _ = run_topic_modeling(texts_2025, n_topics=2, n_top_words=8)
    _, topics_q_2026, _ = run_topic_modeling(texts_2026, n_topics=2, n_top_words=8)
    
    if topics_q_2025:
        print(f"2025 Main Theme: {', '.join(topics_q_2025[0][:6])}")
        # Plot
        ax = axes3[0, q_idx]
        words = topics_q_2025[0][:6]
        y_pos = np.arange(len(words))
        ax.barh(y_pos, range(len(words), 0, -1), color='#3498db', edgecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words, fontsize=10)
        ax.invert_yaxis()
        ax.set_title(f'2025: {short_name}', fontsize=10, fontweight='bold')
        ax.set_xlabel('Importance Rank')
    
    if topics_q_2026:
        print(f"2026 Main Theme: {', '.join(topics_q_2026[0][:6])}")
        # Plot
        ax = axes3[1, q_idx]
        words = topics_q_2026[0][:6]
        y_pos = np.arange(len(words))
        ax.barh(y_pos, range(len(words), 0, -1), color='#e74c3c', edgecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words, fontsize=10)
        ax.invert_yaxis()
        ax.set_title(f'2026: {short_name}', fontsize=10, fontweight='bold')
        ax.set_xlabel('Importance Rank')

fig3.suptitle('Key Question Topic Analysis: 2025 vs 2026\n', 
              fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig3.savefig(data_dir.parent / "Code" / "question_topic_analysis.png", 
             dpi=150, bbox_inches='tight', facecolor='white')
print(f"\n✓ Question-specific analysis saved")

# ============================================================================
# PART 5: Thematic Word Cloud Data
# ============================================================================
print("\n" + "=" * 70)
print("PART 4: COMBINED WORD FREQUENCY SUMMARY")
print("=" * 70)

# Get overall word frequencies
all_2025_text = ' '.join([preprocess_text(t) for t in all_text_2025])
all_2026_text = ' '.join([preprocess_text(t) for t in all_text_2026])

freq_all_2025 = get_word_frequencies(all_text_2025, top_n=25)
freq_all_2026 = get_word_frequencies(all_text_2026, top_n=25)

print("\n2025 Overall Top Words:")
for word, count in freq_all_2025[:15]:
    print(f"  {word}: {count}")

print("\n2026 Overall Top Words:")
for word, count in freq_all_2026[:15]:
    print(f"  {word}: {count}")

# Final comparison plot
fig4, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# 2025
words_25 = [w for w, c in freq_all_2025[:15]]
counts_25 = [c for w, c in freq_all_2025[:15]]
y_pos = np.arange(len(words_25))
ax1.barh(y_pos, counts_25, color='#3498db', edgecolor='black')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(words_25, fontsize=11)
ax1.invert_yaxis()
ax1.set_xlabel('Frequency', fontsize=11)
ax1.set_title('2025 - Overall Top Words\n(All Qualitative Responses)', fontsize=12, fontweight='bold')

# 2026
words_26 = [w for w, c in freq_all_2026[:15]]
counts_26 = [c for w, c in freq_all_2026[:15]]
y_pos = np.arange(len(words_26))
ax2.barh(y_pos, counts_26, color='#e74c3c', edgecolor='black')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(words_26, fontsize=11)
ax2.invert_yaxis()
ax2.set_xlabel('Frequency', fontsize=11)
ax2.set_title('2026 - Overall Top Words\n(All Qualitative Responses)', fontsize=12, fontweight='bold')

fig4.suptitle('Overall Word Frequency Comparison: 2025 vs 2026\n', 
              fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig4.savefig(data_dir.parent / "Code" / "overall_word_comparison.png", 
             dpi=150, bbox_inches='tight', facecolor='white')
print(f"\n✓ Overall comparison saved")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)
print("\nOutput files generated:")
print("  1. word_frequencies_by_question.png - Word frequencies for each survey question")
print("  2. topic_modeling_results.png - LDA topic modeling visualization")
print("  3. question_topic_analysis.png - Key question topic analysis")
print("  4. overall_word_comparison.png - Overall word frequency comparison")
print("\nNote: Coding experience question was excluded from all analyses.")

plt.show()
