# Input data: List of dictionaries
# Note 1: This is a list named "employee_list" with dictionaries as items. Each itme or dictionary contains two
# values with "id" and "name" and "department" as keys with their appropriate values.
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
# Note 2: This is a function named "mod" that takes a list of employees or list data type as input parameter


def mod(employee_list):
    temp = employee_list['name'] + "_" + employee_list["department"]
    return temp


def to_mod_list(employee_list):
    """ Modifies the employee list of dictionaries into list of employee-department strings

    [IMPLEMENT ME]
       1. Use the map() method to apply mod() to all elements in employee_list

    Args:
       employee_list: list of employee objects

    Returns:
       list - A list of strings consisting of name + department.
    """
    # WRITE SOLUTION CODE HERE
    map_mod = map(mod, employee_list)
    result_list = [x for x in map_mod]
    return result_list

    # raise NotImplementedError()


def generate_usernames(mod_list):
    """ Generates a list of usernames

    [IMPLEMENT ME]
       1. Use list comprehension and the replace() function to replace space
          characters with underscores

       List comprehension looks like:
       list = [ function() for <item> in <list> ]

       The format for the replace() function is:

       test_str.replace(“a”, “z”) # replaces every “a” in test_str with “z”

    Args:
       mod_list: list of employee-department strings

    Returns:
       list - A list of usernames consisting of name + department delimited by underscores.
    """
    # WRITE SOLUTION CODE HERE
    replaced_list = [x.replace(" ", "_") for x in mod_list]
    return replaced_list

#    raise NotImplementedError()


def map_id_to_initial(employee_list):
    """ Maps employee id to first initial

    [IMPLEMENT ME]
       1. Use dictionary comprehension to map each employee's id (value) to the first letter in their name (key)

       Dictionary comprehension looks like:
       dict = { key : value for <item> in <list> }

    Args:
       employee_list: list of employee objects

    Returns:
       dict - A dictionary mapping an employee's id (value) to their first initial (key).
    """
    # WRITE SOLUTION CODE HERE
    emp_dict = {}
    for x in employee_list:
        emp_dict[x['name'][0]] = x['id']
    return emp_dict
#    raise NotImplementedError()


def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")


if __name__ == "__main__":
    main()


# 5 + 4 
# 4 + 3
# 3 + 2
# 2 + 1
# 1 + 0 