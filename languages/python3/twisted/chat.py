# ref : https://twistedmatrix.com/documents/current/core/howto/servers.html

from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Chat(LineReceiver):

    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        """Life cycle : connectionMade """
        self.sendLine("What's your name?".encode('utf8'))

    def connectionLost(self, reason):
        """Life cycle : connectionLost """
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        """Call back for  self.sendLine(line)"""
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine("Name taken, please choose another.".encode('utf8'))
            return
        self.sendLine(("Welcome, %s!" % (name,)).encode('utf8'))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name, message)
        for name, protocol in self.users.items():  # name is self.name  and protocol is self
            if protocol != self:
                protocol.sendLine(message.encode('utf8')) # Print message of other user in the line


class ChatFactory(Factory):

    def __init__(self):
        self.users = {} # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)


reactor.listenTCP(8123, ChatFactory())
reactor.run()