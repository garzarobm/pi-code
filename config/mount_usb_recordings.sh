#!/usr/bin/env bash
#
# add_usb_recordings.sh
#
# Mount a newly inserted USB drive at <target user>'s ~/recordings folder.
# Works for any user: pass the username as $1, or it defaults to whoever
# invoked the script (handles sudo correctly via SUDO_USER).
#
# Usage (run from your home folder, or anywhere):
#   sudo ./add_usb_recordings.sh            # mounts for the invoking user
#   sudo ./add_usb_recordings.sh pi         # mounts for user 'pi'
#   sudo ./add_usb_recordings.sh pi sda1    # skip auto-detect, use /dev/sda1
#
# What it does:
#   1. Figures out the target user and their home directory.
#   2. Finds the newest unmounted USB partition (or uses the one you named).
#   3. Creates ~/recordings if missing.
#   4. Mounts the partition there, owned by the target user.
#   5. Optionally appends an fstab entry (by UUID) so it survives reboot.

set -euo pipefail

die() { echo "ERROR: $*" >&2; exit 1; }

[[ $EUID -eq 0 ]] || die "run with sudo (mounting requires root)"

# --- 1. Resolve target user ---------------------------------------------------
TARGET_USER="${1:-${SUDO_USER:-$(logname 2>/dev/null || echo root)}}"
id "$TARGET_USER" &>/dev/null || die "user '$TARGET_USER' does not exist"
TARGET_HOME="$(getent passwd "$TARGET_USER" | cut -d: -f6)"
[[ -d $TARGET_HOME ]] || die "home directory '$TARGET_HOME' not found"
MOUNT_POINT="$TARGET_HOME/recordings"

# --- 2. Find the USB partition ------------------------------------------------
if [[ -n ${2:-} ]]; then
    DEV="/dev/${2#/dev/}"
    [[ -b $DEV ]] || die "'$DEV' is not a block device"
else
    # Newest unmounted partition on a USB-attached disk.
    DEV=""
    while IFS= read -r line; do
        eval "$line"   # sets NAME, TYPE, MOUNTPOINT, PKNAME (lsblk -P output)
        if [[ $TYPE == part && -z $MOUNTPOINT && -n $PKNAME ]]; then
            bus="$(lsblk -dno TRAN "/dev/$PKNAME" 2>/dev/null || true)"
            [[ $bus == usb ]] && DEV="/dev/$NAME"
        fi
    done < <(lsblk -Pno NAME,TYPE,MOUNTPOINT,PKNAME)
    [[ -n $DEV ]] || die "no unmounted USB partition found — is the drive plugged in?"
fi

FSTYPE="$(lsblk -no FSTYPE "$DEV")"
UUID="$(lsblk -no UUID "$DEV")"
[[ -n $FSTYPE ]] || die "$DEV has no filesystem — format it first (e.g. mkfs.ext4 $DEV)"

echo "Target user : $TARGET_USER"
echo "Mount point : $MOUNT_POINT"
echo "USB device  : $DEV ($FSTYPE, UUID=$UUID)"

# --- 3. Prepare mount point ---------------------------------------------------
mkdir -p "$MOUNT_POINT"
mountpoint -q "$MOUNT_POINT" && die "$MOUNT_POINT is already a mount point"

# --- 4. Mount -----------------------------------------------------------------
UID_NUM="$(id -u "$TARGET_USER")"
GID_NUM="$(id -g "$TARGET_USER")"

case "$FSTYPE" in
    vfat|exfat|ntfs)
        # These don't support unix ownership; set it at mount time.
        mount -o "uid=$UID_NUM,gid=$GID_NUM,umask=022" "$DEV" "$MOUNT_POINT"
        FSTAB_OPTS="defaults,nofail,uid=$UID_NUM,gid=$GID_NUM,umask=022"
        ;;
    *)
        mount "$DEV" "$MOUNT_POINT"
        chown "$TARGET_USER:$TARGET_USER" "$MOUNT_POINT"
        FSTAB_OPTS="defaults,nofail"
        ;;
esac

echo "Mounted $DEV at $MOUNT_POINT"

# --- 5. Optional: persist across reboots -------------------------------------
read -rp "Add to /etc/fstab so it mounts on boot? [y/N] " ans
if [[ ${ans,,} == y* ]]; then
    if grep -q "UUID=$UUID" /etc/fstab; then
        echo "fstab already has an entry for UUID=$UUID — skipping"
    else
        cp /etc/fstab "/etc/fstab.bak.$(date +%s)"
        echo "UUID=$UUID  $MOUNT_POINT  $FSTYPE  $FSTAB_OPTS  0  2" >> /etc/fstab
        systemctl daemon-reload 2>/dev/null || true
        echo "fstab entry added (backup saved)"
    fi
fi

echo "Done. Recordings folder ready at $MOUNT_POINT"

