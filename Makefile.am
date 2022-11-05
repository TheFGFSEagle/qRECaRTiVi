SUBDIRS = qrecartivi
ACLOCAL_AMFLAGS = -I m4

bin_SCRIPTS = bin/qrecartivi

pymoddir = $(pythondir)/$(PACKAGE)
export pymoddir

run:
	@echo "Running qrecartivi"
	@PYTHONPATH="${PYTHONPATH}:$(abs_srcdir)" bin/qrecartivi $(ARGS)
