#!/bin/bash

## Java
sudo apt-get update
sudo apt-get install default-jdk

# Maven
tmpdir=`mktemp -d -p .`
cd ${tmpdir}
wget http://apache.mirrors.pair.com/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
tar -xvf apache-maven-3.6.3-bin.tar.gz
sudo mkdir -p /tools/Apache
sudo rm -rf /tools/Apache/apache-maven-3.6.3
sudo mv apache-maven-3.6.3 /tools/Apache
cd ..
sudo rm -rf $tmpdir
echo "Maven installed at /tools/Apache/apache-maven-3.6.3

**Append these lines at the end of your ~/.bashrc file**:
    export M2_HOME=/tools/Apache/apache-maven-3.6.3
    export PATH=\$PATH:\$M2_HOME/bin"
