#!/usr/bin/python3

def test_var_args(f_arg, *argv):
	print("First normal arg:", f_arg)
	for arg in argv:
		print("Another arg through *argv :", arg)

test_var_args("Benson","Mwangi", "Kingori", "Software Engineer")
