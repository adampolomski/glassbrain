from glassbrain.domain import predictor
import numpy as np
    
def test_should_predict():
    # given
    linearPredictor = predictor.LinearSplinesPredictor([1,2,3], [1,2,3,4])
    
    # when, then
    assert [50, 170] == linearPredictor.predictAll([7, 19])
    
def test_should_train():
    # given
    data = np.loadtxt("tests/domain/s5prices.txt")
    
    # when
    linearPredictor = predictor.train(data, [90, 420]);
    
    # then
    assert 3037.21 == linearPredictor.predict(2)
