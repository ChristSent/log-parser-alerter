from LogWatcher import LogWatcher
import argparse
import re

parser = argparse.ArgumentParser("Usage")
parser.add_argument("-foldername", help="Put the fully qualified path to the foldr containing .log files",type=str,required=True)
parser.add_argument("-regex", help="Put the regular expression you would like to match on",type=str, required=True)
parser.add_argument("-action", help="Put the action that should take place on a regex match:Email,LogToFile,LogToDB,Console",type=str, required=True)
parser.add_argument("-ActionEmailAddress", help="Email to whom the matched line should be sent: jsmith@example.com",type=str)
parser.add_argument("-ActionLogFile", help="Put the fully qualified path to the log file that matched lines should be written to.",type=str)
parser.add_argument("-ActionDBConnectionString", help="DB to store matched lines to: 'server=127.0.0.1;uid=root;pwd=12345;database=test'  *Table will be named matched",type=str)
args = parser.parse_args()
foldername = args.foldername
regex = args.regex

def callback(filename, lines):
    for line in lines:
        if(re.match(regex,line)):
            print(line)
lw = LogWatcher(foldername,callback)
lw.loop()