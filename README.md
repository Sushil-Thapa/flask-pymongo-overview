## Designing RESTful API with Python-Flask and MongoDB

This example project demonstrate how to design RESTful API with Python-Flask and
MongoDB. This overview is a part of training program at Fusemachines.

### Assets
1. [Presentation Slides](https://docs.google.com/presentation/d/1uxqeL11U1VsnmMV1ZwcdyGUgzSSDhaUuJs38otCtIvE/edit?usp=sharing)|[PDF](assets/Fusemachines%20Flask_Pymongo%20Training.pdf)
2. [Presentation Document](PRESENTATION.md)


### Installation
##### Cloning the repository
```bash
# Get the project code
git clone https://github.com/Sushil-Thapa/flask-pymongo-overview.git
```

*NOTE: Please use virtual environment to keep all the project's dependencies isolated from other projects.*

##### Create your local environment
```bash
virtualenv -p python3 .venv
source .venv/bin/activate
```

##### Install dependencies

```python
pip install -r requirements.txt
```

##### Start MongoDB Server

If you're using Linux, you could use the following to start the server if you already haven't.

```bash
sudo service mongod start
```

#### Config the application

Change the `MONGO_DBNAME` in the config file according to the database name you are using.

### Start the application

```bash
python run.py
or
gunicorn -b :5000 -w 2 -t 120 app:app
or
FLASK_APP=app.py flask run
```

Once the application is started, go to [localhost](http://localhost:5000/) on Postman and explore the APIs. 
Sample postman collection schema (version 2.1) is [uploaded here.](data/Fuse-Flask-Training.postman_collection.json)


### Using Docker container
- Build container 
  `docker build -t my_docker:latest .`

- Run container 
  `docker run -ti -p 8080:8080 my_docker:latest `