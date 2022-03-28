from unittest.mock import MagicMock

from django.core.exceptions import ValidationError
from django.test import TestCase

from .serializers import *


class UserProfileAbstractSerializerTestCase(TestCase):
    """
    Testing the common serializer to verify the input data

    @author: Ayush Verma <ayush.verma@dal.ca>
    """

    def test_validate_name_with_correct_arguments(self):
        instantiated_profile_class = UserProfileAbstractSerializer()
        t = instantiated_profile_class.validate_name("Ayush Verma")
        self.assertEqual(t, "Ayush Verma")

    def test_validate_name_with_incorrect_arguments(self):
        instantiated_profile_class = UserProfileAbstractSerializer()
        t = instantiated_profile_class.validate_name("Ayush Verma@$%&*($*#^#&$")
        self.assertNotEqual(t, "Ayush Verma")

    def test_validate_first_name_with_correct_argument(self):
        instantiated_profile_class = UserProfileAbstractSerializer()
        t = instantiated_profile_class.validate_first_name("Ayush")
        self.assertEqual(t, "Ayush")

    def test_validate_first_name_with_incorrect_argument(self):
        instantiated_profile_class = UserProfileAbstractSerializer()
        t = instantiated_profile_class.validate_first_name("Ayush@")
        self.assertNotEqual(t, "Ayush")

    def test_validate_last_name_with_correct_argument(self):
        instantiated_profile_class = UserProfileAbstractSerializer()
        t = instantiated_profile_class.validate_last_name("Verma")
        self.assertEqual(t, "Verma")

    def test_validate_last_name_with_incorrect_argument(self):
        instantiated_profile_class = UserProfileAbstractSerializer()
        t = instantiated_profile_class.validate_last_name("Verma@")
        self.assertNotEqual(t, "Verma")

    def test_validate_email_if_email_does_not_exist(self):
        instantiated_profile_class = UserProfileAbstractSerializer()
        t = instantiated_profile_class.validate_email("ayush.verma@dal.ca")
        self.assertEqual(t, "ayush.verma@dal.ca")

    def test_validate_email_if_email_exist(self):
        instantiated_profile_class = UserProfileAbstractSerializer()
        instantiated_profile_class.validate_email = MagicMock(side_effect=ValidationError('Account with this email '
                                                                                          'already exists'))
        self.assertRaises(ValidationError, instantiated_profile_class.validate_email, "dp974154@dal.ca")


class SignUpSerializerTest(TestCase):
    """
   Testing the SignUp serializer to verify the signup methods

   @author: Ayush Verma <ayush.verma@dal.ca>
   """

    def test_validate_if_password_is_correct(self):
        instantiated_signup_class = SignUpSerializer()
        serializer_object = ({
            'password': 'Qwertyu@1234',
            'confirm_password': 'Qwertyu@1234'
        })

        self.assertEqual(instantiated_signup_class.validate(serializer_object), serializer_object)

    def test_validate_if_password_is_incorrect(self):
        instantiated_signup_class = SignUpSerializer()
        serializer_object = ({
            'password': 'Qwertyu@1234',
            'confirm_password': 'Qwertyu@1234@'
        })

        instantiated_signup_class.validate = MagicMock(side_effect=ValidationError('This should be same as password'))
        self.assertRaises(ValidationError, instantiated_signup_class.validate, serializer_object)

    def test_create_user_success(self):
        instantiated_signup_class = SignUpSerializer()
        serializer_object = ({
            'first_name': 'Ayush',
            'last_name': 'Verma',
            'email' : 'ayush.verma@dal.ca',
            'password' : 'Qwerty@1234'
        })
        generated_token = instantiated_signup_class.create(serializer_object)
        self.assertTrue(generated_token)

    def test_create_user_failure(self):
        instantiated_signup_class = SignUpSerializer()
        serializer_object = ({
            'first_name': 'Ayush',
            'email' : 'ayush.verma@dal.ca',
            'password' : 'Qwerty@1234'
        })
        instantiated_signup_class.create = MagicMock(side_effect=ValidationError('No last_name key present'))
        self.assertRaises(ValidationError, instantiated_signup_class.create, serializer_object)

class LoginSerializerTest(TestCase):

    def test_validate_unsuccessful_no_account(self):
        instantiated_login_class = LoginSerializer()
        serializer_object = ({
            'email': 'Ayush',
            'password' : 'john.doe@dal.ca',
            'token' : 'Qwerty@1234',
            'confirm_password' : 'ayush.verma@dal.ca'
        })
        instantiated_login_class.validate = MagicMock(side_effect=ValidationError('this account does not exists'))
        with self.assertRaises(ValidationError):
            instantiated_login_class.validate(serializer_object)

    def test_validate_unsuccessful_wrong_password(self):
        instantiated_login_class = LoginSerializer()
        serializer_object = ({
            'email': 'john.doe@dal.ca',
            'password' : 'Qwerty@1234',
            'token' : 'ffnrfnfnn4nttnti5ntinfnnffnvvs',
            'confirm_password' : 'eQwerty@1234'
        })
        instantiated_login_class.validate = MagicMock(side_effect=ValidationError('Please check your password'))
        with self.assertRaises(ValidationError):
            instantiated_login_class.validate(serializer_object)