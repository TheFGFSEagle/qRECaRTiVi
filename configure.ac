AC_PREREQ([2.69])
AC_INIT([qRECaRTiVi], [1.0], [qrecartivi@geisbergium.fr], [qrecartivi], [geisbergium.fr/qrecartivi/])
AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE

AC_ARG_VAR([PYRCC], [The name or full path of pyrcc. Version 5 is required.])

AC_PROG_GREP
AC_CHECK_PROGS([PYRCC], [pyrcc5 pyrcc], [])
AS_IF([test "x${PYRCC}" = x],
	[AC_MSG_ERROR([Required program pyrcc5 was not found])])

AC_MSG_CHECKING([whether ${PYRCC} has an appropriate version])
AS_IF([test $(pyrcc5 -version 2>&1 | cut -dv -f2 | cut -d"." -f1) -ne "5"], [
	AC_MSG_RESULT([no])
	AC_MSG_ERROR([pyrcc version 5.x.x is required, but ${PYRCC} is a different version])
], [
  AC_MSG_RESULT([yes])
])


AM_PATH_PYTHON([3.6])
AC_CONFIG_FILES([Makefile tabs/Makefile])
AC_OUTPUT
