# hellofastapi
Hello World FastAPI application for demo and test purposes

## How to run the first time

First, git clone this repo:

````
git clone https://github.com/aruljohn/hellofastapi.git
````

Next, create a virtual environment:

````
cd hellofastapi
virtualenv venv
pip install -r requirements.txt
````

## Running the application

To run this application:

````
uvicorn main:app
````

Your output should be something like this:

````
$ uvicorn main:app
INFO:     Started server process [9293]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
````

To run this application in debug mode:

````
uvicorn main:app --debug
````

Your output should be something like this:

````
$ uvicorn main:app --debug
INFO:     Will watch for changes in these directories: ['/Users/arul/github/hellofastapi']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [9304] using statreload
INFO:     Started server process [9306]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
````

## Access the FastAPI application using browser

Go to http://localhost:8000/

You should get output like this:

![image](https://user-images.githubusercontent.com/3209045/132408202-800d6c5e-7c3e-4f5c-bba7-c40a2c020691.png)

Go to http://localhost:8000/message

You should get output like this:

![image](https://user-images.githubusercontent.com/3209045/132408295-d8a39c6d-84c2-49de-a1af-f823f06f14ba.png)


## Stopping the application

To stop this application, press CTRL+C.

After stopping, get out of the virtual environment:

````
deactivate
````
