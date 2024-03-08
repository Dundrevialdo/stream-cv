import cv2
import numpy as np
import streamlit as st


def brightness_and_contrast(img):
    brightness = st.slider('Brightness', -100, 100, 0)
    contrast = st.slider('Contrast', 0.0, 5.0, 1.0, 0.01)
    return cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)


@st.cache_data
def bw_filter(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray


@st.cache_data
def sepia(img):
    img_sepia = img.copy()
    # Converting to RGB as sepia matrix below is for RGB.
    img_sepia = cv2.cvtColor(img_sepia, cv2.COLOR_BGR2RGB)
    img_sepia = np.array(img_sepia, dtype=np.float64)
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.393, 0.769, 0.189],
                                                    [0.349, 0.686, 0.168],
                                                    [0.272, 0.534, 0.131]]))
    img_sepia = np.clip(img_sepia, 0, 255)
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    img_sepia = cv2.cvtColor(img_sepia, cv2.COLOR_RGB2BGR)
    return img_sepia


@st.cache_data
def vignette(img, level):
    height, width = img.shape[:2]

    # Generate vignette mask using Gaussian kernels.
    X_resultant_kernel = cv2.getGaussianKernel(width, width / level)
    Y_resultant_kernel = cv2.getGaussianKernel(height, height / level)

    # Generating resultant_kernel matrix.
    kernel = Y_resultant_kernel * X_resultant_kernel.T
    mask = kernel / kernel.max()

    img_vignette = np.copy(img)

    # Apply the mask to each channel in the input image.
    for i in range(img_vignette.ndim):
        img_vignette[..., i] = img_vignette[..., i] * mask

    return img_vignette


@st.cache_data
def embossed_edges(img):
    kernel = np.array([[0, -3, -3],
                       [3, 0, -3],
                       [3, 3, 0]])
    return cv2.filter2D(img, -1, kernel=kernel)


# may have better results with blurred image
# may look better with a greyscale image
def outline_effect(img):
    k = st.slider('Outline Intensity', 8, 15, 9, 1)
    kernel = np.array([[-1, -1, -1],
                       [-1, k, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(img, ddepth=-1, kernel=kernel)


# may have better results with blurred image
def pencil_sketch(img):
    sketch_option = st.radio('Pencil Sketch Type', ('Grayscale', 'Color'), horizontal=True)
    sigma_s = st.slider('Sigma S', 0.0, 200.0, 60.0)
    sigma_r = st.slider('Sigma R', 0.0, 1.0, 0.45, 0.01)
    shade_factor = st.slider('Shade Factor', 0.0, 0.1, 0.01, 0.01)
    grayscale_sketch, color_sketch = cv2.pencilSketch(
        img,
        sigma_s=sigma_s,
        sigma_r=sigma_r,
        shade_factor=shade_factor
    )
    return grayscale_sketch if sketch_option == 'Grayscale' else color_sketch


# may have better results with blurred image
def stylization_effect(img):
    sigma_s = st.slider('Sigma S', 0.0, 200.0, 60.0)
    sigma_r = st.slider('Sigma R', 0.0, 1.0, 0.45, 0.01)
    return cv2.stylization(img, sigma_s=sigma_s, sigma_r=sigma_r)
