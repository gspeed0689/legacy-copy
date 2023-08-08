#mkdir dev-cdrom
mkdir dev-sr0

python3 ~/cdxu.py -sr 0

#ddrescue -n -r 5 -b2048 /dev/cdrom dev-cdrom/cdimage dev-cdrom/mapfile
#ddrescue -d -r 5 -b2048 /dev/cdrom dev-cdrom/cdimage dev-cdrom/mapfile

ddrescue -n -r 5 -b2048 /dev/sr0 dev-sr0/cdimage dev-sr0/mapfile
ddrescue -d -r 5 -b2048 /dev/sr0 dev-sr0/cdimage dev-sr0/mapfile
