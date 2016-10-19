from flask import Flask
from flask_restful import Resource, Api
from predictor import PredictorRepository
from price import PriceHistoryBuilder, PriceEventRepository
from db import getDb

app = Flask(__name__)
api = Api(app)

predictorRepository = PredictorRepository(db.getDb())
priceEventRepository = PriceEventRepository(db.getDb())

class Predictions(Resource):
    def get(self, predictor_id):
        predictor = predictorRepository.get(predictor_id)
        return predictor.predict(range(1, 19))
    
class PriceEvents(Resource):
    def get(self, predictor_id):
        priceEvents = priceEventRepository.list(predictor_id)
        priceHistoryBuilder = PriceHistoryBuilder()
        for event in priceEvents:
            event.extract(priceHistoryBuilder)
        return priceHistoryBuilder.build()
    
    def post(self):
        return

api.add_resource(Predictions, '/v1/predictors/<predictor_id>/predictions')
api.add_resource(PriceEvents, '/v1/predictors/<predictor_id>/prices')

if __name__ == '__main__':
    app.run(debug=True)