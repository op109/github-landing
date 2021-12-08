from multiprocessing import Process
import time

class Subprocess(Process):

    def __init__(self, name):
        Process.__init__(self)
        self.name = name
    def run(self):
        print()