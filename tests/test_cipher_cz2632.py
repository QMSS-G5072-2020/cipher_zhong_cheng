from cipher_cz2632 import cipher_cz2632

def test_cipher():
    example = 'Come and get me'
    expected = 'Gsqi erh kix qi'
    shift = 4
    actual = cipher_cz2632.cipher(example, shift, encrypt=True)
    assert actual == expected
