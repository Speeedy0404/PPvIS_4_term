import json

json_test = '''{
    "fruits": {
        "appls": {
            "appls1":
                {
                    "name": "appls1",
                    "height": "Семечко в земле",
                    "level_water": 5,
                    "day": 0,
                    "how_many_days_to_grow": 18,
                    "how_many_days_until_the_next_stage": 3,
                    "hp": 9,
                    "condition_vermin": "Все хорошо, никаких вредителей",
                    "condition_illness": "Все хорошо, никаких болезней"
                },
            "appls2":
                {
                    "name": "appls2",
                    "height": "Семечко в земле",
                    "level_water": 5,
                    "day": 0,
                    "how_many_days_to_grow": 18,
                    "how_many_days_until_the_next_stage": 3,
                    "hp": 9,
                    "condition_vermin": "Все хорошо, никаких вредителей",
                    "condition_illness": "Все хорошо, никаких болезней"

                }
        },
        "pear": {
            "pear1":
                {
                    "name": "pear1",
                    "height": "Семечко в земле",
                    "level_water": 5,
                    "day": 0,
                    "how_many_days_to_grow": 18,
                    "how_many_days_until_the_next_stage": 3,
                    "hp": 9,
                    "condition_vermin": "Все хорошо, никаких вредителей",
                    "condition_illness": "Все хорошо, никаких болезней"
                },
            "pear2":
                {
                    "name": "pear2",
                    "height": "Семечко в земле",
                    "level_water": 5,
                    "day": 0,
                    "how_many_days_to_grow": 18,
                    "how_many_days_until_the_next_stage": 3,
                    "hp": 9,
                    "condition_vermin": "Все хорошо, никаких вредителей",
                    "condition_illness": "Все хорошо, никаких болезней"
                }
        }
    },

    "vegetables": {
        "potato": {
            "potato1":
                {
                    "name": "potato1",
                    "height": "Первые 2-3 настоящих листа",
                    "level_water": 5,
                    "day": 0,
                    "how_many_days_to_grow": 18,
                    "how_many_days_until_the_next_stage": 3,
                    "hp": 9,
                    "condition_weeds": "Все хорошо, никаких сорняков",
                    "condition_vermin": "Все хорошо, никаких вредителей",
                    "condition_illness": "Все хорошо, никаких болезней"
                },
            "potato2":
                {
                    "name": "potato2",
                    "height": "Первые 2-3 настоящих листа",
                    "level_water": 5,
                    "day": 0,
                    "how_many_days_to_grow": 18,
                    "how_many_days_until_the_next_stage": 3,
                    "hp": 9,
                    "condition_weeds": "Все хорошо, никаких сорняков",
                    "condition_vermin": "Все хорошо, никаких вредителей",
                    "condition_illness": "Все хорошо, никаких болезней"
                }
        },
        "perec": {
            "perec1":
                {
                    "name": "perec1",
                    "height": "Первые 2-3 настоящих листа",
                    "level_water": 5,
                    "day": 0,
                    "how_many_days_to_grow": 18,
                    "how_many_days_until_the_next_stage": 3,
                    "hp": 9,
                    "condition_weeds": "Все хорошо, никаких сорняков",
                    "condition_vermin": "Все хорошо, никаких вредителей",
                    "condition_illness": "Все хорошо, никаких болезней"
                },
            "perec2":
                {
                    "name": "perec2",
                    "height": "Первые 2-3 настоящих листа",
                    "level_water": 5,
                    "day": 0,
                    "how_many_days_to_grow": 18,
                    "how_many_days_until_the_next_stage": 3,
                    "hp": 9,
                    "condition_weeds": "Все хорошо, никаких сорняков",
                    "condition_vermin": "Все хорошо, никаких вредителей",
                    "condition_illness": "Все хорошо, никаких болезней"
                }
        }
    }

}
'''

if __name__ == "__main__":
    '''
    data = json.loads(json_test)
    print(type(data))
    print(data)
    print(data['fruits']['appls'])
    
    number = len(data['fruits']['appls'])
    data['fruits']['appls']['appls3'] = {
        "name": "appls3",
        "height": "Семечко в земле",
        "level_water": 5,
        "day": 0,
        "how_many_days_to_grow": 18,
        "how_many_days_until_the_next_stage": 3,
        "hp": 9
    }
    print(data['fruits']['appls'])
    del data['fruits']['appls']['appls3']
    print(data['fruits']['appls'])
    for item in data['fruits']:
        print(item)
    data['fruits']['vishna'] = 0
    print('\n')
    print('\n')
    print('\n')
    for item in data['fruits']:
        print(item)
    
    data['fruits']['appls']['appls2']["condition_vermin"] = " НЕ хорошо, вредители"
    print(data['fruits']['appls'])
    '''

    with open("garden_area.json", 'r') as file:
        data = json.load(file)

    del data['fruits']['apple']['apple1']

    with open("garden_area.json", 'w') as file:
        json.dump(data, file, indent=3)

    '''''
    with open("garden_area.json", 'r') as file:
        data = json.load(file)
    
    print(data)
    '''''
