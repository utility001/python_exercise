import random

def first_name(fname: str) -> str:
    """
    Accepts a first name as input and return it

    Parameters
    ----------
    fname: str
        First ame

    Returns
    -------
    str:
         first name
    """
    return fname


def last_name(lname: str) -> str:
    """
    Accepts a first name as input and return it

    Parameters
    ----------
    lname: str
        last name        

    Returns
    -------
    str:
        last name
    """
    return last_name

def welcome_message(fname: str, lname: str) -> None:
    """
    Prints a welcome message to the screen

    Parameters
    ----------
    fname: str
           First Name
    lname: str
           Last Name

    Returns
    -------
    None

    """
    print(f"Welcome, {fname} {lname}")