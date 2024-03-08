from src.filters import *
from src.common import *

st.title('Artistic Image Filters')

uploaded_file = st.file_uploader('Choose an image file:', type=['png', 'jpg'])

st.header('Filter Examples')

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

if not uploaded_file:
    st.stop()

img = load_image(uploaded_file)
output_img = img.copy()

option = st.selectbox('Select a filter:',
                      ('None',
                       'Brighten / Darken',
                       'Black and White',
                       'Sepia / Vintage',
                       'Vignette Effect',
                       '3D Embossed Effect',
                       'Outline Effect',
                       'Pencil Sketch',
                       'Stylization Effect'
                       ))

if option != 'None':
    if option == 'Brighten / Darken':
        output_img = brightness_and_contrast(output_img)
    elif option == 'Black and White':
        output_img = bw_filter(output_img)
    elif option == 'Sepia / Vintage':
        output_img = sepia(output_img)
    elif option == 'Vignette Effect':
        intensity = st.slider('Intensity', 1, 5)
        output_img = vignette(output_img, intensity)
    elif option == '3D Embossed Effect':
        output_img = embossed_edges(output_img)
    elif option == 'Outline Effect':
        output_img = outline_effect(output_img)
    elif option == 'Pencil Sketch':
        output_img = pencil_sketch(output_img)
    elif option == 'Stylization Effect':
        output_img = stylization_effect(output_img)

input_col, output_col = st.columns(2)
with input_col:
    st.header('Original')
    # Display uploaded image.
    st.image(img, channels='BGR', use_column_width=True)
with output_col:
    st.header('Output')
    if output_img.ndim == 3:
        output_img = output_img[..., ::-1]
    st.image(output_img)

    result = Image.fromarray(output_img)
    show_image_download_button(result)
