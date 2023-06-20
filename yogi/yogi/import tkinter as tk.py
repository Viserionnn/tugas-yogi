import tkinter as tk
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Mendapatkan objek endpoint volume default
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume.iid, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Mendapatkan volume maksimum
volume_range = volume.GetVolumeRange()
volume_min = volume_range[0]
volume_max = volume_range[1]

# Fungsi untuk mengatur volume
def set_volume(volume_value):
    volume_level = volume_min + (volume_max - volume_min) * volume_value / 100.0
    volume.SetMasterVolumeLevel(volume_level, None)

# Fungsi untuk mengupdate volume berdasarkan masukan pengguna
def update_volume():
    volume_value = float(entry.get())
    if 0 <= volume_value <= 100:
        set_volume(volume_value)
        label.config(text="Volume diatur: {}%".format(volume_value))
    else:
        label.config(text="Masukkan volume antara 0 hingga 100!")

# Fungsi untuk mengembalikan volume ke nilai awal
def restore_volume():
    set_volume(100)
    entry.delete(0, tk.END)
    entry.insert(0, "100")
    label.config(text="Volume dikembalikan ke nilai awal: 100%")

# Membuat GUI menggunakan Tkinter
window = tk.Tk()
window.title("Tugas Besar Pengatur Volume secara desiBel ")
window.geometry("300x200")
nama_label = tk.Label(window, text="Nama: Hendy Eka Pratama (112021034)", font=("Arial", 20))
nama_label.pack()

nama_label = tk.Label(window, text="Dosen: Ir.Rustamaji", font=("Arial", 20))
nama_label.pack()

# Label untuk judul
title_label = tk.Label(window, text="Pengatur Volume secara desiBel", font=("Times New Roman", 20))
title_label.pack(pady=10)

# Label untuk menampilkan informasi
label = tk.Label(window, text="Masukkan nilai volume (0 hingga 100 dB):", font=("Times New Roman", 16))
label.pack(pady=10)

# Entry untuk masukan nilai volume
entry = tk.Entry(window)
entry.pack(pady=5)
entry.insert(0, "100")

# Tombol untuk mengatur volume
button = tk.Button(window, text="Atur Volume", font=("Times New Roman", 16), command=update_volume)
button.pack(pady=5)

# Tombol untuk mengembalikan volume ke nilai awal
restore_button = tk.Button(window, text="Kembalikan Volume", font=("Times New Roman", 16), command=restore_volume)
restore_button.pack(pady=5)

# Fungsi untuk menutup aplikasi
def close_app():
    window.destroy()

# Menambahkan fungsi close_app() saat menutup jendela
window.protocol("WM_DELETE_WINDOW", close_app)

# Memulai event loop Tkinter
window.mainloop()