type_defs = """
    scalar DateTime

    type User {
        id: Int!
        name: String!
        email: String!
        password: String!
        events(id: Int, name: String, date: DateTime, importance: Int): [Event!]!
    }

    type Event {
        id: Int!
        date: DateTime!
        name: String!
        importance: Int!
        user: User!
    }

    type Query {
        users: [User!]!
        events(importance: Int, name: String): [Event!]! # Добавляем аргументы
        user(id: Int!): User
        event(id: Int!): Event
    }
"""