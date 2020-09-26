from pypmml import Model

_model = Model.fromFile('./resources/model.pmml')


def predict(X: object):
    return _model.predict(X)
