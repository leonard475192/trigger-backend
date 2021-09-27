import os
from pathlib import Path
import shutil
from tempfile import NamedTemporaryFile, SpooledTemporaryFile
import uuid

BASE_DIR = os.getcwd()


def save_file(file: SpooledTemporaryFile, dir: str):
    """
    Save static file.
    args:
        file(SpooledTemporaryFile) :
        dir(str)                   :
    returns:
        static_path(str) :
    """
    try:
        with NamedTemporaryFile(
            delete=False, suffix=Path(str(uuid.uuid4())).suffix, dir=dir
        ) as tmp:
            shutil.copyfileobj(file, tmp)
            e_pub_path = Path(tmp.name)
    finally:
        file.close()
    return str(e_pub_path.relative_to(BASE_DIR))
