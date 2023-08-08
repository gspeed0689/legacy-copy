import shutil as xu
import os
import argparse
import time
import datetime
import platform

from glob import glob

def cmdline():
    parser = argparse.ArgumentParser(description="Copy a CD using shutil.copytree and record errors.")
    if platform.system() == "Linux":
        media_path = glob("/media/*")[0]
        if media_path[-1] != "/":
            media_path += "/"
        media_list = glob(f"{media_path}*")
        if len(media_list) == 1:
            default_src = media_list[0]
        else:
            default_src = None
    parser.add_argument("-i", "--input", 
                help="Input drive",
                default=default_src)
    default_dst = os.getcwd() + os.sep + "contents"
    parser.add_argument("-o", "--output", 
                        help="Output directory", 
                        default=default_dst)
    default_log = os.getcwd() + os.sep + "transfer-log.txt"
    parser.add_argument("-l", "--log-file", 
                        help="Where to place the logs", 
                        dest="logfile", 
                        default=default_log)
    parser.add_argument("-sr", "--scsi-rom",
                        help="enumeration of the scsi rom drive",
                        choices=range(0, 10),
                        dest="scsi",
                        type=int, 
                        default=None)
    args = parser.parse_args()
    return(args)

class cdrecover():
    def __init__(self, src, dst, log_file):
        self.src = src
        self.dst = dst
        self.log_file = log_file
        self.process_start = time.time()
        self.copy_drive()
        self.process_end = time.time()
        self.process_elapsed = self.process_end - self.process_start
        self.write_log()

    def copy_drive(self):
        try:
            xu.copytree(self.src, self.dst)
        except xu.Error as e:
            self.errors = e

    def write_log(self):
        with open(self.log_file, "w+") as f:
            f.write("Geosciences CD Recovery Copy Script\n")
            f.write(datetime.datetime.now().isoformat() + "\n")
            f.write(f"Elapsed time (in seconds): {self.process_elapsed:.1}\n")
            f.write("\n\n")
            if hasattr(self, "errors"):
                f.write("Files errors:\n")
                for ef in self.errors.args[0]:
                    f.write(f"{ef[0]} -- {ef[-1]}\n")

def main():
    args = cmdline()
    src = args.input
    dst = args.output
    logfile = args.logfile
    if src == None and args.scsi != None:
        with open("/etc/mtab", "r") as mtab:
            r = mtab.read()
            s = r.split("\n")
            for line in s:
                splitline = line.split(" ")
                if splitline[0] == f"/dev/sr{args.scsi}":
                    src = splitline[1]
    print(f"{src}\n{dst}")
    cdrecover(src, dst, logfile)

if __name__ == "__main__":
    main()
