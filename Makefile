.SILENT:

all:
	echo "type 'make test'"

test:
	/bin/env python3 test.py
	clean > /dev/null
