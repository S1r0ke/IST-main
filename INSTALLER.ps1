[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
irm get.scoop.sh | iex
scoop bucket add extras
scoop install python
pip install pillow
pip install numpy
pip install tkinter
