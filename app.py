from flask import Flask, jsonify, request, render_template
import joblib
from scripts.fetch_data import fetch_posts, save_posts_to_csv
from scripts.analyze_sentiment import read_posts_from_csv, analyze_sentiment, save_analyzed_data_to_csv

app = Flask(__name__)

# Load the trained model
model = joblib.load('data/model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['GET'])
def fetch():
    subreddit = request.args.get('subreddit', default='Python', type=str)
    limit = request.args.get('limit', default=10, type=int)
    
    try:
        posts = fetch_posts(subreddit, limit)
        save_posts_to_csv(posts)
        return jsonify({"message": f"Saved {len(posts)} posts to data/reddit_posts.csv"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analyze', methods=['GET'])
def analyze():
    try:
        posts = read_posts_from_csv('data/reddit_posts.csv')
        analyzed_posts = analyze_sentiment(posts)
        save_analyzed_data_to_csv(analyzed_posts)
        return jsonify({"message": "Saved analyzed data to data/reddit_posts_analyzed.csv"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    prediction = model.predict([text])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
