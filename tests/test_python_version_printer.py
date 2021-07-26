from unittest.mock import patch

from tox_poetry.python_version_printer import print_python_version


@patch("builtins.print")
def test_print_python_version(mock_print):
    print_python_version()

    mock_print.assert_called_once()

