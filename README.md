<center>

# Project4GA

### Unlocking data-driven insights and predictive capabilities through advanced analytics for strategic decision-making.

</center>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Maintained-green.svg" alt="Maintenance Status">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome">
  <img src="https://img.shields.io/github/stars/YOUR_USERNAME/Project4GA.svg?style=social&label=Star" alt="GitHub Stars">
</p>

---

## The Strategic "Why" (Overview)

> ### The Problem
> Italki is a language learning platform that breaks the traditional mould of classroom foreign language learning. It seeks to bring lower prices to the language learner at their online convenience while promising better success and progress in the student’s learning. As teachers are left to price on their own rates for their lessons, there is a possibly that the market forces tend towards an unfavourable pricing position for the platform and it loses its competitive edge over traditional language learning pedagogical methods.

### The Solution
Project4GA delivers a complete end-to-end data science solution, from initial data extraction and rigorous cleaning to in-depth exploratory data analysis and  machine learning prediction. By providing a structured, modular, and reproducible framework, this project empowers users to demystify teacher's profile data, gain profound insights for teacher's to price themselves more accurately.

See https://public.tableau.com/app/profile/ern.min.peck/viz/CapstoneProjectTableau-ExtractData/Story1
For the Tableau Story and Dashboard!

---

## Key Features

*   📊 **Comprehensive Data Extraction**: Seamlessly gathers raw data from italki.com API establishing a rich and robust foundation for all subsequent analytical processes. (You should contact support@italki.com for permission in order not to violate their terms of service)
*   ✨ **Intelligent Data Preprocessing**: Transforms raw, often messy, datasets into clean, structured, and analysis-ready formats, ensuring data integrity and consistency.
*   📈 **Insightful Exploratory Data Analysis (EDA)**: Uncovers hidden patterns, critical trends, and significant anomalies through a blend of visual and statistical methods, driving deeper domain understanding.
*   🧠 **Advanced Predictive Modeling**: Implements RandomForeset machine learning algorithms to accurately forecast teacher prices. See https://ernmin-project4ga-online-tool.streamlit.app/ for the tool!
*   🗄️ **Persistent Data Storage**: Utilizes an efficient SQLite database and JSON files for reliable and organized storage of processed data, intermediate results, and final model outputs.
*   💻 **Interactive Querying & Analysis**: Provides intuitive tools and interfaces to easily query the stored data, visualize predictions, and interact with the analytical outputs.

---

## Technical Architecture

This project is built upon a robust and widely-adopted data science stack, designed for efficiency, flexibility, and scalability.

| Technology      | Purpose                                            |
| :-------------- | :------------------------------------------------- |
| **Python**      | Core programming language                          |
| **Jupyter Notebook** | Interactive development environment                |
| **Pandas**      | Data manipulation and analysis                     |
| **NumPy**       | Numerical computing with arrays                    |
| **Scikit-learn**| Machine Learning algorithms                        |
| **SQLite**      | Lightweight, serverless relational database        |
| **Seaborn/Plotly** | Data visualization libraries                       |

### Directory Structure

```
📁 Project4GA/
├── 📁 .devcontainer/                   # Development container configuration for the stream lit application
├── 📁 data_cleaning/                   # Scripts and notebooks for data preprocessing
│   └── 📄 data_cleaning.ipynb          # Notebook for cleaning raw data from the API
├── 📁 data_extraction/                 # Scripts for extracting data from sources
│   └── 📄 data_extraction.ipynb        # Script for API calls
├── 📁 EDA/                             # Exploratory Data Analysis notebooks and visualizations
│   └── 📄 EDA.ipynb                    # Notebook for initial data exploration
├── 📁 one_price_cycle/                 # Script for one API call
│   └── 📄 one_price_cycle.ipynb        
├── 📁 online_tool/                     # Components for an online interface or utility
│   └── 📄 p4_tool.py                   # Streamlit application script
├── 📁 prediction_model/                # Scripts and notebooks for building and training models
│   └── 📁 final_prediction_model/
│   └── 📄 prediction_model.ipynb       
├── 📁 prediction_query/                # Scripts for querying trained prediction models
│   └── 📄 predictions_query_korean.ipynb Script to test the autocategorization of courses
├── 📁 SQLite_database/                 # Database files and schema definitions
│   └── 📄 teachers.ipynb               # SQLite Database loading
├── 📄 .gitignore                       # Specifies intentionally untracked files to ignore
├── 📄 italki_price_old.ipynb           # Legacy notebook for iTalki API call
├── 📄 one_teacher.ipynb                # Notebook for specific teacher-centric analysis
└── 📄 README.md                        # Project documentation (this file)
```

---

## Operational Setup

Follow these steps to get Project4GA up and running on your local machine.

### Prerequisites

Ensure you have the following installed:

*   **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/).
*   **pip**: Python package installer (usually comes with Python).
*   **Jupyter**: For running the `.ipynb` notebooks.

### Installation

1.  **Install Dependencies**:
    Install all required Python packages using `pip` and the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```
    *(If `requirements.txt` is missing, you may need to create one by listing the required packages like `pandas`, `numpy`, `scikit-learn`, `jupyter`, `matplotlib`, `seaborn`, `plotly`.)*

### Environment Configuration

*   **Example for API Keys (for files in prediction_query to do autocategorization)**:
    If you need to store sensitive information, consider creating a `config.py` file in the project root (and ensure it's in `.gitignore`) with variables like:
    ```
    API_KEY="your_api_key_here"
    ```
---