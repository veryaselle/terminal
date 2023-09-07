my_path = '/work/users/ao582fpoy/train/tracks.csv'
ident = "INSERT INTO `track` VALUES"

with open("/work/users/ao582fpoy/train/spotifydbdumpshare.sql", 'rb') as big_data:
    with open(my_path, 'w') as file:
        for line in big_data:
            string = line.decode('utf-8')
            if ident in string:
                line = string.replace("INSERT INTO `track` VALUES", " ")
                left = line.split("\'", 2)[1].replace("'", "") if "'" in line else "no track_id"  # Remove single quotes from left or set to "no track_id"
                right = line.rsplit("),(", 1)[-1].split(",", 1)[0].replace("'", "") if "'" in line else "no track_id"  # Remove single quotes from right or set to "no track_id"
                file.write(left + ", track_belongs_to_album, " + right + "\n")  # Add semicolon and newline
                print(left + ", track_belongs_album, " + right + "")

