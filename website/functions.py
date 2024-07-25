#!/usr/bin/env python3

from datetime import datetime
import pytz
from tzlocal import get_localzone

def convert_utc_to_local(utc_datetime):
    # Convert UTC datetime to your local timezone
    local_timezone = get_localzone()
    local_datetime = utc_datetime.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    
    return local_datetime
