import streamlit as st
from PIL import Image
import cv2 
import numpy as np

def main():

    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Welcome', 'Image Classification of Food Items')
    )
    
    if selected_box == 'Welcome':
        welcome() 
    if selected_box == 'Image Classification of Food Items':
        classify_image()

    if selected_box == 'Image Classification of Food Items':
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
        ('Select Image of the Food Item', 'Item - I', 'Item - II', 'Item - III'))

    #st.write('You selected:', option)

    if option == 'Item - I':
        applie_pie = Image.open('692211.jpg')
        st.image(applie_pie, use_column_width=True)
    elif option == 'Item - II':
        omlette = Image.open('234922.jpg')
        st.image(omlette, use_column_width=True)
    elif option == 'Item - III':
        pizza = Image.open('68684.jpg')
        st.image(pizza, use_column_width=True)
    else:
        st.text("No image selected so far")

    if st.button('Classify'):
        st.text("Classifying...")
        if option == 'Item - I':
            st.text("   It's an Apple Pie!")
            st.text("")
            st.text("   Wanna order this item?")
            st.text("   If Yes, proceed to place your order by clicking your favorite link:")
            st.write("      [Swiggy](https://www.swiggy.com/search?q=Apple+Pie)")
            st.write("      [Zomato](https://www.zomato.com/pune/delivery?dishv2_id=b9fcf57e16fa23b2d81bc587ffde4788_2)")
        elif option == 'Item - II':
            st.text("   It's an Omlette!")
            st.text("")
            st.text("   Wanna order this item?")
            st.text("   If Yes, proceed to place your order by clicking the below link:")
            st.write("      [Swiggy](https://www.swiggy.com/search?q=Omelette)")
            st.write("      [Zomato](https://www.zomato.com/pune/delivery?dishv2_id=d5eefa915a939c9a1eaafdd3366b2310_2)")
        elif option == 'Item - III':
            st.text("   It's an Pizza!")
            st.text("")
            st.text("   Wanna order this item?")
            st.text("   If Yes, proceed to place your order by clicking the below link:")
            st.write("      [Swiggy](https://www.swiggy.com/search?q=Pizza)")
            st.write("      [Zomato](https://www.zomato.com/pune/restaurants/pizza?category=1)")
        elif option == 'Select Image of the Food Item':
            st.text("   No food item selected. Please select a valid choice.")

if __name__ == "__main__":
    main()
