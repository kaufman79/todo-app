import streamlit as st
from PIL import Image

with st.expander("Start camera"):
    # start camera
    camera_image = st.camera_input("Camera")

if camera_image: # so that it doesnt try rendering before theres an image
    # converts to a pillow image type.
    img = Image.open(camera_image)

    # makes the PIL image gray
    gray_img = img.convert("L")

    # displays image
    st.image(gray_img)