# Installs and configures Nginx Web Server
exec { 'update':
  command => 'apt-get -y update',
  path    => '/usr/bin/',
}

package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/data':
  ensure => directory,
}

file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Welcome to AirBnB Clone!',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
}

$host_name = $::hostname

$config = "server {
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