file_name=locations
current_time=$(date -u "+%Y_%m_%d_%H_%M_%S")
file_name=/media/data/shared/adsb/${file_name}_$current_time.json
echo $file_name
curl -s -o $file_name "https://opensky-network.org/api/states/all"
