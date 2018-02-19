dnl
dnl $Id$
dnl

AC_PREREQ(2.61)
AC_INIT(oracle-sysvinit, 1.5, soliverr@gmail.com)

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
liblsb='/lib/lsb'
AC_MSG_CHECKING(liblsb)
AC_ARG_WITH(liblsb,
[  --with-liblsb=DIR       Directory for system wide functions files [/lib/lsb] ],
[ case "$withval" in
    no)
        AC_MSG_ERROR(Need liblsb)
        ;;
    [[\\/$]]* | ?:[[\\/]]* )
        liblsb="$withval"
        ;;
    yes | *)
        AC_MSG_ERROR([expected an absolute directory name for --with-liblsb: $withval])
        ;;
  esac ]
)
AC_SUBST(liblsb)
AC_MSG_RESULT($liblsb)

AC_CONFIG_FILES([Makefile logrotate.conf sqlnet.ora listener.ora])
AC_OUTPUT([_pkg-functions test.sh build_expand.sh])
AC_OUTPUT([ora_env.sh])
AC_OUTPUT([oracle-base-functions oracle-asm-functions oracle-dbconsole-functions])
AC_OUTPUT([oracle-grid-functions oracle-listener-functions oracle-rdbms-functions oracle-restart-functions])
AC_OUTPUT([oracle oracle-asm oracle-dbconsole])
AC_OUTPUT([oracle-grid oracle-listener oracle-rdbms oracle-restart])

