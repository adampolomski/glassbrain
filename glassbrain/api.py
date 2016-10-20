from flask import Flask, g, _app_ctx_stack
from flask_restful import Resource, Api
from predictor import PredictorRepository
from price import PriceHistoryBuilder, PriceEventRepository
from pymongo import MongoClient
from glassbrain import app
import os

api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        client = MongoClient(os.environ.get('MONGODB_URI', "mongodb://localhost/db"))
        db = g._database = client.get_default_database()
    return db

class Predictions(Resource):
    def get(self, predictor_id):
        predictor = PredictorRepository().get(predictor_id)
        return predictor.predict(range(1, 19))
    
class PriceEvents(Resource):
    def get(self, predictor_id):
        priceEvents = PriceEventRepository(get_db()).list(predictor_id)
        priceHistoryBuilder = PriceHistoryBuilder()
        for event in priceEvents:
            event.extract(priceHistoryBuilder)
        return priceHistoryBuilder.build()
    
    def post(self):
        return

api.add_resource(Predictions, '/v1/predictors/<predictor_id>/predictions')
api.add_resource(PriceEvents, '/v1/predictors/<predictor_id>/prices')