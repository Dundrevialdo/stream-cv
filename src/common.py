import io
import base64
import cv2
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

from src.filters import bw_filter


def get_image_info(image: Image):
    info = {
        'Mode': image.mode,
        'Width': image.size[0],
        'Height': image.size[1],
    }
    info_df = pd.DataFrame(info, index=[0])
    return info_df


def display_image(im: Image):
    im_info = get_image_info(im)
    im_col, info_col = st.columns([2, 1])
    with im_col:
        st.image(im)
    with info_col:
        st.write(im_info)
    return im


def load_image(uploaded_file, read_mode = cv2.IMREAD_COLOR):
    raw_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    return cv2.imdecode(raw_bytes, read_mode)


def save_image_to_buffer(image: Image, file_format: str):
    fp = io.BytesIO()
    image.save(fp, format=file_format)
    return fp


def show_image_download_button(img, file_format='JPEG'):
    buffer = save_image_to_buffer(img, file_format)
    st.download_button('Download image', data=buffer, file_name=f"image.{file_format}")


def show_image_download_link(img, file_format='JPEG'):
    buffer = save_image_to_buffer(img, file_format)
    img_str = base64.b64encode(buffer.getvalue()).decode()
    href = f'<a href="data:file/txt;base64,{img_str}" download="image.{file_format}">Download image</a>'
    st.markdown(href, unsafe_allow_html=True)


def plot(img1, img2):
    plt.figure(figsize=(20, 10))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Original Image")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Filtered Image")

    plt.show()


def convert_to_grayscale(img):
    do_convert = st.toggle('Convert to grayscale', value=False)
    if do_convert:
        img = bw_filter(img)
    return img
