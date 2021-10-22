# JWT-token-flask-python

### Installation
Copy from source
```bash
git clone https://github.com/Assylken/Jwt-token-flask-python
```

### Usage

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt
from functools import wraps

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/DB-name'
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
db = SQLAlchemy(app)
```

### Examples

You can login into accounts that are exist in Database table 'Users'
There is already created 3 accounts
| id | username | password | token |
| -- | -------- | -------- | ----- |
| 1  | Assylken |  ******  |       |
| 2  |  Donald  |   Duck   |       |
| 3  |  Admin   |  Admin   |       |

Usage examples:

(/login) - After a successful login, a token will be issued for 15 minutes.
![alt text](https://user-images.githubusercontent.com/79912262/138473268-f29eccf3-9107-4b89-9e9c-715de4934404.png)
(/protected) - On this page you can check the validation of your token
![image](https://user-images.githubusercontent.com/79912262/138473301-0726852f-99eb-4ad3-bfca-a4145c21b0ef.png)
![image](https://user-images.githubusercontent.com/79912262/138473334-88d2cb9d-20bd-4a95-be9e-354d20ce0ab9.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
