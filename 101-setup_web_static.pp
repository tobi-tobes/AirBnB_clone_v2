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

exec { 'Create /data directory':
  command => '/bin/mkdir -p /data/web_static/releases/test /data/web_static/shared',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Welcome to AirBnB Clone!',
  require => Exec['Create /data directory'],
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test/',
  force   => true,
  require => File['/data/web_static/releases/test/index.html'],
}

exec { 'Set permissions':
  command => '/bin/chown -R ubuntu:ubuntu /data/',
  require => File['/data/web_static/current'],
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