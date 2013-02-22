# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:35:06 2012

@author: Jacob Simmering

The code used in pingTool is an implentation of python ping tools 
(re)written by George Notaras at http://www.g-loaded.eu/2009/10/30/python-ping/
"""
# this has to be run as root in order to send ICMP messages
import time, pingTool

# change this list to reflect the ip's you want to ping off of
# I wanted to test an IP local to my network, the jump to my 
# ISP's network and a few possible "trouble makers" along the way
# in addition to the final IP of the remote host I pinged against
websites = ['192.168.1.1', 'ip1', 'ip2', 
            'ipOfRemoteTarget']

def monitor(sites = websites, duration = 10, n = 4, 
    outname = 'pingResultsHops.csv'):
    ''' This function pings each target IP n times, pause for 5 seconds
    and then repeat the process for duration minutes. 
    Arguments: 
        sites - a list of IPs to ping
        duration - the number of seconds to collect data
        n - the number of times to ping each IP per sampling phase
        outname - the name of the file to write the data to (as csv)
    Returns:
        by default the function does not return anything to standard output 
        but will write a file with the title of outname to the directory where
        this script is called
    '''
    startTime = time.time()
    endTime = startTime + duration
    pingTime = []
    pingTarget = []
    pingResult = []
    while time.time() <= endTime:
        for site in sites:
            for iteration in range(n):
                # looping here instead of saying count = n in 
                # pingTool.verbose_ping() just to make writing
                # to the lists a bit easier since we want to
                # make sure that the timing and IP variables 
                # are properly aligned in the output
                pingTime.append(time.ctime(time.time()))
                pingTarget.append(site)
                pingResult.append(pingTool.verbose_ping(site, count = 1))
        time.sleep(5)
    writeResults(out = outname, pingTime = pingTime, 
        pingTarget = pingTarget, pingResult = pingResult)

def writeResults(out, pingTime, pingTarget, pingResult):
    ''' A simple function to write the results of the ping tests to 
    a csv file for analysis in R or another tool
    Arguments:
        out - name of the file to be written to
        pingTime - a list of the pingTimes from monitor
        pingTarget - the target IP for each ping
        pingResults - the results of the ping test
    Returns:
        by default, writes out.csv to directory the script was run in
    '''
    fout = open(out, 'w')
    for ping in range(len(pingTime)):
        outStr = str(pingTime[ping]) + ', ' + str(pingTarget[ping]) + ', ' + str(pingResult[ping]) + '\n' 
        fout.write(outStr)
    fout.close()

monitor(outname = 'pingTimes.csv', duration = 60, n = 4)