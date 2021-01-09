from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

client = app.test_client()

accounts = [
    {
        "id": 1,
        "login": "user_1",
        "password": "123"
    },
    {
        "id": 2,
        "login": "user_2",
        "password": "1234"
    },
    {
        "id": 3,
        "login": "user_3",
        "password": "12345"
    },
    {
        "id": 4,
        "login": "user_4",
        "password": "123456"
    },
    {
        "id": 5,
        "login": "user_5",
        "password": "1234567"
    },
    {
        "id": 6,
        "login": "root",
        "password": "root"
    }
]


@app.route('/api/accounts', methods=['GET'])
def get_account_list():
    """Get all user accounts"""
    return jsonify(accounts), 200

@app.route('/api/accounts', methods=['POST'])
def create_account():
    """Create new user account"""
    new_account = request.json
    accounts.append(new_account)
    return jsonify(accounts), 201

@app.route('/api/accounts/<int:account_id>/password', methods=['PUT'])
def update_user_password(account_id):
    """Update password for user account"""
    item = next((x for x in accounts if x['id'] == account_id), None)
    params = request.json
    if not item:
        return {'message': 'No users with this id'}, 400
    item.update(params)
    return item

@app.route('/api/accounts/<int:account_id>', methods=['DELETE'])
def delete_user_account(account_id):
    """Delete user account"""
    idx, _ = next((x for x in enumerate(accounts)
                   if x[1]['id'] == account_id), (None, None))
    accounts.pop(idx)
    return '', 204

@app.route('/api/accounts/login', methods=['POST'])
def login_user():
    """Checking user in system"""
    item = next((x for x in accounts if x['login'] == request.json['login']
                 and x['password'] == request.json['password']), None)
    if not item:
        return {'message': 'User not found in system'}, 400

    return 'User log in system' ,request.json, 200

if __name__ == '__main__':
    app.run()
