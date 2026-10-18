import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Aplikasi Dokter Sederhana", page_icon="🩺")

# Judul Utama
st.title("🩺 Asisten Dokter & Rekomendasi Obat")
st.write(
    "Pilih keluhan atau gejala yang Anda rasakan untuk melihat rekomendasi"
    " obat awal."
)
st.markdown("---")

# Database Penyakit dan Obat
database_gejala = {
    "Demam, Batuk, Pilek": {
        "kondisi": "Flu / Common Cold",
        "obat": [
            "Paracetamol (Pereda demam/nyeri)",
            "Guaifenesin / Obat Batuk",
            "Vitamin C",
        ],
        "saran": (
            "Perbanyak istirahat, minum air hangat, dan makan makanan bergizi."
        ),
    },
    "Sakit Kepala, Pusing, Badan Lemas": {
        "kondisi": "Kelelahan / Masuk Angin",
        "obat": ["Paracetamol", "Vitamin B Kompleks"],
        "saran": "Istirahat yang cukup dan hindari stres berlebihan.",
    },
    "Nyeri Perut, Mual, Kembung": {
        "kondisi": "Gangguan Pencernaan / Maag",
        "obat": ["Antasida Doen (Pereda asam lambung)"],
        "saran": "Makan teratur, hindari makanan pedas, asam, dan kopi.",
    },
    "Gatal-gatal, Kemerahan pada Kulit": {
        "kondisi": "Alergi Ringan / Dermatitis",
        "obat": ["Cetirizine atau Loratadine", "Salep Hidrokortison"],
        "saran": "Hindari pemicu alergi dan jangan digaruk.",
    },
}

# Pilihan Gejala
pilihan = st.selectbox(
    "Pilih Gejala Utama Anda:",
    ["-- Pilih Gejala --"] + list(database_gejala.keys()),
)

# Tombol Eksekusi
if st.button("Cari Rekomendasi Obat"):
  if pilihan == "-- Pilih Gejala --":
    st.warning("⚠️ Silakan pilih salah satu gejala terlebih dahulu.")
  else:
    # Ambil data sesuai pilihan
    hasil = database_gejala[pilihan]

    st.success("✅ Analisis Berhasil!")

    # Tampilkan Hasil
    st.subheader("📋 Hasil Analisis")
    st.write(f"**Kemungkinan Kondisi:** {hasil['kondisi']}")

    st.subheader("💊 Rekomendasi Obat")
    for obat in hasil["obat"]:
      st.markdown(f"- {obat}")

    st.subheader("💡 Saran Medis")
    st.info(hasil["saran"])

    st.markdown("---")
    st.warning(
        "⚠️ **Catatan:** Aplikasi ini hanya simulasi informasi awal. Segera"
        " temui dokter profesional jika keluhan berlanjut."
    )