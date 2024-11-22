import streamlit as st
import math


st.title("Power Estimator")


st.sidebar.header("Input Parameters")


voltage = st.sidebar.number_input("Voltage (V)", min_value=0.0, value=230.0, step=0.1)
current = st.sidebar.number_input("Current (I)", min_value=0.0, value=5.0, step=0.1)
power_factor = st.sidebar.slider("Power Factor (PF)", min_value=0.0, max_value=1.0, value=0.8)


apparent_power = voltage * current 
active_power = apparent_power * power_factor  
reactive_power = math.sqrt(apparent_power**2 - active_power**2)  

st.subheader("Results")
st.write(f"**Apparent Power (S):** {apparent_power:.2f} VA")
st.write(f"**Active Power (P):** {active_power:.2f} W")
st.write(f"**Reactive Power (Q):** {reactive_power:.2f} VAR")
