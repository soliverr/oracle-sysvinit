dnl
dnl $Id$
dnl

AC_PREREQ(2.61)
AC_INIT(oracle-sysvinit, 1.1, soliverr@gmail.com)

dnl Define variable localstatedir
dnl localstatedir='/var'
dnl AC_SUBST(localstatedir)
dnl AC_MSG_RESULT($localstatedir)

dnl Define variable datadir
dnl datadir='${datarootdir}/packages/${PACKAGE_NAME}'
dnl AC_SUBST(datadir)
dnl AC_MSG_RESULT($datadir)


dnl Option: --with-logdir
logdir='${localstatedir}/log/oracle'
AC_MSG_CHECKING(logdir)
AC_ARG_WITH(logdir,
[  --with-logdir=DIR       Directory for logfiles [LOCALSTATEDIR/log/oracle] ],
[ case "$withval" in
    no)
        AC_MSG_ERROR(Need logdir)
        ;;
    [[\\/$]]* | ?:[[\\/]]* )
        logdir="$withval"
        ;;
    yes | *)
        AC_MSG_ERROR([expected an absolute directory name for --with-logdir: $withval])
        ;;
  esac ]
)
AC_SUBST(logdir)
AC_MSG_RESULT($logdir)

dnl Option: --with-confdir
confdir='${sysconfdir}/${PACKAGE_NAME}'
AC_MSG_CHECKING(confdir)
AC_ARG_WITH(confdir,
[  --with-confdir=DIR      Directory for config files [SYSCONFDIR/PACKAGE_NAME] ],
[ case "$withval" in
    no)
        AC_MSG_ERROR(Need confdir)
        ;;
    [[\\/$]]* | ?:[[\\/]]* )
        confdir="$withval"
        ;;
    yes | *)
        AC_MSG_ERROR([expected an absolute directory name for --with-confdir: $withval])
        ;;
  esac ]
)
AC_SUBST(confdir)
AC_MSG_RESULT($confdir)

dnl Directory to install library according with LSB
lsbdir='/lib/lsb'
AC_MSG_CHECKING(lsbdir)
AC_ARG_WITH(lsbdir,
[  --with-lsbdir=DIR      Directory for config files [/lib/lsb] ],
[ case "$withval" in
    no)
        AC_MSG_ERROR(Need confdir)
        ;;
    [[\\/$]]* | ?:[[\\/]]* )
        lsbdir="$withval"
        ;;
    yes | *)
        AC_MSG_ERROR([expected an absolute directory name for --with-lsbdir: $withval])
        ;;
  esac ]
)
AC_SUBST(lsbdir)
AC_MSG_RESULT($lsbdir)

AC_CONFIG_FILES([Makefile logrotate.conf sqlnet.ora listener.ora])
AC_OUTPUT([_pkg-functions test.sh build_expand.sh])
AC_OUTPUT([oracle-sysvinit-functions oracle-asm-functions oracle-dbconsole-functions])
AC_OUTPUT([oracle-grid-functions oracle-listener-functions oracle-rdbms-functions oracle-restart-functions])
AC_OUTPUT([oracle oracle-asm oracle-dbconsole])
AC_OUTPUT([oracle-grid oracle-listener oracle-rdbms oracle-restart])

