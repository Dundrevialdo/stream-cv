from src.common import *
from src.kernels import Kernel
from src.links import Link


def main():
    st.title('Edge detection')

    uploaded_file = st.file_uploader("Select image", type=['png', 'jpg', 'jpeg'])
    if not uploaded_file:
        st.stop()

    img = load_image(uploaded_file)
    output_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    st.header('Set bluring')

    Link.show('blur')
    Link.show('gaussian_blur')

    blur_option = st.radio('', ['No blur', 'Box blur', 'Gaussian blur'])

    if blur_option != 'No blur':
        kernel_size = st.slider('Kernel size', 3, 11, 3, 2)
        kernel = (kernel_size, kernel_size)
        if blur_option == 'Box blur':
            output_img = cv2.blur(output_img, kernel)
        elif blur_option == 'Gaussian blur':
            sigma_x = st.slider('Sigma X', 0.0, 10.0, 0.0, 0.1)
            sigma_y = st.slider('Sigma Y', 0.0, 10.0, 0.0, 0.1)
            output_img = cv2.GaussianBlur(output_img, kernel, sigma_x, sigma_y)

        st.header('Blurred image')
        st.image(output_img)

    st.header('Set edge detection')

    Link.show('sobel')
    Link.show('canny')

    edge_option = st.radio('', ['No detection', 'Sobel', 'Canny', 'Kernel'])

    if edge_option != 'No detection':
        if edge_option == 'Sobel':
            kernel_size = st.slider('Kernel size', -1, 7, 3, 2)
            if kernel_size == -1:
                dx, dy = (1, 1)
            elif kernel_size == 1:
                dx = st.slider('dx', 1, 2, 1, 1)
                dy = st.slider('dy', 1, 2, 1, 1)
            else:
                dx = st.slider('dx', 1, kernel_size-1, 1, 1)
                dy = st.slider('dy', 1, kernel_size-1, 1, 1)
            output_img_dx = cv2.Sobel(output_img, -1, dx, 0, ksize=kernel_size)
            output_img_dy = cv2.Sobel(output_img, -1, 0, dy, ksize=kernel_size)
            output_img = np.maximum(output_img_dx, output_img_dy)

            col1, col2 = st.columns(2)

            with col1:
                st.header('Sobel dx')
                st.image(output_img_dx)

            with col2:
                st.header('Sobel dy')
                st.image(output_img_dy)

        elif edge_option == 'Canny':
            kernel_size = st.slider('Kernel size', 3, 7, 3, 2)
            threshold_1 = st.slider('Threshold 1', 0, 255, 100, 1)
            threshold_2 = st.slider('Threshold 2', 0, 255, 200, 1)
            L2gradient = st.toggle('L2 gradient', value=False)
            output_img = cv2.Canny(
                output_img, threshold_1, threshold_2,
                apertureSize=kernel_size, L2gradient=L2gradient
            )
        elif edge_option == 'Kernel':
            kernel_sobel_x = Kernel.sobel_x
            kernel_sobel_x_inv = Kernel.sobel_x_inv
            kernel_sobel_y = Kernel.sobel_y
            kernel_sobel_y_inv = Kernel.sobel_y_inv
            img_sobel_x = cv2.filter2D(output_img, -1, kernel_sobel_x)
            img_sobel_x_inv = cv2.filter2D(output_img, -1, kernel_sobel_x_inv)
            img_sobel_y = cv2.filter2D(output_img, -1, kernel_sobel_y)
            img_sobel_y_inv = cv2.filter2D(output_img, -1, kernel_sobel_y_inv)

            img_sobel_x_compound = np.maximum(img_sobel_x, img_sobel_x_inv)
            img_sobel_y_compound = np.maximum(img_sobel_y, img_sobel_y_inv)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.header('Sobel X')
                st.image(img_sobel_x)

                st.header('Sobel Y')
                st.image(img_sobel_y)

            with col2:
                st.header('Sobel X inv')
                st.image(img_sobel_x_inv)

                st.header('Sobel Y inv')
                st.image(img_sobel_y_inv)

            with col3:
                st.header('X compound')
                st.image(img_sobel_x_compound)

                st.header('Y compound')
                st.image(img_sobel_y_compound)

            output_img = np.maximum(img_sobel_x_compound, img_sobel_y_compound)

    input_col, output_col = st.columns(2)
    with input_col:
        st.header('Original')
        st.image(img, channels='BGR')

    with output_col:
        st.header('Output')
        st.image(output_img)

        result = Image.fromarray(output_img)
        show_image_download_button(result)


if __name__ == '__main__':
    main()
