Crontab parser for human readable output

For example, the following input argument:
*/15 0 1,15 * 1-5 /usr/bin/find
Should yield the following output:
  
minute
hour
day of month month dayofweek command
0 15 30 45
0
1 15
1 2 3 4 5 6 7 8 9 10 11 12 12345
/usr/bin/find