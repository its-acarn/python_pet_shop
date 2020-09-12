# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(dict):
    name = dict["name"]
    return name


def get_total_cash(dict):
    total_cash = dict["admin"]["total_cash"]
    return total_cash


def add_or_remove_cash(dict, cash_difference):
    dict["admin"]["total_cash"] += cash_difference
    return dict["admin"]["total_cash"]

# def gets_pets_sold():

