def test_get(client):
    assert client.get('/', query_string={'text':'laval;montreal;transit'}).status_code == 200
