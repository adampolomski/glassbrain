from flask import Flask, g
from flask_restful import Resource, Api
from glassbrain.domain.predictor import PredictorRepository
from glassbrain.domain.price import PriceHistoryBuilder, PriceEventRepository
import os

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
    #MONGODB_URI=os.environ.get('MONGODB_URI', None)
))

#def database():
#    db = getattr(g, '_database', None)
#    if db is None:
#        if app.config["MONGODB_URI"] is None:
#            return None
#        client = MongoClient(app.config["MONGODB_URI"])
#        db = g._database = client.get_default_database()
#    return db


class Predictions(Resource):
    def get(self, predictor_id):
        predictor = PredictorRepository().get(predictor_id)
        return map( lambda day: (day, predictor._predict(day)), range(1, 19))
    
class Predictor(Resource):
    #def get(self, predictor_id):
    #    price_events = price_events_repository().list(predictor_id)
    #    price_history_builder = PriceHistoryBuilder()
    #    for event in price_events:
    #        event.extract(price_history_builder)
    #    return price_history_builder.build()
    
    def put(self, predictor_id):
        return {}, 201, {"Location": "/v1/predictors/" + predictor_id}

api = Api(app)
api.add_resource(Predictor, '/v1/predictors/<predictor_id>')
api.add_resource(Predictions, '/v1/predictors/<predictor_id>/predictions')

    