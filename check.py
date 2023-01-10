import os, sys
try:
    __import__("check").menu()
except Exception as e:
    exit(str(e))
