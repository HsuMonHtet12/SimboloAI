import streamlit as st
import tensorflow as tf

st.set_option('deprecation.showfileUploaderEncoding',False)
@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('C:/Users/STH/Desktop/TrainTest/cat_dog_tiger.hdf5')
  return model
model = load_model()
st.write(" Classification")
file=st.file_uploader("upload an image", type=["jpg","png"])

import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(100,100)
    image=ImageOps.fit(image_data,size)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    predict=model.predict(img_reshape)
    return predict
if file is None:
    st.text("Please upload")
else:
  image=Image.open(file)
  st.image(image,use_column_width=True)
  predictions=import_and_predict(image,model)
  class_names=['Cat','Dog','Tiger']
  string=class_names[np.argmax(predictions)]
  st.success(string)
         

    