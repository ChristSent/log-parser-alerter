# log-parser-alerter
This will parse logs in a folder, using a given regular expression then store matches in a databse, send to email, or display on console.

Input to this script will require at least these 3 elements:
1. Folder path: A fully qualified path to a folder containing .log files you wish to monitor
2. Regex: The regular expression you wish to match on fora given line in a log file
3. Action{Console,Email,LogToFile,LogToDB}: This will specify what to do with the line from the monitored log that matched the regex.
*DB Name, Table, and credentials must be passed in if Action is DB.(Must be a mysql datbase)
*File path to log must be put in if Action is LogToFile.
*Email address must be passed in if action is Email.


This input can come from one of 3 sources:
1. Command line: Simply pass in required input as arguments on the command line.(Only 1 folder monitored, with one regex match)
2. CSV file: CSV file containg multiple log folders(with their corresponding regex and Action)
3. Database: MySQL datbase containg multiple log folders(with their corresponding regex and Action)

Sample command line input:
$> main.py -foldername "/var/log/apache2" -regex ".*404 PAGE NOT FOUND.*" -Action Email -ActionEmailAddress jsmith@example.com
