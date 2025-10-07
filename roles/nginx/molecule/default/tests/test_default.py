import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory.yml'
).get_hosts('all')

def test_nginx_installed(host):
    pkg = host.package("nginx")
    assert pkg.is_installed

def test_nginx_service_running_and_enabled(host):
    svc = host.service("nginx")
    assert svc.is_running
    assert svc.is_enabled

def test_nginx_listening_on_port_80(host):
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening
