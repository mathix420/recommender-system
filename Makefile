.SILENT:

all:
	echo "try 'make test'"

test:
	/bin/env python3 test.py
	clean > /dev/null
