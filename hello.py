def hello():
    print("hi")


def greet_user():
    """Greet the user by saying hi."""
    hello()

def greet(name: str) -> str:
    return f"hello, {name}"

if __name__ == "__main__":
    greet_user()
