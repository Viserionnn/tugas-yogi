import streamlit as st

def calculate_transistor():
    # Mendapatkan nilai dari input pengguna
    vcc = float(vcc_entry.value)
    rb = float(rb_entry.value)
    re = float(re_entry.value)
    rc = float(rc_entry.value)
    beta = float(beta_entry.value)

    # Menghitung arus basis
  

    # Menampilkan hasil perhitungan
    result_text = "Arus Basis (Ib): {:.9f} A\nArus Emitter (Ie): {:.9f} A\nTegangan Emitter (Ve): {:.9f} V\nTegangan Kolektor (Vc): {:.9f} V".format(ib , ie , ve, vc)
    result_text = result_text.replace('\n', '<br>')
    result_label.markdown(result_text, unsafe_allow_html=True)

# Menampilkan informasi tugas besar
st.markdown("Nama: Yogi Firmansyah")
st.markdown("NRP: 112021030")
st.markdown("Kelas: BB")
st.markdown("Tugas Besar: Elektronika Analog")
st.markdown("Dosen: Ir. Rustamaji,M.T.")
st.image("penguat.PNG")

# Membuat input fields
vcc = st.number_input("Tegangan Catu Daya (Vcc) (V):")
rb = st.number_input("Resistor Basis (RB) (ohm):")
re = st.number_input("Resistor Emitter (RE) (ohm):")
rc = st.number_input("Resistor Kolektor (RC) (ohm):")
beta = st.number_input("Faktor Penguatan (Beta):")

# Tombol untuk melakukan perhitungan
calculate_button = st.button("Hitung")
result_label = st.empty()

if calculate_button:
    # Menghitung transistor
    ib = (vcc - 0.7) / (rb+(re*(beta+1)))

    # Menghitung arus kolektor
    ic = ib * beta

    # Menghitung arus emitter
    ie = (ic + ib)

    # Menghitung tegangan emitter
    ve = ie * re  

    # Menghitung tegangan kolektor
    vc = ic * rc 

    # Menampilkan hasil perhitungan
    result_text = "Arus Basis (Ib): {:.6f} A\nArus Kolektor (Ic): {:.6f} A\nArus Emitter (Ie): {:.6f} A\nTegangan Emitter (Ve): {:.2f} V\nTegangan Kolektor (Vc): {:.2f} V".format(ib ,ic, ie , ve, vc)
    result_text = result_text.replace('\n', '<br>')
    result_label.markdown(result_text, unsafe_allow_html=True)

st.markdown("---")
st.write("made by yogi firmansyah!")