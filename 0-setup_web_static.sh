#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the folder /data/ if it doesn’t already exist
sudo mkdir -p /data

# Create the folder /data/web_static/ if it doesn’t already exist
sudo mkdir -p /data/web_static

# Create releases/ and shared/ folders in data/ if not already present
sudo mkdir -p /data/web_static/{releases,shared}

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
sudo bash -c 'cat > /data/web_static/releases/test/index.html << EOF
Welcome to AirBnB Clone!
EOF'

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
if [ -L /data/web_static/current ]
then
    rm -rf /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
printf %s "server {
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

     add_header X-Served-By \$hostname;
}
" > /etc/nginx/sites-available/default

# Restart Nginx after changes to configuration
sudo service nginx restart
