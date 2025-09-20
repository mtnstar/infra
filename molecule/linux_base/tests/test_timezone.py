def test_timezone_file(host):
    tz_file = host.file("/etc/timezone")
    assert tz_file.exists
    assert tz_file.contains("Europe/Zurich")

def test_localtime_symlink(host):
    localtime = host.file("/etc/localtime")
    assert localtime.exists
    assert localtime.is_symlink
    assert "Europe/Zurich" in localtime.linked_to
