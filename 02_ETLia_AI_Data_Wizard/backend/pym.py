import pymssql
import pandas as pd
from config import *

# Connexion SQL Server
SERVER = 'localhost'  # ou host.docker.internal si Docker
DATABASE = 'master'

conn = pymssql.connect(server=SERVER,
                       user=UID,
                       password=PWD,
                       database=DATABASE,
                       port=1433)
cursor = conn.cursor()

# Récupérer toutes les tables du schéma dbo
cursor.execute("""
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='dbo'
""")
tables = [row[0] for row in cursor.fetchall()]

# Récupérer toutes les colonnes pour chaque table
schema = {}
for table in tables:
    cursor.execute(f"""
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME='{table}' AND TABLE_SCHEMA='dbo'
    """)
    cols = [row[0] for row in cursor.fetchall()]
    schema[table] = cols

cursor.close()
conn.close()

print(schema)
# toujours conn.commit() apres modification