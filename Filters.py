import io
import base64

import streamlit as st
import cv2

from PIL import Image

from src.filters import *
from src.common import *


# Generating a link to download a particular image file.



# Set title.
st.title('Artistic Image Filters')

# Upload image.
uploaded_file = st.file_uploader('Choose an image file:', type=['png', 'jpg'])

if uploaded_file is not None:
    # Convert the file to an opencv image.
    raw_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)
    input_col, output_col = st.columns(2)
    with input_col:
        st.header('Original')
        # Display uploaded image.
        st.image(img, channels='BGR', use_column_width=True)

    st.header('Filter Examples:')
    # Display a selection box for choosing the filter to apply.
    option = st.selectbox('Select a filter:',
                          ('None',
                           'Black and White',
                           'Sepia / Vintage',
                           'Vignette Effect',
                           'Pencil Sketch',
                           ))

    # Define columns for thumbnail images.
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.caption('Black and White')
        st.image('gallery/filter_bw.jpg')
    with col2:
        st.caption('Sepia / Vintage')
        st.image('gallery/filter_sepia.jpg')
    with col3:
        st.caption('Vignette Effect')
        st.image('gallery/filter_vignette.jpg')
    with col4:
        st.caption('Pencil Sketch')
        st.image('gallery/filter_pencil_sketch.jpg')

    # Flag for showing output image.
    output_flag = 1
    # Colorspace of output image.
    color = 'BGR'

    # Generate filtered image based on the selected option.
    if option == 'None':
        # Don't show output image.
        output_flag = 0
    elif option == 'Black and White':
        output = bw_filter(img)
        color = 'GRAY'
    elif option == 'Sepia / Vintage':
        output = sepia(img)
    elif option == 'Vignette Effect':
        level = st.slider('level', 0, 5, 2)
        output = vignette(img, level)
    elif option == 'Pencil Sketch':
        ksize = st.slider('Blur kernel size', 1, 11, 5, step=2)
        output = pencil_sketch(img, ksize)
        color = 'GRAY'

    with output_col:
        if output_flag == 1:
            st.header('Output')
            st.image(output, channels=color)
            # fromarray convert cv2 image into PIL format for saving it using download link.
            if color == 'BGR':
                result = Image.fromarray(output[:, :, ::-1])
            else:
                result = Image.fromarray(output)
            # Display link.
            show_image_download_button(result)
