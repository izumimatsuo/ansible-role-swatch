import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_lsyncd_is_installed(host):
    package = host.package("swatch")
    assert package.is_installed
    assert package.version.startswith("3.2")


def test_lsyncd_running_and_enabled(host):
    service = host.service("swatchd")
    assert service.is_running
    assert service.is_enabled
