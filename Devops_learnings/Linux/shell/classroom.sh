#!/bin/bash

# Function to check if given command exist !!
is_Command_Exist(){
    local arg="$1"
    type "$arg" &> /dev/null
    return $?
}

# Install Function
install_package(){
    local arg="$1"
    sudo apt install "$arg"
}

# Check Java exist or not?
if is_Command_Exist "java"; then
    echo "Java is installed in this ubuntu"
else
    echo "Java is not installed"
    install_package "openjdk-8-jdk";
fi

# Check Maven exist or not?
if is_Command_Exist "mvn"; then
    echo "Maven is installed in this ubuntu"
else
    echo "mvn is not installed"
    install_package "mvn";
fi