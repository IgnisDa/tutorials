import pytest
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class TestCustomUser:
    @pytest.mark.django_db
    def test_created_version_one(self):
        """This is just an example of a very basic test. You would probably want to
        write a pytest fixture for creating a user instance."""
        CustomUser.objects.create_user(email="test@email.com", password="test-password")
        assert CustomUser.objects.count() == 1

    def test_created_version_two(self, create_custom_user):
        """ The above test but using a pytest fixture. """
        create_custom_user(email="test@email.com", password="test-password")
        assert CustomUser.objects.count() == 1

    def test_value_error_on_invalid_email(self, create_custom_user):
        """ Test that a `ValueError` is raised if we supply an invalid email ID. """
        with pytest.raises(ValueError):
            create_custom_user(email="incorrect-email", password="test-password")
        assert CustomUser.objects.count() == 0

    def test_value_error_on_empty_email(self, create_custom_user):
        """ Test that a `ValueError` is raised if we supply an empty email ID. """
        with pytest.raises(ValueError):
            create_custom_user(email="", password="test-password")
        assert CustomUser.objects.count() == 0

    @pytest.mark.django_db
    def test_error_raised_on_staff_false_superuser_option(self):
        """Test that a `ValueError` is raised if we try to create a superuser
        without `staff` status,"""
        with pytest.raises(ValueError):
            CustomUser.objects.create_superuser(
                email="test@email.com", password="dummy", is_staff=False
            )
        assert CustomUser.objects.count() == 0

    @pytest.mark.django_db
    def test_error_raised_on_superuser_false_superuser_option(self):
        """Test that a `ValueError` is raised if we try to create a superuser
        without `superuser` status,"""
        with pytest.raises(ValueError):
            CustomUser.objects.create_superuser(
                email="test@email.com", password="dummy", is_superuser=False
            )
        assert CustomUser.objects.count() == 0

    def test_uploaded_image_path(self, create_custom_user, create_temp_upload_file):
        """ Test that the image we upload is uploaded to the correct location. """
        image = create_temp_upload_file
        user = create_custom_user(email="test@email.com", password="dummy", image=image)
        assert CustomUser.objects.count() == 1
        assert user.image.url == "/users/test.jpg"
