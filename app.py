import streamlit as st
from PIL import Image


st.title("Hello from Unix Red Hat OpenShift Container Platform!")
st.write("This is a Streamlit app using S2I.")


# Load and display image
image = Image.open("media/redhat.jpg")
st.image(image, caption="This is a Red Hat OpenShift Container Platform", use_container_width=True)
