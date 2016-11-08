from sklearn import linear_model
import math
import collections
import json

'''
@author: Adam Polomski
'''
class LinearSplinesPredictor(object):
    '''
    Basic price predictor with linear splines.
    '''

    def __init__(self, knots, weights, intercept = 0):
        self._knots = knots
        self._weights = weights
        self._intercept = intercept

    def predict(self, X):
        if isinstance(X, collections.Iterable):
            return map(self._predict, X)
        return self._predict(X)
        
    def _predict(self, x):
        xMapped = [x] + map( lambda knot: max(0, x - knot), self._knots)
        return round(sum( w * k for (w, k) in zip(xMapped, self._weights) ) + self._intercept, 2)
    
    def state(self, state):
        return state(self._knots, self._weights, self._intercept)
    
def fit(prices, step, regression):
    best_score = None
    best_predictor = None
    
    for l_knot in range(1, int(prices[-3,0]), step):
        for r_knot in range(l_knot + 1, int(prices[-2,0]), step):
            X = _knotify([l_knot, r_knot], prices[:,0])
            (clf, score) = regression(X, prices[:,1])
            
            if best_predictor is None or score > best_score:
                best_predictor = LinearSplinesPredictor([l_knot, r_knot], clf.coef_, clf.intercept_)
                best_score = score
                
    return best_predictor

def _knotify(knots, days):
    X = [[x, max(0, x-knots[0]), max(0, x-knots[1])] for x in days]
    return X

def linear_regression(X, prices):
    clf = linear_model.LinearRegression();
    clf.fit(X, prices)
    return (clf, clf.score(X, prices))

class PredictorRepository(object):
    
    def __init__(self, db):
        self._db = db
        
    def get(self, identifier):
        data = self._db.get(identifier)
        if data is not None:
            jprd = json.loads(data)
            return LinearSplinesPredictor(jprd["k"], jprd["w"], jprd["i"])
        return None
    
    def store(self, identifier, predictor):
        self._db.set(identifier, predictor.state(self._state))
        return
    
    def delete(self, identifier):
        self._db.delete(identifier)
        return
    
    def _state(knots, weights, intercept):
        return json.dumps({k:knots, w:weights, i:intercept})
