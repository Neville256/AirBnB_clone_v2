#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:nginx /data/
sudo chmod -R 755 /data/web_static/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By '$HOSTNAME';
    root /data/web_static/current;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /data/web_static/current;
        internal;
    }
}" > /etc/nginx/sites-available/my_config

# Create a symbolic link to enable the configuration
sudo ln -s /etc/nginx/sites-available/my_config /etc/nginx/sites-enabled/

# Restart Nginx to apply the configuration
service nginx restart
