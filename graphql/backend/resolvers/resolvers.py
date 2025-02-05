from ariadne import QueryType, ObjectType, make_executable_schema, graphql_sync, ScalarType
from storage.storage import users_data, events_data
from schemes.schemes import type_defs


query = QueryType()
user_type = ObjectType("User")
event_type = ObjectType("Event")


@query.field("users")
def resolve_users(_, info):
    return users_data

@query.field("events")
def resolve_events(_, info, importance: int = None, user_id: int = None, name: str = None,date: str = None): # Добавляем аргументы
    filtered_events = events_data  # Начинаем с полного списка

    if importance is not None:
        filtered_events = [event for event in filtered_events if event["importance"] == importance]
    if user_id is not None:
        filtered_events = [event for event in filtered_events if event["user_id"] == user_id]
    if name is not None:
        filtered_events = [event for event in filtered_events if event["name"] == name]
    if date is not None:
        target_date= date
        filtered_events = [event for event in filtered_events if event["date"] == target_date]

    return filtered_events

@query.field("user")
def resolve_user(_, info, id):
    user = next((user for user in users_data if user["id"] == id), None)
    return user

@query.field("event")
def resolve_event(_, info, id):
    event = next((event for event in events_data if event["id"] == id), None)
    return event


schema = make_executable_schema(type_defs, query, user_type, event_type)
