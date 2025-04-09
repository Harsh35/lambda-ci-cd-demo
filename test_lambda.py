from lambda_function import handler

def test_handler():
    event = {}
    context = None
    result = handler(event, context)
    assert result["statusCode"] == 200