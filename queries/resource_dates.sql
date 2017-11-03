SELECT date.resource_id, date.date_type_id, date.expression, date.begin, date.end, date.label_id, date.era_id, date.calendar_id, resource.repo_id, resource.title, resource.identifier, resource.ead_id, enumeration_value.value 
, CONCAT('/repositories/', resource.repo_id, '/resources/', resource.id) AS Resource_URL
FROM resource
LEFT JOIN date on resource.id=date.resource_id 
LEFT JOIN enumeration_value on enumeration_value.id=date.date_type_id
WHERE resource_id IS NOT NULL