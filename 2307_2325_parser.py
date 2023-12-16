# Purpose: This file is used to parse the data for the database from the csv files

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Function for parse data to the database


def data_parser(df_name, db_table_columns, db_table_name):
    try:
        column_mapping = dict(zip(df_name.columns, db_table_columns))
        df_name.rename(columns=column_mapping, inplace=True)
        df_name.to_sql(db_table_name, engine, if_exists='append', index=False)
        return print(f"Data successfully parsed to {db_table_name} table")
    except Exception as e:
        print(f"Error: {e}")
        return print(f"Data was not parsed to {db_table_name} table")


# Database connection
db_params = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'useruser',
    'database': 'postgres'
}
# Create a connection to the PostgreSQL database
connection = psycopg2.connect(**db_params)
# Create a SQLAlchemy engine
engine = create_engine(
    f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')
connection.close()

# Entities table
# ! For entities table i had to replace 4 nan values in the name column
entity["name"] = entity["name"].fillna(value="no_name")

db_entity_columns = [
    'entity_id', 'name', 'jurisdiction', 'jurisdiction_description', 'country_code', 'country_name', 'incorporation_date', 'inactivation_date', 'struck_off_date', 'closed_date', 'ibc_ruc', 'status', 'company_type', 'service_provider', 'source_id', 'valid_until', 'note'
]

data_parser(entity, db_entity_columns, "entities_2307_2325")

# Roles table
roles_table = sorted(edges.loc[edges['TYPE'] == 'officer_of']['link'].unique())
roles_df = pd.DataFrame(roles_table, columns=["role_type"]).copy()
roles_df.insert(0, 'role_id', range(1, 1 + len(roles_df)))
roles_df = roles_df[["role_id", "role_type"]]
roles_df.to_sql('roles_2307_2325', engine, if_exists='append', index=False)


# Officers table

# ! For officers table i had to replace 4 nan values in the name column
officer["name"] = officer["name"].fillna(value="no_name")

db_officer_columns = [
    'officer_id', 'name', 'country_code', 'country_name', 'source_id', 'valid_until', 'note'
]

data_parser(officer, db_officer_columns, "officers_2307_2325")

# Officer_entity_roles table

tmp = edges[edges["TYPE"] == "officer_of"].copy()
tmp = tmp.merge(roles_df, left_on='link', right_on='role_type').copy()
