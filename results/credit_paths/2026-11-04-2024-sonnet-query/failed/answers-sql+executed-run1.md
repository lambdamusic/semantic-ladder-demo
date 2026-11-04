<invoke name="sql">
SELECT entity_id,name,country,entity_type,parent_id,ultimate_parent_id,record_ids FROM entities WHERE entity_id LIKE 'E0%' OR entity_id IN ('E10','E11') OR regexp_matches(entity_id,'^E[0-9]{2}$') ORDER BY entity_id;
</invoke>



<invoke name="sql">
SELECT * FROM ratings WHERE rated_id IN (SELECT entity_id FROM entities WHERE regexp_matches(entity_id,'^E[0-9]{2}$')) OR rated_id IN ('I01','I02','I03','I04','I05','I06','I07','I08') ORDER BY rated_id, rating_type, ccy_basis, valid_from;
</invoke>



<invoke name="sql">
SELECT * FROM entities WHERE name ILIKE '%Cerid%' OR name ILIKE '%Rotam%' OR name ILIKE '%Belir%' OR name ILIKE '%Wonod%' OR name ILIKE '%Vesol%' OR name ILIKE '%Orrin%' OR name ILIKE '%Brindle%' OR name ILIKE '%Pellam%' ORDER BY entity_id;
</invoke>



<invoke name="sql">
SELECT * FROM instruments WHERE instrument_id NOT LIKE 'I1%' OR guarantor_id<>'' OR credit_risk_of<>issuer_id OR description ILIKE '%Cross%';
</invoke>