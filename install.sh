#Start and enable pigpio service
sudo pigpiod
sudo systemctl enable pigpiod

#Install required python libraries
python3 -m pip install pigpio keyboard