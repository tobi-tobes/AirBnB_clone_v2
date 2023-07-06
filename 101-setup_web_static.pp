# Installs and configures Nginx Web Server
exec { 'update':
  command => 'apt-get -y update',
  path    => '/usr/bin/',
}

package { 'nginx':
  ensure   => installed,
  provider => 'apt',
  require  => Exec['update'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Welcome to AirBnB Clone!',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  force  => true,
}

$host_name = $::hostname

$config = "
server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /var/www/html;
     index       index.html index.htm;

     location	  /redirect_me {
     		   return  301 https://stackoverflow.com/;
     }

     error_page	404 /404.html;
     location	/404 {
     		 root	/var/www/html;
		  internal;
     }

     location     /hbnb_static {
                 alias  /data/web_static/current/;
     }

     add_header X-Served-By ${host_name};
}
"

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => $config,
  notify  => Service['nginx'],
}

service {'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}