from predictor import LinearPredictor

def test_should_predict():
    # given
    predictor = LinearPredictor([1,2,3], [1,2,3,4])
    
    # when, then
    assert 50 == predictor.predict(7)