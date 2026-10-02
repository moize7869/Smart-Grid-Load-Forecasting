import pandas as pd
import numpy as np

# 1. Time range set karna (1 mahine ka data, har ghante ka)
dates = pd.date_range(start='2026-09-01', periods=720, freq='h')

# 2. Temperature Sensor (Sensor 1): Din me garmi, raat me thand
np.random.seed(42)
time_of_day = dates.hour.values
# Sine wave se natural daily temperature cycle banayenge
temperature = 25 + 5 * np.sin((time_of_day - 6) * (2 * np.pi / 24)) + np.random.normal(0, 1, 720)

# 3. Smart Meter Load Sensor (Sensor 2): Load kW mein
# Load temperature se related hai, plus subah-shaam ke routine peaks
base_load = 100
daily_pattern = 20 * np.sin((time_of_day - 6) * (2 * np.pi / 24))
temp_effect = (temperature - 25) * 2 
power_load = base_load + daily_pattern + temp_effect + np.random.normal(0, 2, 720)

# 4. Abnormal Load Spikes (Anomalies) inject karna
# Yeh woh faulty points hain jinhe humara anomaly model baad me detect karega
anomaly_indices = [100, 250, 400, 650]
for idx in anomaly_indices:
    power_load[idx] += 60  # Achanak se 60 kW ka abnormal spike 

# 5. Dataframe banana aur CSV mein save karna
df = pd.DataFrame({
    'Timestamp': dates,
    'Temperature_C': temperature,
    'Power_Load_kW': power_load
})

df.to_csv('smart_grid_data.csv', index=False)
print("Data successfully generated and saved to 'smart_grid_data.csv'")