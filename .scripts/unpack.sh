#!/bin/bash

# Counter for renaming
count=1

# Find all image files in subdirectories and process them
find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -exec sh -c '
    for img; do
        # Get image resolution
        resolution=$(identify -format "%wx%h" "$img")
        width=$(echo $resolution | cut -dx -f1)
        height=$(echo $resolution | cut -dx -f2)

        # Check if resolution is greater than 1440p
        if [ $width -gt 2560 ] || ([ $width -eq 2560 ] && [ $height -gt 1440 ]); then
            # Rename and move the image to current directory
            # Ensuring the filename is unique by appending the counter
            mv "$img" "./picture-$((count++)).${img##*.}"
        fi
    done
' sh {} +
