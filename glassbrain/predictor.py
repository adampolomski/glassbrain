from sklearn import linear_model
'''
@author: Adam Polomski
'''
class LinearSplinesPredictor(object):
    '''
    Basic price predictor with linear splines.
    '''

    def __init__(self, knots, weights):
        self.knots = knots
        self.weights = weights

    def predict(self, x):
        xMapped = [x] + map( lambda knot: max(0, x - knot), self.knots)
        return sum( w * k for (w, k) in zip(xMapped, self.weights) )
    
def train(X, y):
    clf = linear_model.LinearRegression();
    clf.fit(X, y)
    return LinearSplinesPredictor([], [1])