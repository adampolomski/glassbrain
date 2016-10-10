'''
@author: Adam Polomski
'''
class LinearPredictor(object):
    '''
    Basic price predictor.
    '''

    def __init__(self, knots, weights):
        self.knots = knots
        self.weights = weights

    def predict(self, x):
        xMapped = [x] + map( lambda knot: max(0, x - knot), self.knots)
        return sum( w * k for (w, k) in zip(xMapped, self.weights) )
