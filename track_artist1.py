my_path = '/work/users/ao582fpoy/train/track_artist1.csv'
ident = "INSERT INTO `track_artist1` VALUES ("

with open("/work/users/ao582fpoy/train/spotifydbdumpshare.sql", 'rb') as big_data:
    file = open(my_path, 'w')
    for line in big_data:
        string = line.decode('utf-8')
        if ident in string:
            line = string.replace(ident, "")  # Remove the "INSERT INTO `track_artist1` VALUES (" string
            line = line.replace(");", "")  # Remove the trailing ");"
            for pair in line.split("),("):
                left, right = pair.split(",")
                left = left.strip("'(")  # Remove leading single quote and opening parenthesis
                right = right.strip(")'")  # Remove trailing single quote and closing parenthesis
                file.write(left + ", track_belongs_to_artist, " + right + ";\n")  # Add semicolon and newline
                print(left + ", track_belongs_to_artist, " + right + ";")
    file.close()


