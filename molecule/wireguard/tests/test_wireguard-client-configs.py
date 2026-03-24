from pathlib import Path

def test_wireguard_config_dir_exists_locally():
    client_config_dir: Path = Path("/tmp/molecule/wireguard_configs/clients/alice")

    assert client_config_dir.exists(), f"{client_config_dir} missing on controller"
    assert client_config_dir.is_dir(), f"{client_config_dir} is not a directory on controller"

def test_wireguard_client_config():
    client_config_dir: Path = Path("/tmp/molecule/wireguard_configs/clients/alice")

    assert client_config_dir.exists(), f"{client_config_dir} missing on controller"
    assert client_config_dir.is_dir(), f"{client_config_dir} is not a directory on controller"
    
    client_all_config_file: Path = client_config_dir / "vpn-acme-all.conf.vaulted"
    assert client_all_config_file.exists(), f"{client_all_config_file} missing in local inventory"

    client_lan_config_file: Path = client_config_dir / "vpn-acme-lan.conf.vaulted"
    assert client_lan_config_file.exists(), f"{client_lan_config_file} missing in local inventory"
