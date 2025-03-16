### Exercise::: March 13, 2025
from typing import List, Any

def bad_names_checker(customer_names_list: List[Any]):
    """
    This functions filters out bad entries from an input list and yields them
    Bad entries are entries that are not string

    Parameters
    ----------
    customer_names_list: List[Any]
        A list containing names
    
    Yields
    ------
    Any
        Any bad entries in the input list
    """
    for name in customer_names_list:
        if not type(name) == str:
            yield name


input_names = ["Adio", "Chukwudi", 56, 9, "Umar", 45.68]
bad_entries = bad_names_checker(customer_names_list = input_names)

for entry in bad_entries:
    print(entry)