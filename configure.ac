AC_PREREQ([2.69])
AC_INIT([qRECaRTiVi], [1.0], [qrecartivi@geisbergium.fr], [qrecartivi], [geisbergium.fr/qrecartivi/])
AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE

AC_CHECK_PROGS(PYRCC, [pyrcc, pyrcc5])
if test "$PYRCC" = ""; then 
	AC_MSG_ERROR([Qt utility program pyrcc5 is required.])
else
	PYRCCVERSION=`pyrcc -version`
	IFS=" "; PYRCCVERSION=($PYRCCVERSION); unset IFS
	#if test ${PYRCCVERSION[0]} = "pyrcc5"; then
	#	AC_MSG_ERROR([Qt utility program pyrcc5 has version ${PYRCCVERSION[1]}, but at least version v5.0.0 is required])
	#fi
fi


AM_PATH_PYTHON([3.6])
AC_CONFIG_FILES([Makefile])
AC_OUTPUT
