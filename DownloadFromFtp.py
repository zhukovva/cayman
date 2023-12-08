from PyQt5.QtCore import QThread
from ftplib import FTP
from re import findall
from os import mkdir, path


class DownloadFromFtp(QThread):

    def __init__(self, ip_address, parent=None):
        QThread.__init__(self, parent)
        if ip_address:
            self.ftp_ip = ip_address
            self.ftp = FTP(self.ftp_ip)
        if not ip_address:
            raise ValueError("No IP address")

    def get_file_list(self, path):
        self.ftp.cwd(path)
        files = []
        for file in self.ftp.nlst():
            if findall(r'\d{6}.WAV', file):
                files.append(file)
        return files

    def get_local_directory(self, directory, name, data):
        try:
            mkdir(directory)
        except WindowsError as e:
            print(e)
        try:
            mkdir(f'{directory}\\{name}')
        except WindowsError as e:
            print(e)
        try:
            mkdir(f'{directory}\\{name}\\{data}')
        except WindowsError as e:
            print(e)

    def download_files(self, files, directory, name, data):
        path_local_file = f'{directory}\\{name}\\{data}\\'
        for file in files:
            file_host = path.join(f'{path_local_file}{data}_{file}')
            if not path.isfile(file_host):
                with open(file_host, 'wb') as local_file:
                    self.ftp.retrbinary('RETR ' + file, local_file.write)


ip = "192.168.39.200"
node_root = 'DIGIOLOG'
node_channel = 'CHANNEL1'
node_data = '20231208'
path_dir_ftp = f'{node_root}\\{node_channel}\\{node_data}'
directory_local = 'd:\Объекты'
ftp_name = 'Тестовый'

try:
    ftp_object = DownloadFromFtp(ip)
    ftp_object.ftp.login()
    file_list = ftp_object.get_file_list(path_dir_ftp)
    ftp_object.get_local_directory(directory_local, ftp_name, node_data)
    print(file_list)
    ftp_object.download_files(file_list, directory_local, ftp_name, node_data)

except Exception as e:
    print(e)
finally:
    ftp_object.ftp.quit()
