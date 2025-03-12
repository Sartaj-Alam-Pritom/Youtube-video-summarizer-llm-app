🎥 YouTube Video Summarizer LLM App
This is a YouTube Video Summarizer powered by Google Gemini AI and Streamlit.
It extracts the transcript from a YouTube video and provides a detailed yet concise summary in under 250 words.

✨ Features
✅ Extracts video transcripts from YouTube
✅ Summarizes transcripts using Google Gemini AI
✅ Displays video thumbnail and summarized content
✅ Easy-to-use interface with Streamlit

🛠 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Sartaj-Alam-Pritom/Youtube-video-summarizer-llm-app.git
cd Youtube-video-summarizer-llm-app
2️⃣ Create a Virtual Environment (Recommended)
It is recommended to create a virtual environment to manage dependencies.

For Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
For macOS/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up API Key
Create a .env file in the project folder and add your Google API key:

bash
Copy
Edit
GOOGLE_API_KEY="your_api_key_here"
🔹 You can obtain your API key from Google AI Console.

🚀 Run the App
bash
Copy
Edit
streamlit run app.py
🏗 How It Works
1️⃣ Enter a YouTube video URL in the input box.
2️⃣ The app fetches the video transcript using the YouTube Transcript API.
3️⃣ The Google Gemini AI generates a detailed summary of the video.
4️⃣ The summary is displayed along with the video thumbnail.

📌 Technologies Used
🔹 Python
🔹 Streamlit
🔹 Google Generative AI (Gemini)
🔹 YouTube Transcript API
🔹 dotenv

🛑 Important Notes
⚠ Do not push your .env file to GitHub. Add it to .gitignore.
⚠ Ensure you have a valid API key for Google Generative AI.

📜 License
This project is licensed under the MIT License.