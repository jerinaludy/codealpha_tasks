# Import libraries
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("reviews.csv")

# Show first rows
print("\nFIRST 5 REVIEWS:")
print(data.head())

# Function to find sentiment
def get_sentiment(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    else:
        return "Neutral"

# Apply sentiment analysis
data["Sentiment"] = data["Review"].apply(get_sentiment)

# Show results
print("\nSENTIMENT RESULTS:")
print(data)

# Count sentiments
sentiment_count = data["Sentiment"].value_counts()

print("\nSENTIMENT COUNT:")
print(sentiment_count)

# Create bar chart
plt.figure(figsize=(6,5))

plt.bar(
    sentiment_count.index,
    sentiment_count.values
)

plt.title("Sentiment Analysis Result")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()