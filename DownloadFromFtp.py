from PyQt5.QtCore import QThread
import ftplib


class DownloadFromFtp(QThread):

    def __init__(self, ip_address, parent=None):
        QThread.__init__(self, parent)
        self.ftp_ip = ip_address
        self.ftp = None
        self.ftp_channels = []
        self.ftp_day_directories = []
        self.ftp_connection()

    def ftp_connection(self):
        ftp = ftplib.FTP(self.ftp_ip)
        ftp.login()
        ftp.cwd(ftp.nlst()[0])
        self.ftp_channels = ftp.nlst()[2:6]


ftp_object = DownloadFromFtp('192.168.27.200')
print(ftp_object.ftp_channels)
ftp_object.quit()
