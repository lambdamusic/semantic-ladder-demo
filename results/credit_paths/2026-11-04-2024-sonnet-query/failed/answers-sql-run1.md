<parameter name="sql">SELECT * FROM entities WHERE entity_id IN ('CV','VD') OR entity_id ~ '^E[0-9]{2}$' OR name ILIKE '%Cerid%' OR name ILIKE '%Rotam%' OR name ILIKE '%Wonod%' OR name ILIKE '%Vesol%' OR name ILIKE '%Belir%' OR name ILIKE '%Brindle%' OR name ILIKE '%Marlow%' OR name ILIKE '%Orrin%' OR name ILIKE '%Valdoria%' OR name ILIKE '%Corvenia%' OR name ILIKE '%Halden%' ORDER BY entity_id;
SELECT * FROM rating_actions WHERE rated_id IN ('CV','VD') OR rated_id ~ '^(E[0-9]{2}|I0[0-9])$' ORDER BY rated_id, date;
SELECT * FROM instruments WHERE instrument_id NOT LIKE 'I1%' OR guarantor_id IS NOT NULL AND guarantor_id<>'' ORDER BY 1;
```</parameter>
</invoke>