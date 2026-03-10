import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_pdns_service_running(host):
    """Check if PowerDNS service is running"""
    pdns = host.service("pdns")
    assert pdns.is_running
    assert pdns.is_enabled


def test_pdns_listening_on_port(host):
    """Check if PowerDNS is listening on port 5300"""
    socket = host.socket("tcp://127.0.0.1:5300")
    assert socket.is_listening


def test_dns_zone_example_local(host):
    """Test DNS query for example.local zone"""
    # Query the SOA record for the zone
    cmd = host.run("dig @127.0.0.1 -p 5300 example.local SOA +short")
    assert cmd.rc == 0
    assert "ns1.example.local" in cmd.stdout or "example.local" in cmd.stdout


def test_dns_query_ns_record(host):
    """Test DNS NS record query"""
    cmd = host.run("dig @127.0.0.1 -p 5300 example.local NS +short")
    assert cmd.rc == 0
    assert "ns1.example.local" in cmd.stdout


def test_dns_query_a_record(host):
    """Test DNS A record query for ns1.example.local"""
    cmd = host.run("dig @127.0.0.1 -p 5300 ns1.example.local A +short")
    assert cmd.rc == 0
    # Should return an IP address
    assert len(cmd.stdout.strip()) > 0


def test_dns_query_inventory_host(host):
    """Test DNS query for inventory host record"""
    # Query for the test instance itself
    cmd = host.run("dig @127.0.0.1 -p 5300 instance.example.local A +short")
    assert cmd.rc == 0
    # Should return an IP address
    output = cmd.stdout.strip()
    assert len(output) > 0
    # Basic IP validation
    assert output.count('.') == 3


def test_dns_query_manual_record(host):
    """Test DNS query for manually configured record"""
    # Test a manual A record (adjust based on your config)
    cmd = host.run("dig @127.0.0.1 -p 5300 www.example.local A +short")
    assert cmd.rc == 0


def test_pdns_database_exists(host):
    """Check if PowerDNS SQLite database exists"""
    db_file = host.file("/var/lib/powerdns/pdns.sqlite3")
    assert db_file.exists
    assert db_file.user == "pdns"
    assert db_file.group == "pdns"


def test_pdns_config_file(host):
    """Check if PowerDNS config file exists and is valid"""
    config = host.file("/etc/powerdns/pdns.conf")
    assert config.exists
    assert config.contains("gsqlite3")
    assert config.contains("local-port=5300")
