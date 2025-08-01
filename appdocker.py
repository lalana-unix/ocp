import streamlit as st
from PIL import Image
import random
import time

# Set the page configuration

st.markdown(
    "<h2 style='text-align: center;'>My Streamlit app using Dockerfile</h2>",
    unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("media/happy-feet-penguins.gif", use_container_width=True)


st.caption("This is a simple Streamlit app that demonstrates the use of Dockerfile to build and deploy a containerized application on OpenShift.")
#st.image("media/penguin-dance.gif")