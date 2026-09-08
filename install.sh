#Install pigpio
sudo apt-get update
sudo apt-get install -y pigpio python3

#Start and enable pigpio service
sudo systemctl daemon-reload
sudo systemctl enable pigpiod
sudo systemctl start pigpiod  

#Install required python libraries
python3 -m pip install pigpio keyboard --break-system-packages

#Move files to correct locations 
sudo mkdir /home/pi/pageTurner
sudo cp ~/scripts/pageTurner.sh ~/python/*.py /home/pi/pageTurner
sudo chown -R pi:pi /home/pi/pageTurner

sudo cp ~/scripts/pageTurner.service /etc/systemd/system

#Enable services
sudo systemctl daemon-reload
sudo systemctl start pageTurner
sudo systemctl enable pageTurner
