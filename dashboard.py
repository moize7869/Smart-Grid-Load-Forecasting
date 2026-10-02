import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dashboard Title
st.title("⚡ Smart Grid Load Forecasting & Anomaly Detection")
st.write("This dashboard visualizes the actual versus predicted grid load, while detecting and highlighting abnormal power spikes (anomalies).")
# 2. Data Load 
@st.cache_data
def load_data():
    data = pd.read_csv('model_results.csv')
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    return data

df = load_data()

# 3. Graph (Matplotlib)
st.subheader("📊 Load Forecast & Anomaly Graph")

fig, ax = plt.subplots(figsize=(12, 6))

# Actual aur Predicted line plot karna
ax.plot(df['Timestamp'], df['Power_Load_kW'], label='Actual Load (kW)', color='blue', alpha=0.6)
ax.plot(df['Timestamp'], df['Predicted_Load_kW'], label='Predicted Load (kW)', color='green', linestyle='--')

# Anomalies (Jahan flag -1 hai) ko red dots se mark karna
anomalies = df[df['Anomaly_Flag'] == -1]
ax.scatter(anomalies['Timestamp'], anomalies['Power_Load_kW'], color='red', s=50, label='Anomaly / Spike', zorder=5)

# Graph formatting
ax.set_xlabel("Time (Timestamp)")
ax.set_ylabel("Power Load (kW)")
ax.set_title("Electricity Load over Time with Detected Anomalies")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# 4. TO Show the plot in Streamlit
st.pyplot(fig)

st.subheader("📋 Raw Data (Sample)")
st.dataframe(df.head())