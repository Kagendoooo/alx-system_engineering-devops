# puppet script to fix replace phpp character with php 

exec { 'replace_php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
