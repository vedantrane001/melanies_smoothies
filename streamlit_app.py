import requests
import streamlit as st

url = "https://my.smoothiefroot.com/api/fruit/watermelon"

response = requests.get(url)

st.write("Status:", response.status_code)
st.write("Content-Type:", response.headers.get("Content-Type"))
st.write("Response length:", len(response.text))
st.code(response.text)
