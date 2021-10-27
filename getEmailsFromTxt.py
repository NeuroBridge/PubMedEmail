#!/usr/bin/env python3
import os
import re
import argparse
import sys

def main(args):

    # Make sure the file is not empty
    filesize = os.path.getsize(args.inputFile)
    if filesize == 0:
       print(f"input file {args.inputFile} is zero length")
       sys.exit(0)

    emails = find_emails_in_text(args.inputFile)
    if emails:
       nEmails = len(emails)
       for i in range(nEmails):
          print(emails[i])
    else:
       print("No emails found")

def find_emails_in_text(file):
    pattern = re.compile('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}')
    emails = []
    for line in open(file):
       for match in re.finditer(pattern, line):
          emails.append(match.group())
    return (emails)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find email addresses in the named text file")
    parser.add_argument('--inputFile',  action="store", help= "Specify the file to convert")

    args = parser.parse_args()

    main(args)
