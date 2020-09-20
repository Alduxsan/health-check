#!/usr/bin/env python3
import os
import sys
import shutil
import socket
import psutil

def check_reboot():

	"""Devuelve True solo si la computadora tiene un reinicio pendiente."""

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

def check_cpu_constrained():
	"""Retorna True si el cpu esta bajo mucho uso"""
	return psutil.cpu_percent(1) > 75


def check_no_network():
	"""Retorna True si falla al resolver la url de google.com"""
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True

def main():
	checks=[
		(check_reboot,"Reinicio pendiente"),
		(check_cpu_constrained, "CPU Load too high"),
		(check_root_full,"Particion de raiz llena"),
		(check_no_network,"No hay conexion de red"),
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
 

