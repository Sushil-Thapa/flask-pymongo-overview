### Designing RESTful API with Python-Flask and MongoDB

This example project demonstrate how to design RESTful API with Python-Flask and
MongoDB.

First you'll need to get the source of the project. You could do this by cloning the repository:

```bash
# Get the project code
git clone https://github.com/Sushil-Thapa/flask-pymongo-overview.git
```

*NOTE: While working with Python, we would recommend to use virtual environment
to keep all the project's dependencies isolated from other projects.*

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

If you're using Linux, you could use the following to start the server.

```bash
sudo service mongod start
```

#### Config the application

Change the `DBNAME` in the config file according to the database name you are using.

##### Start the application

```bash
python run.py
```

Once the application is started, go to [localhost](http://localhost:5000/) on Postman and explore the APIs.
