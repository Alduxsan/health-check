#!/usr/bin/env python3
import os
import sys
import shutil
import sys

def check_reboot():

	"""Devuelve True si la computadora tiene un reinicio pendiente."""

	return os.path.exists("/run/reboot-required")
	

def check_disk_usage(disk, min_gb, min_percent):
	"""	Returns True if there is enough free disk space."""
	du = shutil.disk_usage(disk)
	#calculate the percentage of free space
	percent_free = 100 * du.free / du.total
	#calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if percent_free < min_gb or percent_free < min_percent:
		return True
	return False


def check_root_full():
	"""Returns True if the root partition is full, False otherwise"""
	return check_disk_usage(disk="/",min_gb=2,min_percent=10)
	
def main():
	
	#check for at least 2 GB and 10% free
	if check_root_full():
		print("ERROR: No hay suficiente espacio en disco.")
		sys.exit(1)

	if check_reboot():
		print("Reinicio pendiente, guarda el trabajo, salva el mundo")
		sys.exit(1)
	
	print("Todo impecable")
	sys.exit(0)
	
main()
 
