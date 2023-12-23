from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


data = {
    '1075920':{'name':'Noah Brown', 'balance': 105},
    '9306783':{'name':'Brent Henry', 'balance': 6096},    
    '7529366':{'name':'Ellen Johnson', 'balance': 120355}    
}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

class DemoApiEndpoint(Resource):
    def __init__(self):
        self.post_args = reqparse.RequestParser()
        self.post_args.add_argument("id",
                                    type=str,
                                    help="You must include a name string with this post request.",
                                    required=True)

    def post(self):
        args = self.post_args.parse_args()
        name = args['name']
        return {
            "message": f'Nice to meet you, {name}!'
        }


class getBalance(Resource):
    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument("id",
                                    type=str,
                                    help="You must include an id string with this post request.",
                                    required=True)

    def get(self):
        args = self.get_args.parse_args()
        user_id = args['id']
        return {
            "message": 'Hello, {}! Your balance is {}.'.format(data[user_id]['name'], data[user_id]['balance'])
        }


class Deposit(Resource):
    def __init__(self):
        self.post_args = reqparse.RequestParser()
        self.post_args.add_argument("id",
                                    type=str,
                                    help="You must include an id with this post request.",
                                    required=True)
        self.post_args.add_argument("amount",
                                    type=str,
                                    help="You must include an amount with this post request.",
                                    required=True)

    def post(self):
        args = self.post_args.parse_args()
        user_id = args['id']
        print("here2")
        if (user_id not in data.keys()):
            return {
                "message": 'id not found.'
            }            
        amount = int(args['amount'])
        if (amount > 10000):
            return {
                "message": 'You cannot deposit more than $10,000 in a single transaction.'
            }
        else:
            data[user_id]['balance'] += amount       
            return {
                "message": 'Deposit of {} successful! Your balance is now {}.'.format(amount, data[user_id]['balance'])
            }        

class Withdraw(Resource):
    def __init__(self):
        self.post_args = reqparse.RequestParser()
        self.post_args.add_argument("id",
                                    type=str,
                                    help="You must include an id with this post request.",
                                    required=True)
        self.post_args.add_argument("amount",
                                    type=str,
                                    help="You must include an amount with this post request.",
                                    required=True)

    def post(self):
        args = self.post_args.parse_args()
        user_id = args['id']

        if (user_id not in data.keys()):
            return {
                "message": 'id not found.'
            }            
        amount = int(args['amount'])
        balance = data[user_id]['balance']
        if (amount > (balance*.9)):
            return {
                "message": 'You cannot withdraw more than 90 percent of your account balance in a single transaction.'
            }
        elif (balance-amount < 100):
            return {
                "message": 'You cannot have less than $100 in your account at any point.'
            }            
        else:
            data[user_id]['balance'] -= amount       
            return {
                "message": 'Withdrawal of {} successful. Your balance is now {}.'.format(amount, data[user_id]['balance'])
            }      

api.add_resource(DemoApiEndpoint, "/api/DemoApiEndpoint")
api.add_resource(Deposit, "/api/Deposit")
api.add_resource(Withdraw, "/api/Withdraw")
api.add_resource(getBalance, "/api/getBalance")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
