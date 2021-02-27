import streamlit as st
from PIL import Image
import cv2 
import numpy as np

def main():

    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Welcome', 'Image Classification')
    )
    
    if selected_box == 'Welcome':
        welcome() 
    if selected_box == 'Image Classification':
        classify_image()

    if selected_box == 'Image Classification':
        selected_box = st.sidebar.selectbox(
            'Choose one of the following models',
            ('MobileNetV2', 'ResNet50', 'InceptionV3')
        )
    
def welcome():
    
    st.title('Image Classification using Streamlit')
    
    st.subheader('A simple app that shows different image classification algorithms. You can choose the options'
             + ' from the dropdown menu at left. This is just a first hand implementation to show how it works on Streamlit. ' + 
             'You are free to add stuff to this app.')
    
    st.image('uhdresto.jpg', use_column_width=True)

def load_image(filename):
    image = cv2.imread(filename)
    return image

def classify_image():

    st.header("Classify Images")
    st.text("")
    st.text("")
    
    option = st.selectbox(
        'Please select the type of image you would like to see',
        ('Select Image', 'Apple Pie', 'Omlette', 'Pizza'))

    st.write('You selected:', option)

    if option == 'Apple Pie':
        applie_pie = Image.open('692211.jpg')
        st.image(applie_pie, use_column_width=True)
    elif option == 'Omlette':
        omlette = Image.open('234922.jpg')
        st.image(omlette, use_column_width=True)
    elif option == 'Pizza':
        pizza = Image.open('68684.jpg')
        st.image(pizza, use_column_width=True)
    else:
        st.text("No image selected so far")

    if st.button('Classify'):
        st.text("Classifying...")
        if option == 'Apple Pie':
            st.text("   It's an Apple Pie!")
        elif option == 'Omlette':
            st.text("   It's an Omlette!")
        elif option == 'Pizza':
            st.text("   It's an Pizza!")
        elif option == 'Select Image':
            st.text("   No image selected. Please select a valid choice.")

if __name__ == "__main__":
    main()
