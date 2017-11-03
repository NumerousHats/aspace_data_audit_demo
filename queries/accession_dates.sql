SELECT date.accession_id, date.date_type_id, date.expression, date.begin, date.end, date.era_id, date.calendar_id, date.label_id, accession.repo_id, accession.title, accession.identifier, enumeration_value.value 
, CONCAT('/repositories/', accession.repo_id, '/accessions/', accession.id) AS Accession_URL
FROM accession
LEFT JOIN date on accession.id=date.accession_id
LEFT JOIN enumeration_value on enumeration_value.id=date.date_type_id
WHERE accession_id IS NOT NULL