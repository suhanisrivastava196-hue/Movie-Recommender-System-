# 🎬 Movie Recommender System

An AI-based **Movie Recommender System** that recommends movies similar to a movie selected by the user. The system uses the **TMDB 5000 Movie Dataset** and a content-based filtering approach to calculate movie similarity.

The application is built with **Python and Streamlit** and provides an interactive interface where users can select a movie and receive personalized movie recommendations along with movie posters and other details.

---

## 🚀 Features

* 🎬 Movie recommendation based on the selected movie
* 🤖 Content-based recommendation system
* 📊 Uses movie similarity scores to find related movies
* 🖼️ Displays posters for recommended movies
* 🎨 Interactive Streamlit web interface
* ⚡ Fast recommendations using a precomputed similarity matrix
* 📦 Uses the TMDB 5000 Movie Dataset

---

## 🧠 How the Recommendation System Works

This project uses **Content-Based Filtering**.

The system analyzes information about movies such as:

* Movie title
* Overview
* Genres
* Keywords
* Cast
* Crew

These features are combined to create a representation of each movie.

The similarity between movies is then calculated using a similarity matrix.

### Recommendation Flow

```text
User selects a movie
        ↓
Find selected movie in dataset
        ↓
Retrieve its index
        ↓
Access similarity scores
        ↓
Sort movies by similarity
        ↓
Select top 5 similar movies
        ↓
Display recommendations
```

---

## 📂 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

The dataset contains information about thousands of movies, including metadata such as:

* Movie titles
* Genres
* Keywords
* Cast
* Crew
* Plot overviews
* Popularity
* Ratings
* Release dates

The recommendation model is trained using information derived from this dataset.

> **Note:** This project uses the TMDB 5000 dataset as its movie data source. It does not use a separate movie dataset for generating recommendations.

---

## 🛠️ Technologies Used

| Technology        | Purpose                       |
| ----------------- | ----------------------------- |
| Python            | Core programming language     |
| Pandas            | Data processing               |
| Scikit-learn      | Similarity calculation        |
| Pickle            | Saving/loading processed data |
| Streamlit         | Web application               |
| TMDB 5000 Dataset | Movie data                    |

---

## 📁 Project Structure

```text
movie-recommender-system/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
└── README.md
```


## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Navigate to the project directory

```bash
cd movie-recommender-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔮 Future Improvements

The project can be extended with:

* 🔎 Movie search functionality
* 🎭 Genre-based filtering
* ⭐ User rating-based recommendations
* 👤 User-specific recommendation profiles
* 🧠 Collaborative filtering
* 🔀 Hybrid recommendation algorithms
* 📈 Recommendation analytics
* 🌐 Deployment using Streamlit Community Cloud
* 📱 Improved responsive UI
* 🎬 More movie metadata and filtering options
* 🧠 Fetching live data from TMDB through API

---

## 📚 Learning Outcomes

Through this project, the following concepts were explored:

* Data preprocessing
* Feature extraction
* Content-based filtering
* Similarity calculation
* Machine learning recommendation systems
* Pandas
* Scikit-learn
* Pickle serialization
* Streamlit application development
* API-based poster retrieval/display

---

## ⚠️ Limitations

Since the recommendation model is based on the **TMDB 5000 Movie Dataset**, recommendations are limited to movies available in the processed dataset.

New movies released after the dataset was collected will not automatically become part of the recommendation model unless the dataset and model are updated.

Some movie posters or metadata may also be unavailable depending on the information present for a particular movie.

## ⚠️ Large Model File

The `similarity.pkl` file is not included in this repository because it exceeds GitHub's 100 MB file-size limit.

The file is generated from the TMDB 5000 dataset during the model-building process.

---

## 👩‍💻 Author

**Suhani Srivastava**

B.Tech Student
Interested in Machine Learning, Data Science, and AI.

---

## 📄 License

This project is intended for educational and academic purposes.

The movie data is sourced from the **TMDB 5000 Movie Dataset**. Please refer to the dataset's original terms and attribution requirements before redistributing the dataset.

---

## ⭐ If You Like This Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.
