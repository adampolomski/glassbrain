class PriceChange(object):

    def __init__(self, value, day):
        self._value = value
        self._day = day
        
    def extract(self, extractor):
        return extractor.change(self._value, self._day)
    
class PriceEventRepository(object):
        
    def __init__(self, db):
        self._db = db
        
    def list(self, identifier):
        return [PriceChange(1000, 0), PriceChange(1200, 1), PriceChange(1500, 4)]
    
class PriceHistoryBuilder(object):
    
    def __init__(self, toDay = None):
        self._prices = []
        self._toDay = toDay
        
    def _getLast(self):
        return (self._prices[-1][0] + 1, self._prices[-1][1]) if self._prices else (0,0)

    def _expandLast(self, toDay):
        (lDay, lPrice) = self._getLast()
        for i in range(lDay, toDay):
            self._prices.append([i, lPrice])

    def change(self, value, day):
        self._expandLast(day)
        self._prices.append([day, value])
        return self
    
    def build(self):
        if self._toDay:
             self._expandLast(self._toDay + 1)
        return self._prices