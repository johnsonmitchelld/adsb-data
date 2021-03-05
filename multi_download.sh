cd ~/dev/adsb-data
(./download.sh) &
(sleep 15 && ./download.sh) &
(sleep 30 && ./download.sh) &
(sleep 45 && ./download.sh)