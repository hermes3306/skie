#!/bin/bash
#wget https://download.oracle.com/java/17/archive/jdk-17.0.9_linux-x64_bin.tar.gz
#tar xvzf jdk-17.0.9_linux-x64_bin.tar.gz
#mv jdk-17.0.9 ~

JAVA_HOME="$HOME/jdk-17.0.9"
# Append JAVA_HOME to .bashrc
if grep -qF "JAVA_HOME" ~/.profile; then
    echo "JAVA_HOME is already set in .bashrc"
else
    # Append JAVA_HOME to .bashrc
    echo "export JAVA_HOME=\"$JAVA_HOME"\" >> ~/.profile
    echo "export PATH=\"\$JAVA_HOME/bin:\$PATH"\" >> ~/.profile
    echo "JAVA_HOME and PATH have been added to .profile"
fi

rm jdk-17.0.9_linux-x64_bin.tar.gz




