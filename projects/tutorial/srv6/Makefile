OCI = 127.0.0.1
APP_OAR = app/target/srv6-tutorial-1.0-SNAPSHOT.oar

p4-build:
	$(info ************ BUILDING P4 PROGRAM ************)
	cd p4src && make build

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
	cd mininet && mn-stratum --mac --custom topo.py --topo tutorialtopo

netcfg:
	$(info ************ PUSHING NETCFG TO ONOS ************)
	onos-netcfg ${OCI} cfg/netcfg.json

app-build: p4-build
	$(info ************ BUILDING ONOS APP ************)
	cd app && maven.local clean package

$(APP_OAR):
	$(error Missing app binary, run 'make app-build' first)

app-reload: $(APP_OAR)
	$(info ************ RELOADING ONOS APP ************)
	onos-app ${OCI} reinstall! app/target/srv6-tutorial-1.0-SNAPSHOT.oar

clean:
	-cd p4src && make clean
	-sudo rm -rf app/target
