-- i
SELECT COUNT(*) 
FROM entities_2307_2325; 


-- ii
SELECT country_name, COUNT(*) AS officer_count
FROM officers_2307_2325
GROUP BY country_name
ORDER BY COUNT(*) DESC
LIMIT 20;

-- iii
SELECT o.officer_id, o.name, a.address
FROM officers_2307_2325 o
LEFT JOIN officers_addresses_2325 oa ON o.officer_id = oa.officer_id
LEFT JOIN addresses_2307_2325 a ON oa.address_id = a.address_id
WHERE o.country_name = 'Greece';


-- iv
SELECT DISTINCT o.officer_id, o.name, a.address FROM officers_2307_2325 o 
LEFT JOIN officers_roles_entities_2307_2325 ore ON o.officer_id = ore.officer_id
LEFT JOIN entities_2307_2325 e ON ore.entity_id = e.entity_id
LEFT JOIN entities_addresses_2307_2325 ea ON e.entity_id = ea.entity_id
LEFT JOIN addresses_2307_2325 a ON ea.address_id = a.address_id
WHERE e.country_name = 'Greece' AND e.jurisdiction_description = 'Seychelles';

-- v
SELECT o.officer_id, o.name, a.address FROM officers_2307_2325 o
LEFT JOIN officers_addresses_2307_2325 oa ON o.officer_id = oa.officer_id
LEFT JOIN addresses_2307_2325 a ON oa.address_id = a.address_id
WHERE o.officer_id = 12156293;


UPDATE addresses_2307_2325 a1
SET address = 'Old Palace, Athens 105 57, Greece'
WHERE a1.address_id IN (
    SELECT a2.address_id
    FROM officers_2307_2325 o
    LEFT JOIN officers_addresses_2307_2325 oa ON o.officer_id = oa.officer_id
    LEFT JOIN addresses_2307_2325 a2 ON oa.address_id = a2.address_id
    WHERE o.officer_id = 12156293
);
