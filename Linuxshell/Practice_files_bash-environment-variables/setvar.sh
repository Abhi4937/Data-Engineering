#!/bin/bash
# Store the value of the HOME environment variable in a variable
user_home=$HOME

# Use the HOME environment variable to change the working directory
cd $HOME

# Utilise an environment variable in a command
echo "Hello, $USER! The current time is: $(date)"
