import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import image
import os

st.title("Restaurant Rating Prediction")
st.write("This innovative restaurant prediction app employs advanced models to provide \
        accurate ratings forecasts, empowering users to make informed dining choices. \
        Users can explore a wealth of insightful trends, including online delivery preferences,\
        diverse cuisine options, and price categories, all presented through an intuitive \
        interface. With tailored, data-driven recommendations, it ensures that users \
        effortlessly discover delightful dining experiences. ")

file_dir = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(file_dir, "resources")
image_path = os.path.join(dir_of_interest, "images.jpg")
img = image.imread(image_path)
st.image(img)