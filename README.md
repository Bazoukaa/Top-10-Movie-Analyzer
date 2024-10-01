
# Top 10 Movie Analyzer 🎬

This project provides a detailed analysis of the top 10 most popular movies from an IMDb dataset. Using various visualizations and statistics, users can explore the relationships between variables like budget, revenue, vote averages, and more.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Data Source](#data-source)
- [License](#license)

## Features
- **Correlation Analysis**: View a correlation matrix of key variables.
- **Genre Analysis**: Bar chart and pie chart showing genre distributions.
- **Release Year Analysis**: Bar chart showing the number of movies released per year.
- **Budget vs Revenue**: Scatter plot comparing the budget and revenue of the top 10 movies.
- **Popularity vs Vote Average**: Scatter plot comparing movie popularity with average votes.
- **Summary Statistics**: Descriptive statistics for the top 10 movies dataset.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/top-10-movie-analyzer.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd top-10-movie-analyzer
   ```

3. **Install the required Python packages**:
   ```bash
   pip install pandas seaborn matplotlib
   ```

4. **Download the IMDb dataset**:
   The system uses an IMDb dataset in CSV format. Download it from [IMDb datasets](https://www.imdb.com/interfaces/) and ensure it's available at the appropriate location, or update the file path in the script.

## Usage

1. **Run the Movie Analyzer**:
   ```bash
   python top_10_movie_analyzer.py
   ```

2. **Choose the type of analysis**:
   - Correlation matrix
   - Genre distribution (bar chart/pie chart)
   - Movies released per year
   - Budget vs. Revenue comparison
   - Popularity vs. Vote Average
   - Summary statistics, and more.

3. **Explore various plots**:
   You can interactively explore different aspects of the top 10 movies by following the menu in the terminal.

## Requirements
- Python 3.x
- pandas
- seaborn
- matplotlib

## Data Source
This project uses IMDb data, which can be downloaded from the official IMDb dataset page [here](https://www.imdb.com/interfaces/).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
