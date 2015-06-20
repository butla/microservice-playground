#!/bin/bash
sudo apt-get install -y python3-pip
pip3 install -r /vagrant/requirements.txt

export PYTHONPATH=/vagrant
bash /vagrant/run_uwsgi.sh &
