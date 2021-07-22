sudo apt install python3-pip build-essential -y
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
rm -rf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure prefix=/usr
sudo make
sudo make install
cd .. && rm -rf ta-lib
python3 -m pip install -r requirements.txt
