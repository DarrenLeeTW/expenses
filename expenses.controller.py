from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = [
    {
        'id': 1,
        'date': '2024-05-01',
        'description': 'Grocery shopping',
        'amount': 45.30,
        'category': 'Food'
    },
    {
        'id': 2,
        'date': '2024-05-03',
        'description': 'Gas',
        'amount': 60.00,
        'category': 'Transportation'
    },
    {
        'id': 3,
        'date': '2024-05-05',
        'description': 'Dinner at restaurant',
        'amount': 85.50,
        'category': 'Entertainment'
    }
]


@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses), 200

@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    if not data or not all(key in data for key in ('date', 'description', 'amount', 'category')):
        return jsonify({"error": "Invalid input"}), 400
    expense = {
        'id': len(expenses) + 1,
        'date': data['date'],
        'description': data['description'],
        'amount': data['amount'],
        'category': data['category']
    }
    expenses.append(expense)
    return jsonify(expense), 201

@app.route('/api/expenses/<int:id>', methods=['GET'])
def get_expense(id):
    expense = next((e for e in expenses if e['id'] == id), None)
    if expense is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(expense), 200

@app.route('/api/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    expense = next((e for e in expenses if e['id'] == id), None)
    if expense is None:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data or not all(key in data for key in ('date', 'description', 'amount', 'category')):
        return jsonify({"error": "Invalid input"}), 400
    expense.update({
        'date': data['date'],
        'description': data['description'],
        'amount': data['amount'],
        'category': data['category']
    })
    return jsonify(expense), 200

@app.route('/api/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    global expenses
    expenses = [e for e in expenses if e['id'] != id]
    return 'success', 204

if __name__ == '__main__':
    app.run(debug=True)
