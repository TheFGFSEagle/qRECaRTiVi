SUBDIRS = tabs images
AUTOMAKE_OPTIONS = gnu
ACLOCAL_AMFLAGS = -I m4

bin_SCRIPTS = qrecartivi

pymoddir = $(pythondir)/$(PACKAGE)
export pymoddir

nobase_pymod_PYTHON = application.py __init__.py mainwindow.py menus.py trayicon.py utils.py resources.py
resources.py: resources.qrc
	@echo "PYRCC $<"
	@ $(PYRCC) $< -o $@ -compress 9

all: resources.py
CLEANFILES = resources.py

run:
	PYTHONPATH=$PYTHONPATH:
