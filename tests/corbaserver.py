from pyhpp.core import ProblemSolver
from pyhpp.corbaserver import Server

ps = ProblemSolver.create()

server = Server (ps, False)
server.startCorbaServer()
server.processRequest (True)
