SELECT archival_object.title AS component_title, resource.title AS resource_title, resource.ead_id, archival_object.level_id, date.expression, date.begin, date.end, date.date_type_id, date.label_id, date.certainty_id, date.calendar_id, date.era_id, enumeration_value.value
, CONCAT('/repositories/', resource.repo_id, '/resources/', resource.id) AS Resource_URL
, CONCAT('/repositories/', archival_object.repo_id, '/archival_objects/', archival_object.id) AS Component_URL
FROM archival_object
LEFT JOIN date on archival_object.id=date.archival_object_id
LEFT JOIN enumeration_value on enumeration_value.id=archival_object.level_id
LEFT JOIN resource on archival_object.root_record_id=resource.id
WHERE archival_object.repo_id=2 #use for separating repositories
LIMIT 0, 5000 #use for creating groups of records