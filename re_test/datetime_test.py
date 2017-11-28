# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	utc_dt = dt.replace(tzinfo=timezone.utc)
	tz = re.match(r'^UTC([+-])([0][0-9]|[1][0-2]|[0-9]):([0]{2})$', tz_str)
	v_tz = tz.group(1)
	v_hour = int(tz.group(2))
	if v_tz == '+':
		tz_utc_nm = timezone(timedelta(hours=v_hour))
	else:
		tz_utc_nm = timezone(timedelta(hours=-v_hour))
	new_utc = utc_dt.replace(tzinfo=tz_utc_nm)
	return new_utc.timestamp()


if __name__ == '__main__':
	t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
	assert t1 == 1433121030.0, t1
	t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
	assert t2 == 1433121030.0, t2
	print('ok')
