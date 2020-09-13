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


def get_pets_sold(dict):
    no_pets_sold = dict["admin"]["pets_sold"]
    return no_pets_sold


def increase_pets_sold(dict, num_of_pets_change):
    dict["admin"]["pets_sold"] += num_of_pets_change
    return dict["admin"]["pets_sold"]


def get_stock_count(pets_dict):
    stock_count = len(pets_dict["pets"])
    return stock_count


def get_pets_by_breed(pets_dict, pet_breed):
    pet_list = pets_dict["pets"]
    selected_breed_list = []
    for pet in pet_list:
        if pet["breed"] == pet_breed:
            selected_breed_list.append(pet_breed)
    return selected_breed_list


def find_pet_by_name(pets_dict, pet_name):
    pet_list = pets_dict["pets"]
    pet_info = None
    for pet in pet_list:
        if pet["name"] == pet_name:
            pet_info = pet
    return pet_info


def remove_pet_by_name(pets_dict, pet_name):
    pet_list = pets_dict["pets"]
    pet_index = None

    for i, pets_dict in enumerate(pet_list):
        if pets_dict["name"] == pet_name:
            pet_index = i
            del pet_list[pet_index]

def add_pet_to_stock(pets_dict, new_pet_item):
    pet_list = pets_dict["pets"]
    return pet_list.append(new_pet_item)

def get_customer_cash(customer):
    return customer["cash"]
    


