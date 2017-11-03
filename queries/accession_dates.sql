SELECT date.accession_id, date.date_type_id, date.expression, date.begin, date.end, accession.repo_id, accession.identifier, enumeration_value.value 
FROM accession
LEFT JOIN date on accession.id=date.accession_id
LEFT JOIN enumeration_value on enumeration_value.id=date.date_type_id
WHERE accession_id IS NOT NULL