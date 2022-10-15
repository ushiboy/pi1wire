import os
import shutil
import tempfile
import uuid

import pytest


@pytest.fixture
def temp_dir_path():
    p = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
    os.mkdir(p)
    yield p
    if os.path.exists(p):
        shutil.rmtree(p)
