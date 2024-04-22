from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for demonstration purposes
users = []

# Route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    user_data = request.get_json()
    users.append(user_data)
    return jsonify({'message': 'User registered successfully'}), 201

# Route to retrieve user information
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

# Route to update user information
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user.update(user_data)
            return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
