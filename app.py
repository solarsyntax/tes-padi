import streamlit as st
from PIL import Image

st.set_page_config(page_title="🌾 Klasifikasi Penyakit Daun Padi", layout="centered")

# --- Sidebar ---
with st.sidebar:
    st.markdown("## 👤 Info Aplikasi")
    st.markdown("""
    **Nama Aplikasi**:  
    Klasifikasi Penyakit Daun Padi

    **Kelas**:  
    - Streamlit  
    - Python
    """)
    st.markdown("---")
    st.info("Gunakan gambar dari kamera atau galeri untuk mulai klasifikasi.")

# --- Header Utama ---
st.markdown("<h1 style='text-align: center; color: #228B22;'>🌾 Klasifikasi Penyakit Daun Padi</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload gambar daun padi yang ingin Anda klasifikasikan</p>", unsafe_allow_html=True)

# --- Upload & Kamera ---
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📁 Unggah dari Galeri", type=["jpg", "jpeg", "png"])

with col2:
    camera_image = st.camera_input("📷 Ambil dari Kamera")

# --- Menampilkan Gambar ---
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📂 Gambar dari Galeri", use_column_width=True)
elif camera_image is not None:
    image = Image.open(camera_image)
    st.image(image, caption="📷 Gambar dari Kamera", use_column_width=True)

# --- Hasil Klasifikasi (dummy/placeholder) ---
if image:
    st.markdown("---")
    st.markdown("<h3 style='color: #006400;'>📊 Hasil Klasifikasi</h3>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h4 style="color: #2e7d32;">✅ Hasil Deteksi: <span style="color: #1b5e20;">Hawar Daun Bakteri</span></h4>
            <p style="margin-top: 10px;">Rekomendasi: Gunakan fungisida berbasis tembaga dan hindari irigasi berlebih.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔁 Coba Gambar Lain"):
        st.experimental_rerun()
