import pytest
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class TestCustomUser:

    @pytest.mark.django_db
    def test_created_version_one(self):
        """ This is just an example of a very basic test. You would probably want to
        write a pytest fixture for creating a user instance. """
        CustomUser.objects.create_user(email='test@email.com', password='test-password')
        assert CustomUser.objects.count() == 1

    def test_created_version_two(self, create_custom_user):
        """ The above test but using a pytest fixture. """
        create_custom_user(email='test@email.com', password='test-password')
        assert CustomUser.objects.count() == 1

    def test_value_error_on_invalid_email(self, create_custom_user):
        """ Test that a ValueError is raised if we supply an invalid email ID. """
        with pytest.raises(ValueError):
            create_custom_user(email='incorrect-email', password='test-password')
        assert CustomUser.objects.count() == 0
