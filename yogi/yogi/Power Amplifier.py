import streamlit as st

def power_amplifier_calculator(voltage_supply, collector_current, collector_resistor):
    power = (voltage_supply - 0.7) * collector_current
    efficiency = (power / voltage_supply) * 100
    return power, efficiency

st.title("Kalkulator Power Amplifier dengan Fixed Bias")
st.write("Masukkan nilai tegangan suplai, arus kolektor, dan resistor kolektor untuk menghitung daya dan efisiensi")

voltage_supply = st.number_input("Tegangan Suplai (Volt)", min_value=0.0, step=0.1)
collector_current = st.number_input("Arus (Ampere)", min_value=0.0, step=0.1)
collector_resistor = st.number_input("Resistor (Ohm)", min_value=0.0, step=0.1)

if st.button("Hitung"):
    power, efficiency = power_amplifier_calculator(voltage_supply, collector_current, collector_resistor)
    st.write(f"Daya = {power} Watt")
    st.write(f"Efisiensi = {efficiency} %")
