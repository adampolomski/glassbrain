from glassbrain.domain import predictor
import numpy as np
from mock import Mock
    
def test_should_predict():
    # given
    linearPredictor = predictor.LinearSplinesPredictor([1,2,3], [1,2,3,4])
    
    # when, then
    assert linearPredictor.predict_all([7, 19]) == [50, 170]
    
def test_should_iterate_over_knots():
    # given
    data = np.array([[x, x] for x in range(1,10)])
    def mock_regression(X, prices):
        if X == predictor._knotify([4,7], data[:,0]):
            return (Mock(coef_ = [1], intercept_ = 1), 1)
        return (Mock(coef_ = [1], intercept_ = 0), 0)
    
    # when
    linearPredictor = predictor.fit(data, 1, mock_regression);
    
    # then
    assert linearPredictor.predict(0) == 1
    
def test_should_fit_linear_regression():
    # given
    data = np.loadtxt("tests/domain/s5prices.txt")
    
    # when
    (clf, score) = predictor.linear_regression(predictor._knotify([100,420], data[:,0]), data[:,1]);
    
    # then
    assert score > 0.88