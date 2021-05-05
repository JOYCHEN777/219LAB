# This is the code that runs this example.
from person import Person
from Pyro5.api import Proxy
import sys
import Pyro5.errors

# sys.excepthook 对全局异常进行捕获
sys.excepthook = Pyro5.errors.excepthook

# uri = input("enter the uri of the warehouse:").strip()

warehouse = Proxy("PYRONAME:example.warehouse")
janet = Person("Janet")
henry = Person("Henry")
janet.visit(warehouse)
henry.visit(warehouse)
