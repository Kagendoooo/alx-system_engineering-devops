# create a manifest that kills a process named killmenow usig puppet

exec { 'pkill -f killmenow':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
