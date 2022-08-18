#pip install pyftpdlib


import ftplib
from datetime import datetime

vhost = ""
vuser = ""
vpass = "" 

def grabFile(filename):
  localfile = open(filename, 'wb')
  ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
  localfile.close()


ftp = ftplib.FTP(vhost)
ftp.login(vuser, vpass)

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