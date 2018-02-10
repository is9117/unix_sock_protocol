
import sys
import os
import time
from unix_sock_protocol import USP_CLIENT


    

if __name__ == "__main__":

    client = USP_CLIENT(sys.argv[1])
    
    client.send(sys.argv[2])