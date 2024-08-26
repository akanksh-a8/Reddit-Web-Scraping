import pandas as pd
from textblob import TextBlob
import csv

# Read posts from CSV
def read_posts_from_csv(filename='data/reddit_posts.csv'):
    return pd.read_csv(filename)

# Analyze sentiment of posts
def analyze_sentiment(posts):
    analyzed_posts = []
    for index, row in posts.iterrows():
        title = row['Title']
        text = row['Selftext']
        sentiment = analyze_text(title + ' ' + text)
        analyzed_posts.append([title, text, sentiment])
    return analyzed_posts

# Analyze text using TextBlob
def analyze_text(text):
    analysis = TextBlob(text)
    return 'Positive' if analysis.sentiment.polarity > 0 else 'Negative'

# Save analyzed data to CSV
def save_analyzed_data_to_csv(analyzed_posts, filename='data/reddit_posts_analyzed.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Selftext', 'Sentiment'])
        writer.writerows(analyzed_posts)

if __name__ == "__main__":
    posts = read_posts_from_csv()
    analyzed_posts = analyze_sentiment(posts)
    save_analyzed_data_to_csv(analyzed_posts)
    print("Saved analyzed data to data/reddit_posts_analyzed.csv")
