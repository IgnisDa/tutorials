import pytest
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


@pytest.fixture()
def create_custom_user(db):
    def _create_custom_user(*args, **kwargs):
        """ Create a test user with email, password etc supplied in the fixture call. """
        return CustomUser.objects.create_user(*args, **kwargs)
    return _create_custom_user
