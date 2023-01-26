import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    input_message = 'Hello'

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('Hello', '2')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 2)

    assert encrypt_message(input_message, -2) == 'olleH'
    assert encrypt_message(input_message, 2) == 'oll_eH'
    assert encrypt_message(input_message, 1) == 'H_olle'
    assert encrypt_message(input_message, 3) == 'leH_ol'
