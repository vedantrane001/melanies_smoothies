import requests
import streamlit as st

url = "https://my.smoothiefroot.com/api/fruit/watermelon"

response = requests.get(url)

st.write("Status:", response.status_code)
st.write("Content-Type:", response.headers.get("Content-Type"))
st.code(response.text)
