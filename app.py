import sys
import os
import getopt
import message_crawler

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

def print_usage():
    print(
"""
USAGE: 
    python start_crawl_message.py
    python start_crawl_message.py --take-mode=NEW
    python start_crawl_message.py --take-mode=OLD""")

if len(sys.argv) > 1:
    try:
        options, args = getopt.getopt(sys.argv[1:], "", ["take-mode="])
    except:
        print_usage()
        exit(1)

message_crawler.run()
