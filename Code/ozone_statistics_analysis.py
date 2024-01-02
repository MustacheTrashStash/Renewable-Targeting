import pandas as pd

# Load ozone data
df = pd.read_csv('Datasets/daily-ozone-by-county.csv')  # replace with your actual file path

# Basic statistical summary of ozone levels
ozone_stats = df['Ozone'].describe()
print(ozone_stats)