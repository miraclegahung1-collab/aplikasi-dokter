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

if "nama_pasien" not in st.session_state:
    st.session_state["nama_pasien"] = "User"

if "alamat_pasien" not in st.session_state:
    st.session_state["alamat_pasien"] = "Jakarta, ID"

# 2. Header Aplikasi (Nama & Alamat Pasien Bisa Diubah)
col_logo, col_user = st.columns([2, 2])
with col_logo:
    st.title("**docaja**")
    st.caption("Solusi Kesehatan Terintegrasi & Informasi Obat")

with col_user:
    st.session_state["nama_pasien"] = st.text_input(
        "👤 Nama Pasien:", value=st.session_state["nama_pasien"]
    )
    st.session_state["alamat_pasien"] = st.text_input(
        "📍 Alamat Pasien:", value=st.session_state["alamat_pasien"]
    )

st.markdown("---")

# ==============================================================================
# Halaman 1: MENCARI OBAT
# ==============================================================================
if st.session_state["page"] == "mencari_obat":
    if st.button("Kembali", key="back_obat"):
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
            "nama": "Metformin 500mg",
            "kategori": "Diabetes / Penurun Gula Darah",
            "dosis": "2x1 tablet sesudah makan",
            "kegunaan": "Mengontrol dan menurunkan kadar gula darah pada pasien diabetes tipe 2.",
        },
        {
            "nama": "Captopril 25mg",
            "kategori": "Tekanan Darah Tinggi / Jantung",
            "dosis": "2-3x1 tablet sehari sebelum makan",
            "kegunaan": "Menurunkan tekanan darah tinggi serta membantu melindungi fungsi jantung pasca-serangan.",
        },
        {
            "nama": "Loperamide 2mg",
            "kategori": "Diare",
            "dosis": "2 tablet saat awal diare, lalu 1 tablet tiap BAB cair (maksimal 12mg/hari)",
            "kegunaan": "Memperlambat gerak usus untuk meredakan frekuensi buang air besar saat diare akut.",
        },
        {
            "nama": "Domperidone 10mg",
            "kategori": "Mual & Muntah / Lambung",
            "dosis": "3x1 tablet sebelum makan",
            "kegunaan": "Meredakan rasa mual, muntah, serta keluhan perut kembung akibat perlambatan pencernaan.",
        },
        {
            "nama": "Acyclovir 400mg",
            "kategori": "Antivirus / Infeksi Kulit",
            "dosis": "5x1 tablet sehari selama 5-7 hari",
            "kegunaan": "Mengatasi infeksi virus seperti herpes simpleks, cacar air, dan herpes zoster.",
        },
        {
            "nama": "Salep Hydrocortisone 2.5%",
            "kategori": "Krim Alergi & Radang Kulit",
            "dosis": "2-3 kali sehari dioleskan tipis pada bagian kulit yang meradang",
            "kegunaan": "Mengurangi peradangan, kemerahan, dan rasa gatal akibat dermatitis atau eksim.",
        },
        {
            "nama": "Mefenamic Acid 500mg",
            "kategori": "Pereda Nyeri Haid & Sakit Gigi",
            "dosis": "3x1 tablet sesudah makan (maksimal 7 hari)",
            "kegunaan": "Meredakan nyeri haid (dismenore), sakit gigi, serta nyeri otot atau sendi.",
        },
        {
            "nama": "Dextromethorphan HBr 15mg",
            "kategori": "Batuk Tidak Berdahak",
            "dosis": "3x1 tablet sehari",
            "kegunaan": "Menekan dorongan batuk di pusat saraf untuk meredakan batuk kering.",
        },
        {
            "nama": "Asam Folat 1mg",
            "kategori": "Vitamin Kehamilan & Sel Darah",
            "dosis": "1x1 tablet sehari",
            "kegunaan": "Mencegah cacat tabung saraf pada janin serta membantu pembentukan sel darah merah.",
        },
        {
            "nama": "Vitamin B12 (Cyanocobalamin 50 mcg)",
            "kategori": "Vitamin Saraf & Anemia",
            "dosis": "1x1 tablet sehari sesudah makan",
            "kegunaan": "Mencegah anemia pernisiosa, memperbaiki kerusakan sel saraf, dan menambah energi.",
        },
        {
            "nama": "Zink (Zinc Sulfate 20mg)",
            "kategori": "Vitamin Imunitas & Pemulihan Diare",
            "dosis": "1x1 tablet sehari selama 10 hari (terutama untuk diare anak)",
            "kegunaan": "Mempercepat penyembuhan diare dan mengoptimalkan fungsi sistem kekebalan tubuh.",
        },
        {
            "nama": "Minyak Ikan / Fish Oil (Omega-3 1000mg)",
            "kategori": "Vitamin Jantung & Otak",
            "dosis": "1x1 kapsul lunak sehari sesudah makan",
            "kegunaan": "Menjaga kesehatan jantung, menurunkan kadar trigliserida, serta mendukung fungsi kognitif otak.",
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
        {
            "nama": "Amoxicillin 500mg",
            "kategori": "Antibiotik",
            "dosis": "3x1 kapsul habiskan sesuai resep dokter",
            "kegunaan": "Mengatasi infeksi bakteri pada saluran pernapasan, gigi, dan THT.",
        },
        {
            "nama": "Glimepiride 2mg",
            "kategori": "Diabetes / Gula Darah",
            "dosis": "1x1 tablet sebelum sarapan pagi",
            "kegunaan": "Menurunkan kadar gula darah pada pasien diabetes melitus tipe 2.",
        },
        {
            "nama": "Amlodipine 10mg",
            "kategori": "Tekanan Darah Tinggi / Hipertensi",
            "dosis": "1x1 tablet sehari",
            "kegunaan": "Menurunkan tekanan darah dan melonggarkan pembuluh darah.",
        },
        {
            "nama": "Simvastatin 20mg",
            "kategori": "Kolesterol",
            "dosis": "1x1 tablet malam hari sebelum tidur",
            "kegunaan": "Menurunkan kadar kolesterol jahat (LDL) dan trigliserida dalam darah.",
        },
        {
            "nama": "Vitamin C 1000mg",
            "kategori": "Vitamin & Imunitas",
            "dosis": "1x1 tablet sehari sesudah makan",
            "kegunaan": "Meningkatkan daya tahan tubuh dan menangkal radikal bebas.",
        },
        {
            "nama": "Vitamin D3 1000 IU",
            "kategori": "Vitamin Tulang & Imun",
            "dosis": "1x1 kapsul sehari sesudah makan",
            "kegunaan": "Membantu penyerapan kalsium untuk kesehatan tulang dan menjaga imun.",
        },
        {
            "nama": "Vitamin B Complex",
            "kategori": "Vitamin Saraf & Stamina",
            "dosis": "1x1 tablet sehari",
            "kegunaan": "Menjaga kesehatan sistem saraf, mencegah kelelahan, dan memelihara metabolisme.",
        },
        {
            "nama": "Suplemen Multivitamin + Mineral (Enervon-C / Becefort)",
            "kategori": "Vitamin Pemulihan",
            "dosis": "1x1 tablet sehari",
            "kegunaan": "Mempercepat pemulihan tubuh setelah sakit dan mencukupi kebutuhan vitamin harian.",
        },
        {
            "nama": "Kalsium (Calcium Laktat / Osteocare)",
            "kategori": "Vitamin & Suplemen Tulang",
            "dosis": "1-2 kali sehari sesudah makan",
            "kegunaan": "Mencegah osteoporosis dan menjaga kekuatan tulang serta gigi.",
        },
        {
            "nama": "Vitamin E 400 IU",
            "kategori": "Vitamin Kulit & Antioksidan",
            "dosis": "1x1 kapsul lunak sehari",
            "kegunaan": "Menjaga kesehatan kulit, kelembapan sel, serta sebagai antioksidan kuat.",
        },
    ]

    query = st.text_input(
        "Masukkan kata kunci (contoh: Paracetamol, Maag, Demam, Asma, Alergi):",
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
                    st.markdown(f"### **{item['nama']}**")
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
# Halaman 2: CARI RUMAH SAKIT (Disesuaikan dengan Fitur Pencarian, Alamat & Jam Buka)
# ==============================================================================
elif st.session_state["page"] == "cari_rs":
    if st.button("Kembali", key="back_rs"):
        st.session_state["page"] = "home"
        st.rerun()

    st.subheader("Pencarian Rumah Sakit")
    st.write("Ketikkan nama rumah sakit yang ingin dicari:")

    database_rs_lengkap = [
        {
            "nama": "RSUPN Dr. Cipto Mangunkusumo (RSCM)",
            "alamat": "Jl. Pangeran Diponegoro No.71, Kenari, Kec. Senen, Kota Jakarta Pusat",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Jumat (08:00 - 15:00)",
            "kota": "Jakarta Pusat",
            "tipe": "Kelas A (Rujukan Nasional)",
            "layanan": "IGD 24 Jam, Bedah Saraf, Onkologi, Jantung",
        },
        {
            "nama": "RS Advent Manado (RSAM)",
            "alamat": "Jl. Teling Atas, Kec. Wanea, kota Manado, Sulawesi Utara",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Jumat (08:00 - 15:00)",
            "kota": "Manado",
            "tipe": "Swasta",
            "layanan": "IGD 24 Jam, Poli Umum, Bedah, Anak",
        },
        {
            "nama": "RS Pancaran Kasih (RSPK)",
            "alamat": "Jl. Sam Ratulangi, Titiwungan Utara, Kec. Sario, Kota Manado, Sulawesi Utara",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Sabtu (08:00 - 20:00)",
            "kota": "Manado",
            "tipe": "Swasta",
            "layanan": "IGD 24 Jam, Kebidanan, Penyakit Dalam",
        },
        {
            "nama": "RS Kanker Dharmais",
            "alamat": "Jl. Letjen S. Parman Kav. 84-86, Slipi, Kec. Palmerah, Kota Jakarta Barat",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Jumat (08:00 - 16:00)",
            "kota": "Jakarta Barat",
            "tipe": "Pusat Kanker Nasional",
            "layanan": "Kemoterapi, Radioterapi, Bedah Tumor",
        },
        {
            "nama": "RS Siloam Kebon Jeruk",
            "alamat": "Jl. Raya Perjuangan No.8, Kebon Jeruk, Kota Jakarta Barat",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Sabtu (08:00 - 20:00)",
            "kota": "Jakarta Barat",
            "tipe": "Swasta Internasional",
            "layanan": "Pusat Jantung, Orthopedi, IGD 24 Jam",
        },
        {
            "nama": "RS Jantung dan Pembuluh Darah Harapan Kita",
            "alamat": "Jl. Letjen S. Parman, Palmerah, Kota Jakarta Barat",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Jumat (07:30 - 15:30)",
            "kota": "Jakarta Barat",
            "tipe": "Pusat Jantung Nasional",
            "layanan": "Kardiologi Anak & Dewasa, Bedah Jantung",
        },
{
            "nama": "RSUP Dr. Sardjito",
            "alamat": "Jl. Kesehatan No.1, Sendowo, Sinduadi, Kec. Mlati, Kabupaten Sleman, Yogyakarta",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Jumat (08:00 - 14:00)",
            "kota": "Yogyakarta",
            "tipe": "Kelas A",
            "layanan": "IGD 24 Jam, Transplantasi Organ, MOP",
        },
        {
            "nama": "RSUP Dr. Hasan Sadikin",
            "alamat": "Jl. Pasteur No.38, Pasteur, Kec. Sukajadi, Kota Bandung",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Jumat (08:00 - 15:00)",
            "kota": "Bandung",
            "tipe": "Kelas A",
            "layanan": "Pusat Pelayanan Medis Terpadu & IGD",
        },
        {
            "nama": "RSUD Dr. Soetomo",
            "alamat": "Jl. Mayjen Prof. Dr. Moestopo No.6-8, Airlangga, Kec. Gubeng, Kota Surabaya",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Jumat (08:00 - 14:00)",
            "kota": "Surabaya",
            "tipe": "Kelas A",
            "layanan": "Trauma Center, IGD 24 Jam, Kedokteran Nuklir",
        },
        {
            "nama": "RS Hermina Kemayoran",
            "alamat": "Jl. Selang Srengseng No.3, Kemayoran, Kota Jakarta Pusat",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Setiap Hari (08:00 - 21:00)",
            "kota": "Jakarta Pusat",
            "tipe": "Spesialis Ibu & Anak",
            "layanan": "Poliklinik Kebidanan, NICU/PICU, Dokter Anak",
        },
        {
            "nama": "RS Pondok Indah",
            "alamat": "Jl. Metro Duta Kav. UE, Pondok Indah, Kebayoran Lama, Jakarta Selatan",
            "jam_buka": "IGD: 24 Jam | Poliklinik: Senin - Sabtu (08:00 - 20:00)",
            "kota": "Jakarta Selatan",
            "tipe": "Swasta Modern",
            "layanan": "Check-up Khusus, IVF, Minimally Invasive Surgery",
        },
    ]

    query_rs = st.text_input(
        "🔍 Masukkan nama rumah sakit atau kota (contoh: RSCM, Siloam, Yogyakarta):",
        "",
    )

    if query_rs:
        hasil_rs = [
            r
            for r in database_rs_lengkap
            if query_rs.lower() in r["nama"].lower()
            or query_rs.lower() in r["kota"].lower()
            or query_rs.lower() in r["layanan"].lower()
        ]

        if hasil_rs:
            st.success(f"Ditemukan {len(hasil_rs)} rumah sakit yang cocok:")
            for rs in hasil_rs:
                with st.container():
                    st.markdown(f"### 🏥 **{rs['nama']}**")
                    st.write(f"📍 **Alamat:** {rs['alamat']}")
                    st.write(f"⏰ **Jam Buka:** {rs['jam_buka']}")
                    st.caption(f"Kota: {rs['kota']} | Tipe: {rs['tipe']}")
                    st.write(f"**Fasilitas Utama:** {rs['layanan']}")
                    st.markdown("---")
        else:
            st.error(
                f"Rumah sakit dengan kata kunci '{query_rs}' tidak ditemukan."
            )
    else:
        st.info("Ketikkan nama rumah sakit atau kota di kolom pencarian di atas untuk mulai mencari.")

# ==============================================================================
# Halaman 3: PEMERIKSAAN
# ==============================================================================
elif st.session_state["page"] == "pemeriksaan":
    if st.button("Kembali", key="back_pem"):
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
            st.info(f"**Ringkasan Kondisi:** {kalimat_kesimpulan}")


# ==============================================================================
# HALAMAN UTAMA (HOME)
# ==============================================================================
else:
    # Inisialisasi state untuk navigasi sub-halaman Layanan Kesehatan
    if "sub_page" not in st.session_state:
        st.session_state["sub_page"] = "menu_utama"

    # ==========================================================================
    # 1. LAYAR KHUSUS: PANDUAN PENCEGAHAN
    # ==========================================================================
    if st.session_state["sub_page"] == "panduan_pencegahan":
        if st.button("Kembali", key="back_pencegahan"):
            st.session_state["sub_page"] = "menu_utama"
            st.rerun()

        st.subheader("Panduan Pencegahan Penyakit")
        st.write("Ketikkan nama penyakit yang ingin Anda hindari untuk melihat langkah-langkah pencegahannya secara lengkap:")
        
        query_cegah = st.text_input("Ketik nama penyakit (contoh: Tifus, DBD, Hipertensi, Diabetes):", "")

        database_pencegahan = {
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

        "Demam Berdarah (DBD)": {

            "kondisi": "Infeksi virus Dengue melalui gigitan nyamuk Aedes aegypti",

            "kategori_obat": "Penurun Panas & Suplemen (Pengawasan Medis Ketat)",

            "saran": "Perbanyak minum air putih untuk cegah dehidrasi, cek trombosit berkala, dan segera ke rumah sakit jika muncul tanda bahaya.",

        },

        "Tifus / Demam Tifoid": {

            "kondisi": "Infeksi bakteri Salmonella enterica pada saluran pencernaan",

            "kategori_obat": "Antibiotik Resep Dokter & Vitamin",

            "saran": "Konsumsi makanan lunak/bubur yang tidak pedas dan asam, istirahat total total di tempat tidur.",

        },

        "Hipertensi / Tekanan Darah Tinggi": {

            "kondisi": "Tekanan darah di atas normal (>140/90 mmHg)",

            "kategori_obat": "Obat Antihipertensi Resep Dokter",

            "saran": "Kurangi konsumsi garam/natrium, hindari stres, rutin olahraga ringan, dan cek tensi berkala.",

        },

        "Diabetes / Gula Darah Tinggi": {

            "kondisi": "Gangguan metabolisme tubuh dalam memproses glukosa darah",

            "kategori_obat": "Obat Antidiabetes / Insulin (Resep Dokter)",

            "saran": "Batasi makanan/minuman manis, perbanyak serat, dan kontrol kadar gula darah rutin.",

        },

        "Kolesterol Tinggi": {

            "kondisi": "Kadar lemak jahat (LDL) melebihi batas normal dalam darah",

            "kategori_obat": "Golongan Statin / Suplemen Omega-3",

            "saran": "Hindari makanan berlemak jenuh/gorengan, perbanyak konsumsi sayur, buah, dan oat.",

        },

        "Diare & Keracunan Makanan": {

            "kondisi": "Infeksi saluran pencernaan akibat bakteri atau makanan tidak higienis",

            "kategori_obat": "Oralit, Zink, & Anti-diare",

            "saran": "Minum larutan oralit setiap selesai BAB cair, konsumsi makanan netral seperti pisang atau roti tawar.",

        },

        "Sembelit / Konstipasi": {

            "kondisi": "Susah buang air besar atau feses terlalu keras",

            "kategori_obat": "Laksatif / Pencahar Ringan",

            "saran": "Perbanyak minum air putih minimal 2 liter per hari, makan makanan berserat tinggi, dan aktif bergerak.",

        },

        "Alergi Kulit & Biduran (Kaligata)": {

            "kondisi": "Reaksi alergi terhadap makanan, cuaca dingin, atau obat tertentu",

            "kategori_obat": "Antihistamin (Cetirizine / Loratadine)",

            "saran": "Hindari pemicu alergi, kompres dingin pada area yang gatal, dan jangan digaruk agar tidak infeksi.",

        },

        "Cacar Air": {

            "kondisi": "Infeksi virus Varicella-zoster yang menimbulkan bintil berair",

            "kategori_obat": "Antivirus, Bedak Salicyl / Oles Soothing, & Penurun Panas",

            "saran": "Jangan memecahkan bintil air agar tidak meninggalkan bekas luka, istirahat di rumah agar tidak menular.",

        },

        "Asma & Sesak Napas": {

            "kondisi": "Penyempitan saluran pernapasan akibat reaksi alergi atau udara dingin",

            "kategori_obat": "Inhaler Bronkodilator / Salbutamol",

            "saran": "Duduk tegak, atur napas perlahan, hindari paparan debu, bulu hewan, atau asap rokok.",

        },

        "Insomnia / Susah Tidur": {

            "kondisi": "Gangguan tidur yang menyebabkan sulit memula atau mempertahankan tidur",

            "kategori_obat": "Suplemen Herbal / Melatonin",

            "saran": "Batasi penggunaan gadget sebelum tidur, buat kamar senyaman dan sedingin mungkin, hindari kafein di sore hari.",

        },

        "Anemia / Kurang Darah": {

            "kondisi": "Kekurangan sel darah merah atau hemoglobin dalam tubuh",

            "kategori_obat": "Suplemen Penambah Darah (Fe) & Vitamin B12",

            "saran": "Konsumsi makanan tinggi zat besi seperti bayam, hati, daging merah, dan buah kaya Vitamin C.",

        },

        "Sakit Gigi & Gusi Bengkak": {

            "kondisi": "Peradangan pada saraf gigi atau jaringan pendukung gigi",

            "kategori_obat": "Pereda Nyeri (Ibuprofen / Asam Mefenamat)",

            "saran": "Kumur dengan air hangat yang dicampur garam, kompres dingin pipi bagian luar, segera ke dokter gigi.",

        },

        "Nyeri Sendi & Asam Urat": {

            "kondisi": "Penumpukan kristal asam urat pada persendian yang memicu radang",

            "kategori_obat": "Allopurinol & Pereda Nyeri Sendi",

            "saran": "Kurangi makanan tinggi purin (jeroan, melinjo, seafood), perbanyak minum air putih.",

        },

        "Vertigo & Sakit Kepala Berputar": {

            "kondisi": "Sensasi lingkungan terasa berputar yang bersumber dari gangguan keseimbangan",

            "kategori_obat": "Obat Antivertigo (Betahistine)",

            "saran": "Segera duduk atau berbaring di tempat datar saat serangan datang, hindari gerakan kepala mendadak.",

        },

        "Sariawan & Panas Dalam": {

            "kondisi": "Luka kecil di dalam mulut akibat gesekan, kekurangan vitamin, atau stres",

            "kategori_obat": "Aloclair / Larutan Penyegar / Vitamin C",

            "saran": "Perbanyak buah yang mengandung vitamin C, hindari makanan pedas dan panas sementara waktu.",

        },

        "Sinusitis": {

            "kondisi": "Peradangan pada dinding sinus di sekitar rongga hidung",

            "kategori_obat": "Dekongestan & Spray Hidung Saline",

            "saran": "Hirup uap air hangat, gunakan humidifier di ruangan, istirahat cukup.",

        },

        "Infeksi Saluran Kemih (ISK)": {

            "kondisi": "Infeksi bakteri pada bagian saluran kemih yang memicu nyeri saat buang air kecil",

            "kategori_obat": "Antibiotik Resep Dokter & Pereda Nyeri",

            "saran": "Jangan menahan buang air kecil, perbanyak minum air putih, jaga kebersihan area intim.",

        },

        "Mata Merah & Iritasi (Konjungtivitis)": {

            "kondisi": "Peradangan pada selaput konjungtiva mata akibat debu atau infeksi",

            "kategori_obat": "Tetes Mata Antibiotik / Air Mata Buatan",

            "saran": "Jangan mengucek mata, hindari penggunaan lensa kontak sementara, cuci tangan secara rutin.",

        },

        "Radang Tenggorokan / Faringitis": {

            "kondisi": "Infeksi atau iritasi pada tenggorokan yang membuat sakit saat menelan",

            "kategori_obat": "Lozenge (Permen Tenggorokan) & Antiinflamasi",

            "saran": "Perbanyak minum air hangat, kumur air garam, hindari makanan berminyak atau es.",

        },

        "Kram Otot & Kelelahan Fisik": {

            "kondisi": "Kontraksi otot yang datang tiba-tiba dan terasa nyeri akibat kelelahan atau dehidrasi",

            "kategori_obat": "Suplemen Magnesium & Kalium",

            "saran": "Lakukan peregangan otot perlahan, kompres hangat pada area kram, istirahat cukup.",

        },

        "Eksim / Dermatitis": {

            "kondisi": "Kondisi kulit meradang, kemerahan, kering, dan sangat gatal",

            "kategori_obat": "Salep Kortikosteroid Ringan / Pelembap Khusus",

            "saran": "Gunakan sabun mandi yang hipoalergenik, oleskan pelembap rutin setelah mandi.",

        },

        "Rinitis Alergi (Flu Alergi)": {

            "kondisi": "Reaksi hidung bersin-bersin dan berair akibat paparan debu, bulu, atau serbuk",

            "kategori_obat": "Antihistamin Oral",

            "saran": "Bersihkan rumah secara berkala dari debu karpet, gunakan masker saat membersihkan ruangan.",

        },

        "Batu Ginjal / Nyeri Pinggang": {

            "kondisi": "Endapan mineral keras yang terbentuk di dalam ginjal",

            "kategori_obat": "Pereda Nyeri & Peluruh Batu Ginjal Herbal/Medis",

            "saran": "Minum air putih dalam jumlah sangat banyak (2.5 - 3 liter sehari) untuk membantu melunturkan.",

        },

        "Kecemasan / Anxiety Ringan": {

            "kondisi": "Rasa khawatir berlebihan yang memicu jantung berdebar dan sesak napas ringan",

            "kategori_obat": "Vitamin Penenang Saraf / Suplemen Relaksasi",

            "saran": "Lakukan teknik pernapasan diafragma (tarik napas dalam dari hidung, buang perlahan dari mulut), meditasi.",

        },

        "Pneumonia / Paru-Paru Basah": {

            "kondisi": "Infeksi serius yang menginflamasi kantung udara di salah satu atau kedua paru-paru",

            "kategori_obat": "Antibiotik Kuat & Obat Batuk Resep Dokter",

            "saran": "Istirahat total di tempat tidur, perbanyak asupan cairan hangat, dan segera lakukan rontgen dada atau kontrol dokter.",

        },

        "Bronkitis Akut": {

            "kondisi": "Peradangan pada saluran bronkus yang membawa udara ke paru-paru",

            "kategori_obat": "Pengencer Dahak & Bronkodilator",

            "saran": "Hindari paparan asap rokok dan polusi udara, gunakan pelembap udara (humidifier) di kamar.",

        },

        "Gerd / Asam Lambung Naik": {

            "kondisi": "Naiknya asam lambung ke kerongkongan yang memicu rasa terbakar di dada (heartburn)",

            "kategori_obat": "Antasida & Penghambat Pompa Proton (Omeprazole/Lansoprazole)",

            "saran": "Jangan langsung berbaring setelah makan (beri jeda 2-3 jam), hindari makanan berlemak dan asam.",

        },

        "Hepatitis A / Radang Hati": {

            "kondisi": "Infeksi virus yang menyerang organ hati melalui makanan atau air yang terkontaminasi",

            "kategori_obat": "Suplemen Pelindung Hati & Penurun Panas",

            "saran": "Istirahat total, hindari makanan berlemak tinggi, dan pisahkan alat makan agar tidak menular.",

        },

        "Batu Empedu": {

            "kondisi": "Terbentuknya cairan pencernaan yang mengeras di dalam kantung empedu",

            "kategori_obat": "Pereda Nyeri Kolik & Pelarut Batu Empedu (Pengawasan Dokter)",

            "saran": "Batasi makanan tinggi kolesterol dan lemak hewani, serta makan dalam porsi kecil tapi sering.",

        },

        "Gagal Ginjal Kronis": {

            "kondisi": "Penurunan fungsi ginjal secara bertahap dalam menyaring limbah darah",

            "kategori_obat": "Obat Pengontrol Tekanan Darah & Suplemen Khusus Ginjal",

            "saran": "Batasi konsumsi protein, garam, kalium, dan cairan sesuai anjuran dokter spesialis ginjal.",

        },

        "Glaukoma": {

            "kondisi": "Peningkatan tekanan bola mata yang dapat merusak saraf optik",

            "kategori_obat": "Tetes Mata Khusus Penurun Tekanan Intraokular (Resep Dokter)",

            "saran": "Hindari posisi kepala lebih rendah dari tubuh dalam waktu lama, dan lakukan pemeriksaan mata rutin.",

        },

        "Katarak": {

            "kondisi": "Kekeruhan pada lensa mata yang membuat penglihatan menjadi kabur",

            "kategori_obat": "Tetes Mata Vitamin Mata (Hanya untuk Gejala Awal)",

            "saran": "Gunakan kacamata hitam saat di luar ruangan untuk melindungi mata dari sinar UV matahari.",

        },

        "Otitis Media / Infeksi Telinga Tengah": {

            "kondisi": "Infeksi bakteri atau virus pada ruang di belakang gendang telinga",

            "kategori_obat": "Tetes Telinga Antibiotik & Pereda Nyeri",

            "saran": "Jaga agar telinga tidak kemasukan air saat mandi, hindari membersihkan telinga menggunakan cotton bud terlalu dalam.",

        },

        "Tonsilitis / Radang Amandel": {

            "kondisi": "Peradangan pada kelenjar amandel di tenggorokan akibat infeksi",

            "kategori_obat": "Pereda Nyeri & Antibiotik (Jika Disebabkan Bakteri)",

            "saran": "Kumur dengan air hangat bergaram, konsumsi makanan yang lembut dan dingin untuk mengurangi nyeri telan.",

        },

        "Gout / Serangan Asam Urat Akut": {

            "kondisi": "Nyeri sendi parah secara mendadak akibat kristal asam urat",

            "kategori_obat": "Colchicine & Obat Antiinflamasi Nonsteroid (NSAID)",

            "saran": "Kompres dingin pada sendi yang meradang, istirahatkan kaki atau tangan, dan perbanyak minum air putih.",

        },

        "Osteoporosis": {

            "kondisi": "Penyakit tulang yang membuat tulang rapuh dan mudah patah",

            "kategori_obat": "Suplemen Kalsium Tinggi & Vitamin D3",

            "saran": "Lakukan olahraga beban ringan secara teratur, berjemur di pagi hari, dan hindari merokok.",

        },

        "Carpal Tunnel Syndrome (CTS)": {

            "kondisi": "Tekanan pada saraf median di pergelangan tangan yang memicu kesemutan dan nyeri",

            "kategori_obat": "Vitamin B1 & Pereda Nyeri Antiinflamasi",

            "saran": "Istirahatkan tangan secara berkala jika sering mengetik, lakukan peregangan pergelangan tangan.",

        },

        "Bell's Palsy": {

            "kondisi": "Kelemahan atau kelumpuhan sementara pada salah satu sisi otot wajah",

            "kategori_obat": "Kortikosteroid Oral & Vitamin Saraf (B1, B6, B12)",

            "saran": "Lindungi mata yang sakit dengan penutup atau kacamata saat tidur karena kelopak mata sulit menutup sempurna.",

        },

        "Stroke Ringan / TIA": {

            "kondisi": "Gangguan pasokan darah sementara ke bagian otak",

            "kategori_obat": "Pengencer Darah & Obat Pengontrol Tekanan Darah",

            "saran": "Segera bawa ke instalasi gawat darurat (IGD) rumah sakit terdekat jika merasakan kebas mendadak atau bicara pelo.",

        },

        "Penyakit Jantung Koroner": {

            "kondisi": "Penyempitan atau penyumbatan pembuluh darah arteri koroner jantung",

            "kategori_obat": "Aspirin, Statin, & Nitrat (Berdasarkan Resep Dokter)",

            "saran": "Hindari aktivitas fisik yang terlalu berat secara mendadak, kelola stres dengan baik, dan jaga pola makan.",

        },

        "Aritmia / Jantung Berdebar": {

            "kondisi": "Gangguan irama detak jantung (terlalu cepat atau terlalu lambat)",

            "kategori_obat": "Anti-aritmia (Resep Dokter Spesialis Jantung)",

            "saran": "Kurangi konsumsi kafein, hindari minuman beralkohol, dan istirahat cukup saat dada terasa berdebar.",

        },

        "Varises": {

            "kondisi": "Pembengkakan dan pelebaran pembuluh darah vena, biasanya di kaki",

            "kategori_obat": "Salep/Krim Penguat Vena & Kaki Penyangga (Stoking Kompresi)",

            "saran": "Hindari berdiri atau duduk terlalu lama, posisikan kaki lebih tinggi saat berbaring.",

        },

        "Hemoroid / Ambeien": {

            "kondisi": "Pembengkakan pembuluh darah di sekitar rektum atau anus",

            "kategori_obat": "Salep Ambeien Topikal & Pelunak Feses",

            "saran": "Perbanyak makan makanan berserat tinggi, jangan mengejan terlalu kuat saat BAB, dan mandi air hangat.",

        },

        "Malaria": {

            "kondisi": "Penyakit infeksi parasit yang ditularkan melalui gigitan nyamuk Anopheles",

            "kategori_obat": "Obat Antimalaria Khusus (Kombinasi Resep Dokter)",

            "saran": "Gunakan kelambu saat tidur di daerah endemis, pakai losion anti nyamuk, dan tuntaskan obat sampai habis.",

        },

        "Chikungunya": {

            "kondisi": "Infeksi virus yang menyebabkan demam tinggi dan nyeri sendi hebat",

            "kategori_obat": "Pereda Nyeri & Penurun Panas (Paracetamol)",

            "saran": "Istirahat total karena nyeri sendi bisa bertahan lama, perbanyak konsumsi cairan bergizi.",

        },

        "Kurap / Infeksi Jamur Kulit (Tinea)": {

            "kondisi": "Infeksi jamur pada lapisan kulit luar yang membentuk lingkaran merah gatal",

            "kategori_obat": "Salep Antijamur Topikal (Ketoconazole / Miconazole)",

            "saran": "Jaga kulit tetap kering dan bersih, jangan berbagi handuk atau pakaian dengan orang lain.",

        },

        "Kutu Air (Tinea Pedis)": {

            "kondisi": "Infeksi jamur pada sela-sela jari kaki",

            "kategori_obat": "Krim Antijamur & Bedak Tabur Antiseptik",

            "saran": "Cuci kaki bersih lalu keringkan sela-sela jari setiap selesai beraktivitas, gunakan kaus kaki bersih.",

        },

        "Ketombe & Dermatitis Seboroik": {

            "kondisi": "Peradangan kulit kepala yang menyebabkan kulit mengelupas dan bersisik",

            "kategori_obat": "Shampo Ketokonazol atau Selenium Sulfida",

            "saran": "Gunakan shampo khusus anti-ketombe 2-3 kali seminggu, bilas rambut hingga bersih sempurna.",

        },

        "Jerawat Parah (Acne Vulgaris)": {

            "kondisi": "Penyumbatan kelenjar minyak kulit oleh sel kulit mati dan bakteri",

            "kategori_obat": "Krim Benzoyl Peroxide / Asam Salisilat / Retinoid",

            "saran": "Jangan memencet jerawat dengan tangan kotor agar tidak bernanah dan meninggalkan bopeng.",

        },

        "Rosacea": {

            "kondisi": "Penyakit kulit kronis yang menyebabkan kemerahan dan pembuluh darah terlihat di wajah",

            "kategori_obat": "Gel/Krim Antiinflamasi Khusus Wajah",

            "saran": "Gunakan tabir surya setiap hari, hindari makanan pedas dan minuman panas yang memicu kemerahan.",

        },

        "Batu Empedu / Kolik Biliar": {

            "kondisi": "Nyeri perut kanan atas akibat sumbatan saluran empedu",

            "kategori_obat": "Antispasmodik & Pereda Nyeri Perut",

            "saran": "Hindari konsumsi makanan bersantan kental dan berlemak tinggi secara berlebihan.",

        },

        "Gastritis Kronis": {

            "kondisi": "Peradangan dinding lambung jangka panjang",

            "kategori_obat": "Antasida & Penurun Asam Lambung Rutin",

            "saran": "Makan tepat waktu, hindari stres berlebih, serta jauhi makanan pedas, asam, dan bersoda.",

        },

        "Kista Ovarium": {

            "kondisi": "Kantong berisi cairan yang terbentuk di dalam atau di permukaan indung telur",

            "kategori_obat": "Analgesik & Terapi Hormon (Sesuai Resep Dokter Obgyn)",

            "saran": "Lakukan pemeriksaan USG panggul secara berkala jika mengalami nyeri perut bawah yang konsisten.",

        },

        "Miom / Uterine Fibroids": {

            "kondisi": "Tumor jinak yang tumbuh di dalam atau di dinding rahim",

            "kategori_obat": "Obat Pengontrol Nyeri Haid & Penyeimbang Hormon",

            "saran": "Perbanyak konsumsi sayuran hijau dan buah segar, batasi daging merah berlebih.",

        },

    }

        if query_cegah:
            keyword = query_cegah.lower().strip()
            ditemukan_cegah = False
            for kunci, langkah_langkah in database_pencegahan.items():
                if kunci in keyword:
                    st.success(f"Panduan Pencegahan yang sesuai untuk: **{query_cegah.capitalize()}**")
                    for langkah in langkah_langkah:
                        st.write(langkah)
                    ditemukan_cegah = True
                    break
            
            if not ditemukan_cegah:
                st.warning(f"Panduan spesifik untuk '{query_cegah}' belum tersedia di database.")
                st.info(
                    f"**Langkah Pencegahan Umum untuk '{query_cegah}':**\n"
                    "1. Jaga kebersihan diri dan lingkungan sekitar secara konsisten.\n"
                    "2. Konsumsi makanan bergizi seimbang untuk memperkuat sistem kekebalan tubuh.\n"
                    "3. Cukupi waktu istirahat dan hidrasi tubuh dengan air putih.\n"
                    "4. Segera periksakan diri ke dokter jika gejala awal mulai dirasakan."
                )
        else:
            st.info("Silakan ketikkan nama penyakit di atas.")

    # ==========================================================================
    # 2. LAYAR KHUSUS: MENDETEKSI VIRUS
    # ==========================================================================
    elif st.session_state["sub_page"] == "mendeteksi_virus":
        if st.button("Kembali", key="back_virus"):
            st.session_state["sub_page"] = "menu_utama"
            st.rerun()

        st.subheader("Mendeteksi Virus & Tingkat Ancaman")
        st.write("Masukkan nama virus serta efeknya pada kegiatan sehari-hari atau kondisi tertentu:")

        nama_virus_input = st.text_input("Nama Virus (contoh: Influenza, COVID-19, Rabies, HIV):", "")
        efek_virus_input = st.text_area("Efek virus pada kegiatan sehari-hari / kondisi tertentu:", placeholder="Contoh: Menyebabkan demam tinggi, sesak napas, dan membuat tubuh sangat lemas sehingga tidak bisa beraktivitas.")

        database_ancaman_virus = {
            "influenza": {"persen": 25, "kategori": "Ancaman Ringan - Sedang"},
            "covid-19": {"persen": 60, "kategori": "Ancaman Sedang - Tinggi"},
            "rabies": {"persen": 100, "kategori": "Ancaman Sangat Mematikan / Darurat"},
            "hiv": {"persen": 85, "kategori": "Ancaman Tinggi (Menyerang Kekebalan Tubuh)"},
            "dengue": {"persen": 70, "kategori": "Ancaman Tinggi (Risiko Penurunan Trombosit Drastis)"}
        }

        if st.button("Hasilnya", type="primary", use_container_width=True):
            if not nama_virus_input or not efek_virus_input:
                st.warning("Mohon lengkapi nama virus dan kolom efek kegiatannya terlebih dahulu.")
            else:
                key_v = nama_virus_input.lower().strip()
                persen_ancaman = 45 
                kategori_ancaman = "Ancaman Menengah"

                for k, v in database_ancaman_virus.items():
                    if k in key_v:
                        persen_ancaman = v["persen"]
                        kategori_ancaman = v["kategori"]
                        break

                st.markdown("---")
                st.subheader(f"Hasil Analisis Ancaman Virus: {nama_virus_input.capitalize()}")
                st.metric(label="Tingkat Ancaman terhadap Tubuh", value=f"{persen_ancaman}%")
                st.progress(persen_ancaman / 100)
                st.info(f"**Klasifikasi Risiko:** {kategori_ancaman}")
                st.write(f"**Analisis Dampak Berdasarkan Kondisi Anda:** Virus ini mengganggu kegiatan harian karena menimbulkan efek: *'{efek_virus_input}'*. Tingkat ancaman mencapai **{persen_ancaman}%**. Segera lakukan tindakan medis atau isolasi jika diperlukan.")

    # ==========================================================================
    # 3. LAYAR KHUSUS: KESEHATAN JIWA
    # ==========================================================================
    elif st.session_state["sub_page"] == "kesehatan_jiwa":
        if st.button("Kembali", key="back_jiwa"):
            st.session_state["sub_page"] = "menu_utama"
            st.rerun()

        st.subheader("Kesehatan Jiwa")
        st.write("Silakan tuliskan kalimat mengenai bagaimana kondisi perilaku atau perasaan yang sedang Anda alami saat ini:")

        kondisi_perilaku = st.text_area(
            "Kolom Kondisi Perilaku Pasien:",
            placeholder="Contoh: Merasa cemas berlebihan setiap malam, sulit tidur, sering merasa lelah, dan menarik diri dari lingkungan sosial."
        )

        if st.button("Hasilnya", type="primary", use_container_width=True):
            if not kondisi_perilaku:
                st.warning("Mohon tuliskan kondisi perilaku Anda terlebih dahulu pada kolom di atas.")
            else:
                st.markdown("---")
                st.subheader("Hasil Penilaian & Analisis Kesehatan Jiwa")
                
                teks_rendah = kondisi_perilaku.lower()
                if "berat" in teks_rendah or "putus asa" in teks_rendah or "menyakiti" in teks_rendah or "panik" in teks_rendah:
                    tingkat_gawat = "Tingkat Gawat Kesehatan Jiwa: Cukup Tinggi (Butuh Perhatian Profesional Segera)"
                    warna_box = st.error
                else:
                    tingkat_gawat = "Tingkat Gawat Kesehatan Jiwa: Ringan - Sedang (Stress Akibat Beban Harian)"
                    warna_box = st.warning

                warna_box(tingkat_gawat)
                st.write(f"**Berdasarkan kalimat perilaku Anda:** *'{kondisi_perilaku}'*, sistem mendeteksi adanya beban emosional atau tekanan mental yang sedang mempengaruhi aktivitas Anda.")
                
                st.markdown("### 🛡️ Langkah-Langkah Pencegahan & Penanganan:")
                st.write("1. **Teknik Pernapasan Relaksasi:** Tarik napas perlahan dari hidung, tahan beberapa detik, lalu hembuskan lewat mulut untuk menenangkan sistem saraf.")
                st.write("2. **Kurangi Pemicu Stres:** Batasi sementara paparan hal-hal yang memperburuk kecemasan Anda.")
                st.write("3. **Berbagi Cerita:** Ungkapkan perasaan kepada orang terdekat yang dapat dipercaya.")
                st.write("4. **Istirahat Cukup & Rutinitas Sehat:** Pastikan tidur teratur dan lakukan aktivitas fisik ringan.")
                st.info(" **Catatan Penting:** Untuk memastikan kepastian kondisi kesehatan jiwa Anda secara menyeluruh, disarankan berkonsultasi langsung dengan psikolog atau psikiater profesional.")

    # ==========================================================================
    # TAMPILAN UTAMA (MENU UTAMA DENGAN TAB 1 & TAB 2)
    # ==========================================================================
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

        tab1, tab2 = st.tabs(["Informasi Keluhan", "Layanan Kesehatan"])

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
            "Demam Berdarah (DBD)": {
                "kondisi": "Infeksi virus Dengue melalui gigitan nyamuk Aedes aegypti",
                "kategori_obat": "Penurun Panas & Suplemen (Pengawasan Medis Ketat)",
                "saran": "Perbanyak minum air putih untuk cegah dehidrasi, cek trombosit berkala, dan segera ke rumah sakit jika muncul tanda bahaya.",
            },
            "Tifus / Demam Tifoid": {
                "kondisi": "Infeksi bakteri Salmonella enterica pada saluran pencernaan",
                "kategori_obat": "Antibiotik Resep Dokter & Vitamin",
                "saran": "Konsumsi makanan lunak/bubur yang tidak pedas dan asam, istirahat total total di tempat tidur.",
            },
        }

        # TAB 1: INFORMASI KELUHAN (TETAP UTUH SEPERTI SEMULA)
        with tab1:
            st.markdown("### Cari Informasi Keluhan")
            st.write("Ketikkan gejala atau keluhan kesehatan yang ingin Anda ketahui:")
            
            input_keluhan = st.text_input(
                "Masukkan keluhan (contoh: Flu, Maag, Pusing, Batuk, Demam):",
                ""
            )

            if input_keluhan:
                ditemukan = False
                for gejala, data in database_medis.items():
                    if input_keluhan.lower() in gejala.lower() or input_keluhan.lower() in data['kondisi'].lower():
                        st.success(f"Ditemukan informasi untuk: **{gejala}**")
                        st.write(f"**Indikasi Medis:** {data['kondisi']}")
                        st.write(f"**Kategori Obat:** {data['kategori_obat']}")
                        st.info(f"**Saran Penanganan:** {data['saran']}")
                        ditemukan = True
                        break
                
                if not ditemukan:
                    st.warning(f"Keluhan '{input_keluhan}' tidak ditemukan secara spesifik di database.")
                    st.info(
                        f" **Saran Umum untuk '{input_keluhan}':** "
                        "Pastikan istirahat cukup, penuhi cairan tubuh, dan konsultasikan ke dokter jika gejala berlanjut."
                    )
            else:
                st.info("Silakan ketikkan keluhan atau gejala di atas untuk melihat penjelasannya.")

        # TAB 2: LAYANAN KESEHATAN (BERISI 3 TOMBOL PILIHAN SESUAI PERMINTAAN)
        with tab2:
            st.markdown("### Layanan Kesehatan")
            st.write("Silakan pilih menu layanan di bawah ini:")

            if st.button("Panduan Pencegahan", use_container_width=True, key="btn_menu_pencegahan"):
                st.session_state["sub_page"] = "panduan_pencegahan"
                st.rerun()

            if st.button("Mendeteksi Virus", use_container_width=True, key="btn_menu_virus"):
                st.session_state["sub_page"] = "mendeteksi_virus"
                st.rerun()

            if st.button("Kesehatan Jiwa", use_container_width=True, key="btn_menu_jiwa"):
                st.session_state["sub_page"] = "kesehatan_jiwa"
                st.rerun()