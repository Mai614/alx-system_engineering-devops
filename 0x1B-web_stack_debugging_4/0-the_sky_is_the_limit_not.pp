# Modify the Nginx configuration file to adjust a specific parameter
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',  # Replace '15' with '4096' in Nginx config
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart the Nginx service to apply the configuration changes
exec { 'nginx-restart':
  command => 'nginx restart',  # Restart Nginx after configuration changes
  path    => '/etc/init.d/'
}
