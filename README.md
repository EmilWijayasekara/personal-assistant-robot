# Personal Assistant Robot

This project aims to create a personal assistant robot capable of executing various commands such as playing music via YouTube, performing Google searches, taking notes, and setting alarms.

## Features

- **Play Music:** Plays music from YouTube based on voice commands.
- **Google Searches:** Conducts Google searches and retrieves information.
- **Note-Taking:** Records notes and saves them for future reference.
- **Alarm Setting:** Sets alarms based on user requests.

## Installation

To get started with the Personal Assistant Robot, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/EmilWijayasekara/personal-assistant-robot.git
   cd personal-assistant-robot
Install the required dependencies:

sh
Copy code
pip install -r requirements.txt
Configure API Keys:

YouTube API key
Google Custom Search API key
Create a config.json file in the root directory and add your keys:

json
Copy code
{
  "youtube_api_key": "YOUR_YOUTUBE_API_KEY",
  "google_search_api_key": "YOUR_GOOGLE_SEARCH_API_KEY"
}
Run the application:

sh
Copy code
python main.py
Usage
Once the application is running, you can use voice commands to interact with the personal assistant robot. Some example commands include:

"Play [song name] on YouTube."
"Search for [query] on Google."
"Take a note: [note content]."
"Set an alarm for [time]."
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to update the documentation if necessary.

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Create a new Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
YouTube Data API
Google Custom Search API
SpeechRecognition
PyAudio
