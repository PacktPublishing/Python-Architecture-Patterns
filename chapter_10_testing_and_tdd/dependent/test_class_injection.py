from unittest.mock import patch
from class_injection import Model
from class_injection import ModelInjection, WriterInjection


@patch('class_injection.Writer.write')
def test_model(mock_write):

    model = Model('test_model')
    model.save()

    mock_write.assert_called_with('model.txt', 'test_model')


def test_modelinjection():

    EXPECTED_DATA = 'test_modelinjection'
    EXPECTED_FILENAME = 'model_injection.txt'

    class MockWriter:

        def write(self, filename, data):
            self.filename = filename
            self.data = data

    writer = MockWriter()
    model = ModelInjection(EXPECTED_DATA, EXPECTED_FILENAME,
                           writer)
    model.save()

    assert writer.data == EXPECTED_DATA
    assert writer.filename == EXPECTED_FILENAME
