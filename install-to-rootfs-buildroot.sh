#!/bin/sh
ROOTFS_PATH=$1
if [ -z "$ROOTFS_PATH" ]; then
    echo "Usage: $0 <path-to-rootfs>"
    exit 1
fi

rsync -av --exclude='.git' --exclude='__pycache__' --exclude='*.pyc' ./rootfs/buildroot/ "$ROOTFS_PATH/"
rsync -av --exclude='.git' --exclude='__pycache__' --exclude='*.pyc' --exclude='rootfs' ./ "$ROOTFS_PATH/root/PSFree-Luckfox"
echo "Repackaging firmware required with new rootfs. Run \`./build.sh firmware\` on luckfox-pico SDK directory"
