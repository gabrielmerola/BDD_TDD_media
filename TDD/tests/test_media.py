from TDD.src.media import Media

class TestMedia(object):
    
    def test_calcMedia(self):
        result = Media.media(10, 10)
        assert result == 10
    
    def test_calcMedia2(self):
        result = Media.media(10, 50)
        assert result == 30
    
    def test_calcMedia3(self):
        result = Media.media(8, 64)
        assert result == 36
    
    def test_calcMedia4(self):
        result = Media.media(15, 55)
        assert result == 35
    
    def test_calcMedia5(self):
        result = Media.media(80, 20)
        assert result == 50