from typing import List

def from_marketing() -> List[str]:
    """
    This function returns a list of names from the marketing team

    Parameters
    ----------
    None

    Returns
    -------
    List[str]
        A list containing names
    """

    return ["Wofai", "Zainab", "A4atullah"]


# help(str)

def confirm_valid_names(input_list: List[str]) -> None:
    """
    Check that the input list contains only valid names

    Valid names are names that contain only alphabetic characters

    Parmeters
    ---------
    input_list: list of str
        The list of names to be validated
    
    Returns
    -------
    None
        This function does not return anything if all names are valid.

    Raises
    ------
    ValueError
        If a name conatains non-alphabetic characters

    """
    for name in input_list:
        # Check if each name is not a alphabetic string
        if not name.isalpha():
            raise ValueError(f"'{name}' is not a name. "
                             "Names should only contain alphabetic strings. (A-Z) or (a-z). "
                             "Please check with the marketing team")
    

if __name__ == "__main__":
    names = from_marketing()
    confirm_valid_names(input_list=names)