import json
import pandas as pd
import sys
# Read the CSV file
try:
    csv_file = sys.argv[1]
except :
    csv_file = 'DataSets/HeatMap_deltas_UnEnt_Delay.csv'

print(f"Your requested file is {csv_file}")
json_file = csv_file.replace('.csv', '.json')
df = pd.read_csv(csv_file)  
# Convert CSV to JSON
df_json = df.to_dict(orient='records')

# Save as JSON
with open(json_file, 'w') as f:
    json.dump(df_json, f, indent=2)

print(f"Saved to {json_file}")