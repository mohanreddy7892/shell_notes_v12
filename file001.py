#some code
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
touch "$failed_file"

# Iterate over each path in the input file
while IFS= read -r path; do
    # Check if the path exists and is accessible
    if [ -e "$path" ]; then
        # Get the current permissions of the path
        current_permissions=$(stat -c "%a" "$path")

        # Extract the first two digits of the current permissions
        prefix_permissions="${current_permissions%??}"

        # Set the new permissions by appending "4" to the prefix permissions
        new_permissions="${prefix_permissions}4"

        # Attempt to change the permissions of the path
        if chmod "$new_permissions" "$path"; then
            # Output the path and the updated permissions
            echo "Changed permissions of $path to $new_permissions"
        else
            # Append the failed path and its current permission to failtochangepermission.txt file
            echo "$path,$current_permissions" >> "$failed_file"
        fi
    else
        # Append the path to failtochangepermission.txt file with an indication of inaccessibility
        echo "$path,Inaccessible" >> "$failed_file"
    fi
done < "$input_file"


