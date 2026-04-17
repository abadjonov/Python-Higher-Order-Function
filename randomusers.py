from dataset import randomuser_data


def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    return list(
        map(
            lambda user: f"{user['name']['first']} {user['name']['last']}",
            data["results"],
        )
    )

full_names = get_full_names(randomuser_data)
print(full_names)

def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    filtered_users = filter(
        lambda user: user["location"]["country"].lower() == country.lower(),
        data["results"]
    )
    
    mapped_users = map(
        lambda user: {
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user["email"]
        },
        filtered_users
    )
    
    return list(mapped_users)

users_country = get_users_by_country(randomuser_data, 'India')
print(users_country)

def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """ 
    users = data["results"]

    males = list(filter(lambda u: u["gender"] == "male", users))
    females = list(filter(lambda u: u["gender"] == "female", users))
    
    return {
        "male": len(males),
        "female": len(females)
    }

result = count_users_by_gender(randomuser_data)
print(result)

def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    filtered_users = filter(
        lambda user: user["dob"]["age"] > age, 
        data["results"]
    )
    
    emails = map(
        lambda user: user["email"], 
        filtered_users
    )
    
    return list(emails)

emails = get_emails_of_older_than(randomuser_data, 60)

print(emails)


def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    sorted_users = sorted(
        data["results"], 
        key=lambda user: user["dob"]["age"], 
        reverse=descending
    )
    
    result = [
        {
            "name": f"{user['name']['first']} {user['name']['last']}",
            "age": user["dob"]["age"]
        }
        for user in sorted_users
    ]
    
    return result

print("O'sish:", sort_users_by_age(randomuser_data, descending=False))
print("Kamayish:", sort_users_by_age(randomuser_data, descending=True))

def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    target_letter = letter.lower()
    
    filtered_users = filter(
        lambda user: user["login"]["username"].lower().startswith(target_letter),
        data["results"]
    )
    
    usernames = map(
        lambda user: user["login"]["username"], 
        filtered_users
    )
    
    return list(usernames)
usernames = get_usernames_starting_with(randomuser_data, "g")

print(usernames)

def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    pass


def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    users = data["results"]
    
    if not users:
        return 0.0
    
    ages = map(lambda user: user["dob"]["age"], users)
    
    total_age = sum(ages)
    count = len(users)
    
    return total_age / count

avg = get_average_age(randomuser_data)
print(avg)

def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    coords = map(
        lambda user: (
            user["location"]["coordinates"]["latitude"], 
            user["location"]["coordinates"]["longitude"]
        ),
        data["results"]
    )
    
    return list(coords)

coordinates = get_all_coordinates(randomuser_data)
print(coordinates)


def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    users = data["results"]
    
    oldest_user = max(users, key=lambda user: user["dob"]["age"])
    
    return {
        "name": f"{oldest_user['name']['first']} {oldest_user['name']['last']}",
        "age": oldest_user["dob"]["age"],
        "email": oldest_user["email"]
    }

oldest = get_oldest_user(randomuser_data)
print(oldest)

def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    pass


def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    pass
