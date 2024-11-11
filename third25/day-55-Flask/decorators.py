class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False
    
def is_authenticated_user(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print('You need to be authenticated, please log in')
    return wrapper

@is_authenticated_user
def create_new_post(user):
    print(f'{user.name} you have a new post in the page')

new_user = User(name="Edwin")
new_user.is_logged_in = False

create_new_post(new_user)