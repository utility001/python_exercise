### Exercise::: March 13, 2025
# TODO::: Add documentation and annnotations

def bad_names_checker(customer_names_list):
    """
    Yields bad entries

    # TODO::: What is yield???
    # TODO::: What is a generator????
    """
    for name in customer_names_list:
        if not type(name) == str:
            yield name

if __name__ == "__main__":
    # Lets assume that these are the names we got from the marketing team
    input_names = ["Samson", "Yes", 56, 9]
    bad_entries = bad_names_checker(customer_names_list = input_names)

    # TODO: Question::: What if `bad entries` is empty. How do we know if a generator contains stuff??

    # Checl for the bad entries and print them
    for entry in bad_entries:
        print(entry)