import cv2
import streamlit as st


def median_filter(img):
    ksize = st.slider('Kernel size', 3, 11, 3, 2)
    return cv2.medianBlur(img, ksize)


def bilateral_filter(img):
    d = st.slider('d', -1, 100, 5, 1)
    sigma_space = st.slider('Space distance', 0.0, 500.0, 20.0, 0.1)
    sigma_color = st.slider('Color distance', 0.0, 500.0, 100.0, 0.1)
    st.write(f'd={d}, sigma_space={sigma_space}, sigma_color={sigma_color}')
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)
