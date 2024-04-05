from GetRequester import GetRequester
import json

URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = "[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
CONVERTED_DATA = json.loads(JSON_STRING)

def test_get_response():
    '''get_response_body function returns response.'''
    requester = GetRequester(URL)
    assert requester.get_response_body() == JSON_STRING

def test_load_json():
    '''load_json function returns response.'''
    requester = GetRequester(URL)
    assert requester.load_json() == CONVERTED_DATA
