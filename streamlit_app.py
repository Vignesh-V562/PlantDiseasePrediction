import streamlit as st
import tensorflow as tf
import numpy as np

# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size = (128,128))
    inputArray = tf.keras.preprocessing.image.img_to_array(image)
    inputArray = np.array([inputArray])
    prediction = model.predict(inputArray)
    result_index = np.argmax(prediction)
    return result_index

# Sidebar
st.sidebar.image("L2.png")
st.sidebar.markdown(""" ## Welcome to Vignesh's❤️ Plant🌿Prediction Home🏡""")
st.sidebar.title("Dashboard")

app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Prediction"])

# Home page
if(app_mode == "Home"):
    st.header("PLANT 🌿 DISEASE RECOGNITION 🔍 SYSTEM")
    image_Path = "home_page.jpeg"
    st.image(image_Path,use_column_width=True)
    st.markdown("""
   # 🌿 Welcome to the Plant Disease Recognition System! 🔍  

### 🌱 Our Mission  
At **Plant Disease Recognition System**, we aim to assist farmers, gardeners, and agricultural professionals in 
**identifying plant diseases efficiently**. By leveraging advanced machine learning techniques, we provide **quick, accurate, 
and reliable** disease detection to help protect crops and ensure a **healthier harvest**.  

---

## 🚀 How It Works  

1. **Upload Image:**  
   - Navigate to the **Disease Recognition** page.  
   - Upload an image of a plant leaves showing signs of disease.  

2. **🧠 AI Analysis:**  
   - Our system uses **cutting-edge algorithms** to analyze the image.  
   - Detects possible diseases with high accuracy.  

3. **Get Results & Recommendations:**  
   - Receive a detailed **diagnosis** and potential treatment recommendations.  
   - Take informed action to protect your crops.  

---

## ✅ Why Choose Us?  

- **🎯 High Accuracy:** 
- **💡 User-Friendly:** 
- **⚡ Fast & Efficient:**  
- **📚 Continuous Improvement:**  

---

## 🎉 Get Started  

Ready to analyze your plant’s health?  

👉 **Click on the [Disease Recognition](#) page in the sidebar** to upload an image and get instant insights!  

---

## 📌 Additional Features  

🔍 **Disease Database:** Browse a **comprehensive list** of plant diseases, symptoms, and preventive measures.  
🛠 **Expert Tips:** Get **farming tips** and best practices to keep your plants healthy.  
🌍 **Community Support:** Join our **forum** and discuss with experts and fellow growers.  

---

## 👥 About Us  

🌾 We are a team of **AI enthusiasts, agronomists, and developers** dedicated to improving **agriculture through technology**. Our goal is to make plant disease detection **accessible, fast, and reliable** for everyone.  

📖 Learn more on the **[About Us](#)** page.  

---

## 🔗 Connect With Us  
 
📧 **Email:** [vignesh23110571@snuchennai.edu.in](#)  
📱 **Social Media:**  
   -  | [@arts_of_vicky](#) | [Vignesh Velmurugan](#) 


🌱 **Together, let's build a healthier future for our crops!** 🌍🌿  

""")

# About
elif(app_mode =="About"):
    st.balloons()
    st.header("About")
    st.markdown("""
    #### About Dataset
    - This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
        This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided 
        into 80/20 ratio of training and validation set preserving the directory structure.
    - A new directory containing 33 test images is created later for prediction purpose.
    - you can get the Dataset from [Kaggle - new plant disease dataset](#) or from my github page.
                
#### Content
    1. train (70295 images)
    2. test (33 images)
    3. validation (17572 images)
                
## 🔗 Connect With Us  
 
**Email:** [vignesh23110571@snuchennai.edu.in](#)  
**Social Media:**  
-  | [arts_of_vicky](#) | [Vignesh Velmurugan](#) 
- **Together, let's build a healthier future for our crops!** 🌍🌿
""")

#Prediction page
elif(app_mode=="Disease Prediction"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image")
    if(st.button("Show Image")):
        st.image(test_image,use_column_width=True)
    #prediction Button
    col1,col2,col3 = st.columns([1,1,3])
    with col3:
       Predict_but =  st.button("predict")
    if(Predict_but):
        st.snow()
        st.write("Our prediction")
        result_index = model_prediction(test_image)
        #Define class
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))