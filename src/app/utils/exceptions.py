class UserAlreadyExistsError(Exception):
    """Raised when trying to create a user with an email that is already taken."""
    pass

class UserNotFoundError(Exception):
    """Raised when a requested user does not exist."""
    pass

class TokenInvalidError(Exception):
    """Raised when a token is expired, corrupted, or invalid."""
    pass