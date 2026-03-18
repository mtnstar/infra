def test_wireguard_config_file_exists(host):
    config_file = host.file("/etc/wireguard/wg0.conf")
    
    assert config_file.exists
    assert config_file.is_file


def test_wireguard_config_file_content(host):
    """Test that the WireGuard configuration file contains expected content."""
    config_file = host.file("/etc/wireguard/wg0.conf")
    
    content = config_file.content_string
    
    # Check for required sections and parameters
    assert "[Peer]\n# Alice" in content
    # assert "# Ansible managed" in content
    # assert "Address = 10.10.0.1/24" in content
    # assert "ListenPort = 51820" in content
    # assert "PrivateKey = " in content
