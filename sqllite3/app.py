from flask import Flask, render_template, request, jsonify
import sqlite3
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
# Database connection
def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table (auto run once)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def home():
    return render_template('index.html')





# Get all employees (Read)
@app.route('/api/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    employees = conn.execute('SELECT * FROM employees').fetchall()
    conn.close()
    return jsonify([dict(row) for row in employees])

# Add employee (Create)
@app.route('/api/employees', methods=['POST'])
def add_employee():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO employees (name, age, department) VALUES (?, ?, ?)',
                 (data['name'], data['age'], data['department']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Employee added'})

# Delete employee
@app.route('/api/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Employee deleted'})

# Update employee
@app.route('/api/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    conn = get_db_connection()
    conn.execute('UPDATE employees SET name = ?, age = ?, department = ? WHERE id = ?',
                 (data['name'], data['age'], data['department'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Employee updated'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
