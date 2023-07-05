#!/usr/bin/env bash
re='^[0-9]+$'
if [[ $# -eq 0 ]]; then
    echo "ERROR: Version is not specified" >&2
    kill -INT $$
elif ! [[ $1 =~ $re ]]; then
    echo "ERROR: Version is not a number" >&2
    kill -INT $$
elif [[ ${#1} -ne 2 && ${#1} -ne 3 ]]; then
    echo "ERROR: Version is not 2 or 3 digits" >&2
    kill -INT $$!
else
    major_version=${1:0:2}
fi

export DEFAULT_RENDERER=vray
if [ "$major_version" = '40' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray_adv_42090_katana3.0_linux_x64_30952
elif [ "$major_version" = '36' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray_adv_42090_katana3.0_linux_x64_30952
elif [ "$major_version" = '35' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray_adv_42090_katana3.0_linux_x64_30952
elif [ "$major_version" = '32' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray_adv_42090_katana3.0_linux_x64_30952
elif [ "$major_version" = '31' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray_adv_42090_katana3.0_linux_x64_30952
elif [ "$major_version" = '30' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray_adv_42090_katana3.0_linux_x64_30952
elif [ "$major_version" = '26' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray_adv_42090_katana2.5_linux_x64_30320
elif [ "$major_version" = '25' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray_adv_42090_katana2.5_linux_x64_30320
elif [ "$major_version" = '16' ]; then
    export VRAY_INSTALL_PATH=/opt/chaosgroup/vray-3.0_katana-1.5
else
    echo "vray not available for major version $major_version"
    kill -INT $$!
fi
export VRAY_FOR_KATANA_PLUGINS_x64=$VRAY_INSTALL_PATH/vrayplugins
export PATH=$PATH:$VRAY_INSTALL_PATH/RenderBin
export KATANA_RESOURCES=$KATANA_RESOURCES:$VRAY_INSTALL_PATH
