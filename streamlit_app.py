import streamlit as st

from PIL import Image
image = Image.open('data/bernie.png')
st.image(image, caption='Bernie!', use_column_width=True)

