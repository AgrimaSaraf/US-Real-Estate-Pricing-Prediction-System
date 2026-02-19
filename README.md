# US-Real-Estate-Pricing-Prediction-System
Built an end-to-end US real-estate price prediction system using large-scale housing, location, and economic data; performed rigorous data cleaning, feature engineering, and multi-model evaluation (linear and tree-based) to generate market-aligned home valuations and analyze pricing errors across regions

# US Real Estate Price Prediction

This project builds an end-to-end machine learning pipeline to predict US house prices using historical housing, location, and economic data.

## Problem
Accurately estimating house prices is difficult due to regional variation, economic conditions, and property characteristics. This project aims to build a data-driven pricing model and evaluate its performance across regions.

## Dataset
- Property features (size, rooms, year built)
- Location indicators (ZIP code, latitude, longitude)
- Economic signals (interest rates, income)

## Approach
1. Data cleaning and preprocessing
2. Exploratory data analysis
3. Feature engineering
4. Model training and comparison
5. Model evaluation and error analysis

## Models Used
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

## Evaluation Metrics
- RMSE
- MAE

## Results
Tree-based models outperform linear baselines, especially in high-variance housing markets.

## Future Improvements
- Add school quality and crime data
- Use time-series modeling
- Deploy as a web application
