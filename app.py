import streamlit as st
from PIL import Image
import random
import time

# Set the page configuration

st.markdown(
    "<h2 style='text-align: center;'>This is a Streamlit app using S2I</h2>",
    unsafe_allow_html=True)

# Load and display image
image = Image.open("media/ocp.jpg")
st.image(image, caption="Genereat picture from AI", use_container_width=True)

st.write("This is a simple Streamlit app that demonstrates the use of S2I (Source-to-Image) to build and deploy a containerized application on OpenShift.")
#st.image("media/penguin-dance.gif")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("media/penguin-dance.gif", use_container_width=True)
