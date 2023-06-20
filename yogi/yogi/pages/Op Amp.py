import streamlit as st

def calculate_op_amp():
    # Mendapatkan nilai dari input pengguna
    vin = float(vin_input)
    rf = float(rf_input)
    rin = float(rin_input)

    # Menghitung tegangan output
    vout = (-rf / rin) * vin

    # Menampilkan hasil perhitungan
    st.write("Tegangan Output:", vout, "V")

# Judul aplikasi
st.title("Aplikasi Operasional Amplifier")
st.image("/home/appuser/yogi/yogi/in.PNG")

# Input fields
vin_input = st.number_input("Tegangan Masukan (Vin) (V):")
rin_input = st.number_input("Resistor Input (R1) (ohm):")
rf_input = st.number_input("Resistor Feedback (Rf) (ohm):")

# Tombol untuk melakukan perhitungan
calculate_button = st.button("Hitung")
if calculate_button:
    calculate_op_amp()
