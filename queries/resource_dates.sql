SELECT date.resource_id, date.date_type_id, date.expression, date.begin, date.end, resource.repo_id, resource.ead_id, enumeration_value.value 
FROM resource
LEFT JOIN date on resource.id=date.resource_id 
LEFT JOIN enumeration_value on enumeration_value.id=date.date_type_id
WHERE resource_id IS NOT NULL