import datetime


users_data = [
    {"id": 1, "name": "Alice", "email": "alice@gmail.com", "password": "pass"},
    {"id": 2, "name": "Bob", "email": "bob@gmail.com", "password": "secret"},
]

events_data = [
    {"id": 1, "date": datetime.datetime(2025, 1, 31, 12, 30, 0), "name": "univercity", "importance": 5, "user_id": 1},
    {"id": 2, "date": datetime.datetime(2025, 2, 23, 11, 0, 0), "name": "exam", "importance": 8, "user_id": 1},
    {"id": 3, "date": datetime.datetime(2025, 3, 15, 14, 0, 0), "name": "picnic", "importance": 5, "user_id": 1},
    {"id": 4, "date": datetime.datetime(2025, 4, 20, 10, 0, 0), "name": "conference", "importance": 8, "user_id": 2},
    {"id": 5, "date": datetime.datetime(2025, 5, 10, 16, 0, 0), "name": "party", "importance": 3, "user_id": 1},
]