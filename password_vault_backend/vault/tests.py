import random
import string

from django.conf import settings
from django.test import TestCase

from .Aes import *
from .MatrixTranspositionCypher import MatrixTranspositionCypher

pivot = AESCipher(settings.AES_KEY)
string_to_be_encrypted = "Knock Knock! Encrypt this text please"
encrypted_string = pivot.encrypt(string_to_be_encrypted)


class AESCipherTestCase(TestCase):
    """
    Testing the serializer for Encryption
    @auhor: Shalin Awadiya <sh290595@dal.ca> and
    @author: Ayush Verma <ayush.verma@dal.ca>
    """

    def test_encryption_success(self):
        # Check weather the encrypted string has some content
        self.assertTrue(encrypted_string)

    def test_decryption_success(self):
        # Passing the encrypted content to the decryption function
        decrypted_message = pivot.decrypt(encrypted_string)
        self.assertEqual(decrypted_message, string_to_be_encrypted)

    def test_decryption_failure(self):
        # Passing the encrypted content to the decryption function
        decrypted_message = pivot.decrypt(encrypted_string)
        self.assertNotEqual(decrypted_message, "Some random string")

    def test_encryption_length(self):
        # Confirm if the encrypted results in 256 SHA hash
        self.assertNotEqual(len(encrypted_string) % 64, 0);

    def test_encryption_return_type(self):
        # Confirm if the encrypted ciphertext is in string and not in AES bytes
        returnError = False
        if isinstance(encrypted_string, bytes):
            returnError = True
        self.assertEqual(returnError, False)

    def test_decryption_return_type(self):
        # Confirm if the decrypted plaintext is in string and not in AES bytes
        decrypted_string = pivot.decrypt(encrypted_string)
        returnError = False
        if isinstance(decrypted_string, bytes):
            returnError = True
        self.assertEqual(returnError, False)

