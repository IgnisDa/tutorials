import shutil
import tempfile
from pathlib import Path

import pytest
import requests
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

CustomUser = get_user_model()


@pytest.fixture()
def create_custom_user(db):
    def _create_custom_user(*args, **kwargs):
        """ Create a test user with email, password etc supplied in the fixture call. """
        return CustomUser.objects.create_user(*args, **kwargs)

    return _create_custom_user


@pytest.fixture()
def create_temp_upload_file(settings):
    """This creates a image file for testing and then automatically deletes it
    after the test is complete."""
    temp_dir = tempfile.gettempdir()
    temp_media_root = tempfile.mkdtemp()
    temp_download_dir = tempfile.mkdtemp()
    file_name = Path(temp_dir) / temp_download_dir / "test.jpg"
    response = requests.get("https://picsum.photos/300")
    with open(file_name, "wb") as f:
        f.write(response.content)
    with open(file_name, "rb") as f:
        content = f.read()
    settings.MEDIA_ROOT = temp_media_root
    file = SimpleUploadedFile(name=file_name, content=content)
    yield file
    shutil.rmtree(temp_media_root, ignore_errors=True)
