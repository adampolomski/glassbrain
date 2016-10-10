import predictor

def test_should_predict():
    # given
    linearPredictor = predictor.LinearSplinesPredictor([1,2,3], [1,2,3,4])
    
    # when, then
    assert 50 == linearPredictor.predict(7)
    
def test_should_train():
    # when
    linearPredictor = predictor.train([[0,0], [1,1] , [2,2]], [0,1,2]);