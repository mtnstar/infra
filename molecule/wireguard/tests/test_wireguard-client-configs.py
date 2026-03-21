from pathlib import Path

def test_wireguard_config_dir_exists_locally(molecule_inventory_dir):
    client_config_dir: Path = molecule_inventory_dir / "wireguard_configs" / "clients"

    assert client_config_dir.exists(), f"{client_config_dir} missing on controller"
    assert client_config_dir.is_dir(), f"{client_config_dir} is not a directory on controller"
