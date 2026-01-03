# Student Exam Analysis

A beginner-friendly data analysis project that demonstrates how to analyze student exam scores using Python, pandas, and matplotlib.

## Project Overview

This project is designed to help beginners learn fundamental data analysis concepts including:
- **Data Loading**: Working with DataFrames
- **Data Exploration**: Understanding your dataset
- **Data Cleaning**: Handling and preparing data
- **Statistical Analysis**: Computing mean, median, standard deviation
- **Data Visualization**: Creating meaningful charts and graphs

## Dataset

The project includes a sample dataset with exam scores from 8 students across 4 subjects:
- **Math**
- **English**
- **Science**
- **History**

Scores range from 75 to 96, providing a realistic dataset for analysis.

## Key Features

✨ **Statistical Analysis**
- Calculate mean scores by subject
- Compute median and standard deviation
- Identify top and bottom performers
- Calculate class averages

📊 **Data Visualizations**
- **Box Plot**: Distribution of scores by subject
- **Bar Chart**: Individual student averages
- **Line Chart**: Score comparison across subjects
- **Histogram**: Distribution of student average scores

## Requirements

All dependencies are listed in `requirements.txt`:

```
pandas==2.0.3
matplotlib==3.7.2
numpy==1.24.3
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kevin-vasilescu/Student-Exam-Analysis.git
cd Student-Exam-Analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the analysis script:

```bash
python exam_analysis.py
```

The script will:
1. Load the sample student data
2. Display the dataset overview
3. Calculate and print statistical summaries
4. Identify top and bottom performers
5. Generate visualization charts
6. Save the visualization as `exam_analysis.png`

## Output

The script produces:
- **Console Output**: Detailed statistics and insights
- **Visualization**: A 2x2 dashboard with 4 charts saved as PNG

## Learning Outcomes

After exploring this project, you'll understand:
- How to load and manipulate data with pandas
- Basic statistical analysis methods
- How to create publication-quality visualizations
- Python best practices for data analysis
- How to structure a data analysis project

## Project Structure

```
Student-Exam-Analysis/
├── exam_analysis.py       # Main analysis script
├── requirements.txt       # Project dependencies
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## Code Comments

The `exam_analysis.py` script includes detailed comments explaining each step, making it easy for beginners to understand the code and modify it for their own datasets.

## Extending the Project

You can extend this project by:
- Adding more students or subjects
- Loading data from CSV or Excel files
- Implementing additional statistical measures
- Creating interactive visualizations with plotly
- Building a web interface with Streamlit
- Adding data validation and error handling

## Example Dataset Modification

To use your own data, simply modify the `data` dictionary in `exam_analysis.py`:

```python
data = {
    'Student': ['Name1', 'Name2', ...],
    'Math': [score1, score2, ...],
    'English': [score1, score2, ...],
    'Science': [score1, score2, ...],
    'History': [score1, score2, ...]
}
```

## Author

Created by Kevin Vasilescu

## License

MIT License - feel free to use this project for learning and personal projects.

## Feedback & Contributions

If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request.

---

**Happy Learning!** 📚 If you found this helpful, please consider giving it a star ⭐
