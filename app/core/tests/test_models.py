from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):

        email = 'test@example.com'
        password = '123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))



    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for sample_email in sample_emails:
            user = get_user_model().objects.create_user(sample_email[0], 'sample123')
            self.assertEqual(user.email, sample_email[1])


    def test_new_user_with_no_email(self):
       with self.assertRaises(ValueError):
        get_user_model().objects.create_user('','123')


    def test_new_user_with_no_password(self):
       with self.assertRaises(ValueError):
        get_user_model().objects.create_user('test','')


    def test_create_superuser(self):

       user = get_user_model().objects.create_superuser('test@example.com','test123')

       self.assertTrue(user.is_superuser)
       self.assertTrue(user.is_staff)

