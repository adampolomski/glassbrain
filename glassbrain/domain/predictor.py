from sklearn import linear_model
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

    def predictAll(self, X):
        return map(self.predict, X)
        
    def predict(self, x):
        xMapped = [x] + map( lambda knot: max(0, x - knot), self._knots)
        return round(sum( w * k for (w, k) in zip(xMapped, self._weights) ) + self._intercept, 2)

def train(prices, knots):
    X = [[x[0], max(0, x[0]-knots[0]), max(0, x[0]-knots[1])] for x in prices]
    clf = linear_model.LinearRegression();
    clf.fit(X, prices[:,1])
    return LinearSplinesPredictor(knots, clf.coef_, clf.intercept_)

class PredictorRepository(object):
        
    def get(self, identifier):
        return LinearSplinesPredictor([1,2,3], [1,2,3,4])
    
    def store(self, identifier, predictor):
        return
