import random

from task_1 import first_name, last_name

def random_date() -> str:
    """
    returns a random date

    Parameters
    ----------
    None

    Returns
    -------
    str:
        A random date between 1990 and 2002
    """
    random_year = random.choice(range(1994, 2003, 1))
    random_month = random.choice(range(1, 13, 1))
    random_day = random.choice(range(1, 29, 1))

    return f"{random_year} - {random_month} - {random_day}"

if __name__ == "__main__":
    pass