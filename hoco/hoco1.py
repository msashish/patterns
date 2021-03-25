from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('samples/database.conf')
host = conf.get_string('databases.mysql.host')
same_host = conf.get('databases.mysql.host')
same_host = conf['databases.mysql.host']
same_host = conf['databases']['mysql.host']
port = conf['databases.mysql.port']
username = conf['databases']['mysql']['username']
password = conf.get_config('databases')['mysql.password']
password = conf.get('databases.mysql.password', 'default_password') #  use default value if key not found


print(host, same_host, port, username, password)
print(conf.get('retries_msg'))
print(conf.get('data-center-east'))
print(conf.get('large-jvm-opts'))