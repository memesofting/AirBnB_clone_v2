#!/usr/bin/env bash
# Script sets up web servers for deployment of web_static

# install nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt update
    sudo apt install nginx
fi

# create folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create fake html file
echo "<html>
  <head>
  </head>
  <body>
    Hello, this is a test page.
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test folder
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" $nginx_config; then
    sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' $nginx_config
fi

# Restart Nginx to apply the new configuration
sudo service nginx restart
