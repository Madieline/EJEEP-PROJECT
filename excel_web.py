import pandas as pd
import streamlit as st
import time

sheet_idA = '16CwByzI3-J0o36W7vs4hZ1Ovmyc2uV0DhJH4Cj96rU8'

dfA = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_idA}/export?format=csv")

st.set_page_config(layout="centered")

st.image(https://www.flaticon.com/free-icon/bus_1023464?term=bus&page=1&position=18&origin=search&related_id=1023464, width=100)
st.title("Line A")
st.write(dfA.head(3))

st.title("Line B")
st.write(dfA.iloc[5:8])

st.title("Express")
st.write(dfA.iloc[10:14])


time.sleep(60 * 1)  # Refresh every 5 minutes (adjust as needed)
st.experimental_rerun()
