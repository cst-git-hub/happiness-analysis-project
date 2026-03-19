![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/pandas-data%20analysis-orange)
![Plotly](https://img.shields.io/badge/plotly-interactive%20viz-purple)
![Status](https://img.shields.io/badge/project-portfolio-green)


## Global Happiness Analysis - Data analysis project exploring the relationship between **happiness and institutional & socio-economic factors** across countries.

# Dashboard Demo

![Demo](images/Happiness_Demo.gif) - Showcases the main outputs of the project: zoom and hover interactions, revealing regional and country-level data.


The project builds a small **end-to-end data pipeline** that collects, cleans and analyzes global datasets on:

- Happiness
- Corruption
- Democracy
- Life expectancy

The goal is to examine how these factors relate to national happiness levels and to visualize the results using **statistical analysis and interactive visualizations**.


# Project Motivation

Happiness is often considered one of the ultimate indicators of quality of life.
The **World Happiness Report**, based on the Gallup World Poll survey, measures life satisfaction using the **Cantril Ladder**, a 10-step self-assessment scale.

Research behind the report suggests that a large share of the variation in happiness can be explained by several factors including:

- health and life expectancy
- institutional quality
- corruption levels
- freedom of choice

This project focuses on three measurable external indicators:

- **Life Expectancy**
- **Corruption Perception Index**
- **Democracy Index**

The aim is to explore their relationship with the **Happiness Index** using statistical methods and visual analytics.


#Research Question:

Do institutional quality and life conditions explain cross-country differences in happiness?

Hypotheses:

* H1: Higher life expectancy increases happiness
* H2: Lower corruption increases happiness
* H3: Higher democracy increases happiness


# Key Findings

Correlation analysis shows **moderately strong positive relationships**  between happiness and all three explanatory variables (0.59 � 0.72).  A **1 year increase in life expectancy**, for example,  corresponds to approximately **+0.11 increase in happiness score** based on the regression slope.
Scatter plots with regression lines illustrate these relationships and highlight several **outlier countries** where happiness deviates from expected levels.


# Data Sources

The project combines four international datasets.

| Dataset | Organization | Source |
| Happiness Index | World Happiness Report | ourworldindata.org
| Corruption Perception Index | Transparency International | ourworldindata.org
| Democracy Index | Economist Intelligence Unit | worldbank.org
| Life Expectancy | World Bank / global health datasets |www.worldometers.info

Data acquisition is implemented through a combination of:

- **1 web scraping script**
- **3 direct dataset downloads**


# Data Pipeline

The project implements a simple **data engineering pipeline**.


## Data Pipeline Architecture

Data sources
   │
   ├── Web scraping (Happiness dataset)
   ├── CPI dataset download
   ├── Democracy Index download
   └── Life expectancy dataset download
          │
          ▼
Raw data storage
(data/raw)
          │
          ▼
Data cleaning & harmonization
- column normalization
- country name standardization
- ISO country code matching
          │
          ▼
Clean datasets
(data/clean)
          │
          ▼
Data merging
          │
          ▼
Statistical analysis
- correlation
- OLS regression
          │
          ▼
Visualizations
- scatter regression plots
- interactive world maps


Reusable utilities for these tasks are implemented in the utils module.


## Reproducibility

The full pipeline can be reproduced with the following steps.:

Clone the repository:

git clone https://github.com/ cst-git-hub/happiness-analysis-project.git
cd happiness-analysis-project


https://github.com/cst-git-hub/happiness-analysis-project.git

Install dependencies:
pip install -r requirements.txt

Run the full data pipeline:
python run_pipeline.py

Open the analysis notebook:
happiness_analysis_2024.ipynb
run cell1

This will reproduce the cleaned datasets and all analysis steps.


## Statistical Analysis

The analysis includes:
* correlation analysis
* OLS regression
* interpretation of:
- slope
- R
- p-values

Results are visualized using regression scatter plots.


## Visualizations

The project includes several visual outputs:

Correlation matrix heatmap

Scatter regression analysis
Relationships between:
* Happiness vs Corruption
* Happiness vs Democracy
* Happiness vs Life Expectancy

Global interactive maps
Interactive choropleth maps visualize each variable across countries.
Variables visualized:
* Happiness
* Corruption
* Democracy
* Life Expectancy


## Technology Stack

Python ecosystem:
* Python
* pandas
* NumPy
* Plotly
* Jupyter Notebook
Data processing:
* fuzzy matching
* ISO country code mapping
* modular ETL scripts


## Project Structure

Happiness_analysis/

data/
   raw/ *_raw.csv         # data files as downloaded
   clean/ *_cleaned.csv   # files processed

scripts/
   dl_*.py        # data download scripts
   cl_*.py        # cleaning scripts

utils/
   iso mapping
   fuzzy matching
   dataframe utilities

notebooks/
   happiness_analysis_2024.ipynb

images/
   visualization outputs

run_pipeline.py


## Skills Demonstrated

### Data Engineering
- Web scraping
- Data ingestion
- ETL pipeline design
- Data cleaning and normalization

### Data Analysis
- Exploratory data analysis
- Correlation analysis
- OLS regression
- Outlier detection

### Data Visualization
- Interactive Plotly visualizations
- Scatter regression plots
- Choropleth world maps

### Tools
- Python
- Jupyter Notebook
 - Pandas
- Plotly
- Seaborn
- Numpy
- Matplotlib


## Future Improvements - Possible extensions:
* multivariate regression model
* add time series analysis
* additional explanatory variables (GDP, population, education, etc)
* apply machine learning models
* build full interactive dashboard
* dashboard deployment (Streamlit)


## Example Visualizations:

images/
- 3_scatterdiags_dashboard.png (3 scatter charts with same (y) axis on one dashboard)
- Corr_Heatmap.png (correlation (matrix) heatmap)
- Happiness_Demo.gif (short demo video)
- Happiness_World_map.png (choropleth map chart)
- Scatter_chart_corruption.png (scatter chart -corruption vs. happiness)

