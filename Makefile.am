SUBDIRS = tabs images
ACLOCAL_AMFLAGS = -I m4

bin_SCRIPTS = qrecartivi

pymoddir = $(pythondir)/$(PACKAGE)
export pymoddir

nobase_pymod_PYTHON = application.py __init__.py mainwindow.py menus.py trayicon.py utils.py resources.py
resources.py: resources.qrc style.qss images/icon.png
	@echo "PYRCC $<"
	@ $(PYRCC) $< -o $@ -compress 9

all: resources.py
CLEANFILES = resources.py

run:
	@echo "Running qrecartivi"
	@PYTHONPATH=${PYTHONPATH}:$(abs_srcdir)/..; ./qrecartivi $(ARGS)
