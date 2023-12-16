**Draft code for reuse**

roles_officers_2[roles_officers_2['entity_id'].astype(str).str.startswith('11')].shape[0]
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
from sqlalchemy import create_engine

# Assuming you have an SQLAlchemy engine named 'engine' and DataFrames for each table

table_names = ['table1', 'table2', 'table3']
dataframes = [df1, df2, df3] # Replace df1, df2, df3 with your actual DataFrames

# Write SQL statements to a file

sql_file_name = 'xxxx-data.sql'

with open(sql_file_name, 'w') as sql_file:
for table_name, df in zip(table_names, dataframes): # Use to_sql to insert data into the PostgreSQL table
df.to_sql(table_name, engine, if_exists='append', index=False, chunksize=1000)

        # Manually generate SQL insert statements for documentation
        for chunk in pd.read_sql(f"SELECT * FROM {table_name}", engine, chunksize=1000):
            chunk.to_sql(table_name, engine, if_exists='append', index=False)
            for _, row in chunk.iterrows():
                values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in row])
                sql_statement = f"INSERT INTO {table_name} ({', '.join(chunk.columns)}) VALUES ({values});\n"
                sql_file.write(sql_statement)

print(f"SQL statements have been written to {sql_file_name}.")

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
for entities table i had to replace 4 nan values in the name column

entity["name"] = entity["name"].fillna(value = "no_name")

# 1. Map DataFrame Columns to Database Columns

db_table_columns = [
'entity_id',
'name',
'jurisdiction',
'jurisdiction_description',
'country_code',
'country_name',
'incorporation_date',
'inactivation_date',
'struck_off_date',
'closed_date',
'ibc_ruc',
'status',
'company_type',
'service_provider',
'source_id',
'valid_until',
'note'
]

column_mapping = dict(zip(entity.columns, db_table_columns))
entity.rename(columns=column_mapping, inplace=True)

CREATE TABLE entities_2307_2325 (
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

**Officers**
The same as entities, there was 4 NaN in name collum.

column_mapping = dict(zip(officer.columns, db_table_columns))
officer.rename(columns=column_mapping, inplace=True)

db_table_columns = [
'officer_id',
'name',
'country_code',
'country_name',
'source_id',
'valid_until',
'note'
]

officer["name"] = officer["name"].fillna(value = "no_name")

officer.to_sql('officers_2325', engine, if_exists='append', index=False)

**Roles_officers**
roles_officers = edges.loc[edges['TYPE'] == 'officer_of']
roles_officers_2 = roles_officers.merge(roles_df, left_on='link', right_on='role_type').copy()
roles_officers_2.drop(columns=["TYPE","link","role_type"], inplace=True)
roles_officers_2 = roles_officers_2[['START_ID', 'role_id', 'END_ID', 'start_date', 'end_date', 'sourceID', 'valid_until']]
roles_officers_2.insert(0, 'officer_role_id', range(1, 1 + len(roles_officers_2)))

--
db_table_columns = [
'officer_role_id',
'officer_id',
'role_id',
'entity_id',
'start_date',
'end_date',
'source_id',
'valid_until'
]
column_mapping = dict(zip(roles_officers_2.columns, db_table_columns))
--

roles_officers_2.rename(columns=column_mapping, inplace=True)

#after deletting 5 rows by hand roles_officers_2 = roles_officers_2.drop(index=309344)

roles_officers_2.to_sql('roles_officer_2325', engine, if_exists='append', index=False)

**intermediatries**
CREATE TABLE intermediaries_2325 (
intermediary_id SERIAL PRIMARY KEY,
name VARCHAR(255),
country_code VARCHAR(15),
country_name VARCHAR(255),
status VARCHAR(100),
source_id VARCHAR(255),
valid_until VARCHAR(255),
note TEXT
);

intermediary_2 = intermediary.copy()

db_table_columns = [
'intermediary_id',
'name',
'country_code',
'country_name',
'status',
'source_id',
'valid_until',
'note'
]
column_mapping = dict(zip(intermediary_2.columns, db_table_columns))
intermediary_2.rename(columns=column_mapping, inplace=True)

intermediary_2.to_sql('intermediaries_2325', engine, if_exists='append', index=False)

**intermediary entities**

inter_entity = edges[edges["TYPE"] == "intermediary_of"].copy()

inter_entity.drop(columns=["TYPE","link"], inplace=True)

inter_entity.insert(0, 'intermediary_entity_id', range(1, 1 + len(inter_entity)))

db_table_columns = [
'intermediary_entity_id',
'intermediary_id',
'entity_id',
'start_date',
'end_date',
'source_id',
'valid_until'
]
column_mapping = dict(zip(inter_entity.columns, db_table_columns))
inter_entity.rename(columns=column_mapping, inplace=True)

inter_entity.to_sql('interm_entities_2325', engine, if_exists='append', index=False)

-- Create IntermediaryOffshoreEntities Table (Many-to-Many Relationship)
CREATE TABLE interm_entities_2325 (
intermediary_entity_id SERIAL PRIMARY KEY,
intermediary_id INTEGER REFERENCES intermediaries_2325(intermediary_id),
entity_id INTEGER REFERENCES entities_2325(entity_id),
start_date DATE,
end_date DATE,
source_id VARCHAR(255),
valid_until VARCHAR(255)
);

**Adresses**

CREATE TABLE addresses_2325 (
address_id SERIAL PRIMARY KEY,
name VARCHAR(255),
address TEXT,
country_code VARCHAR(255),
country_name VARCHAR(100),
source_id VARCHAR(255),
valid_until VARCHAR(255),
note TEXT
);

address_2 = address.copy()

db_table_columns = [
'address_id',
'name',
'address',
'country_code',
'country_name',
'source_id',
'valid_until',
'note'
]
column_mapping = dict(zip(address_2.columns, db_table_columns))
address_2.rename(columns=column_mapping, inplace=True)

address_2.to_sql('addresses_2325', engine, if_exists='append', index=False)

**adresses_entities**

register_addresses = edges[edges["TYPE"] == "registered_address"].copy()
addresses_entities = register_addresses[register_addresses['START_ID'].astype(str).str.startswith('10')].copy()
addresses_entities.insert(0, 'entity_address_id', range(1, 1 + len(addresses_entities)))
addresses_entities = addresses_entities.rename(columns={"register_address_id": "entity_address_id"})

db_table_columns = [
'entity_address_id',
'entity_id',
'address_id',
'start_date',
'end_date',
'source_id',
'valid_until'
]
column_mapping = dict(zip(addresses_entities.columns, db_table_columns))
addresses_entities.rename(columns=column_mapping, inplace=True)

addresses_entities.to_sql('entities_addresses_2325', engine, if_exists='append', index=False)

**addresses_officers**

addresses_officers = register_addresses[~register_addresses['START_ID'].astype(str).str.startswith('10')].copy()

addresses_officers.drop(columns=["officer_entity_address_id"], inplace=True) #!this may be obsolete

addresses_officers.insert(0, 'officer_address_id', range(1, 1 + len(addresses_officers)))
db_table_columns = [
'officer_address_id',
'officer_id',
'address_id',
'start_date',
'end_date',
'source_id',
'valid_until'
]
column_mapping = dict(zip(addresses_officers.columns, db_table_columns))
addresses_officers.rename(columns=column_mapping, inplace=True)

addresses_officers.to_sql('officers_addresses_2325', engine, if_exists='append', index=False)
