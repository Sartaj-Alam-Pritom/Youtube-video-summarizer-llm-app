# 🎥 YouTube Video Summarizer  

This is a *YouTube Video Summarizer* powered by *Google Gemini AI* and *Streamlit*.  
It extracts the transcript from a YouTube video and provides a detailed yet concise summary within *250 words*.  

## ✨ Features  
✅ Extracts video transcripts from YouTube  
✅ Summarizes transcripts using *Google Gemini AI*  
✅ Displays video thumbnail for easy reference  
✅ Provides an easy-to-use *Streamlit* interface  

## 🛠 Installation  

### 1️⃣ Clone the Repository  
sh
git clone https://github.com/Sartaj-Alam-Pritom/Youtube-video-summarizer-llm-app.git
cd your-repo-name


### 2️⃣ Create a Virtual Environment (Recommended)  
It is recommended to create a virtual environment to manage dependencies.  

For Windows:  
sh
python -m venv venv
venv\Scripts\activate

For macOS/Linux:  
sh
python3 -m venv venv
source venv/bin/activate


### 3️⃣ Install Dependencies  
sh
pip install -r requirements.txt


### 4️⃣ Set Up API Key  
Create a .env file in the project folder and add your *Google Gemini API key*:  
sh
GOOGLE_API_KEY="your_api_key_here"

🔹 You can obtain your API key from [Google AI Console](https://ai.google.dev/).  

## 🚀 Run the App  
sh
streamlit run app.py


## 🏗 How It Works  
1️⃣ Enter a YouTube video *URL* in the input box.  
2️⃣ The app *fetches the transcript* using the *YouTube Transcript API*.  
3️⃣ *Google Gemini AI* generates a *detailed summary* of the video (within *250 words*).  
4️⃣ The *summary is displayed* along with the video *thumbnail*.  

## 📌 Technologies Used  
🔹 Python  
🔹 Streamlit  
🔹 Google Generative AI (Gemini)  
🔹 YouTube Transcript API  
🔹 dotenv  

## 🛑 Important Notes  
⚠ Do *not* push your .env file to GitHub. Add it to .gitignore.  
⚠ Ensure you have a *valid API key* for *Google Generative AI*.  

## 📜 License  
This project is licensed under the *MIT License*.