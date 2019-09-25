import ui
import login
import parse
import dwnld

if __name__ == "__main__":
    user = ui.get_username()
    passwd = ui.get_password()
    html = login.login(user, passwd)
    isbn_list = parse.parse(html)
    dwnld.download_books(isbn_list)
