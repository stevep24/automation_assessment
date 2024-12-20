from exercise_2 import json_data

draw_ID, Status, game_type, data =json_data()

def test_drawId():
    assert draw_ID==data['drawId']
    assert type(data['drawId']) == int


def test_Active():
    assert data['status'] == 'active'
    if  data['status'] == 'active':
        print("current active draw id number is",draw_ID)
