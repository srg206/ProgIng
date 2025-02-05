from ariadne import QueryType, ObjectType, make_executable_schema, graphql_sync, ScalarType
from storage.storage import users_data, events_data
from schemes.schemes import type_defs


query = QueryType()
user_type = ObjectType("User")
event_type = ObjectType("Event")
