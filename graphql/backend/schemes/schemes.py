type_defs = """
    type User {
        id: Int
        name: String
        email: String
        password: String
        events(id: Int, name: String, date: String, importance: Int): [Event]
    }

    type Event {
        id: Int
        date: String
        name: String
        importance: Int
        user: User
    }

    type Query {
        users: [User]
        events(importance: Int,user_id: Int, name: String, date: String ): [Event]
        user(id: Int): User
        event(id: Int): Event
    }
"""