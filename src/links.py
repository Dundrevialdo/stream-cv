import streamlit as st


class Link:
    blur = {
        'url': 'https://docs.opencv.org/4.5.2/d4/d86/group__imgproc__filter.html#ga8c45db9afe636703801b0b2e440fce37',
        'label': 'cv2.blur()'
    }
    gaussian_blur = {
        'url': 'https://docs.opencv.org/4.5.2/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1',
        'label': 'cv2.GaussianBlur()'
    }
    sobel = {
        'url': 'https://docs.opencv.org/4.5.2/d4/d86/group__imgproc__filter.html#gacea54f142e81b6758cb6f375ce782c8d',
        'label': 'cv2.Sobel()'
    }
    canny = {
        'url': 'https://docs.opencv.org/4.5.2/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de',
        'label': 'cv2.Canny()'
    }

    @staticmethod
    def show(link_name):
        link = getattr(Link, link_name)
        st.page_link(link['url'], label=link['label'])
