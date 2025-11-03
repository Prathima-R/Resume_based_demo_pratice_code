#!/bin/bash
###############################################################################
# Author  : Prathima R
# Title   : EC2 Uptime Monitor Script
# Purpose : To check how long the EC2 instance has been running (uptime)
#           and log the details with timestamps for server monitoring.
# Date    : 2025-11-03
###############################################################################

# Set the path for the log file
LOG_FILE="/home/ec2-user/ec2_uptime.log"

# Print a header for readability in the log
echo "=====================================================" >> $LOG_FILE
echo "Uptime Check performed at: $(date)" >> $LOG_FILE
echo "-----------------------------------------------------" >> $LOG_FILE

# Run the uptime command and append output to the log file
uptime >> $LOG_FILE

# Print a separator for clarity
echo "=====================================================" >> $LOG_FILE
echo "" >> $LOG_FILE

# Optional: Display the latest uptime entry on the console
echo "✅ EC2 Uptime logged successfully at $(date)"
echo "📄 Log File: $LOG_FILE"
