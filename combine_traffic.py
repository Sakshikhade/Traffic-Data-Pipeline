import pandas as pd

# Load actual traffic data
actual_df = pd.read_csv('traffic_processed.csv')
actual_df['date'] = pd.to_datetime(actual_df['date'])

# Load predicted traffic data
predicted_df = pd.read_csv('predicted_traffic.csv')
predicted_df['date'] = pd.to_datetime(predicted_df['date'])

# Merge on 'date' and 'location'
merged_df = pd.merge(actual_df, predicted_df, on=['date', 'location'], how='outer')

# Sort data for better readability
merged_df.sort_values(by=['location', 'date'], inplace=True)

# Save to new file
merged_df.to_csv('traffic_combined.csv', index=False)

print("✅ Combined data saved as traffic_combined.csv")
