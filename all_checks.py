#!/usr/bin/env python3
import os
import sys

def check_reboot():

	"""Devuelve True si la computadora tiene un reinicio pendiente."""

	return os.path.exist("/run/reboot-required")
	
def main():
	if check_reboot():
		print("Reinicio pendiente, guarda el trabajo, salva el mundo")
		sys.exit(1)
	print("all ok")
	sys.exit(0)
	
main()
 
