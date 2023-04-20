from sag_py_hello.sample import hello


def test_sample() -> None:
    # Arrange
    my_name = "Groot"

    # Act
    actual: str = hello(my_name)

    # Assert
    assert actual == "Hello Groot!"
