from src.common import *
from src.kernels import Kernel


def filter_2d(image, kernel):
    return cv2.filter2D(image, -1, kernel)


def main():
    st.title('Kernels')
    uploaded_file = st.file_uploader("Select image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        st.header('Select a kernel:')

        kernels = [attr for attr in dir(Kernel) if not attr.startswith('_')]
        option = st.selectbox('Select a kernel:', kernels)
        st.write(getattr(Kernel, option))

        img = load_image(uploaded_file)

        input_col, output_col = st.columns(2)
        with input_col:
            st.header('Original')
            st.image(img, channels='BGR', use_column_width=True)

        output = img.copy()
        if option.startswith('sobel'):
            output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        output = filter_2d(output, getattr(Kernel, option))

        with output_col:
            st.header('Filtered')
            if output.ndim == 3:
                output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            st.image(output)

            result = Image.fromarray(output)
            show_image_download_button(result)


if __name__ == '__main__':
    main()
