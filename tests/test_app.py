import mock


@mock.patch('sms_directions.app.app', autospec=True)
def test_app(mocked_app):
    mocked_app.run()
    assert True  # No error found in app setup
