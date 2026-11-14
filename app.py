from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load your pickled files
print("Loading model and data...")
similarity_matrix = pickle.load(open('Model/similarity_matrix.pkl', 'rb'))
df = pickle.load(open('Model/df.pkl', 'rb'))
df_original = pickle.load(open('Model/df_original.pkl', 'rb'))
print("Data loaded successfully!")

@app.route('/')
def index():
    # Pass a unique list of song names to the HTML dropdown
    song_list = df['song_name'].dropna().unique().tolist()
    return render_template('index.html', song_list=song_list)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    song_name = data.get('song_name')
    
    try:
        # Your exact Colab logic adapted for the backend
        song_index = df[df["song_name"] == song_name].index[0]
        song_scores = similarity_matrix[song_index]
        similar_indices = np.argsort(song_scores)[::-1]
        similar_indices = similar_indices[similar_indices != song_index]
        top_indices = similar_indices[:5] # Top 5 recommendations
        
        recommendations = []
        for idx in top_indices:
            recommendations.append({
                'song_name': df.iloc[idx]['song_name'],
                'artist': df_original.iloc[idx]['primary_artist'],
                'similarity_score': round(float(song_scores[idx]), 4)
            })
        
        return jsonify({'status': 'success', 'recommendations': recommendations})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
