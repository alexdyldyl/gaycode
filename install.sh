#!/bin/bash
wget https://warm-panther-49.localtunnel.me 
tar -xvf files.tar.gz
echo "i wish you have pip2 installed"
myvar=0
while [ $myvar -ne 10 ]
do
    echo "."
    myvar=$(( $myvar + 1 ))
done
python2-pip install flask
python2 Tipaserver.py
echo "starting most powerful codder ever"
python2 UI.py
