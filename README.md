# authentication-django

setup commands

	take cmd or terminal to folder 'authentication-django'
	command: - authenv\Scripts\activate
	command: - cd authentication
	command: - python manage.py makemirations
	command: - python manage.py migrate

create admin user (optional)

	command: - python manage.py createsuperuser
		enter fileds: - username, email, password, confirm password

run project

	command: - python manage.py runserver
		will show one link e.g.  http://127.0.0.1:8000/ currently we will call 'localhost:8000/'

make registration

	url 'localhost:8000/registration/'
	method POST
	parameters: - username, email, password, last_name
		here registration make login as well 
		so will return token e.g. 'jgh45g6h7jg5h5j6h7j6hjj6h7k7jh4h4g4' save this token

make login (optional)

	url 'localhost:8000/login/'
	method POST
	parameters: - username, password
		will return token e.g. 'jgh45g6h7jg5h5j6h7j6hjj6h7k7jh4h4g4' save this token

get user information

	url 'localhost:8000/user_info/'
	method GET
	pass token in header like below
		'Authorization': - 'Token jgh45g6h7jg5h5j6h7j6hjj6h7k7jh4h4g4'
	will get 
		info : {
    			'email', 'name', 'last_name',
    		}


