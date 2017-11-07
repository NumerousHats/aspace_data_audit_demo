select CONCAT('/config/enumeration_values/', ev.id) as URI
                , ev.position
                , ev.value
from enumeration_value ev
WHERE ev.enumeration_id = 14