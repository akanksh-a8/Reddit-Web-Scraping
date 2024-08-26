import praw
import csv

# Initialize Reddit API
def initialize_reddit_api():
    return praw.Reddit(
        client_id='eecroIcnIlxeiWCuHyj6TA',
        client_secret='jqZkPRFJovfREGA7bwSPJfVDNSMesA',
        user_agent='akr-bot'
    )

# Fetch posts from a subreddit
def fetch_posts(subreddit_name, limit=10):
    reddit = initialize_reddit_api()
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for submission in subreddit.hot(limit=limit):
        posts.append([submission.title, submission.selftext, submission.created_utc])
    return posts

# Save posts to CSV
def save_posts_to_csv(posts, filename='data/reddit_posts.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Selftext', 'Created_UTC'])
        writer.writerows(posts)

if __name__ == "__main__":
    posts = fetch_posts('Python', limit=10)
    save_posts_to_csv(posts)
    print(f"Saved {len(posts)} posts to data/reddit_posts.csv")
