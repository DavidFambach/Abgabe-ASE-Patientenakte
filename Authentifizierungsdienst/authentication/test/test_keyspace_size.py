from random import randint

from django.contrib.auth.password_validation import validate_password
from rest_framework.test import APITestCase


class TestUserRegister(APITestCase):
    def test_password_keyspace_brut_force(self):
        """returns the size of the keyspace. The size is determined by examining each individual password in a sample."""

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜabcdefghijklmnopqrstuvwxyzäöü1234567890!\"§$%&/()=?{[]}\#'*+~.:,;-_<>|^°@€µ"
        len_alphabet = len(alphabet)
        pw_length = 10
        original_keyspace = pow(len_alphabet, pw_length)

        sample_size = 200000
        keyspace = sample_size
        sample = 0

        # gradually create all passwords and check whether they meet the restrictions
        while sample < sample_size:
            pw_cur = ""
            # within this preliminary loop, the current password is created using its id
            pw_id = randint(0, original_keyspace)

            for pos in range(pw_length - 1, -1, -1):
                pw_cur += (alphabet[pw_id // (len_alphabet ** pos) % len_alphabet])

            try:
                validate_password(password=pw_cur, user=None)
            except Exception as e:
                keyspace -= 1

            sample += 1
        assert keyspace * (original_keyspace / sample_size) > (1*(10**20))
