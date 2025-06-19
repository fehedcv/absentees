import easyocr
import re
import streamlit as st
import cv2
from PIL import Image
import numpy as np
from datetime import datetime

reader = easyocr.Reader(['en'], gpu=False)

st.title("Absentees Automation")
numbers = []
img = st.file_uploader("ADD PIC",["png","jpg"])
if st.button("SUBMIT"):
    st.image(img,caption="UPLOADED IMAGE")
    image = Image.open(img).convert('RGB')
    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)


    results = reader.readtext(image_cv)
    for box, text, confidence in results:
        found = re.findall(r'\b\d{1,2}\b', text)
        numbers.extend(found)



roll_map = {
    "1":"Aadhinath",
    "2":"Abhimanyu",
    "3":"Abhinav A",
    "4":"Abhishek KB",
    "5":"Abhinav Krishna",
    "6":"Adhil Chandra",
    "7":"Adityanarayanan",
    "8":"Akshay",
    "9":"Aleena Fathima",
    "10":"Aman",
    "11":"Anandhakrishnan",
    "12":"Anaswara",
    "13":"Anusree",
    "14":"Asif Kamal",
    "15":"Aswin Das",
    "16":"Athul Krishna",
    "17":"Danish Ahmed",
    "18":"Dilshad OK",
    "19":"Fahad Mohammed Kabeer",
    "20":"Fathima Hiba KM",
    "21":"Fathima Minha",
    "22":"Fathima Thehsina",
    "23":"Fidha P",
    "24":"Gopika KT",
    "25":"Hari",
    "26":"Hemanth PT",
    "27":"Hiba A",
    "28":"Hikka",
    "29":"Krishnapriya",
    "30":"Lamisha",
    "31":"Mohammed Abile",
    "32":"Mohammed Yahfin",
    "33":"Mruduldev",
    "34":"Diyan",
    "35":"Anas",
    "36":"Hisham",
    "37":"Hisham AK",
    "38":"Minhaj",
    "39":"Shahad",
    "40":"Shinadh",
    "41":"Swalih",
    "42":"Muhsina",
    "43":"Nurul Ameen",
    "44":"Praveen MT",
    "45":"Ridhwan",
    "46":"Rilwan",
    "47":"Rinsha",
    "48":"Risham",
    "49":"Shifana",
    "50":"Shimna",
    "51":"Sudeep",
    "52":"Suhair",
    "53":"Thazmeen",
    "54":"Vishnu",
    "55":"Vivek",
    "56":"Jumana Janiya",
    "57":"Anfas Roshan",
    "58":"Prarthana",
    "59":"Deva Manas",
    "60":"Fidha C",
    "61":"",
    "62":"Sreethu",
    "63":"",
    "64":"Amna Rasvin"
}
now = datetime.now()
date_str = now.strftime("%d-%m-%Y")    # e.g., 19-06-2025
day_str = now.strftime("%A")    

st.write(f"ABSENTEES {date_str}")
st.write(day_str)
for num in numbers:
    name = roll_map.get(num, "❌ Not Found")
    st.write(f"{num} → {name}")
