import pytest
from camel import snake_case

def main():
    test_snake_case()


def test_snake_case():
    assert(snake_case("name")) == "name"
    assert(snake_case("firstName")) == "first_name"
    assert(snake_case("preferredFirstName")) == "preferred_first_name"


if __name__ == "__main__":
    main()