from glassbrain.domain import predictor
import numpy as np
    
def test_should_predict():
    # given
    linearPredictor = predictor.LinearSplinesPredictor([1,2,3], [1,2,3,4])
    
    # when, then
    assert [50, 170] == linearPredictor.predict_all([7, 19])
    
def test_should_train():
    # given
    data = np.loadtxt("tests/domain/s5prices.txt")
    
    # when
    linearPredictor = predictor.fit(data, 10);
    
    # then
    assert 13300 > np.mean((linearPredictor.predict_all(data[:,0]) - data[:,1]) ** 2)