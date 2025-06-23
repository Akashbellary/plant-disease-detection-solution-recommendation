import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image

def load_model_and_classes():
    try:
        model_path = os.path.join(os.path.dirname(__file__), 'tomato_model.h5')
        model = load_model(model_path)
        input_shape = model.input_shape[1:3]
        return model, True, input_shape[0], input_shape[1]
    except Exception as e:
        print("Model loading failed:", e)
        return None, False, 224, 224

def predict_disease(img, model, img_height, img_width):
    img = img.resize((img_width, img_height))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_index]) * 100

    from demo_data import tomato_classes
    return tomato_classes[predicted_index], confidence



