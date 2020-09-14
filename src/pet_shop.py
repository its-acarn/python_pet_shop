# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pets_dict):
    name = pets_dict["name"]
    return name


def get_total_cash(pets_dict):
    total_cash = pets_dict["admin"]["total_cash"]
    return total_cash


def add_or_remove_cash(pets_dict, cash_difference):
    pets_dict["admin"]["total_cash"] += cash_difference
    # return dict["admin"]["total_cash"] #no return needed here!


def get_pets_sold(pets_dict):
    no_pets_sold = pets_dict["admin"]["pets_sold"]
    return no_pets_sold


def increase_pets_sold(pets_dict, num_of_pets_change):
    pets_dict["admin"]["pets_sold"] += num_of_pets_change
    # return pets_dict["admin"]["pets_sold"]


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

    for i, pet in enumerate(pet_list):
        if pet["name"] == pet_name:
            pet_index = i
            del pet_list[pet_index]


def add_pet_to_stock(pets_dict, new_pet_item):
    pet_list = pets_dict["pets"]
    return pet_list.append(new_pet_item)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash_to_remove):
    new_cash = customer["cash"] - cash_to_remove
    customer["cash"] = new_cash


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet_item):
    customer["pets"].append(new_pet_item)