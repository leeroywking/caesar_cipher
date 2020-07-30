from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import c_encrypt, c_decrypt, brute_force_c_decrypt
from random import randint
def test_version():
    assert __version__ == '0.1.0'

def test_c_encrypt():
    assert c_encrypt("abcd", 1) == "bcde"

def test_c_encrypt_wrap():
    assert c_encrypt("abcd", 27) == "bcde"

def test_c_encrypt_negative():
    assert c_encrypt("abcd", -1) == "zabc"

def test_c_decrypt():
    crypted = c_encrypt("abcd", 5000)
    assert c_decrypt(crypted, 5000) == "abcd"

def test_brute_force_c_decrypt():
    crypted = c_encrypt("The man walks alone at night because of a fear of muggers", 2333)
    attempt = brute_force_c_decrypt(crypted)
    assert attempt == "the man walks alone at night because of a fear of muggers"

def test_brute_force_c_decrpt2():
    crypted = c_encrypt("The quick brown fox jumps over the lazy dog", 999)
    attempt = brute_force_c_decrypt(crypted)
    assert attempt == "the quick brown fox jumps over the lazy dog"

def test_brute_force_assigned():
    for i in range(10): #running it ten times to reduce the chance I got lucky
        crypted = c_encrypt("It was the best of times, it was the worst of times.", randint(0,10000))
        attempt = brute_force_c_decrypt(crypted)
        assert attempt == "it was the best of times, it was the worst of times."