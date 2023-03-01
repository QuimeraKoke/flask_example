from app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.user_type = data['user_type_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_user(cls, email, password):
        query = "SELECT * FROM user WHERE email = %(email)s AND password=%(password)s;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('social_credit').query_db(query, {"email": email, "password": password})
        user = None
        if len(results):
            user = cls(results[0])
        return user
