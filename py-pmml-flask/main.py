import flask
from logging.config import dictConfig

import model

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'level': 'INFO',
        },
        'another.module': {
            'level': 'DEBUG',
        },
    }
}

dictConfig(DEFAULT_LOGGING)


app = flask.Flask("py-pmml-flask")

@app.route("/predict", methods=["POST"])
def predict_batch():
    predictions = []
    for x in flask.request.json:
        y_hat = model.predict(x)
        predictions.append({ 
            "predictedClass": y_hat["predicted_class"],
            "probability": y_hat["probability"]
        })

    print(predictions)
    return flask.jsonify(predictions)

def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
