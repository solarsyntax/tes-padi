import streamlit as st
from PIL import Image

st.set_page_config(page_title="🌾 Klasifikasi Penyakit Daun Padi", layout="wide")

# Inject Bootstrap CSS dari CDN
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
    body {
        background-color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .card-custom {
        background-color: #e8f5e9;
        border-left: 5px solid #388e3c;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.markdown("## 👤 Info Aplikasi")
    st.markdown("""
    **Nama Aplikasi**  
    Klasifikasi Penyakit Daun Padi

    **Teknologi**  
    - Streamlit  
    - Python  
    """)
    st.markdown("---")
    st.info("📸 Unggah gambar dari galeri atau ambil dari kamera.")

# Header
st.markdown("""
    <div class="container text-center">
        <h1 class="text-success">🌾 Klasifikasi Penyakit Daun Padi</h1>
        <p class="text-muted">Unggah atau ambil gambar untuk mendeteksi penyakit daun padi secara otomatis</p>
    </div>
""", unsafe_allow_html=True)

# Upload dan Kamera dengan grid Bootstrap
st.markdown("""
    <div class="container">
      <div class="row">
        <div class="col-md-6">
""", unsafe_allow_html=True)
uploaded_file = st.file_uploader("📁 Unggah Gambar dari Galeri", type=["jpg", "jpeg", "png"])
st.markdown("</div><div class='col-md-6'>", unsafe_allow_html=True)
camera_image = st.camera_input("📷 Ambil Gambar dari Kamera")
st.markdown("</div></div></div>", unsafe_allow_html=True)

# Tampilkan gambar
image = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📂 Gambar dari Galeri", use_column_width=True)
elif camera_image:
    image = Image.open(camera_image)
    st.image(image, caption="📷 Gambar dari Kamera", use_column_width=True)

# Hasil klasifikasi dummy
if image:
    st.markdown("""
        <div class="container">
            <div class="card-custom">
                <h4 class="text-success">✅ Deteksi: <span class="fw-bold">Hawar Daun Bakteri</span></h4>
                <p class="mb-0">💡 Rekomendasi: Gunakan fungisida berbasis tembaga dan hindari penyiraman berlebih.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔁 Coba Gambar Lain"):
        st.experimental_rerun()
