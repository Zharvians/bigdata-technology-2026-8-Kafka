import streamlit as st
import pandas as pd
import plotly.express as px
import glob
import time

# ===== CONFIG =====
st.set_page_config(page_title="Fraud Dashboard", layout="wide")

# ===== CUSTOM CSS =====
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.metric-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ===== TITLE =====
st.title("🚨 Real-Time Fraud Detection Dashboard")

# ===== LOAD DATA (REALTIME + STABIL) =====
files = sorted(glob.glob("stream_data/realtime_output/*.parquet"))

if not files:
    st.warning("Belum ada data masuk dari Spark...")
    st.stop()

time.sleep(1)

dfs = []
# ambil beberapa file terakhir biar data banyak
for f in reversed(files[-15:]):  # bisa ubah jumlah file di sini
    try:
        dfs.append(pd.read_parquet(f))
    except:
        continue

if not dfs:
    st.warning("Data belum siap...")
    st.stop()

df = pd.concat(dfs, ignore_index=True)

# ambil minimal 50 data terakhir
df = df.tail(50)

# ===== SAFETY CHECK =====
if "status" not in df.columns:
    st.error("Kolom 'status' belum ada di data")
    st.stop()

# ===== METRICS =====
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("💳 Total Transaksi", len(df))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("🚨 Total Fraud", len(df[df["status"]=="FRAUD"]))
    st.markdown('</div>', unsafe_allow_html=True)

# ===== CHART =====
col3, col4 = st.columns(2)

with col3:
    fig = px.pie(df, names="status", title="Distribusi Status", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with col4:
    fig2 = px.histogram(df, x="jumlah", color="status", nbins=30,
                        title="Distribusi Jumlah Transaksi")
    st.plotly_chart(fig2, use_container_width=True)

# ===== TABLE =====
st.subheader("📊 Transaksi Terbaru")
st.dataframe(df, use_container_width=True)

# ===== AUTO REFRESH =====
time.sleep(2)
st.rerun()