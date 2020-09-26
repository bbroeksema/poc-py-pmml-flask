# PY-PMML-FLASK

A small proof-of-concept to get some hands-on experience with exposing PMML models through a flask interface.

## Getting started

```bash
$ git clone 
$ python -m venv venv
$ source venv/bin/activate
$ pip install -R requirements.txt
$ cd py-pmml-flask
$ python main.py
```

At this point you should have a flaks service running. 
Now you can sent a request as follows:

```bash
$ curl --header "Content-Type: application/json" \
  -X POST \
  --data @data/request.json \
  http://localhost:5000/predict | jq
```
