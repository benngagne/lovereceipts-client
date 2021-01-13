# LoveReceipts ESC/POS Client

## Usage
The LoveReceipts ESC/POS Client is built to be used alongside with the LoveReceipts Server. In the `client.py` file, change the websockets URI to the LoveReceipt Server's IP/domain. The default server port is 15753... change if needed. Also, install all python dependencies with pip3 and the included requirements.txt file.

You will also need to change the thermal printers VenderID, ProductID, Interface number, and EP_IN and EP_OUT variables in the python script. First, use `lsusb` to get a list of USB devices connected to your device. Find the thermal printer and note the Vender and Product ID's. Then use `lsusb -vvv -d xxxx:xxxx` where `xxxx:xxxx` is the VenderID and ProductID for the thermal printer, that will give you the Interface number, and EP_IN/EP_OUT locations for the printer.

For other types of printers, including network and serial printers, refer to the `python-escpos` [documentation](https://python-escpos.readthedocs.io/en/latest/index.html) to modify the script. 