# Amir Abu Hani
builtIn_users = {"lebron": {"gender": "male", "age": 27, "profession": "programmer",
                            "favorite tv show": "breaking bad", "favorite food": "pizza"},
                 "alice": {"gender": "female", "age": 23, "profession": "nurse",
                           "favorite tv show": "survivor", "favorite food": "fruit salad"},
                 "steph": {"gender": "male", "age": 35, "profession": "basketball player",
                           "favorite tv show": "Doctor who", "favorite food": " burger"},
                 "sofia": {"gender": "female", "age": 31, "profession": "teacher", "favorite tv show": "friends",
                           "favorite food": "steak"}
                 }

age_rules = [age for age in range(22, 30)]
professions_rules = ["programmer", "nurse", "engineer", "psychologist"]
favorite_tv_show_rules = ["survivor", "big bang theory", "friends", "breaking bad"]
favorite_food_rules = ["fruit salad", "steak", "pizza", "sushi", "soup"]


def match_users():
    user_name = input("Enter your name: ")
    user_gender = input("Enter your gender: ")
    user_age = int(input("Enter your age: "))
    user_profession = input("Enter your profession: ")
    user_favorite_tv_show = input("Enter your favorite tv show: ")
    user_favorite_food = input("Enter your favorite food: ")

    match_found = False
    for item in builtIn_users:
        age_match = user_age in age_rules and builtIn_users[item]["age"] in age_rules
        profession_match = user_profession in professions_rules and builtIn_users[item][
            "profession"] in professions_rules
        favorite_tv_show_match = user_favorite_tv_show in favorite_tv_show_rules and builtIn_users[item][
            "favorite tv show"] in favorite_tv_show_rules
        favorite_food_match = user_favorite_food in favorite_food_rules and builtIn_users[item][
            "favorite food"] in favorite_food_rules
        if age_match and profession_match and favorite_tv_show_match and favorite_food_match:
            print(F"Congratulations! there is a match between you and {item}")
            match_found = True
    if not match_found:
        print("Sorry! There is no match between you and any of the built-in users")


match_users()



