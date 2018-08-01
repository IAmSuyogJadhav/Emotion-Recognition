#!/bin/bash
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install -y python3
sudo apt-get install -y python3-pip

mkdir ~/.emotion-recognition
cp frontend ~/.emotion-recognition -r
cp backend ~/.emotion-recognition -r

### PROBLEM HERE: MODULE EXPRESS NOT FOUND
echo "Installing Node Modules..."
npm --prefix ./frontend install
npm i express

echo "Installing required Python Dependencies..."
pip3 install -r requirements.txt

echo "alias emotion-recognition=\"node ~/.emotion-recognition/frontend\"" >> ~/.bash_aliases
source ~/.bashrc
echo "All set!"
echo "Now Just type emotion-recognition on the terminal to launch the webapp!"
