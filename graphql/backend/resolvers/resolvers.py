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
def resolve_events(_, info, importance: int = None, user_id: int = None, date: str = None, name: str = None): # Добавляем аргументы
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

@user_type.field("events")
def resolve_user_events(user, info, event_id: int = None, name: str = None, date: str = None, importance: int =None):
    events = [event for event in events_data if event["user_id"] == user["id"]]
    
    if event_id is not None:
        events = [event for event in events if event["id"] == event_id]
    if name is not None:
        events = [event for event in events if event["name"] == name]
    if date is not None:
        events = [event for event in events if event["date"] == date]
    if importance is not None:
        events = [event for event in events if event["importance"] == importance]
    return events
@event_type.field("user")
def resolve_event_user(event, info):
    user = next((user for user in users_data if user["id"] == event["user_id"]), None)
    return user



schema = make_executable_schema(type_defs, query, user_type, event_type)
