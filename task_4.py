def from_marketing():
    """
    Call this function to get a list of names from the marketing team
    """

    return ["Wofai", "Zainab", "A4atullah"]


# help(str)


def confirm_valid_names(input_list: list[str]):
    """
    Check that the input list contains only valid names

    Parmeters
    ---------

    Raises
    ------
    ValueError

    """
    for name in input_list:
        # Checs if the string is an alphabetic string
        if not name.isalpha():
            raise ValueError(f"{name} is not a name. "
            "Check with the marketing team")


if __name__ == "__main__":
    names = from_marketing()
    confirm_valid_names(input_list=names)