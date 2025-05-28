import streamlit as st
import requests

st.title("Remote Alarm Trigger")

public_url = "https://fifty-trees-brush.loca.lt/"  # Replace with LocalTunnel URL

if st.button("Trigger Alarm"):
    try:
        response = requests.get(f"{public_url}/trigger_alarm")
        if response.status_code == 200:
            st.success("Alarm triggered!")
        else:
            st.error("Failed to trigger alarm.")
    except Exception as e:
        st.error(f"Error: {e}")
