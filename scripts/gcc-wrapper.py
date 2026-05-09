#!/usr/bin/env python3
import sys, subprocess

def main():
    args = sys.argv[1:]
    try:
        proc = subprocess.Popen(args, stderr=subprocess.PIPE)
        for line in proc.stderr:
            line = line.decode("utf-8", errors="replace")
            sys.stderr.write(line)
        result = proc.wait()
    except OSError as e:
        result = e.errno
    sys.exit(result)

main()
