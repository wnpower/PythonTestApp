import sys, os

INTERP = os.path.dirname(os.path.abspath(__file__)) + "/venv/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
  
from miapp import app as application
