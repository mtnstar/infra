from pathlib import Path

def test_wireguard_config_dir_exists_locally(molecule_inventory_dir):
    client_config_dir: Path = molecule_inventory_dir / "wireguard_configs" / "clients"

    assert client_config_dir.exists(), f"{client_config_dir} missing on controller"
    assert client_config_dir.is_dir(), f"{client_config_dir} is not a directory on controller"

def test_wireguard_client_config(host, molecule_inventory_dir):
    client_config_dir: Path = molecule_inventory_dir / "wireguard_configs" / "clients" / "alice"

    assert client_config_dir.exists(), f"{client_config_dir} missing on controller"
    assert client_config_dir.is_dir(), f"{client_config_dir} is not a directory on controller"
    
    client_all_config_file: Path = client_config_dir / "vpn-acme-all.conf.vault"
    assert client_all_config_file.exists(), f"{client_all_config_file} missing in local inventory"

    client_lan_config_file: Path = client_config_dir / "vpn-acme-lan.conf.vault"
    assert client_lan_config_file.exists(), f"{client_lan_config_file} missing in local inventory"
