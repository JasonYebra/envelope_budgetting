from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Need_goal:
        def __init__(self, data):
            self.id = data['id']
            self.user_id = data['user_id']
            self.name = data['name']
            self.deadline = data['deadline']
            self.goal_amount = data['goal_amount']
            self.current_amount = data['current_amount']
            self.description = data['description']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']

            self.user = {}
        
        @classmethod
        def add_need_goal(cls, data):
            query = "INSERT INTO needs(user_id, name, deadline, goal_amount, current_amount, description) VALUE (%(user_id)s, %(name)s, %(deadline)s, %(goal_amount)s, %(current_amount)s, %(description)s);"
            result = connectToMySQL('budget_schema').query_db(query, data)
            return result
        @classmethod
        def get_need_goals(cls,data):
            query = "SELECT * FROM needs LEFT JOIN users ON users.id = needs.user_id WHERE users.id = %(user_id)s;"
            result = connectToMySQL('budget_schema').query_db(query, data)
            all_needGoals = []
            for item in result:
                needGoal = cls(item)
                user_data = {
                    "id": item['id'],
                    "first_name": item['first_name'],
                    "last_name": item['last_name'],
                    "email": item['email'],
                    "username": item['username'],
                    "password": item['password'],
                    "created_at": item['created_at'],
                    "updated_at": item['updated_at']
                    }
                needGoal.user = user.User(user_data)
                all_needGoals.append(needGoal)
            return all_needGoals

        @classmethod
        def get_one_goal(cls,data):
            query = "SELECT * FROM needs LEFT JOIN users ON users.id = needs.user_id WHERE needs.id = %(id)s;"
            result = connectToMySQL('budget_schema').query_db(query, data)
            need_goal = cls(result[0])
            user_data = {
                "id": result[0]['id'],
                "first_name": result[0]['first_name'],
                "last_name": result[0]['last_name'],
                "email": result[0]['email'],
                "username": result[0]['username'],
                "password": result[0]['password'],
                "created_at": result[0]['created_at'],
                "updated_at": result[0]['updated_at']
            }
            need_goal.user = user.User(user_data)
            return need_goal

        @classmethod
        def get_one_user_goal(cls,data):
            query = "SELECT * FROM needs LEFT JOIN users ON users.id = needs.user_id WHERE users.id = %(id)s;"
            result = connectToMySQL('budget_schema').query_db(query, data)
            need_goal = cls(result[0])
            user_data = {
                "id": result[0]['id'],
                "first_name": result[0]['first_name'],
                "last_name": result[0]['last_name'],
                "email": result[0]['email'],
                "username": result[0]['username'],
                "password": result[0]['password'],
                "created_at": result[0]['created_at'],
                "updated_at": result[0]['updated_at']
            }
            need_goal.user = user.User(user_data)
            return need_goal

        @classmethod
        def update_current_amount(cls, data):
            query = "UPDATE needs SET current_amount = %(new_amount)s WHERE needs.id = %(id)s"
            result = connectToMySQL('budget_schema').query_db(query, data)
            return result

        @classmethod
        def update_goal(cls,data):
            query = "UPDATE needs SET name = %(name)s, deadline = %(deadline)s, goal_amount = %(goal_amount)s, description = %(description)s WHERE needs.id = %(id)s"
            result = connectToMySQL('budget_schema').query_db(query, data)
            return result

        # @classmethod
        # def get_one(cls, data):
        #     query = "SELECT * FROM needs WHERE needs.id = %(id)s;"
        #     result = connectToMySQL('budget_schema').query_db(query, data)
            
        #     return result
