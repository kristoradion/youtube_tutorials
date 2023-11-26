import sys
print("Hello world!")
argv = sys.argv
print(f"Your inputs are {argv}")
if len(argv)>1:
	print(f"input argv[1] = {argv[1]}")
else:
	print("You don't have argv[1]")
if len(argv)>2:
	print(f"input argv[2] = {argv[2]}")
else:
	print("You don't have argv[2]")
