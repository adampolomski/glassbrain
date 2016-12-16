from flask import Flask, g, request
from flask_restful import Resource, Api
from glassbrain.domain.predictor import PredictorRepository, LinearSplinesPredictor, NoSuchPredictor
from glassbrain.domain.price import PriceHistoryBuilder, PriceEventRepository
import os
import redis

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(
    REDIS_URL=os.environ.get('REDIS_URL', None)
))

def database():
    db = getattr(g, '_database', None)
    if db is None:
        if app.config["REDIS_URL"] is None:
            return None
        db = g._database = redis.from_url(app.config["REDIS_URL"])
    return db

def predictor_repository():
    return PredictorRepository(database())

class Predictions(Resource):
    def get(self, predictor_id):
        p_from = request.args.get('from', 0, int)
        p_step = request.args.get('step', 1, int)
        p_count = request.args.get('count', 10, int)
        
        predictor = predictor_repository().get(predictor_id)
        if predictor is None:
            return 404
        return list(map( lambda day: (day, predictor.predict(day)), range(p_from, p_from + p_count * p_step, p_step)))
    
class Predictor(Resource):
    
    def put(self, predictor_id):
        predictor_repository().store(predictor_id, LinearSplinesPredictor([1, 2, 3], [1, 2, 3, 4]))
        return {}, 201, {"Location": "/v1/predictors/" + predictor_id}
    
    def delete(self, predictor_id):
        try:
            predictor_repository().delete(predictor_id)
            return {}, 200
        except NoSuchPredictor:
            return {}, 404

api = Api(app)
api.add_resource(Predictor, '/v1/predictors/<predictor_id>')
api.add_resource(Predictions, '/v1/predictors/<predictor_id>/predictions')

    