#!/bin/bash
# This script will download and start Apache, and then create a
# symlink between your synced files directory and the location where
# Apache will look for the content
apt-get update
apt-get install -y apache2
if ! [ -L /var/www ]; then
rm -rf /var/www
ln -fs /vagrant /var/www
fi