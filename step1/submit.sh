#!/bin/bash
source /mnt/t3nfs01/data01/swshare/psit3/etc/profile.d/cms_ui_env.sh
source $VO_CMS_SW_DIR/cmsset_default.sh
cd $1
eval `scramv1 runtime -sh`
combine -M Asymptotic $3 -n $3
eval `mv higgsCombine${3}.Asymptotic.mH120.root $2`
