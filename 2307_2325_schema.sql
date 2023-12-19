-- Roles Table
CREATE TABLE roles_2307_2325 (
    role_id SERIAL PRIMARY KEY,
    role_type VARCHAR(100) NOT NULL
);

-- Entities Table
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

-- Officers Table
CREATE TABLE officers_2307_2325 (
    officer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country_code VARCHAR(3),
    country_name VARCHAR(100),
    source_id VARCHAR(255),
    valid_until VARCHAR(255),
    note TEXT
);

-- Many-to-Many Relationship 
CREATE TABLE officers_roles_entities_2307_2325 (
    officer_role_entity_id SERIAL PRIMARY KEY,
    officer_id INTEGER REFERENCES officers_2307_2325(officer_id),
    role_id INTEGER REFERENCES roles_2307_2325(role_id),
    entity_id INTEGER REFERENCES entities_2307_2325(entity_id),
    start_date DATE,
    end_date DATE,
    source_id VARCHAR(255),
    valid_until VARCHAR(255)
);


-- Many-to-Many Relationship 
CREATE TABLE officers_roles_officers_2307_2325 (
    officer_role_officer_id SERIAL PRIMARY KEY,
    officer_id_1 INTEGER REFERENCES officers_2307_2325(officer_id),
    role_id INTEGER REFERENCES roles_2307_2325(role_id),
    officer_id_2 INTEGER REFERENCES officers_2307_2325(officer_id),
    start_date DATE,
    end_date DATE,
    source_id VARCHAR(255),
    valid_until VARCHAR(255)
);


-- Many-to-Many Relationship
CREATE TABLE officers_roles_intermediaries_2307_2325 (
    officer_role_intermediary_id SERIAL PRIMARY KEY,
    officer_id INTEGER REFERENCES officers_2307_2325(officer_id),
    role_id INTEGER REFERENCES roles_2307_2325(role_id),
    intermediary_id INTEGER REFERENCES intermediaries_2307_232(intermediary_id),
    start_date DATE,
    end_date DATE,
    source_id VARCHAR(255),
    valid_until VARCHAR(255)
);


-- Intermediaries Table
CREATE TABLE intermediaries_2307_2325 (
    intermediary_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_code VARCHAR(15),
    country_name VARCHAR(255),
    status VARCHAR(100),
    source_id VARCHAR(255),
    valid_until VARCHAR(255),
    note TEXT
);

-- Addresses table
CREATE TABLE addresses_2307_2325 (
    address_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    country_code VARCHAR(255),
    country_name VARCHAR(100),
    source_id VARCHAR(255),
    valid_until VARCHAR(255),
    note TEXT
);

-- Many-to-Many Relationship
CREATE TABLE intermediaries_entities_2307_2325 (
    intermediary_entity_id SERIAL PRIMARY KEY,
    intermediary_id INTEGER REFERENCES intermediaries_2307_232(intermediary_id),
    entity_id INTEGER REFERENCES entities_2307_2325(entity_id),
    start_date DATE,
    end_date DATE,
    source_id VARCHAR(255),
    valid_until VARCHAR(255) 
);

-- Many-to-Many Relationship
CREATE TABLE officers_addresses_2325 (
    officer_address_id SERIAL PRIMARY KEY,
    officer_id INTEGER REFERENCES officers_2307_2325(officer_id),
    address_id INTEGER REFERENCES addresses_2307_2325(address_id),
    start_date DATE,
    end_date DATE,
    source_id VARCHAR(255),
    valid_until VARCHAR(255)
);


-- Many-to-Many Relationship
CREATE TABLE entities_addresses_2325 (
    entity_address_id SERIAL PRIMARY KEY,
    entity_id INTEGER REFERENCES entities_2307_2325(entity_id),
    address_id INTEGER REFERENCES addresses_2307_2325(address_id),
    start_date DATE,
    end_date DATE,
    source_id VARCHAR(255),
    valid_until VARCHAR(255)
);

