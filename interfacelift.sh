#!/bin/bash

# Cron does not have the environment variables needed to use gsettings. We need environment variables which are set after a user has logged into the X server. Here, we use the process of an existing graphical program to set the appropriate environment variables.

# Help came mainly from this answer (among others):
# http://stackoverflow.com/questions/10374520/gsettings-with-cron

# Find the process ID of a graphical program we know is running
PID=$(pgrep gnome-session)

# Obtain the dbus address from the environment of the graphical process
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

# Move to the directory this script is in so we can run the Python script
cd "$(dirname "$0")"

# Run the script!
python ./interfacelift.py
