import random

def first_name() -> str:
    """
    returns random first names

    Parameters
    ----------
    None

    Returns
    -------
    str:
         A random first name
    """
    random_first_names = [
        "Micheal", "Elizabeth", 
        "Babatunde", "Yewande"
        "Kamal", "Yusroh",
        "Chukwudi", "Adaeze",
        "Daniel", "Esther", 
        "Umar", "Uwa",
        "Charles", "Sandra"
        "Alao", "Amope"
        ]
    return random.choice(random_first_names)


def last_name() -> str:
    """
    returns random last names

    Parameters
    ----------
    None

    Returns
    -------
    str:
         A random last name
    """
    random_last_names = [
        "Bello", "Danladi", "Balogun",
        "Azikiwe", "Coker", "Adeoye", 
        "Arinze", "Adesina", "Coker"
        ]
    return random.choice(random_last_names)

def concat_name(fname: str, lname: str) -> None:
    """
    outputs a string containing first and last names

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
    print(f"My name is {fname} {lname}")

if __name__ == "__main__":
    concat_name(
        fname=first_name(), 
        lname=last_name()
        )