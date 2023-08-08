#mkdir dev-cdrom
mkdir dev-sr1

python3 ~/cdxu.py -sr 1

#ddrescue -n -r 5 -b2048 /dev/cdrom dev-cdrom/cdimage dev-cdrom/mapfile
#ddrescue -d -r 5 -b2048 /dev/cdrom dev-cdrom/cdimage dev-cdrom/mapfile

ddrescue -n -r 5 -b2048 /dev/sr1 dev-sr1/cdimage dev-sr1/mapfile
ddrescue -d -r 5 -b2048 /dev/sr1 dev-sr1/cdimage dev-sr1/mapfile
