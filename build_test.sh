#! /bin/bash

./build.sh

package=`cat ./configure.ac | sed -ne 's/^AC_INIT(\([^,]*\)\s*,.*/\1/gp'`

distr=REDHAT
destdir=$distr

./configure --prefix=`pwd`/$destdir/  \
 --with-lsbdir=`pwd`/$destdir/lib/lsb \
 --with-confdir=`pwd`/$destdir/etc/sysconfig \
 --with-logdir=`pwd`/$destdir/var/log/oracle

chmod +x test.sh

make install DISTRIB=$distr DESTDIR=$destdir prefix="/" \
  lsbdir=/lib/lsb \
  sysconfdir=/etc confdir=/etc/sysconfig \
  logdir=/var/log/oracle
  docdir=/usr/share/doc \
|| exit 1


distr=DEBIAN
destdir=$distr

./configure --prefix=`pwd`/$destdir/ --sysconfdir=`pwd`/$destdir/etc \
 --with-lsbdir=`pwd`/$destdir/lib/lsb \
 --with-confdir=`pwd`/$destdir/etc/default \
 --with-logdir=`pwd`/$destdir/var/log/oracle

chmod +x test.sh

make install DISTRIB=$distr DESTDIR=$destdir prefix="/" \
  lsbdir=/lib/lsb \
  sysconfdir=/etc confdir=/etc/default \
  logdir=/var/log/oracle
  docdir=/usr/share/doc \
|| exit 1
