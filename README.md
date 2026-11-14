# 🎵 EchoMatch | AI Music Recommendation System

An interactive web application that recommends similar tracks based on audio/metadata features using **Cosine Similarity**, powered by a **Flask** backend and a modern **glassmorphism web UI**.

---

## 🚀 Features
* **AI-Powered Recommendations:** Computes and ranks song similarities instantly using precalculated cosine matrices.
* **Interactive Frontend:** Built with custom HTML5, CSS3, and JavaScript featuring smooth animations, responsive layout, and a modern Spotify-inspired dark mode.
* **Lightweight Backend:** Uses a Flask web server to bridge Python data science workflows with browser-based interfaces.

---

## 🛠️ Tech Stack
* **Machine Learning & Data:** Python, Pandas, NumPy, Google Colab (Model Training & Vectorization)
* **Backend:** Flask (Python Web Framework)
* **Frontend:** HTML5, CSS3 (Flexbox, Glassmorphic effects), Vanilla JavaScript (`fetch` API)

---

## 📂 Project Structure
```text
MusicRecommendationApp/
├── app.py                 # Flask server & recommendation logic
├── requirements.txt       # Python dependencies
├── .gitignore             # Git exclusion rules (ignores heavy model files)
├── templates/
│   └── index.html         # Frontend user interface
└── static/
    └── style.css          # Custom styling and animations

```


⚙️ How to Run Locally
1. Prerequisites
Make sure you have Python installed on your machine.

2. Clone the Repository
Bash
git clone [https://github.com/Siddham-coder/Music_Recommendation_App.git](https://github.com/Siddham-coder/Music_Recommendation_App.git)
cd MusicRecommendationApp
3. Install Dependencies
Install the required Python packages (Flask, Pandas, NumPy):

Bash
pip install flask pandas numpy
4. Add Your Model Files
Because the trained similarity matrix and dataframe pickle files (.pkl) are heavy, they are excluded from version control via .gitignore.

Export your similarity_matrix.pkl and df.pkl from your Google Colab notebook.

Place them directly into the root MusicRecommendationApp/ folder.

5. Run the Application
Start your local Flask development server:

Bash
python app.py
Open your browser and navigate to: http://127.0.0.1:5000

💡 How It Works
Data Prep (Colab): Songs are processed and vectorized, and a cosine similarity matrix is computed.

Export: The dataframe and similarity matrix are serialized using Python's pickle library.

Request Lifecycle: When a user selects a song on the frontend, JavaScript sends a POST request to the Flask backend.

Lookup & Response: Flask looks up the song index, finds the top matching indices from the similarity matrix, extracts artist details, and returns JSON recommendations back to the UI.
