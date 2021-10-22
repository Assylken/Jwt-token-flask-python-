from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt
from functools import wraps

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Aizhan1212@localhost/PythonAssignment'
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key = True)
    login = db.Column('login', db.Unicode)
    password = db.Column('password', db.Unicode)
    token = db.Column('token', db.Unicode)
    def __init__(self, id, login, password, token):
        self.id = id
        self.login = login
        self.password = password
        self.token = token

        
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        print(token)
        if not token:
            return jsonify({'message' : 'Token is missing'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return "<h1> Hello, Could not verify the token </h1>"
             
        return f(*args, **kwargs)
    return decorated


@app.route('/protected')
@token_required
def protected():
     return "<h1> Hello, token which is provided is correct </h1>"

@app.route('/login')
def login():
        auth = request.authorization 
        if auth:
            usernamedata = Users.query.filter_by(login = auth.username, password = auth.password).first() 
            if usernamedata is not None:
                token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(minutes=15)}, app.config['SECRET_KEY'])
                update_token = Users.query.filter_by(id = usernamedata.id).first()
                token2 = token.decode("utf-8")
                update_token.token = token2
                db.session.commit()
                return jsonify({'token': token.decode('UTF-8')}) 
            else:         
                return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'}) 
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'}) 

if __name__ == '__main__':
    app.run(debug=True)

