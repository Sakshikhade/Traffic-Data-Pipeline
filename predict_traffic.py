import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

# Load your traffic data
df = pd.read_csv('traffic_processed.csv')

# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Create directory to save plots
os.makedirs("forecasts", exist_ok=True)

# Get unique locations
locations = df['location'].unique()

# Store all forecasts
all_forecasts = []

# Loop through each location and train a model
for loc in locations:
    sub_df = df[df['location'] == loc][['date', 'avg_volume']].rename(columns={'date': 'ds', 'avg_volume': 'y'})

    if len(sub_df) < 10:
        continue  # Not enough data to train

    # Train the Prophet model
    model = Prophet(daily_seasonality=True)
    model.fit(sub_df)

    # Forecast next 7 days
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    # Save predictions
    forecast['location'] = loc
    all_forecasts.append(forecast[['ds', 'yhat', 'location']].tail(7))

    # Plot and save
    fig = model.plot(forecast)
    plt.title(f'Traffic Volume Forecast - {loc}')
    plt.savefig(f"forecasts/{loc}_forecast.png")
    plt.close()

# Merge all forecasts and save
final_df = pd.concat(all_forecasts)
final_df.rename(columns={'ds': 'date', 'yhat': 'predicted_avg_volume'}, inplace=True)
final_df.to_csv('predicted_traffic.csv', index=False)

print("✅ Forecasts completed and saved to predicted_traffic.csv and /forecasts folder.")
