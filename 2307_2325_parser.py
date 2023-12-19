# Purpose: This file is used to parse the data for the database from the csv files
import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Read csv files

folder_path = 'csv_panama_papers'
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df_name = csv_file.split('.')[2] if len(csv_file.split('.')) > 2 else None
    globals()[df_name] = pd.read_csv(file_path)

edges = csv.copy()

# Function for parse data to the database


def data_parser(df_name, db_table_columns, db_table_name):
    try:
        column_mapping = dict(zip(df_name.columns, db_table_columns))
        df_name.rename(columns=column_mapping, inplace=True)
        df_name.to_sql(db_table_name, engine, if_exists='append', index=False)
        return print(f"Data successfully parsed to {db_table_name} table")
    except Exception as e:
        # print(f"Error: {e}") uncomment this line to see more of the error
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


# Intermediaries table

db_inter_columns = [
    'intermediary_id', 'name', 'country_code', 'country_name', 'status', 'source_id', 'valid_until', 'note'
]

data_parser(intermediary, db_inter_columns, "intermediaries_2307_2325")


# Preprocessing edges table

tmp = edges[edges["TYPE"] == "officer_of"].copy()
tmp = tmp.merge(roles_df, left_on='link', right_on='role_type').copy()
tmp.drop(columns=["TYPE", "link", "role_type"], inplace=True)
tmp = tmp[['START_ID', 'role_id', 'END_ID',
           'start_date', 'end_date', 'sourceID', 'valid_until']]

# officer_role_entity table

officers_roles_entities = tmp[tmp['END_ID'].astype(
    str).str.startswith('10')].copy()
officers_roles_entities.insert(
    0, 'officer_role_entity_id', range(1, 1 + len(officers_roles_entities)))
db_ore_columns = [
    'officer_role_entity_id', 'officer_id', 'role_id', 'entity_id', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(officers_roles_entities, db_ore_columns,
            "officers_roles_entities_2307_2325")

# officer_role_officer table

officers_roles_officers = tmp[tmp['END_ID'].astype(
    str).str.startswith('12')].copy()
officers_roles_officers.insert(
    0, 'officer_role_officer_id', range(1, 1 + len(officers_roles_officers)))
db_oro_columns = [
    'officer_role_officer_id', 'officer_id_1', 'role_id', 'officer_id_2', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(officers_roles_officers, db_oro_columns,
            "officers_roles_officers_2307_2325")

# officer_role_intermediary table

officers_roles_intermediaries = tmp[tmp['END_ID'].astype(
    str).str.startswith('11')].copy()
officers_roles_intermediaries.insert(0, 'officer_role_intermediary_id', range(
    1, 1 + len(officers_roles_intermediaries)))
db_ori_columns = [
    'officer_role_intermediary_id', 'officer_id', 'role_id', 'intermediary_id', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(officers_roles_intermediaries, db_ori_columns,
            "officers_roles_intermediaries_2307_2325")


# Intermediaries_entities table


inter_entity = edges[edges["TYPE"] == "intermediary_of"].copy()
inter_entity.drop(columns=["TYPE", "link"], inplace=True)
inter_entity.insert(0, 'intermediary_entity_id',
                    range(1, 1 + len(inter_entity)))

db_ie_columns = [
    'intermediary_entity_id', 'intermediary_id', 'entity_id', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(inter_entity, db_ie_columns, "intermediaries_entities_2307_2325")


# Addresses table

db_address_columns = [
    'address_id', 'name', 'address', 'country_code', 'country_name', 'source_id', 'valid_until', 'note'
]
data_parser(address, db_address_columns, "addresses_2307_2325")


# Preprocessing for register_addresses
register_addresses = edges[edges["TYPE"] == "registered_address"].copy()
register_addresses.drop(columns=["TYPE", "link"], inplace=True)
addresses_entities = register_addresses[register_addresses['START_ID'].astype(
    str).str.startswith('10')].copy()
addresses_officers = register_addresses[~register_addresses['START_ID'].astype(
    str).str.startswith('10')].copy()


# Entities_address table

addresses_entities.insert(0, 'entity_address_id',
                          range(1, 1 + len(addresses_entities)))

db_ea_columns = [
    'entity_address_id', 'entity_id', 'address_id', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(addresses_entities, db_ea_columns, "entities_addresses_2307_2325")

# Officers_address table

addresses_officers.insert(0, 'intermediary_entity_id',
                          range(1, 1 + len(addresses_officers)))

db_oa_columns = [
    'officer_address_id', 'officer_id', 'address_id', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(addresses_officers, db_oa_columns, "officers_addresses_2307_2325")
