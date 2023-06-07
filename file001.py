#!/bin/bash

# Check if the input file is provided as a command-line argument
if [ $# -eq 0 ]; then
    echo "Please provide the input file as a command-line argument."
    exit 1
fi

input_file="$1"  # Use the first positional parameter as the input file

# Verify if the input file exists and is readable
if [ ! -f "$input_file" ] || [ ! -r "$input_file" ]; then
    echo "Input file not found or not readable: $input_file"
    exit 1
fi

failed_file="failtochangepermission.txt"

# Create an empty failtochangepermission.txt file if it doesn't exist
> "$failed_file"

# Iterate over each path in the input file
while IFS= read -r path; do
    # Check if the path exists and is accessible
    if [ -e "$path" ]; then
        # Get the current permissions of the path
        current_permissions=$(stat -c "%a" "$path")

        # Extract the first digit of the current permissions
        last_digit=${current_permissions: -1}

        # Set the new permissions if the last digit is not already 4
        if [ "$last_digit" != "4" ]; then
            new_permissions="${current_permissions%?}4"

            # Attempt to change the permissions of the path
            chmod "$new_permissions" "$path"

            # Check the exit status of the chmod command
            if [ $? -eq 0 ]; then
                # Output the path and the updated permissions
                echo "Changed permissions of $path to $new_permissions"
            else
                # Append the failed path and its current permission to failtochangepermission.txt file
                echo "$path,$current_permissions" >> "$failed_file"
            fi
        fi
    else
        # Append the path to failtochangepermission.txt file with an indication of inaccessibility
        echo "$path,Inaccessible" >> "$failed_file"
    fi
done < "$input_file"