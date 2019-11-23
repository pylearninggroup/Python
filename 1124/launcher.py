#!/usr/bin/python3
# coding: utf-8

# untitled - launcher.py
# 17/11/2019 18:30
#

__author__ = "Benny <benny.think@gmail.com>"
import PySimpleGUI as sg
import subprocess
import logging

logging.basicConfig(level=logging.INFO)


def cmder(cmd):
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)


mysql_start = 'cd /Users/benny/Apps/mysql/bin && ./mysqld'
mysql_stop = 'killall mysqld'
mongodb_start = '/Users/benny/Apps/mongodb/bin/mongod --dbpath=/Users/benny/Apps/mongodb/data'
mongodb_stop = 'killall mongod'
sg.change_look_and_feel('Material1')  # Add a touch of color
# All the stuff inside your window.

MySQL = sg.Button('Start', key='MySQL', size=(10, 5))
MongoDB = sg.Button('Start', key='mongodb', size=(10, 5))
layout = [
    [sg.Text('MySQL'), MySQL],
    [sg.Text('MongoDB'), MongoDB],
]

# Create the Window
window = sg.Window('Database Launcher', layout, size=(300, 300))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'MySQL' and MySQL.ButtonText == 'Start':
        logging.info(f'Starting {event}...')
        cmder(mysql_start)
        window['MySQL'].update('Stop')
        logging.info(f'{event} started.')
    elif event == 'MySQL' and MySQL.ButtonText == 'Stop':
        logging.info(f'Stopping {event}...')
        cmder(mysql_stop)
        window['MySQL'].update('Start')
        logging.info(f'{event} stopped.')
    elif event == 'mongodb' and MongoDB.ButtonText == 'Start':
        logging.info(f'Starting {event}...')
        cmder(mongodb_start)
        window['mongodb'].update('Stop')
        logging.info(f'{event} started.')
    elif event == 'mongodb' and MongoDB.ButtonText == 'Stop':
        logging.info(f'Stopping {event}...')
        cmder(mongodb_stop)
        window['mongodb'].update('Start')
        logging.info(f'{event} stopped.')

    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break

logging.warning("Close MongoDB and MySQL...")
cmder(mysql_stop)
cmder(mongodb_stop)
logging.warning('Exiting...')
window.close()
