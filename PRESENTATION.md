# Fusemachines Training, Flask-MongoDB Overview
We'll go through basics of building backend server with flask. We wont go too much into detail but enough to get started and use Flask to serve ML models. Feel free to dive in and ask questions.

## Technology - Web development Stack
1. Frontend
		- How things looks, contents&webpages:  HTML,CSS, JS
2. Backend
		- How things works, Logic and data: Java, Python, PHP, Ruby
3. DevOps
4. Mobile App
5. Databases

## RESTful APIs
- API: way to communicate one software to another
- REpresentational State Transfer
- a software architectural style that defines a set of constraints to be used for creating Web services.
#### Characteristics of REST service
1.  **Client-server based architecture :**_Client/server architecture is a computing model in which the server hosts, delivers and manages most of the resources and services to be consumed by the client._
2.  **Stateless :** _A REST HTTP request consists of all the data needed by the server to understand and give back the response. Once a request is served, the server doesn't remember if the request has arrived after a while._$$
3.  **Cacheable :** Cache is a component that stores data so future requests for the data can be served faster. The database can be a potential tuning piece in a web application. In order to scale an application well, we need to cache content and deliver it as a response._
4.  **Multiple layered system :** _The REST API can be served from multiple servers. One server can request the other, and so forth._
5.  **Representation of resources :** _The REST API provides the uniform interface to talk to. It also has the advantage of requesting a specific data format as the response. The Internet Media Type (MIME type) can tell the server that the requested resource is of that particular type._

### Best Practices for RESTful APIs
1. Always apply versioning for your API
2. Use meaningful HTTP status codes (200 OK, 404 NotFOund, 201 Created etc.)
3. Secure data with authentication

## HTTP Verbs and CRUD
- GET: Read
- POST: Create
- PUT: Update
- DELETE : Delete

## Flask
#### Introduction
1. Microframework for python web development
2. Designed for expansion
3. Includes web server(WSGI) and template(Jinja) engine
		a. WSGI: Web Server Gateway Interface, a simple and universal interface between web servers and web applications or frameworks
		b. Jinja2: templating language for Python, modelled after Django’s templates
4. Easy to add new functionality via extensions
	#### Common Extensions
	1. Admin
	2. Database
	3. Authentication
	4. Email
	5. Ecommerce

#### Flask Features
1. Builtin development server and debugger
2. RESTful request dispatching
3. Templating
4. Secure cookie handling
5. Integrated support for testing

#### Handson Session
1. How to setup flask and create your first Flask application.
	- mkdir sample_flask
	- cd sample_flask
	- virtualenv .venv/
	- source .venv/bin/activate
	- pip install flask
	Write code in basic_app.py
	Can be served with any WSGI HTTP server.

Resources:

1. [Fusemachines Presentation Slides](https://docs.google.com/presentation/d/1uxqeL11U1VsnmMV1ZwcdyGUgzSSDhaUuJs38otCtIvE/edit?usp=sharing)
2. [Flask Official Documentation](http://flask.pocoo.org/docs/1.0/)
3. [MogoDB Official Tutorial](https://docs.mongodb.com/manual/tutorial/)
4. [MongoDB CRUD operations with Python](https://micropyramid.com/blog/mongodb-crud-operations-with-python-pymongo/)
