from flask import Flask, g, request
from flask_restful import Resource, Api
from glassbrain.domain.predictor import PredictorRepository
from glassbrain.domain.price import PriceHistoryBuilder, PriceEventRepository
import os

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
    #MONGODB_URI=os.environ.get('MONGODB_URI', None)
))

def database():
    return None

#    db = getattr(g, '_database', None)
#    if db is None:
#        if app.config["MONGODB_URI"] is None:
#            return None
#        client = MongoClient(app.config["MONGODB_URI"])
#        db = g._database = client.get_default_database()
#    return db

def predictor_repository():
    return PredictorRepository()

class Predictions(Resource):
    def get(self, predictor_id):
        p_from = request.args.get('from', 0, int)
        p_step = request.args.get('step', 1, int)
        p_count = request.args.get('count', 10, int)
        
        predictor = predictor_repository().get(predictor_id)
        return map( lambda day: (day, predictor._predict(day)), range(p_from, p_from + p_count * p_step, p_step))
    
class Predictor(Resource):
    
    def put(self, predictor_id):
        return {}, 201, {"Location": "/v1/predictors/" + predictor_id}

api = Api(app)
api.add_resource(Predictor, '/v1/predictors/<predictor_id>')
api.add_resource(Predictions, '/v1/predictors/<predictor_id>/predictions')

    