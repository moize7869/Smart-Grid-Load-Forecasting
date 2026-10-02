import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest

# 1. Data Load 
print("Loading data...")
df = pd.read_csv('smart_grid_data.csv')

# 2. Data Preprocessing (Feature Engineering)
# Machine Learning model ko time samajh nahi aata, isliye hum Timestamp se 'Hour' nikalenge
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Hour'] = df['Timestamp'].dt.hour

# Features (X) aur Target (y) set karna
# Hum model ko 'Hour' aur 'Temperature' batayenge, aur wo 'Power Load' predict karega
X = df[['Hour', 'Temperature_C']]
y = df['Power_Load_kW']

# 3. Prediction Model: Linear Regression
print("Training Prediction Model (Linear Regression)...")
model_lr = LinearRegression()
model_lr.fit(X, y)
df['Predicted_Load_kW'] = model_lr.predict(X)

# 4. Anomaly Detection Model: Isolation Forest
print("Training Anomaly Detection Model (Isolation Forest)...")
# contamination=0.01 ka matlab hum maan rahe hain ki lagbhag 1% data abnormal hai
model_iso = IsolationForest(contamination=0.01, random_state=42)
# Isolation forest return karta hai 1 (Normal) aur -1 (Anomaly)
df['Anomaly_Flag'] = model_iso.fit_predict(df[['Power_Load_kW']])

# 5. Final output should be save in new file
df.to_csv('model_results.csv', index=False)
print("Success! Models trained and output 'model_results.csv' saved.")