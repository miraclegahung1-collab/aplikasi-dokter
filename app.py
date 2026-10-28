import streamlit as st

# 1. Konfigurasi Halaman & Tema
st.set_page_config(
    page_title="docaja - Konsultasi & Obat",
    page_icon="🩺",
    layout="centered",
)

# Kustomisasi CSS agar kotak putih berfungsi sebagai tombol yang bersih
st.markdown(
    """
    <style>
    .main { background-color: #f8f9fa; }
    /* Mengubah tombol bawaan Streamlit agar menyerupai kotak putih bersih */
    .stButton>button {
        background-color: #ffffff;
        color: #1f2937;
        border-radius: 12px;
        border: 1px solid #d1d5db;
        padding: 1.5rem 1rem;
        font-weight: 600;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #f3f4f6;
        border-color: #9ca3af;
        color: #000000;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Inisialisasi Session State untuk Navigasi Halaman
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# 2. Header Aplikasi
col_logo, col_user = st.columns([3, 1])
with col_logo:
    st.title("**docaja**")
    st.caption("Solusi Kesehatan Terintegrasi & Informasi Obat")

with col_user:
    st.markdown("👤 **Pasien:** User")
    st.caption("📍 Jakarta, ID")

st.markdown("---")

# ==============================================================================
# Halaman 1: MENCARI OBAT
# ==============================================================================
if st.session_state["page"] == "mencari_obat":
    if st.button("⬅️ Kembali", key="back_obat"):
        st.session_state["page"] = "home"
        st.rerun()

    st.subheader("Mencari Obat")
    st.write("Ketikkan nama obat atau keluhan/penyakit yang ingin disembuhkan:")

    database_obat_lengkap = [
        {
            "nama": "Paracetamol 500mg",
            "kategori": "Demam & Nyeri / Flu",
            "dosis": "3x1 tablet sesudah makan",
            "kegunaan": "Meredakan demam, sakit kepala, dan nyeri ringan hingga sedang.",
        },
        {
            "nama": "Ibuprofen 400mg",
            "kategori": "Nyeri & Peradangan / Migrain",
            "dosis": "3x1 tablet sesudah makan",
            "kegunaan": "Mengurangi rasa sakit, pembengkakan, dan peradangan.",
        },
        {
            "nama": "Antasida Doen",
            "kategori": "Maag & Asam Lambung",
            "dosis": "3x1 tablet dikunyah sebelum makan",
            "kegunaan": "Menetralkan asam lambung berlebih dan meredakan nyeri ulu hati.",
        },
        {
            "nama": "Omeprazole 20mg",
            "kategori": "Maag Kronis / GERD",
            "dosis": "1x1 kapsul sebelum makan pagi",
            "kegunaan": "Mengurangi produksi asam lambung pada penderita GERD/Gastritis.",
        },
        {
            "nama": "Cetirizine 10mg",
            "kategori": "Alergi & Gatal",
            "dosis": "1x1 tablet sehari",
            "kegunaan": "Meredakan gejala alergi seperti bersin-bersin, gatal, dan bentol.",
        },
        {
            "nama": "Salbutamol Inhaler / 2mg",
            "kategori": "Sesak Napas / Asma",
            "dosis": "Sesuai petunjuk dokter / saat sesak",
            "kegunaan": "Membuka saluran pernapasan yang menyempit saat serangan asma.",
        },
        {
            "nama": "Ambroxol 30mg",
            "kategori": "Batuk Berdahak",
            "dosis": "3x1 tablet sesudah makan",
            "kegunaan": "Pengencer dahak agar lebih mudah dikeluarkan saat batuk.",
        },
        {
            "nama": "Oralit Garam Dehidrasi",
            "kategori": "Diare / Dehidrasi",
            "dosis": "Dilarutkan dalam 200ml air tiap habis BAB",
            "kegunaan": "Mencegah dan mengatasi dehidrasi akibat diare atau muntah.",
        },
    ]

    query = st.text_input(
        "🔍 Masukkan kata kunci (contoh: Paracetamol, Maag, Demam, Asma, Alergi):",
        "",
    )

    if query:
        hasil = [
            o
            for o in database_obat_lengkap
            if query.lower() in o["nama"].lower()
            or query.lower() in o["kategori"].lower()
            or query.lower() in o["kegunaan"].lower()
        ]

        if hasil:
            st.success(f"Ditemukan {len(hasil)} obat yang cocok:")
            for item in hasil:
                with st.container():
                    st.markdown(f"### 💊 **{item['nama']}**")
                    st.write(f"**Indikasi/Kategori:** {item['kategori']}")
                    st.write(f"**Aturan Dosis:** {item['dosis']}")
                    st.write(f"**Kegunaan:** {item['kegunaan']}")
                    st.markdown("---")
        else:
            st.error(
                f"Obat atau keluhan '{query}' tidak ditemukan. Coba gunakan kata kunci lain."
            )
    else:
        st.info("Ketikkan sesuatu di kolom pencarian di atas untuk memulai.")

# ==============================================================================
# Halaman 2: CARI RUMAH SAKIT
# ==============================================================================
elif st.session_state["page"] == "cari_rs":
    if st.button("⬅️ Kembali", key="back_rs"):
        st.session_state["page"] = "home"
        st.rerun()

    st.subheader("Daftar Rumah Sakit Terdekat & Populer")
    st.write(
        "Berikut adalah daftar rumah sakit yang siap melayani perawatan dan konsultasi medis:"
    )

    daftar_rs = [
        {
            "nama": "RSUPN Dr. Cipto Mangunkusumo (RSCM)",
            "kota": "Jakarta Pusat",
            "tipe": "Kelas A (Rujukan Nasional)",
            "layanan": "IGD 24 Jam, Bedah Saraf, Onkologi, Jantung",
        },
        {
            "nama": "RS Siloam Kebon Jeruk",
            "kota": "Jakarta Barat",
            "tipe": "Swasta Internasional",
            "layanan": "Pusat Jantung, Orthopedi, IGD 24 Jam",
        },
        {
            "nama": "RS Kanker Dharmais",
            "kota": "Jakarta Barat",
            "tipe": "Pusat Kanker Nasional",
            "layanan": "Kemoterapi, Radioterapi, Bedah Tumor",
        },
        {
            "nama": "RS Jantung dan Pembuluh Darah Harapan Kita",
            "kota": "Jakarta Barat",
            "tipe": "Pusat Jantung Nasional",
            "layanan": "Kardiologi Anak & Dewasa, Bedah Jantung",
        },
        {
            "nama": "RSUP Dr. Sardjito",
            "kota": "Yogyakarta",
            "tipe": "Kelas A",
            "layanan": "IGD 24 Jam, Transplantasi Organ, MOP",
        },
        {
            "nama": "RSUP Dr. Hasan Sadikin",
            "kota": "Bandung",
            "tipe": "Kelas A",
            "layanan": "Pusat Pelayanan Medis Terpadu & IGD",
        },
        {
            "nama": "RSUD Dr. Soetomo",
            "kota": "Surabaya",
            "tipe": "Kelas A",
            "layanan": "Trauma Center, IGD 24 Jam, Kedokteran Nuklir",
        },
        {
            "nama": "RS Hermina Kemayoran",
            "kota": "Jakarta Pusat",
            "tipe": "Spesialis Ibu & Anak",
            "layanan": "Poliklinik Kebidanan, NICU/PICU, Dokter Anak",
        },
        {
            "nama": "RS Pondok Indah",
            "kota": "Jakarta Selatan",
            "tipe": "Swasta Modern",
            "layanan": "Check-up Khusus, IVF, Minimally Invasive Surgery",
        },
        {
            "nama": "RSUP H. Adam Malik",
            "kota": "Medan",
            "tipe": "Kelas A",
            "layanan": "Pusat Rujukan Sumatera Utara",
        },
    ]

    for rs in daftar_rs:
        with st.container():
            st.markdown(f"🏥 **{rs['nama']}**")
            st.caption(f"📍 {rs['kota']} | Tipe: {rs['tipe']}")
            st.write(f"**Fasilitas Utama:** {rs['layanan']}")
            st.markdown("---")

# ==============================================================================
# Halaman 3: PEMERIKSAAN
# ==============================================================================
elif st.session_state["page"] == "pemeriksaan":
    if st.button("⬅️ Kembali", key="back_pem"):
        st.session_state["page"] = "home"
        st.rerun()

    st.subheader("Formulir Pemeriksaan Kesehatan Pasien")
    st.write("Silakan isi formulir data kondisi kesehatan Anda di bawah ini:")

    with st.form("form_pemeriksaan"):
        nama_penyakit = st.text_input(
            "Nama Penyakit / Keluhan Utama",
            placeholder="Contoh: Demam tinggi, Asam Lambung",
        )
        tipe_darah = st.selectbox("Tipe Darah", ["A", "B", "AB", "O"])
        usia = st.number_input(
            "Usia (Tahun)", min_value=1, max_value=120, value=25
        )
        gender = st.radio("Gender", ["Laki-laki", "Perempuan"], horizontal=True)
        kegiatan = st.text_area(
            "Kegiatan / Aktivitas Harian",
            placeholder="Contoh: Bekerja di depan komputer 8 jam, Olahraga ringan 2x seminggu",
        )
        nama_obat = st.text_input(
            "Nama Obat yang Sedang Dikonsumsi",
            placeholder="Contoh: Paracetamol, Omeprazole, Tidak ada",
        )
        jumlah_konsumsi = st.text_input(
            "Berapa banyak/sering obat tersebut dikonsumsi?",
            placeholder="Contoh: 2 kali sehari, 1 tablet",
        )

        submit_button = st.form_submit_button(
            "Kirim", type="primary", use_container_width=True
        )

    if submit_button:
        if not nama_penyakit or not kegiatan or not nama_obat:
            st.warning("Mohon lengkapi seluruh formulir sebelum mengirim.")
        else:
            kalimat_kesimpulan = (
                f"Berdasarkan analisis pemeriksaan, kondisi pasien berusia {usia} tahun dengan keluhan {nama_penyakit} "
                f"memerlukan evaluasi pola aktivitas '{kegiatan}' serta penyesuaian konsumsi obat {nama_obat} ({jumlah_konsumsi}) "
                f"guna mempercepat proses pemulihan kesehatan secara optimal."
            )
            st.success("✅ Formulir Berhasil Terkirim!")
            st.info(f"💡 **Ringkasan Kondisi:** {kalimat_kesimpulan}")

# ==============================================================================
# HALAMAN UTAMA (HOME)
# ==============================================================================
else:
    st.subheader("Layanan Utama")
    c1, c2, c3 = st.columns(3)

    # Hanya 3 kotak putih yang berfungsi langsung sebagai tombol utama
    with c1:
        if st.button("Mencari Obat", key="btn_obat"):
            st.session_state["page"] = "mencari_obat"
            st.rerun()

    with c2:
        if st.button("Cari Rumah Sakit", key="btn_rs"):
            st.session_state["page"] = "cari_rs"
            st.rerun()

    with c3:
        if st.button("Pemeriksaan", key="btn_pemeriksaan"):
            st.session_state["page"] = "pemeriksaan"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["💬 Informasi Keluhan", "👨‍⚕️ Pilih Spesialis"])

    database_medis = {
        "Flu & Batuk Pilek": {
            "kondisi": "Infeksi Saluran Pernapasan Atas (ISPA) / Flu",
            "kategori_obat": "Obat Bebas (OTC)",
            "saran": "Istirahat cukup, konsumsi air hangat, dan gunakan masker saat beraktivitas.",
        },
        "Maag & Nyeri Lambung": {
            "kondisi": "Gastritis / Dispepsia (Asam Lambung)",
            "kategori_obat": "Obat Bebas Terbatas",
            "saran": "Makan dengan porsi kecil tapi sering, hindari kopi dan pedas.",
        },
        "Sakit Kepala & Migrain": {
            "kondisi": "Tension Headache / Migrain Ringan",
            "kategori_obat": "Obat Bebas",
            "saran": "Kurangi waktu layar (screen time) dan istirahat di ruangan gelap.",
        },
    }

    with tab1:
        st.markdown("### 🔍 Informasi Singkat Keluhan")
        gejala_pilihan = st.selectbox(
            "Pilih keluhan untuk melihat penjelasan:",
            ["-- Pilih Keluhan --"] + list(database_medis.keys()),
        )

        if gejala_pilihan != "-- Pilih Keluhan --":
            data = database_medis[gejala_pilihan]
            st.write(f"**Indikasi:** {data['kondisi']}")
            st.write(f"**Kategori Obat:** {data['kategori_obat']}")
            st.info(f"**Catatan:** {data['saran']}")

    with tab2:
        st.markdown("### 👨‍⚕️ Dokter Terdekat yang Tersedia")
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
            st.button(f"Konsultasi dengan {doc['nama']}", key=doc["nama"])
            st.markdown("---")