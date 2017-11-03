SELECT date.id, date.archival_object_id, archival_object.root_record_id, archival_object.repo_id, date.expression, date.begin, date.end FROM date 
LEFT JOIN enumeration_value on enumeration_value.id=date.expression
LEFT JOIN archival_object on date.archival_object_id=archival_object.id
WHERE date.expression IS NOT NULL
AND date.archival_object_id IS NOT NULL
AND archival_object.repo_id=4 #insert repo id
LIMIT 0, 5000
