from abc import ABCMeta, abstractmethod

__author__ = 'itamar'


class HostScanner(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_host_alive(self, host):
        raise NotImplementedError()


class HostFinger(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_host_fingerprint(self, host):
        raise NotImplementedError()

from infection_monkey.network.ping_scanner import PingScanner
from infection_monkey.network.tcp_scanner import TcpScanner
from infection_monkey.network.smbfinger import SMBFinger
from infection_monkey.network.sshfinger import SSHFinger
from infection_monkey.network.httpfinger import HTTPFinger
from infection_monkey.network.elasticfinger import ElasticFinger
from infection_monkey.network.mysqlfinger import MySQLFinger
from infection_monkey.network.info import local_ips, get_free_tcp_port
from infection_monkey.network.mssql_fingerprint import MSSQLFinger
from infection_monkey.network.k8s_kubelet_ro_fingerprint import K8sKubeletRoFinger