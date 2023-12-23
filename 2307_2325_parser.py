import os
import pandas as pd

# Read csv files

folder_path = 'csv_panama_papers'
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df_name = csv_file.split('.')[2] if len(csv_file.split('.')) > 2 else None
    globals()[df_name] = pd.read_csv(file_path)

edges = csv.copy()


# function to parse data and rename columns
def data_parser(df_name, db_table_columns):
    column_mapping = dict(zip(df_name.columns, db_table_columns))
    df_name.rename(columns=column_mapping, inplace=True)


entity["name"] = entity["name"].fillna(value="no_name")

db_entity_columns = [
    'entity_id', 'name', 'jurisdiction', 'jurisdiction_description', 'country_code', 'country_name', 'incorporation_date', 'inactivation_date', 'struck_off_date', 'closed_date', 'ibc_ruc', 'status', 'company_type', 'service_provider', 'source_id', 'valid_until', 'note'
]

data_parser(entity, db_entity_columns)

# Roles table
roles_table = sorted(edges.loc[edges['TYPE'] == 'officer_of']['link'].unique())
roles_df = pd.DataFrame(roles_table, columns=["role_type"]).copy()
roles_df.insert(0, 'role_id', range(1, 1 + len(roles_df)))
roles_df = roles_df[["role_id", "role_type"]]


# Officers table

# ! For officers table i had to replace 4 nan values in the name column
officer["name"] = officer["name"].fillna(value="no_name")

db_officer_columns = [
    'officer_id', 'name', 'country_code', 'country_name', 'source_id', 'valid_until', 'note'
]

data_parser(officer, db_officer_columns)


# Intermediaries table

db_inter_columns = [
    'intermediary_id', 'name', 'country_code', 'country_name', 'status', 'source_id', 'valid_until', 'note'
]

data_parser(intermediary, db_inter_columns)


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
data_parser(officers_roles_entities, db_ore_columns)
# officer_role_officer table

officers_roles_officers = tmp[tmp['END_ID'].astype(
    str).str.startswith('12')].copy()
officers_roles_officers.insert(
    0, 'officer_role_officer_id', range(1, 1 + len(officers_roles_officers)))
db_oro_columns = [
    'officer_role_officer_id', 'officer_id_1', 'role_id', 'officer_id_2', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(officers_roles_officers, db_oro_columns)

# officer_role_intermediary table

officers_roles_intermediaries = tmp[tmp['END_ID'].astype(
    str).str.startswith('11')].copy()
officers_roles_intermediaries.insert(0, 'officer_role_intermediary_id', range(
    1, 1 + len(officers_roles_intermediaries)))
db_ori_columns = [
    'officer_role_intermediary_id', 'officer_id', 'role_id', 'intermediary_id', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(officers_roles_intermediaries, db_ori_columns)


# Intermediaries_entities table


inter_entity = edges[edges["TYPE"] == "intermediary_of"].copy()
inter_entity.drop(columns=["TYPE", "link"], inplace=True)
inter_entity.insert(0, 'intermediary_entity_id',
                    range(1, 1 + len(inter_entity)))

db_ie_columns = [
    'intermediary_entity_id', 'intermediary_id', 'entity_id', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(inter_entity, db_ie_columns)


# Addresses table

db_address_columns = [
    'address_id', 'name', 'address', 'country_code', 'country_name', 'source_id', 'valid_until', 'note'
]
data_parser(address, db_address_columns)


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
data_parser(addresses_entities, db_ea_columns)

# Officers_address table

addresses_officers.insert(0, 'intermediary_entity_id',
                          range(1, 1 + len(addresses_officers)))

db_oa_columns = [
    'officer_address_id', 'officer_id', 'address_id', 'start_date', 'end_date', 'source_id', 'valid_until'
]
data_parser(addresses_officers, db_oa_columns)


# mapping DataFrames to table names
df_table_mapping = {
    'roles_df': 'roles_2307_2325',
    'entity': 'entities_2307_2325',
    'officer': 'officers_2307_2325',
    'address': 'addresses_2307_2325',
    'intermediary': 'intermediaries_2307_2325',
    'officers_roles_entities': 'officers_roles_entities_2307_2325',
    'officers_roles_officers': 'officers_roles_officers_2307_2325',
    'officers_roles_intermediaries': 'officers_roles_intermediaries_2307_2325',
    'inter_entity': 'intermediaries_entities_2307_2325',
    'addresses_entities': 'entities_addresses_2307_2325',
    'addresses_officers': 'officers_addresses_2307_2325'
}
# sql  output file name
sql_file = '2307_2325_data.sql'

with open(sql_file, 'w') as file:
    for df_name, table_name in df_table_mapping.items():
        df = globals()[df_name]
        for index, row in df.iterrows():
            row_values = ["NULL" if pd.isna(value) else "'" + str(value).replace(
                "'", "''") + "'" if isinstance(value, str) else str(value) for value in row]
            insert_statement = "INSERT INTO {} ({}) VALUES ({});\n".format(
                table_name, ', '.join(df.columns), ', '.join(row_values))
            file.write(insert_statement)
