import pandas as pd
import sqlite3

conn = sqlite3.connect('data.db')

# ---- CSV ----
df_csv = pd.read_csv('tnpopmod.csv')
df_csv.to_sql(
    'population',
    conn,
    if_exists='replace',
    index=False
)

# ---- XLS (single sheet) ----
df_xls = pd.read_excel('tamilnadu_workers.xls')  # reads the only sheet
df_xls.to_sql(
    'labour',
    conn,
    if_exists='replace',
    index=False
)

conn.close()
