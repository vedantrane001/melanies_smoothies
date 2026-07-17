import requests
import streamlit as st

url = "https://my.smoothiefroot.com/api/fruit/watermelon"

response = requests.get(url)

st.write("Status Code:", response.status_code)
st.write("Headers:", response.headers)
st.write("Raw Response:")
st.code(response.text)
