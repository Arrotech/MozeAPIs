**School Portal**

Create a school portal with python, flask, postgres, HTML, CSS and JavaScript.


Below are the Endpoints that have been created.

| EndPoints       | Functionality  | HTTP Method  |
| ------------- |:-------------:| -----:|
| /api/v1/portal/auth/register | Create user| POST |
| /api/v1/portal/auth/login | Login to account |GET|
| /api/v1/portal/exams |  Add Exams | POST |
| /api/v1/portal/exams | Fetch all Exams | GET |
| /api/v1/portal/exams/<int:exam_id> | Fetch one Exam | GET |
| /api/v1/portal/exams/<int:exam_id> | Edit an Exam | PUT |
| /api/v1/portal/exams/<int:exam_id> | Delete an Exam | DELETE |
| /api/v1/portal/users/<int:user_id> | Fetch a specific user | GET |



**TOOLS TO BE USED IN THE CHALLENGE**
1. Server-Side Framework:[Flask Python Framework](http://flask.pocoo.org/)
2. Linting Library:[Pylint, a Python Linting Library](https://www.pylint.org/)
3. Style Guide:[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
4. Testing Framework:[PyTest, a Python Testing Framework](https://docs.pytest.org/en/latest/)
5. Testing Framework:[Coverage, a Python Testing Framework](https://coverage.readthedocs.io/en/v4.5.x/)



**Requirements**

		Install python

		Install pip

		virtualenv

		Postgres


**How to run the application**
 1. Make a new directory on your computer
 2. `git clone` this  <code>[repo](https://github.com/Arrotech/Portal/)</code>
 3. Create virtual environment by typing this in the terminal - virtualenv -p python3 venv
 4. run `pip install -r requirements.txt` on the terminal to install the dependencies
 5. Create a .env file on the root folder of the project. Add the following  environmental variables.



 		source venv/bin/activate

		export FLASK_APP=run.py

		export FLASK_DEBUG=1

		export APP_SETTINGS="testing"

		export FLASK_ENV=development

		export DB_NAME="test_portal"

		export DB_USER="postgres"

		export DB_HOST="localhost"

		export DB_PASSWORD="postgres"

		export SECRET_KEY="thisisarrotech"

		export DB_TEST_NAME="test_politico"

 6. Then type on the terminal ```source .env``` to activate the environment and also to export all the environment variables.
 7. Then type on the terminal ```flask run``` to start and run the server.



**Author**

     Harun Gachanja Gitundu
