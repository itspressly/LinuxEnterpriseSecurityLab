#!/bin/bash


echo "////  TechCorp Server Report  \\\\"

echo

echo  "Hostname:"
hostname

echo

echo "Current User:"
whoami

echo

echo "Kernel:"
uname -r

echo

echo "Disk Usage:"
df -h

echo

echo "Memory:"
free -h

echo

echo "Running Uptime:"
uptime

echo

echo "IP Adress:"
hostname -I

echo

echo "=========================================================="

