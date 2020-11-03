import requests
import os
from requests.auth import HTTPBasicAuth

class Client():
    def __init__(self, url, token, download_path):
        self.api_url = url
        self.token = token
        self.download_path = download_path

    def _make_dir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def _write_file(self, resp, file_name):
        self._make_dir(self.download_path)
        if resp:
            with open(self.download_path + file_name,"wb") as download_file:
                download_file.write(resp.content)
        else:
            print('Access failed!')

    def download(self, file_name):
        url = self.api_url + file_name
        headers = {'Token':self.token}
        resp = requests.get(url, headers=headers)
        self._write_file(resp, file_name)


if __name__ == "__main__":
    API_URL = 'http://x.x.x.x:8800/helloweb/api/'
    TOKEN = 'admin'
    FILENAME = 'tests.docx'
    DOWNLOADPATH = './downloaded/'
    Client = Client(API_URL, TOKEN, DOWNLOADPATH)
    Client.download(FILENAME)