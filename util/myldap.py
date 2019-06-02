import ldap

import util.config as config


def get_ldap_server_url():
    return config.get_config().get('main', 'ldap_server')


def get_base_dn():
    return config.get_config().get('main', 'base_dn')


def get_admin_cn():
    return config.get_config().get('main', 'admin_cn')


def get_admin_dn():
    return get_admin_cn() + ',' + get_base_dn()


def get_admin_pass():
    return config.get_config().get('main', 'admin_pass')


def get_group_ou():
    return config.get_config().get('main', 'group_ou')


def get_group_dn():
    return get_group_ou() + ',' + get_base_dn()


def get_user_dn(uid: str):
    return 'uid=' + uid + ',' + get_group_dn()


def check_account(username: str, password: str) -> bool:
    ldap_conn = ldap.initialize(get_ldap_server_url())
    ldap_conn.simple_bind_s(get_user_dn(username), password)
    return True


def reset_password(username: str, password_new: str):
    ldap_conn = ldap.initialize(get_ldap_server_url())
    ldap_conn.simple_bind_s(get_admin_dn(), get_admin_pass())
    ldap_conn.passwd_s(get_user_dn(username), None, password_new)
