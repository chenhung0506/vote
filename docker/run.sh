#!/bin/bash
PUSH_IMG='false'
GIT_HEAD="$(git rev-parse --short=7 HEAD)"
GIT_DATE=$(git log HEAD -n1 --pretty='format:%cd' --date=format:'%Y%m%d-%H%M')
TAG="${GIT_HEAD}-${GIT_DATE}"
WORK_PATH=$(dirname "$0")
source ${WORK_PATH}/build.sh 

ENV=dev.env
# TAG=$(git rev-parse --short HEAD)-$(date '+%Y%m%d-%H%M') 
export REPO=harbor.emotibot.com/bfop
export CONTAINER=customized

select_number $1
echo "mode: "$?

if [[ "$1" =~ ^[0-9] ]]
    then
    echo "befor:" $@
    set -- "${@:2:$#}"
    echo "after:" $@
fi

setting_getopts $@

execute_option $mode

echo 'PUSH_IMG:' $PUSH_IMG
if [ $PUSH_IMG = 'true' ] ; then
    execute_option 5
fi