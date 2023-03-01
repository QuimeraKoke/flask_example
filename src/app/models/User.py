from app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.user_type = data['user_type_id']
        self.balance = data['balance']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('social_credit').query_db(query, {"email": email})
        print(results)
        user = None
        if len(results):
            user = cls(results[0])
        return user

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, user_type_id, balance) values \
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(user_type)s, %(balance)s)"
        results = connectToMySQL('social_credit').query_db(query, data)
        return results
