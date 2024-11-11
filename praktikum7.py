
import tkinter as tk #Mengimpor modul Tkinter dan memberinya alias tk untuk memudahkan penulisan.
from tkinter import messagebox #Mengimpor modul messagebox dari Tkinter untuk menampilkan kotak pesan (misalnya, untuk kesalahan input).

def prediksi_prodi():
    try:
        for entry in nilai_entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0-100.")
        
        hasil.set("Hasil Prediksi: Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0-100.")
#memunculkan hasil prediksi berupa teknologi informasi, jika nilai jang dimasukkan tidak berupa angka dari 0-100 maka akan muncul error "pastikan semua input adalah angka antara 0-100"
    

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") 
root.configure(bg="yellow")
#mengatur nama judul utama aplikasi dan background

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10, )
#mengatur font dan tata letak judul

nilai_labels = []
nilai_entries = []
#untuk menyimpan objek label dan entry yang akan dibuat dalam loop berikutnya
for i in range(1, 11): #membuat 10 nilai mata pelajaran label dan entry
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i}:")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e") #menempatkan label di dalam jendela menggunakan sistem layout grid.
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5) #menempatkan entry di dalam jendela menggunakan sistem layout grid.
    nilai_labels.append(label)
    nilai_entries.append(entry)
#Menambahkan objek label dan entry yang baru dibuat ke dalam list agar bisa di akses 

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)
#memubuat tombol hasil prediksi dari prediksi_prodi yang di atas

hasil = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil, font=("Arial", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)
#memunculkan output dari hasil prediksi dibawah tombol hasil prediksi

root.mainloop() #untuk menjalankan program