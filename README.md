# MoodTuner
MoodTuner
# MoodTunes

MoodTunes is a Python project that recommends songs based on the user's mood inferred from Spotify playlist descriptions. It utilizes sentiment analysis and keyword extraction to recommend songs that match the user's current mood.

## How it Works

1. **Data Loading:** The project loads a dataset containing Spotify playlist information, including titles, artists, and descriptions.
2. **Sentiment Analysis:** It analyzes the sentiment of playlist descriptions using the VADER sentiment analysis tool to infer the mood associated with each playlist.
3. **Keyword Extraction:** Keywords are extracted from playlist descriptions to further understand the content of each playlist.
4. **Recommendation:** Based on the user's input mood, the project recommends songs associated with playlists that match the mood and contain relevant keywords.

## Installation

1. Clone the repository:

    ```bash
    [git clone https://github.com/wikipycoder/MoodTuner.git]
    ```

2. Navigate to the project directory:

    ```bash
    cd MoodTunes
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `moodtuner.py` script:

    ```bash
    python moodtuner.py
    ```

2. Enter your current mood when prompted.

3. The program will recommend songs based on your mood.

## Project Structure

- `moodtuner.py`: Main Python script for running the MoodTunes application.
- `spotify_millsongdata.csv`: Dataset containing Spotify playlist information.
- `README.md`: This file providing an overview of the project.
- `requirements.txt`: List of required Python packages for the project.


