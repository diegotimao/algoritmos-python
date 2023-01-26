import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    input_message = 'Hello'

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('Hello', '2')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 2)
