# Configures Nginx & system limits to handle increased traffic

exec { 'increase concurrency':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
} -> exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
