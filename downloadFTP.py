#pip install pyftpdlib


import ftplib
from datetime import datetime

def grabFile(filename):
  localfile = open(filename, 'wb')
  ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
  localfile.close()


ftp = ftplib.FTP("72.167.38.171")
ftp.login("crisol@alephimprime.com", "8?oBzYnnDK,5")

data = []
fecha = datetime.now().strftime('%Y%m%d')
print(fecha)

ftp.dir(data.append)

for line in data:
    if fecha in line:
        comp = line.split()
        print(comp[-1])
        filename = comp[-1]
        grabFile(filename)

ftp.quit()