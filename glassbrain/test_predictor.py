import predictor
    
def test_should_predict():
    # given
    linearPredictor = predictor.LinearSplinesPredictor([1,2,3], [1,2,3,4])
    
    # when, then
    assert [50, 170] == linearPredictor.predict([7, 19])
    
def test_should_train():
    # then
    linearPredictor = predictor.train([[0,0], [1,1] , [2,2]], [0,1,2]);