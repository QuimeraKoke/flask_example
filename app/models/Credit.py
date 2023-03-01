from app.config.mysqlconnection import connectToMySQL


class Credit:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.amount = data['amount']
        self.user_id = data['user_id']
        self.announcement_id = data['announcement_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user = None
        self.announcement = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM credits LEFT JOIN announcements ON announcements.id = credits.announcement_id LEFT JOIN ;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('social_credit').query_db(query)
        credits = {}
        for announcement in results:
            announcement['id'] = announcement['announcements.id']
            announcement['created_at'] = announcement['announcements.created_at']
            announcement['updated_at'] = announcement['announcements.updated_at']
            tmp = cls(announcement)
            credits = {}
            user_data = {
                "id": announcement['users.id'],
                "name": announcement['name'],
                "email": announcement['email'],
                "created_at": announcement['users.created_at'],
                "updated_at": announcement['users.updated_at'],
            }
            tmp.user = User(user_data)
            announcements.append( tmp )
        return announcements

    @classmethod
    def create_announcement(cls, title, description, amount, user_id):
        query = "INSERT INTO announcements (title, description, amount, user_id) VALUES ( %(title)s , %(description)s , %(amount)s , %(user_id)s )"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        announcement_id = connectToMySQL('social_credit').query_db(query, {
            "title": title,
            "description": description,
            "amount": amount,
            "user_id": user_id
        })
        return announcement_id

