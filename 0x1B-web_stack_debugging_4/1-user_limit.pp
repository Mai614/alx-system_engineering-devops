
# Increase the hard file limit for the 'holberton' user in the system limits configuration file
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',  # Change 'holberton' hard file limit to 50000
  path    => '/usr/local/bin/:/bin/'
}

# Increase the soft file limit for the 'holberton' user in the system limits configuration file
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',  # Change 'holberton' soft file limit to 50000
  path    => '/usr/local/bin/:/bin/'
}
