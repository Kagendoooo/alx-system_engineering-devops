#Install a package 

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
