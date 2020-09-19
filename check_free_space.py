#!/usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absolutgbe, min_percent):
	"""	Returns True if there is enough free disk space."""
	du = shutil.disk_usage(disk)
	#calculate the percentage of free space
	percent_free = 100 * du.free / du.total
	#calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_absolute:
		return False
	return True

#check for at least 2 GB and 10% free
if not check_disk_usage(dik="/",min_absolute=2,min_percent=10):
	print("ERROR: No hay suficiente espacio en disco.")
	sys.exit(1)

print("Todo funciona impecable.")
sys.exit(0)
