import re

def test_wireguard_config_file_exists(host):
    config_file = host.file("/etc/wireguard/wg0.conf")
    
    assert config_file.exists
    assert config_file.is_file


def test_wireguard_config_file_permissions(host):
    config_file = host.file("/etc/wireguard/wg0.conf")
    
    # WireGuard config files should be readable only by root for security
    assert config_file.user == "root"
    assert config_file.group == "root"
    assert config_file.mode == 0o600


def test_wireguard_server_conf_content(host):
    config_file = host.file("/etc/wireguard/wg0.conf")
    
    wg0_conf_content = config_file.content_string
    
    # server part
    assert "[Interface]" in wg0_conf_content
    assert "# Ansible managed" in wg0_conf_content
    assert "Address = 10.10.0.1/24" in wg0_conf_content
    assert "ListenPort = 51842" in wg0_conf_content
    assert "PrivateKey = " in wg0_conf_content
    assert "DNS = 8.8.8.8" in wg0_conf_content

    # client peer part
    alice_peer = (
        r'# BEGIN peer alice\n'
        r'\[Peer\]\n'
        r'PublicKey = [A-Za-z0-9+/]{43}=\n'
        r'AllowedIPs = 10\.10\.0\.2/32\n'
        r'PreSharedKey = [A-Za-z0-9+/]{43}=\n'
        r'# END peer alice'
    )
    
    assert re.search(alice_peer, wg0_conf_content), "alice peer section not found or invalid format"
