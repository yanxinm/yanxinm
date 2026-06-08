#!/usr/bin/env python3
"""Check if today is the last working day of month/quarter/year.
Output formats:
  NOT_TODAY              → not the right day
  LAST_WORKING_DAY|month → last working day of month
  LAST_WORKING_DAY|quarter → last working day of quarter
  LAST_WORKING_DAY|year  → last working day of year
"""
import calendar
from datetime import date, timedelta

def last_working_day(ref_date):
    """Return the last working day of ref_date's month."""
    last_day = ref_date.replace(
        day=calendar.monthrange(ref_date.year, ref_date.month)[1]
    )
    while last_day.weekday() >= 5:  # Mon=0..Sun=6
        last_day -= timedelta(days=1)
    return last_day

today = date.today()
lwd = last_working_day(today)

if today != lwd:
    print("NOT_TODAY")
else:
    print(f"LAST_WORKING_DAY|{today.isoformat()}|month")
    if today.month in [3, 6, 9, 12]:
        print(f"LAST_WORKING_DAY|{today.isoformat()}|quarter")
    if today.month == 12:
        print(f"LAST_WORKING_DAY|{today.isoformat()}|year")
