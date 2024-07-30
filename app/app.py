# that gives:
# http://127.0.0.1:5000/users
# http://127.0.0.1:5000/users/username?value=marek
# http://127.0.0.1:5000/users/shell?value=/usr/sbin/nologin
# http://127.0.0.1:5000/users/homedir?value=/root


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLAlchemy database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@127.0.0.1/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'Users'
    username = db.Column(db.String(50), primary_key=True, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    gid = db.Column(db.Integer, nullable=False)
    shell = db.Column(db.String(100), nullable=False)
    homedir = db.Column(db.String(255), nullable=False)

# Utility function to dynamically filter by columns
def get_users_by_columns(params):
    query = User.query
    for column_name, value in params.items():
        column = getattr(User, column_name, None)
        if column is None:
            return None, f"Invalid column: {column_name}"
        query = query.filter(column == value)
    return query.all(), None

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([{
        'username': user.username,
        'uid': user.uid,
        'gid': user.gid,
        'shell': user.shell,
        'homedir': user.homedir
    } for user in users])

@app.route('/users/<primary_column>', methods=['GET'])
def get_users(primary_column):
    value = request.args.get('value')
    if not value:
        return jsonify({"error": "No value provided for primary column query"}), 400
    
    query_params = request.args.to_dict()
    query_params.pop('value', None)
    query_params[primary_column] = value

    users, error = get_users_by_columns(query_params)
    if error:
        return jsonify({"error": error}), 400
    
    if users:
        return jsonify([{
            'username': user.username,
            'uid': user.uid,
            'gid': user.gid,
            'shell': user.shell,
            'homedir': user.homedir
        } for user in users])
    else:
        return jsonify({"error": "No users found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
