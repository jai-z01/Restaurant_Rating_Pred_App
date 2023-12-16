# Restaurant Rating Prediction App

## Overview
This repository contains the source code for a restaurant rating prediction app built with Streamlit. The app leverages advanced models to provide accurate ratings forecasts, helping users make informed dining choices. Users can explore insightful trends such as online delivery preferences, diverse cuisine options, and price categories through an intuitive interface.

## Features
- **Home Page**: Provides an introduction to the app and showcases an image.
- **Visualize Page**: Offers interactive visualizations based on the restaurant dataset, allowing users to explore various trends and insights.
- **Predict Page**: Allows users to input restaurant details (City, Cuisines, Cost Per Person, No. of Best Sellers, Delivery, and Booking) and predicts the restaurant rating using a pre-trained machine learning model.

## Installation
To run the app locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/restaurant-rating-prediction.git
   cd restaurant-rating-prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run Home.py
   ```

4. Access the app in your web browser at [http://localhost:8501](http://localhost:8501).

## Contents
- `Home.py`: Contains the Streamlit app Home page code.
- `Rating_Pred_Model.ipynb`: Trains a machine learning model for restaurant rating prediction. (See details below)
- `predict.py`: Allows users to input restaurant details and predicts the restaurant rating using the trained model.
- `resources`: Includes necessary resources for the app.
- `display.csv`: Sample dataset for visualization.

## Dataset
The dataset used in this project is sourced from Kaggle and can be found [here](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants). It contains information about various restaurants in Bangalore, including their cuisine types, city locations, menu items, ratings, and more. The dataset serves as the basis for training the machine learning model and visualizing trends within the app.

## Acknowledgments
This project was developed using Streamlit, Pandas, NumPy, Matplotlib, Plotly, and scikit-learn.

Feel free to explore, contribute, or use this project as a starting point for your own restaurant rating prediction app!

*Note: Ensure that you have Python and pip installed on your machine before running the app.*
