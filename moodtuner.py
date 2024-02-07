import pandas as pd
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
import random
# Replace "path/to/dataset" with the actual path to your playlist data
data = pd.read_csv("spotify_millsongdata.csv")

# Extract playlist names
playlist_text = data["text"].head(500)



def clean_text(text):
# Convert to lowercase, remove punctuation and stop words
    text = text.lower()
    text = "".join([c for c in text if c.isalnum() or c.isspace()])
    stopwords = ["the", "a", "an", "of", ...]  # Add your stopwords list
    text = " ".join([word for word in text.split() if word not in stopwords])
    return text



def extract_keywords(text):
  tokens = word_tokenize(text)
  # You can apply additional filtering based on Part-of-speech if desired
  keywords = [word for word in tokens if len(word) > 3]  # Filter short words
  return keywords



def infer_mood_from_text(text):
  """
  Infers mood from text using VADER sentiment analysis.

  Args:
    text: The text to analyze.

  Returns:
    The inferred mood based on VADER sentiment score and thresholds.
  """
  # Instantiate VADER analyzer
  analyzer = SentimentIntensityAnalyzer()

  # Analyze sentiment
  sentiment = analyzer.polarity_scores(text)

  # Define mood thresholds based on sentiment score (expanded)
  mood_thresholds = {
      "happy": (0.75, 1.0),  # Highly positive sentiment
      "joyful": (0.5, 0.75),  # Moderately positive sentiment
      "calm": (0.25, 0.5),  # Slightly positive or neutral sentiment
      "neutral": (-0.25, 0.25),  # Balanced sentiment
      "sad": (-0.75, -0.25),  # Slightly negative sentiment
      "angry": (-1.0, -0.75),  # Moderately negative sentiment
      "depressed": (-1.0, -0.5)  # Highly negative sentiment
  }

  # Map sentiment score to mood based on thresholds
  for mood, (lower_threshold, upper_threshold) in mood_thresholds.items():
    if sentiment["compound"] >= lower_threshold and sentiment["compound"] <= upper_threshold:
      return mood

  # Return none if no mood matches thresholds
  return None








def main():
    user_mood = input("How are you feeling right now?: ")

    cleaned_text = [clean_text(desc) for desc in playlist_text]
    print(len(cleaned_text), type(cleaned_text))

    mood_keywords = {}
    for text in tqdm(cleaned_text):
        mood = infer_mood_from_text(text) # Replace with your function to infer mood from text

        if mood not in mood_keywords:
            mood_keywords[mood] = []
            mood_keywords[mood].extend(extract_keywords(text))
    
    mood_songs = {}
    for mood in mood_keywords:
        mood_songs[mood] = mood_keywords[mood]

    def recommend_songs_by_mood(mood):
        random.shuffle(mood_songs[mood])  # Shuffle for variety
        return mood_songs[mood][:5]  # Recommend the first 5 songs

    recommended_songs = recommend_songs_by_mood(user_mood)
    print(recommended_songs)

if __name__ == "__main__":
    main()