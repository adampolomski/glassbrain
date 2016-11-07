from sklearn import linear_model
import math

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

    def predict_all(self, X):
        return map(self.predict, X)
        
    def predict(self, x):
        xMapped = [x] + map( lambda knot: max(0, x - knot), self._knots)
        return round(sum( w * k for (w, k) in zip(xMapped, self._weights) ) + self._intercept, 2)

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
        predictor = self._db.get(identifier)
        if predictor is not None:
            return LinearSplinesPredictor([1,2,3], [1,2,3,4])
        return None
    
    def store(self, identifier, predictor):
        self._db.set(identifier, predictor)
        return
