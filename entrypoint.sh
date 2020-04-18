#!/bin/sh
set -e

CMD="python demoserver.py -b ${BASEPATH} -d ${DELAY} -p ${PORT} -s ${SIZE}"
echo "Going to run: ${CMD}"

exec ${CMD}
