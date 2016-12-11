#
# Custom awk.py module
#


class controller:
    def __init__(self , f):
        self.m_file = f
        self.m_handlers = []

    def subscribe(self , o):
        self.m_handlers.append(o)

    def run(self):

        for o in self.m_handlers:
            o.begin()

        s = self.m_file.readline()

        while s != "":

            for o in self.m_handlers:
                o.process_line(s)

            s = self.m_file.readline()

        for o in self.m_handlers:
            o.end()

    def print_results(self):

        print
        print "Results:"
        print

        for o in self.m_handlers:
            print "------------------------------------------------------"
            print o.description()
            print "------------------------------------------------------"
            print o.result()