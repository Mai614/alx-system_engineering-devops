# Puppet manifest to install nginx
package { 'nginx':
  ensure => installed,
}

file_line { 'm':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.google.com/webhp?hl=ar&ictx=2&sa=X&ved=0ahUKEwiL6tWZ4cmBAxVyRKQEHYZ-DaAQPQgK permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
