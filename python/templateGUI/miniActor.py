import logging

import actorcore.ICC
from actorcore.QThread import QThread
from functools import partial


class OurActor(actorcore.ICC.ICC):
    def __init__(self, name, productName=None, modelNames=None, configFile=None, logLevel=logging.INFO):
        # This sets up the connections to/from the hub, the logger, and the twisted reactor.
        #
        modelNames = [] if modelNames is None else modelNames
        actorcore.ICC.ICC.__init__(self, name,
                                   productName=productName,
                                   configFile=configFile,
                                   modelNames=modelNames)

        self.logger.setLevel(logLevel)
        self.everConnected = False
        self.allThreads = {}

        self.createThread('cmdrThread')

    def createThread(self, name):
        thread = QThread(self, name)
        thread.start()
        thread.handleTimeout = self.sleep
        self.allThreads[name] = thread

    def connectionMade(self):
        if self.everConnected is False:
            logging.info("alive!!!!")
            self.everConnected = True

    def disconnectActor(self):
        self.shuttingDown = True

    def threadCmd(self, **kwargs):
        self.allThreads['cmdrThread'].putMsg(partial(self.cmdr.call, **kwargs))

    def sleep(self):
        pass


def connectActor(modelNames):
    theActor = OurActor('templategui',
                        productName='templateGUI',
                        modelNames=modelNames,
                        logLevel=logging.DEBUG)

    theActor.run(doReactor=False)
    return theActor
