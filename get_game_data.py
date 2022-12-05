import os   # opratin system
import json  # json files
import shutil # allow to do some compy and overwrite operations
from subprocess import PIPE, run  # allow us to run go code any terminal comment 
import sys # to get access to the command line arguments

def main():
    pass

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("you must pass a source and target directory -only.")
