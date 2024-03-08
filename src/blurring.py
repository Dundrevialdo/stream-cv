import cv2
import streamlit as st


@st.cache_data
def box_blur(img, kernel):
    return cv2.blur(img, kernel)


@st.cache_data
def gaussian_blur(img, kernel, sigma_x, sigma_y):
    return cv2.GaussianBlur(img, kernel, sigma_x, sigma_y)


def blur_image(img):
    img = img.copy()
    blur_option = st.radio('', ['No blur', 'Box blur', 'Gaussian blur'], horizontal=True)
    if blur_option == 'No blur':
        return img

    kernel_size = st.slider('Kernel size', 3, 11, 3, 2)
    kernel = (kernel_size, kernel_size)

    if blur_option == 'Box blur':
        img = box_blur(img, kernel)
    elif blur_option == 'Gaussian blur':
        sigma_x = st.slider('Sigma X', 0.0, 10.0, 0.0, 0.1)
        sigma_y = st.slider('Sigma Y', 0.0, 10.0, 0.0, 0.1)
        img = gaussian_blur(img, kernel, sigma_x, sigma_y)
    return img
