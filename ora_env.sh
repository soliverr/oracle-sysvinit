#! /bin/bash
#
# Export Oracle variables.
#
# Usage:
#   ora_env.sh [--sid SID] [--force] [--get-var VARIABLE_NAME]
#
# $Id$
#

source /lib/lsb/oracle-sysvinit-functions

largs="$@"

for i in $largs ; do
  case "$i" in
    --sid) shift
           ssid="$1"
           continue
    ;;
    --get-var) shift
           svarname="$1"
           continue
    ;;
    --force) 
           sforce="$i"
           continue
    ;;
  esac
done

if [ -n "$svarname" ] ; then
  oracle_cfg "$svarname" "$ssid"
elif [ -n "$ssid" ] ; then
  oracle_env "$ssid" $sforce
else
  oracle_env
fi

# Remove functions
func=`set | sed -ne 's/^\(oracle_.*\) *().*/\1/p' | tr -d '\n'`
unset $func
unset func ssid svarname sforce i largs
unset ORACLE_OKAY ORACLE_ERROR ORACLE_NOSID ORACLE_PASS

