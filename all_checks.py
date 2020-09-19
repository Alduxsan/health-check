#!/usr/bin/env python3
import os
import sys
import shutil
import sys

def check_reboot():

	"""Devuelve True si la computadora tiene un reinicio pendiente."""

	return os.path.exists("/run/reboot-required")
	

def check_disk_usage(disk, min_gb, min_percent):
	"""	Devuelve True si no hay suficiente espacio en disco"""
	du = shutil.disk_usage(disk)
	#calculate the percentage of free space
	percent_free = 100 * du.free / du.total
	#calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if percent_free < min_gb or percent_free < min_percent:
		return True
	return False


def check_root_full():
	"""Devuelve True si la particion de raiz esta llena"""
	return check_disk_usage(disk="/",min_gb=2,min_percent=10)
	
def main():
	checks=[
		(check_reboot,"Reinicio pendiente"),
		(check_root_full,"Particion de raiz llena"),
		]
	everything_ok = True
	for check, msg in checks:
		if check():
			print(msg)
			everything_ok=False
			
	if not everything_ok:
		sys.exit(1)
	
	print("Todo impecable")
	sys.exit(0)
	
main()
 
