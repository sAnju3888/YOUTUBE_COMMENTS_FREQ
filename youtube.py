import requests
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
# Replace with your API key
API_KEY = 'AIzaSyCcCwSIbQQRBIPjheTxL7WplpxsesEyVvA'
# Replace with the YouTube video ID you want to fetch comments for
VIDEO_ID = 'mbLEZVysOc8'

# API endpoint for fetching video comments
api_endpoint = f'https://www.googleapis.com/youtube/v3/commentThreads'
# Parameters for the API request
params = {
    'part': 'snippet',
    'videoId': VIDEO_ID,
    'key': API_KEY,
    'maxResults':10000,
}
# Sending the API request
response = requests.get(api_endpoint, params=params)

word_list = []
if response.status_code == 200:
    data = response.json()
    for item in data.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        word_list.append(comment) 
else:
    print(f"Error: {response.status_code}")
    print(response.text)


nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

word_freq = defaultdict(int)  # Initialize a defaultdict to count word frequencies

for sentence in word_list:
    words = nltk.word_tokenize(sentence.lower())
    words = [word for word in words if word not in stop_words and word.isalpha()]
    for word in words:
        word_freq[word] += 1

# Sort words by frequency
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
count = 0
# Print the most common words and their frequencies
for word, freq in sorted_words:
    if count < 10:
        print(f"{word}: {freq}")
    else:
        break 
    count += 1


