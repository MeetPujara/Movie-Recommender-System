# 🎬 Movie Recommendation System 🎬

This project implements a movie recommendation system using machine learning techniques. It leverages a dataset of movies and their associated metadata to build a model that can suggest similar movies based on user selection. The system consists of a data processing and model building component (implemented in a Jupyter Notebook) and a Streamlit web application that provides an interactive user interface for exploring movie recommendations.

🚀 **Key Features:**

*   **Data Preprocessing:** Cleans and transforms movie data, handling missing values and converting string representations of lists into usable Python lists.
*   **Feature Extraction:** Extracts relevant features from movie data, such as genres, keywords, cast, and crew, to create a comprehensive movie profile.
*   **Text Vectorization:** Converts textual movie features into numerical vectors using `CountVectorizer`, enabling similarity calculations.
*   **Stemming:** Applies stemming to reduce words to their root form, improving the accuracy of similarity calculations.
*   **Cosine Similarity:** Calculates the cosine similarity between movie vectors to identify movies with similar characteristics.
*   **Streamlit Web App:** Provides a user-friendly interface for selecting a movie and viewing recommendations.
*   **Poster Fetching:** Retrieves movie posters from the TMDb API to enhance the visual appeal of the recommendations.
*   **Google Drive Integration:** Downloads necessary data files from Google Drive, simplifying deployment and setup.
*   **Caching:** Implements caching to improve the performance of the web application.

🛠️ **Tech Stack:**

| Category    | Technology                      | Description                                                                                                |
|-------------|---------------------------------|------------------------------------------------------------------------------------------------------------|
| **Frontend**  | Streamlit                       | Python library for creating interactive web applications.                                                 |
| **Backend**   | Python                          | Programming language used for data processing, model building, and web application logic.                   |
| **Data Science**| pandas                          | Data manipulation and analysis.                                                                            |
|             | numpy                           | Numerical computing.                                                                                       |
|             | scikit-learn                    | Machine learning library for text vectorization, cosine similarity calculation, and model building.        |
|             | nltk                            | Natural Language Toolkit for stemming.                                                                     |
| **API**       | TMDb API                        | The Movie Database API for fetching movie posters.                                                          |
| **Data Storage**| Pickle                          | Python object serialization for saving and loading the movie data and similarity matrix.                     |
| **Utilities** | ast                             | Safely evaluate strings containing Python literal structures.                                               |
|             | requests                        | Making HTTP requests to the TMDb API.                                                                      |
|             | gdown                           | Downloading files from Google Drive.                                                                       |
| **Environment**| requirements.txt              | Specifies project dependencies and their versions.                                                         |

📦 **Getting Started / Setup Instructions:**

### Prerequisites

*   Python 3.6 or higher
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all the dependencies listed in the `requirements.txt` file, including `streamlit`, `pandas`, `scikit-learn`, and other necessary libraries.

3.  **Download the necessary data files:**
    The `app.py` script uses `gdown` to download `movies.pkl` and `similarity.pkl` from Google Drive. Ensure that `gdown` is installed (`pip install gdown`). The script will automatically download the files if they are not present in the current directory. If you prefer to download manually, you can use `gdown <file_id>` for each file.

### Running Locally

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    This command will start the Streamlit web application. Open your web browser and navigate to the address displayed in the terminal (usually `http://localhost:8501`) to access the application.

📂 **Project Structure**

```
├── app.py                          # Streamlit web application
├── movie-recommender-system.ipynb  # Jupyter Notebook for data processing and model building
├── movies.pkl                      # Serialized movie data (created by the notebook)
├── similarity.pkl                  # Serialized similarity matrix (created by the notebook)
├── requirements.txt                # List of Python package dependencies
└── README.md                       # Project documentation (this file)
```

📸 **Screenshots**

*(Space reserved for screenshots of the application)*

🤝 **Contributing**

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Submit a pull request.

📝 **License**

This project is licensed under the [MIT License](LICENSE).

📬 **Contact**

If you have any questions or suggestions, feel free to contact me at [your_email@example.com](mailto:your_email@example.com).

💖 **Thanks**

Thank you for checking out this movie recommendation system! I hope you find it useful and interesting.

This is written by [readme.ai](https://readme-generator-phi.vercel.app/).
