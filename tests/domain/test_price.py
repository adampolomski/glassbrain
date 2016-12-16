from glassbrain.domain import price


def test_should_build_price_history():
    # given
    builder = price.PriceHistoryBuilder()
    
    # when, then
    assert [[0, 1000], [1, 1000], [2, 2000], [3, 1500]] == builder.change(1000, 0).change(2000, 2).change(1500, 3).build()


def test_should_build_price_history_to_day():
    # given
    builder = price.PriceHistoryBuilder(4)
    
    # when, then
    assert [[0, 1000], [1, 1000], [2, 2000], [3, 1500], [4, 1500]] == builder.change(1000, 0).change(2000, 2).change(1500, 3).build()
