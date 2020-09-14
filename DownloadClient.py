import requests
import os
from requests.auth import HTTPBasicAuth

class Client():
    def __init__(self, account, password, file_name, download_path):
        self.account = account
        self.paasword = password
        self.file_name = file_name
        self.download_path = download_path

    def _make_dir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def download(self):
        url = 'http://10.141.124.235/helloweb/download/' + self.file_name
        self._make_dir(self.download_path)
        resp = requests.get(url,auth=HTTPBasicAuth(self.account,self.paasword))
        with open(self.download_path+self.file_name,"wb") as download_file:
            download_file.write(resp.content)


if __name__ == "__main__":
    ACCOUNT = 'usr'
    PASSWORD = '123'
    FILENAME = 'tests.xlsx'
    DOWNLOADPATH = './downloaded/'
    Client = Client(ACCOUNT, PASSWORD, FILENAME, DOWNLOADPATH)
    Client.download()