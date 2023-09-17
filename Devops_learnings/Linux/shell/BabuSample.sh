#!/bin/bash

ssh -o StrictHostKeyChecking=no ubuntu@3.108.62.151 <<EOF
directory="kick-webdriver-sel"

if test -d \$directory; then
    echo "Latest scripts are pulled from git"
    cd \$directory/
    git pull
    cd ..
else
    echo "Fresh scripts are cloned from git"
    git clone https://github.com/manickamraj/kick-webdriver-sel.git
fi

cd \$directory/
chmod +x check-app-install-scripts.sh
./check-app-install-scripts.sh
EOF