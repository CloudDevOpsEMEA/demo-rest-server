#!/bin/sh
set -e

CMD="python demoserver.py"

if [ ! -z "${BASEPATH}" ] ; then
  CMD="${CMD} -b ${BASEPATH}"
fi

if [ ! -z "${DELAY}" ] ; then
  CMD="${CMD} -d ${DELAY}"
fi

if [ ! -z "${PORT}" ] ; then
  CMD="${CMD} -p ${PORT}"
fi

if [ ! -z "${SIZE}" ] ; then
  CMD="${CMD} -s ${SIZE}"
fi

echo "Going to run: ${CMD}"

exec ${CMD}
