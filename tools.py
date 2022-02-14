"""Tools script that holds a variety of functions"""

import os


def nornir_set_creds(norn, username="test", password=None):
    """
    Handler so credentials are not stored in cleartext.
    Thank you Kirk!
    """
    if not username:
        username = os.environ.get("USER")
    if not password:
        password = os.environ.get("PASSWORD")

    for host_obj in norn.inventory.hosts.values():
        host_obj.username = username
        host_obj.password = password
