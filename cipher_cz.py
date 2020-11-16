def cipher(text, shift, encrypt=True):
    """
    Encrypts texts by shifting each plaintext letter to a fixed number of places down the alphabet. 

    Parameters
    ----------
    text : Words that will be converted. Should be string.
    shift : Number of places to shift text in the alphabet. Should be integer.
    encrypt : Encrypt or Decrypt. Should be Boolean.

    Returns
    -------
    The outcome should be a string.

    Examples
    --------
    cipher('Hello!',4,encrypt=True)
    'Lipps!'

    cipher('Lipps!',4,encrypt=False)
    'Hello!'

    cipher('Hello!',-4,encrypt=True)
    'Pmttw!'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
