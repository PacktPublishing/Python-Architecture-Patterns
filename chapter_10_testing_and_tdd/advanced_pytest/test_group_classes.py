from tdd_example import parameter_tdd


class TestEdgesCases():

    def test_negative(self):
        assert parameter_tdd(-1) == 0

    def test_zero(self):
        assert parameter_tdd(0) == 0

    def test_ten(self):
        assert parameter_tdd(10) == 100

    def test_eleven(self):
        assert parameter_tdd(11) == 100


class TestRegularCases():

    def test_five(self):
        assert parameter_tdd(5) == 25

    def test_seven(self):
        assert parameter_tdd(7) == 49
