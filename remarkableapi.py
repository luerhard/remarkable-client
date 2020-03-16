from configparser import ConfigParser
import json
import logging
import sys
import requests


class HTTPError(Exception):

    def __init__(self, msg, code=None):
        self.code = code
        self.message = msg

    def __str__(self):
        return f"HTTPError {self.code}: {self.message}"


class RemarkableAPI:

    COLLECTION_TYPE = "CollectionType"
    DOCUMENT_TYPE = "DocumentType"
    AUTH_API = "https://my.remarkable.com"
    SERVICE_DISCOVERY_API = ("https://service-manager-production-dot-"
                             "remarkable-production.appspot.com")
    STORAGE_API = ("https://document-storage-production-dot-"
                   "remarkable-production.appspot.com")

    def __init__(self, config_path):
        self.logger = self.setup_logger()
        self.config_path = config_path
        self.config = ConfigParser()
        self.config.read(self.config_path)
        self.token = self.config.get("Tokens", "bearer_token")

    @staticmethod
    def setup_logger():
        logging.captureWarnings(True)
        datefmt = "%H:%M:%S"
        logger = logging.getLogger("remarkable_client")
        logger.propagate = False
        logger.setLevel(logging.DEBUG)

        stream_fmt = "[%(asctime)s.%(msecs)03d] %(message)s"
        stream_formatter = logging.Formatter(fmt=stream_fmt, datefmt=datefmt)

        stream_handler = logging.StreamHandler(stream=sys.stdout)

        stream_handler.setFormatter(stream_formatter)
        stream_handler.setLevel(logging.DEBUG)

        logger.addHandler(stream_handler)

        return logger

    def header(self):
        header = {"Authorization": "Bearer " + self.token}
        self.logger.debug("HEADER: %s", header)
        return header

    def new_token(self, code):
        data = {
            "code": code,
            "deviceDesc": "desktop-windows",
            "deviceID": "123456"
        }
        data = json.dumps(data)
        self.logger.info("Registering new device")
        resp = requests.post(self.AUTH_API + "/token/json/2/device/new",
                             data=data)
        if resp.status_code == 200:
            return resp.text
        raise HTTPError(resp.text, resp.status_code)

    def refresh_token(self):
        self.logger.info("Requesting new Token")
        resp = requests.post(self.AUTH_API + "/token/json/2/user/new",
                             headers=self.header())

        if resp.status_code == 200:
            #self.config.set("Tokens", "token", resp.text)
            #with open(self.config_path, "w") as cfg:
            #    self.config.write(cfg)
            return resp.text
        raise HTTPError(resp.text, resp.status_code)

    def list_items(self):
        request_url = self.STORAGE_API + "/document-storage/json/2/docs"
        self.logger.info("Listing all items")
        self.logger.debug("Using URL: %s", request_url)
        resp = requests.get(request_url, headers=self.header())
        if resp.status_code == 200:
            return json.loads(resp.text)
        raise HTTPError(resp.text, resp.status_code)

    def download_item(self, document_id):
        request_url = self.STORAGE_API + "/document-storage/json/2/docs"
        data = {"query": {
            "doc": document_id,
            "withBlob": "true",
        }}
        data = json.dumps(data)
        resp = requests.get(request_url, data=data, headers=self.header())
        if resp.status_code == 200:
            return json.loads(resp.text)
        raise HTTPError(resp.text, resp.status_code)


if __name__ == "__main__":
    api = RemarkableAPI("config.ini")
    #print(api.refresh_token())
    print(api.list_items())
    #
