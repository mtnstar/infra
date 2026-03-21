import os
from pathlib import Path
import pytest

@pytest.fixture(scope="session")
def molecule_inventory_file():
    inv = os.environ.get("MOLECULE_INVENTORY_FILE")
    if not inv:
        pytest.skip("MOLECULE_INVENTORY_FILE not set (not running under Molecule)")
    return Path(inv).resolve()

@pytest.fixture(scope="session")
def molecule_inventory_dir(molecule_inventory_file):
    return molecule_inventory_file.parent
