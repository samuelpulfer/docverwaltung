#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# NOTE: take care to keep the syntax bash compatible
#

# application information
meta_name="webpy"
meta_version="0.0.3"

# webserver port
port=8090

# log files
web_logfile="var/access.log"
app_logfile="var/application.log"
sql_logfile="var/sql.log"

# session defaults
session_salt="9222a425-76e1-4c76-b6ad-40a2410ee207"
session_timeout=86400 #24 * 60 * 60, # 24 hours   in seconds
session_dir='var'
session_dir_prefix="session_"
# session_name="framework" # autogenerated from meta["name"]
session_cookie_domain=None
session_ignore_expiry=True
session_ignore_change_ip=False
session_expired_message='Session expired'

user_db="etc/user.db"
