from sklearn import linear_model
'''
@author: Adam Polomski
'''
class LinearSplinesPredictor(object):
    '''
    Basic price predictor with linear splines.
    '''

    def __init__(self, knots, weights):
        self._knots = knots
        self._weights = weights

    def predictAll(self, X):
        return map(self.predict, X)
        
    def predict(self, x):
        xMapped = [x] + map( lambda knot: max(0, x - knot), self._knots)
        return sum( w * k for (w, k) in zip(xMapped, self._weights) )    

def train(X, y):
    clf = linear_model.LinearRegression();
    clf.fit(X, y)
    return LinearSplinesPredictor([], [1])

class PredictorRepository(object):
        
    def get(self, identifier):
        return LinearSplinesPredictor([1,2,3], [1,2,3,4])
    
    def store(self, identifier, predictor):
        return
