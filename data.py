# Import Faker Library
from faker import Faker

# create and initialize a faker generator 
faker = Faker()

# predefined list of groceries words
items_list  = ["Soda", "Milk", "Chips","Eggs","Breads","Breakfast","Beer","Water"]

def get_user_data():
    """
    Generating fake data using Faker library
    """
    return {
        "user_id": faker.unique.random_int(min=11, max=9999999),
        "name": faker.name(),
        "address": faker.address(),
        "created_at": faker.year(),
        "phone" : faker.phone_number(),
        "items":','.join([str(elem) for elem in set(faker.words(3, True, items_list))]),
        "total_cost": faker.random_int(10, 100),
        "order_id": faker.uuid4()
    }


# to remove whitespace from string 
def remove_whitespaces(string):
    return "".join(string.split())

# final data with email address
def get_registered_user():
    data = get_user_data()
    data['email'] = f"{remove_whitespaces(data['name'])}@gmail.com"
    return data


if __name__ == "__main__":
    print(get_registered_user())