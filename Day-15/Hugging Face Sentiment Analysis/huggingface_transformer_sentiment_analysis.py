import pandas as pd
from transformers import pipeline

print("=" * 60)
print("START: Loading amazon_reviews.csv...")

# Load data
df = pd.read_csv("amazon_reviews.csv")
df = df.head(500)
print(f"✓ Loaded {len(df)} reviews")

# Fill missing reviews
df["review"] = df["review"].fillna("")

print("Loading sentiment-analysis pipeline...")

# Load sentiment pipeline
classifier = pipeline("sentiment-analysis")
print("✓ Pipeline loaded")

# Convert reviews to list and trim long text
reviews = df["review"].astype(str).str[:512].tolist()

print(f"Analyzing sentiment for {len(reviews)} reviews...")

# Predict in batch
results = classifier(reviews)

# Extract labels
df["sentiment"] = [
    "Positive" if result["label"] == "POSITIVE" else "Negative"
    for result in results
]

print("✓ Sentiment analysis completed!")
print("=" * 60)

# Save output
df.to_csv("amazon_reviews_with_sentiment.csv", index=False)

print("\nFirst 5 results:")
print(df.head())
