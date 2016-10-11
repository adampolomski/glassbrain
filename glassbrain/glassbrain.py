from flask import Flask
from flask_restful import Resource, Api
from predictor import PredictorRepository

app = Flask(__name__)
api = Api(app)

predictorRepository = PredictorRepository()

class Predictions(Resource):
    def get(self, predictor_id):
        predictor = predictorRepository.get(predictor_id)
        return predictor.predict(range(1, 19))

api.add_resource(Predictions, '/v1/predictors/<predictor_id>/predictions')

if __name__ == '__main__':
    app.run(debug=True)