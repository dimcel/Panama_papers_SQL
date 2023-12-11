**Draft code for reuse**

max_lengths = {}

# Iterate over each column in the DataFrame

for column in entity.columns: # Calculate the maximum length for each cell in the column
max_length_in_column = entity[column].astype(str).apply(len).max()

    # Store the result in the dictionary
    max_lengths[column] = max_length_in_column

# Print the maximum lengths for each column

for column, max_length in max_lengths.items():
print(f"Maximum length in '{column}': {max_length}")

---

**--**

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Assuming you have a DataFrame named 'df' and a PostgreSQL connection is established

# PostgreSQL connection parameters

db_params = {
'host': 'localhost',
'port': 5432,
'user': 'postgres',
'password': 'useruser',
'database': 'postgres'
}

# Create a connection to the PostgreSQL database

connection = psycopg2.connect(\*\*db_params)

# Create a SQLAlchemy engine

engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

# Replace 'entities_2325' with your actual table name

table_name = 'entities_2325'

# Transfer the DataFrame to the PostgreSQL database

entity.to_sql(table_name, engine, if_exists='append', index=False)

# Close the database connection

connection.close()

**Entities**
for entities table i had to replace 4 nan values in the name column and also change the attribute types to be able to have 865 character long notes! i will change it to TEXT to be good for the future!

entity["name"] = entity["name"].fillna(value = "no_name")

And renamed the dataframe to mach the database names

# 1. Map DataFrame Columns to Database Columns

column_mapping = dict(zip(entity.columns, db_table_columns))
entity.rename(columns=column_mapping, inplace=True)

CREATE TABLE entities_2325 (
entity_id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
jurisdiction VARCHAR(255),
jurisdiction_description VARCHAR(255),
country_code VARCHAR(3),
country_name VARCHAR(100),
incorporation_date DATE,
inactivation_date DATE,
struck_off_date DATE,
closed_date DATE,
ibc_ruc VARCHAR(255),
status VARCHAR(255),
company_type VARCHAR(255),
service_provider VARCHAR(255),
source_id VARCHAR(255),
valid_until VARCHAR(255),
note TEXT
);

---

**Roles**

# unique of this is the ROLE table

--sql table
CREATE TABLE roles_2325 (
role_id SERIAL PRIMARY KEY,
role_type VARCHAR(100) NOT NULL
);

roles_table = sorted(edges.loc[edges['TYPE'] == 'officer_of']['link'].unique())
roles_df = pd.DataFrame(roles_table, columns=["role_type"])
roles_df["role_id"] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
roles_df = roles_df[["role_id","role_type"]]
roles_df.to_sql('roles_2325', engine, if_exists='append', index=False)
