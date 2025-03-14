### Exercise::: March 13, 2025
from typing import List, Any

def bad_names_checker(customer_names_list: List[Any]):
    """
    Yields bad entries
    
    Bad entries are entries that are not strings

    Parameters
    ----------
    List[Any]:
        A list containing names
    
    Yields
    ------
    Any
        Any bad entries in the input list
    """
    for name in customer_names_list:
        if not type(name) == str:
            yield name

if __name__ == "__main__":
    # Lets assume that these are the names we got from the marketing team
    input_names = ["Adio", "Chukwudi", 56, 9, "Umar", 45.68]
    bad_entries = bad_names_checker(customer_names_list = input_names)

    # Check for the bad entries and print them
    for entry in bad_entries:
        print(entry)