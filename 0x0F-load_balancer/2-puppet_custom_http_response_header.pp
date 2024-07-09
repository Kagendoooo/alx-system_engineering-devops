# Ensure the system is updated
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Ensure the nginx package is installed
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# Create the index.html file
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Add custom redirect rule to the Nginx configuration
exec { 'redirect_me':
  command  => 'sed -i "24i\\       rewrite ^/redirect_me https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Add custom HTTP header to the Nginx configuration
exec { 'HTTP header':
  command  => 'sed -i "25i\\       add_header X-Served-By \\$HOSTNAME;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

