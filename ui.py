from getpass import getpass

def get_username() -> str:
    u = input("UTORID: ")
    return u

def get_password() -> str:
    return getpass("Password: ")

"""Deprecated
def get_download_location() -> str:
    loc = ""
    while loc == "":
        loc = input("Download Location \n(i.e. /Documents/textbooks): ")
    return loc
"""