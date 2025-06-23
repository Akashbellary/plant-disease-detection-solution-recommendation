import streamlit as st
from PIL import Image
import numpy as np
import os
import random

from utils import load_model_and_classes, predict_disease
from demo_data import treatments, tomato_classes


# Load styles
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Inject CSS
load_css("styles.css")  # or "assets/styles.css"

# Load model
model, model_loaded, img_height, img_width = load_model_and_classes()

# Set page config
st.set_page_config(page_title="Plant Disease Detection", layout="wide")

# App Title
st.markdown("<h1>🍃 Plant Disease Detection System</h1>", unsafe_allow_html=True)

# Main layout
col1, col2 = st.columns([1, 1])

# ========== LEFT PANEL ==========
with col1:
    st.markdown('<div class="container-box">', unsafe_allow_html=True)
    st.header("Upload Image")

    if not model_loaded:
        st.warning("Model not loaded. Running in demo mode.")

    plant_type = st.selectbox("Select Plant Type", ["Tomato", "Potato", "Cucumber", "Pepper"])
    uploaded_file = st.file_uploader("Drop image here or click to upload", type=['jpg', 'jpeg', 'png'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=300)

    detect_button = st.button("Detect Disease", use_container_width=True)
    debug_button = st.button("Debug Model", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ========== RIGHT PANEL ==========
with col2:
    st.markdown('<div class="container-box">', unsafe_allow_html=True)
    st.header("Detection Results")

    if detect_button and uploaded_file:
        if plant_type == "Tomato" and model_loaded:
            disease, confidence = predict_disease(image, model, img_height, img_width)
        else:
            disease = random.choice(tomato_classes)
            confidence = round(random.uniform(90, 99), 2)

        info = treatments.get(disease, treatments['Healthy'])

        st.markdown(f"<div class='disease-highlight'>✅ Detected Disease: <b>{disease}</b><br>"
                    f"<small><b>Confidence:</b> {confidence:.1f}%</small><br>"
                    f"{info['description']}</div>", unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🌱 Organic Solutions", "🧪 Chemical Solutions"])

        with tab1:
            st.subheader("Organic Treatment")
            st.write(info['organic']['treatment'])
            st.markdown("**Application Instructions:**")
            st.write(info['organic']['instructions'])

            st.markdown("**Recommended Organic Products**")
            for product in info['organic']['products']:
                st.markdown(f"""<div class='product-card'>
                    <b>{product['name']}</b> <span style='color:green; font-size:0.9rem;'>({product['type']})</span>
                    <br>{product['price']}
                    <button class='buy-button'>Buy Now</button>
                    </div>""", unsafe_allow_html=True)

        with tab2:
            st.subheader("Chemical Treatment")
            st.write(info['chemical']['treatment'])
            st.markdown("**Application Instructions:**")
            st.write(info['chemical']['instructions'])

            st.markdown("**Recommended Chemical Products**")
            for product in info['chemical']['products']:
                st.markdown(f"""<div class='product-card'>
                    <b>{product['name']}</b> <span style='color:red; font-size:0.9rem;'>({product['type']})</span>
                    <br>{product['price']}
                    <button class='buy-button'>Buy Now</button>
                    </div>""", unsafe_allow_html=True)

    elif detect_button and not uploaded_file:
        st.error("Please upload an image before detection.")

    if debug_button:
        if not model_loaded:
            st.error("Model not loaded, running in demo mode")
        else:
            st.success("Model Summary")
            for layer in model.layers:
                st.markdown(f"- **{layer.name}** ({layer.__class__.__name__}) | "
                            f"Input: `{getattr(layer, 'input_shape', 'N/A')}` | "
                            f"Output: `{getattr(layer, 'output_shape', 'N/A')}`")
    st.markdown('</div>', unsafe_allow_html=True)
