# ONOS Container-Based Environment

> Note: These instructions are adapted from the ONOS P4 tutorial, [here](https://github.com/opennetworkinglab/onos-p4-tutorial).

First, install the prerequisites listed in APPENDIX-Z, and clone the `taurus-onos` 
repository.

```
cd ~
git clone https://github.com/msbaz2013/onos.git
cd onos
```

## Build and Run Projects

Select one of the projects listed under `projects` folder. For example, ...
```
cd ~/onos
export PROJECT_DIR=$PWD/projects/bridge
```

### 1. Compile the P4 program and ONOS app

```
cd $PROJECT_DIR
make p4-build
make app-build
```

### 2. Start the ONOS controller 

In a separate shell, run ...
```
cd $PROJECT_DIR
make onos
```

### 3. Load the ONOS application 
```
cd $PROJECT_DIR
make app-reload
```

### 4. Start Mininet
In a separate shell, run ...
```
cd $PROJECT_DIR
make topo
```

### 5. Push netcfg to ONOS
```
cd $PROJECT_DIR
make netcfg
```

### 6. Check flow rules
Log into ONOS CLI, using ...
```
make onos-cli
```

and type ...
```
onos> flows -s any devices:s1
```

### 7. Ping hosts
In mininet, run ...
```
mininet> h1 ping h2
```

# APPENDX-Z: Prerequisites

### Install Docker
```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
sudo usermod -aG docker $(whoami)
sudo systemctl restart docker
```