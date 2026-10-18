import streamlit as st

# 1. Konfigurasi Halaman & Tema
st.set_page_config(
    page_title="Halodoc Clone - Konsultasi & Obat",
    page_icon="🩺",
    layout="centered",
)

# Kustomisasi CSS ala Halodoc (Warna Merah/Merah Muda & Kartu Clean)
st.markdown(
    """
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        background-color: #e0004d;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #c00042;
        color: white;
    }
    .service-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #eee;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. Header Aplikasi
col_logo, col_user = st.columns([3, 1])
with col_logo:
  st.title("🩺 **halodokter**")
  st.caption("Solusi Kesehatan Terintegrasi & Informasi Obat")

with col_user:
  st.markdown("👤 **Pasien:** User")
  st.caption("📍 Jakarta, ID")

st.markdown("---")

# 3. Kategori Layanan Utama (Fitur ala Halodoc)
st.subheader("Layanan Utama")
c1, c2, c3 = st.columns(3)

with c1:
  st.markdown(
      '<div class="service-card">💊<br><b>Chat Dokter & Obat</b></div>',
      unsafe_allow_html=True,
  )
with c2:
  st.markdown(
      '<div class="service-card">🏥<br><b>Cari Rumah Sakit</b></div>',
      unsafe_allow_html=True,
  )
with c3:
  st.markdown(
      '<div class="service-card">🧪<br><b>Tes Laboratorium</b></div>',
      unsafe_allow_html=True,
  )

st.markdown("<br>", unsafe_allow_html=True)

# 4. Tab Menu Utama
tab1, tab2 = st.tabs(["💬 Cek Gejala & Rekomendasi Obat", "👨‍⚕️ Pilih Spesialis"])

# Database Diagnosa & Obat
database_medis = {
    "Flu & Batuk Pilek": {
        "kondisi": "Infeksi Saluran Pernapasan Atas (ISPA) / Flu",
        "kategori_obat": "Obat Bebas (OTC)",
        "obat": [
            {"nama": "Paracetamol 500mg", "dosis": "3x1 tablet sesudah makan"},
            {"nama": "Sutra Batuk / Guaifenesin", "dosis": "3x1 sendok takar"},
            {"nama": "Vitamin C 500mg", "dosis": "1x1 tablet sehari"},
        ],
        "saran": (
            "Istirahat cukup, konsumsi air hangat, dan gunakan masker jika"
            " beraktivitas."
        ),
    },
    "Maag & Nyeri Lambung": {
        "kondisi": "Gastritis / Dispepsia (Asam Lambung)",
        "kategori_obat": "Obat Bebas Terbatas",
        "obat": [
            {
                "nama": "Antasida Doen Kunyah",
                "dosis": "3x1 tablet sebelum makan",
            },
            {
                "nama": "Omeprazole 20mg",
                "dosis": "1x1 kapsul sebelum makan pagi",
            },
        ],
        "saran": "Makan dengan porsi kecil tapi sering, hindari kopi dan pedas.",
    },
    "Sakit Kepala & Migrain": {
        "kondisi": "Tension Headache / Migrain Ringan",
        "kategori_obat": "Obat Bebas",
        "obat": [
            {
                "nama": "Ibuprofen 400mg / Paracetamol",
                "dosis": "3x1 tablet jika nyeri",
            },
            {"nama": "Vitamin B-Complex", "dosis": "1x1 tablet sehari"},
        ],
        "saran": "Kurangi waktu layar (screen time) dan istirahat di ruangan gelap.",
    },
}

with tab1:
  st.markdown("### 🔍 Konsultasi Keluhan Kesehatan")

  gejala_pilihan = st.selectbox(
      "Pilih keluhan atau gejala yang dirasakan saat ini:",
      ["-- Pilih Keluhan --"] + list(database_medis.keys()),
  )

  if st.button("Mulai Diagnosa & Cari Obat"):
    if gejala_pilihan == "-- Pilih Keluhan --":
      st.warning("Silakan pilih keluhan terlebih dahulu.")
    else:
      data = database_medis[gejala_pilihan]

      # Tampilan Hasil Konsultasi ala Halodoc
      st.success("Analisis Sistem Selesai")

      st.markdown(f"#### 📊 Hasil Diagnosa Awal")
      st.write(f"**Indikasi:** {data['kondisi']}")
      st.write(f"**Kategori Obat:** {data['kategori_obat']}")

      st.markdown("---")
      st.markdown("#### 📄 Resep Digital & Rekomendasi Obat")

      # Menampilkan daftar obat dalam bentuk kartu resep
      for item in data["obat"]:
        with st.container():
          col_a, col_b = st.columns([2, 1])
          with col_a:
            st.markdown(f"💊 **{item['nama']}**")
            st.caption(f"Aturan pakai: {item['dosis']}")
          with col_b:
            st.caption(" Status: Ready")
          st.markdown("---")

      st.markdown("#### 💡 Catatan Dokter")
      st.info(data["saran"])

      st.warning(
          "⚠️ **Disclaimer:** Ini adalah simulasi rekomendasi obat. Jika gejala"
          " tidak membaik dalam 3 hari, konsultasikan langsung dengan dokter."
      )

with tab2:
  st.markdown("### 👨‍⚕️ Dokter Terdekat yang Tersedia")
  st.write("Fitur simulasi untuk janji temu dokter.")

  dokter_list = [
      {
          "nama": "dr. Andi Pratama, Sp.PD",
          "spesialis": "Spesialis Penyakit Dalam",
          "rating": "⭐ 4.9",
          "pengalaman": "8 Tahun",
      },
      {
          "nama": "dr. Siti Rahma, Sp.A",
          "spesialis": "Spesialis Anak",
          "rating": "⭐ 4.8",
          "pengalaman": "5 Tahun",
      },
  ]

  for doc in dokter_list:
    st.write(f"**{doc['nama']}** - {doc['spesialis']}")
    st.caption(
        f"Rating: {doc['rating']} | Pengalaman: {doc['pengalaman']}"
    )
    st.button(f"Chat dengan {doc['nama']}", key=doc["nama"])
    st.markdown("---")
