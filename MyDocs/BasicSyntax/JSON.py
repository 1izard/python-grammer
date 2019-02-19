menu = {
    "breakfirst": {
        "hours": "7-11",
        "items": {
            "breakfirst burritos": "$6.00",
            "pancakes": "$4.00"
        }
    },
    "lunch": {
        "hours": "11-3",
        "items": {
            "hamburger": "$5.00"
        }
    },
    "dinner": {
        "hours": "3-10",
        "items": {
            "spaghetti": "$8.00"
        }
    }
}

# encode
import json
menu_json = json.dump(menu)

# decode
menu2 = json.loads(menu_json)
