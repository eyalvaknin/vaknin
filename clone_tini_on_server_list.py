#!/usr/bin/python
import os
import sys

def main(server_list_file):

    ServerList = []
    with open(server_list_file, "r") as f:
        for server in f.readlines():
            s2 = "ssh -t " + server.rstrip() +  " \"git clone https://eyalvaknin:Idov2010@github.com/iguazio/tini.git\""
            print s2
            os.system(s2)


if __name__ == '__main__':
    main(sys.argv[1])

