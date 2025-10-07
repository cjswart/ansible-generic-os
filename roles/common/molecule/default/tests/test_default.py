import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory.yml'
).get_hosts('all')

def test_packages_installed(host):
    for pkg in ["curl", "vim", "git"]:
        package = host.package(pkg)
        assert package.is_installed

def test_user_created(host):
    user = host.user("devops")
    assert user.exists
    assert "sudo" in user.groups

def test_motd_exists(host):
    motd = host.file("/etc/motd")
    assert motd.exists
    assert motd.contains("Welcome")

def test_ssh_root_login_disabled(host):
    config = host.file("/etc/ssh/sshd_config").content_string
    assert "PermitRootLogin no" in config
