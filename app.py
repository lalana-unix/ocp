import streamlit as st
from PIL import Image


# Set the page configuration

st.markdown(
    "<h2 style='text-align: center;'>Streamlit app using S2I</h2>",
    unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    #st.image("media/happy-feet-penguins.gif", use_container_width=True)
    st.image("media/penguin-dance.gif", use_container_width=True)
    st.text("Dancing")
    #st.image("media/ocp.jpg", use_container_width=True)
    
    
st.caption("This is a simple Streamlit app that demonstrates the use of S2I (Source-to-Image) to build and deploy a containerized application on OpenShift.")
#st.image("media/penguin-dance.gif")
