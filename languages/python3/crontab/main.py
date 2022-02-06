#!/usr/bin/env python
# coding: utf-8

from crontab import CronTab

# Work on Windows too
CronTab()
file_cron = CronTab(tabfile='filename.tab')
mem_cron = CronTab(tab="""
  * * * * * command
""")

