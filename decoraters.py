import functools

def make_secure(access_level):
    def decorator(func):
        @functools.wrap(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permission for user {user['user_name']}"
        return secure_function
    return decorator
