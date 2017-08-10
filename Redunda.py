#
# Redunda-lib-Python
# Redunda.py
#
# Created by Ashish Ahuja (Fortunate-MAN) on 23rd July 2017.
#
# A python library for using Redunda.
#

from urllib import request, parse
import json
import pickle

class Redunda:
    """
    The main class you need to use to use Redunda
    """
    def __init__(self, key, filesToSync, version="unknown"):
        """
        Construct a new 'Redunda' object.
        
        :param str key: The instance key you get from Redunda
        :param filesToSync: A list of files which you want to sync with Redunda; should be empty if no files should be synced. The list should be made up of dictionaries, in the format '{"name": <enter filename>, "ispickle": <bool>}'
        :param str version: Optional variable to tell the version of the bot; is "unknown" by default
        :return: returns nothing
        """
        self.key = key
        #'filesToSync' should be a list of dicts, in the format {"name": "<enter name>", "ispickle": <Bool>}
        self.filesToSync = filesToSync
        self.version = version
        self.location = "unknown"
        self.eventCount = 0
        self.shouldStandby = False

    def sendStatusPing(self):
        """
        Sends a status ping to Redunda with the instance key specified while constructing the object.
        """
        data = parse.urlencode({"key": self.key, "version": self.version}).encode()
        req = request.Request("https://redunda.sobotics.org/status.json", data)

        response = request.urlopen(req)

        jsonReturned = json.loads(response.read().decode("utf-8"))

        self.location = jsonReturned["location"]
        self.shouldStandby = jsonReturned["should_standby"]
        self.eventCount = jsonReturned["event_count"]

    def uploadFile(self, filename, ispickle=False):
        """
        Uploads a single file to Redunda.

        :param str filename: The name of the file to upload
        :param bool ispickle: Optional variable to be set to True is the file is a pickle; default is False.
        :returns: returns nothing
        """
        print("Uploading file {} to Redunda.".format(filename))
        
        url = "https://redunda.sobotics.org/bots/data/{}?key={}".format(filename,self.key)
        
        #Set the content type to 'application/octet-stream'
        header = {"Content-type": "application/octet-stream"}
        
        filedata = ""

        #Read the data from a file to a string.
        if filename.endswith(".pickle") or ispickle:
            try:
                with open(filename, "rb") as fileToRead:
                    data = pickle.load(fileToRead)
            except pickle.PickleError as perr:
                print("Pickling error occurred: {}".format(perr))
                return
            filedata = json.dumps(data)
        else:
            try:
                with open(filename, "r") as fileToRead:
                    filedata = fileToRead.read()
            except IOError as ioerr:
                print("IOError occurred: {}".format(ioerr))
                return

        requestToMake = request.Request(url, data=filedata.encode("utf-8"), headers=header)

        #Make the request.
        response = request.urlopen(requestToMake)

        if response.code >= 400:
            print("Error occurred while uploading file '{}' with error code {}.".format(filename,response.code))

    def downloadFile(self, filename, ispickle=False):
        """
        Downloads a single file from Redunda.

        :param str filename: The name of the file you want to download
        :param bool ispickle: Optional variable which tells if the file to be downloaded is a pickle; default is False.
        :returns: returns nothing
        """
        print("Downloading file {} from Redunda.".format(filename))

        url = "https://redunda.sobotics.org/bots/data/{}?key={}".format(filename,self.key)

        requestToMake = request.Request(url)

        #Make the request.
        response = request.urlopen(requestToMake)

        if response.code != 200:
            print("Error occured while downloading file '{}' with error code {}.".format(filename,response.code))


        filedata = response.read().decode("utf-8")

        try:
            if filename.endswith (".pickle") or ispickle:
                data = json.loads(filedata)
                try:
                    with open(filename, "wb") as fileToWrite:
                        pickle.dump (data, fileToWrite)
                except pickle.PickleError as perr:
                    print("Pickling error occurred: {}".format(perr))
                    return
            else:
                with open (filename, "w") as fileToWrite:
                    fileToWrite.write(filedata)
        except IOError as ioerr:
            print("IOError occurred: {}".format(ioerr))
            return

    def uploadFiles(self):
        """
        Uploads all the files in 'filesToSync'
        """
        for each_file in self.filesToSync:
            self.uploadFile(each_file["name"], each_file["ispickle"])

    def downloadFiles(self):
        """
        Downloads all the files in 'filesToSync'
        """
        for each_file in self.filesToSync:
            self.downloadFile(each_file["name"], each_file["ispickle"])


