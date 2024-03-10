from src.common import *
from src.links import Link
from src.noise_reduction import median_filter, bilateral_filter
from src.common import convert_to_grayscale


def main():
    st.title('Noise reduction')

    uploaded_file = st.file_uploader("Select image", type=['png', 'jpg', 'jpeg'])
    if not uploaded_file:
        st.stop()

    img = load_image(uploaded_file)
    output_img = convert_to_grayscale(img)

    st.header('Median filter')
    Link.show('median_filter')
    median_output_img = median_filter(output_img)

    st.header('Bilateral filter')
    Link.show('bilateral_filter')
    bilateral_output_img = bilateral_filter(output_img)

    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if median_output_img.ndim == 3:
        median_output_img = cv2.cvtColor(median_output_img, cv2.COLOR_BGR2RGB)
    if bilateral_output_img.ndim == 3:
        bilateral_output_img = cv2.cvtColor(bilateral_output_img, cv2.COLOR_BGR2RGB)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Original')
        st.image(img)

    with col2:
        st.header('Median filter')
        st.image(median_output_img)

        result = Image.fromarray(median_output_img)
        show_image_download_button(result, file_name='median_filter')

    with col3:
        st.header('bilateral filter')
        st.image(bilateral_output_img)

        result = Image.fromarray(bilateral_output_img)
        show_image_download_button(result, file_name='bilateral_filter')


if __name__ == '__main__':
    main()
