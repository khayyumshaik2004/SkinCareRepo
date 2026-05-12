import streamlit as st
import tensorflow as tf
import tf_keras as keras
from tf_keras.preprocessing.image import load_img, img_to_array
from tf_keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import pandas as pd
from PIL import Image
from io import BytesIO
from recommendations_data import RECOMMENDATIONS

# ------------------------
# Custom Layer to fix "groups" error
# ------------------------
class CustomDepthwiseConv2D(keras.layers.DepthwiseConv2D):
    def __init__(self, **kwargs):
        if 'groups' in kwargs:
            kwargs.pop('groups')
        super().__init__(**kwargs)

    @classmethod
    def from_config(cls, config):
        if 'groups' in config:
            config.pop('groups')
        return super().from_config(config)

# -------------------------------
# Load model and data
# -------------------------------
MODEL_PATH = 'skin_classification_model.h5'

st.set_page_config(page_title="AI Skin Type Detector", layout="centered")

@st.cache_resource
def load_model():
    return keras.models.load_model(MODEL_PATH, custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D}, compile=False)

@st.cache_data
def load_recommendations():
    # Convert RECOMMENDATIONS dict to a DataFrame
    data = []
    for skin_type, items in RECOMMENDATIONS.items():
        for item in items:
            row = item.copy()
            row['Skin Type'] = skin_type
            row['Product'] = item['Product_English']  # Map to expected column name
            data.append(row)
    return pd.DataFrame(data)

model = load_model()
recommendations_df = load_recommendations()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("💆‍♀️ AI-Powered Skin Type Classification")
st.write("Upload a clear image of your skin to detect your skin type and get personalized skincare recommendations.")

uploaded_file = st.file_uploader("📤 Upload a skin image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image")

    # Preprocess the image
    img = image.resize((224, 224))
    img_array = img_to_array(img)
    img_array = preprocess_input(img_array.reshape(1, 224, 224, 3))

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    class_names = ['acne', 'dry', 'oil']
    predicted_class = class_names[predicted_class_index].capitalize()
    # Display results
    if predicted_class=='Acne':
        st.info("Your skin type is prone to acne. Consider using non-comedogenic products and maintaining a regular cleansing routine.")
        # Filter recommendations
        st.subheader(f"🌿 Recommended Products for {predicted_class} Skin:")
        predicted_class_lower = predicted_class.lower()
        filtered_recommendations = recommendations_df[
            recommendations_df['Skin Type'].str.lower() == predicted_class_lower
        ]
        # Show recommendations
        if not filtered_recommendations.empty:
            for _, row in filtered_recommendations.iterrows():
                st.markdown(f"""
                **Product:** {row['Product']}  
                🧴 **Recommendation:** {row['Recommendation']}  
                🔗 [Visit Website]({row['Website']})
                """)
    else:
        classes = ["Dry Skin", "Oily Skin"]
        def load_model_secondary():
            try:
                return keras.models.load_model("Skin-Type-Recognition", compile=False)
            except Exception as e:
                st.error(f"Error loading secondary model: {e}")
                return None

        model = load_model_secondary()
        IMAGE_SHAPE = (224, 224)
        def load_and_prep_image(image):
            """
            Reads an image from filename, turns it into a tensor and reshapes 
            it to (img_shape, img_shape,, color_channels)
            """
            # Read in the image
            # img = tf.io.read_file(filename)
            # Decode the read file into a tensor
            image = tf.image.decode_image(image)
            # Resize the image  
            image = tf.image.resize(image, size=IMAGE_SHAPE)
            #Grayscale
            if image.shape[2] == 1:
                image = tf.image.grayscale_to_rgb(image)
                # Rescale the image (getting all values between 0 & 1)
                # image = image/255

            return image

        content = uploaded_file.getvalue()

        st.write("Predicted Skin type :")
        with st.spinner("Classifying....."):
            img = load_and_prep_image(content)
            label = model.predict(tf.expand_dims(img, axis=0))
            st.write(classes[int(tf.argmax(tf.squeeze(label).numpy()))])
        st.write("")
        image = Image.open(BytesIO(content))
