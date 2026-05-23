# ETL Layer
import sqlite3
import pandas as pd
from pathlib import Path

# Create Base path
BASE_DIR = Path(__file__).resolve().parent.parent

#Create data path
DATA_PATH = BASE_DIR / "data" / "SampleSuperstore.csv"

# Create database path
DB_PATH = BASE_DIR / "database" / "superstore.db"

# Ensure database folder exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Read the csv file
df = pd.read_csv(DATA_PATH)

# Remove duplicates
df1 = df.copy()

df1 = df1.drop_duplicates()

# Create connection
conn = sqlite3.connect(DB_PATH)

df1.to_sql('superstore', conn, if_exists='replace', index=False)

# # save the changes
conn.commit()

# # close the connection
conn.close()