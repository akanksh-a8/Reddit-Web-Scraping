import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

def train_model(data_path='data/reddit_posts_analyzed.csv', model_path='data/model.pkl'):
    # Load the labeled data
    data = pd.read_csv(data_path)
    
    # Check the column names
    print("Columns available in the data:", data.columns)
    
    # Prepare data for training
    X = data['Title']  # Column with text data
    y = data['Sentiment']  # Column with sentiment labels
    
    # Create a pipeline with a vectorizer and a classifier
    pipeline = Pipeline([
        ('vect', CountVectorizer()),  # Convert text to feature vectors
        ('clf', MultinomialNB())  # Train a Naive Bayes classifier
    ])
    
    # Train the model
    pipeline.fit(X, y)
    
    # Save the trained model
    joblib.dump(pipeline, model_path)
    print("Model trained and saved to", model_path)

if __name__ == "__main__":
    train_model()
