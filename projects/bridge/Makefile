OCI = 127.0.0.1
APP_OAR = app/target/bridge-1.0-SNAPSHOT.oar

p4-build:
	$(info ************ BUILDING P4 PROGRAM ************)
	cd p4src && make build

p4rt-shell: p4-build
	$(info ************ STARTING P4 RUNTIME SHELL ************)
	p4runtime-sh --grpc-addr 127.0.0.1:50001 --device-id 1 --election-id 0,1 --config p4src/build/p4info.txt,p4src/build/bmv2.json

onos:
	$(info ************ STARTING ONOS ************)
	ONOS_APPS=gui,drivers.bmv2,lldpprovider,hostprovider \
	onos

onos-debug:
	$(info ************ STARTING ONOS ************)
	ONOS_APPS=gui,drivers.bmv2,lldpprovider,hostprovider \
	onos debug

onos-cli:
	$(info ************ STARTING ONOS CLI ************)
	onos-cli

topo:
	$(info ************ STARTING MININET TOPOLOGY ************)
	cd mininet && mn-stratum --mac --custom topo.py --topo singleswitch

netcfg:
	$(info ************ PUSHING NETCFG TO ONOS ************)
	onos-netcfg ${OCI} cfg/netcfg.json

app-build: p4-build
	$(info ************ BUILDING ONOS APP ************)
	cd app && maven clean package

$(APP_OAR):
	$(error Missing app binary, run 'make app-build' first)

app-reload: $(APP_OAR)
	$(info ************ RELOADING ONOS APP ************)
	onos-app ${OCI} reinstall! ${APP_OAR}

clean:
	-cd p4src && make clean
	-sudo rm -rf app/target
