OCI = 127.0.0.1

p4rt-shell:
	$(info ************ STARTING P4 RUNTIME SHELL ************)
	p4runtime-sh --grpc-addr 127.0.0.1:50001 --device-id 1 --election-id 0,1 --config p4src/basic_p4info.txt,p4src/basic.json

onos:
	$(info ************ STARTING ONOS ************)
	ONOS_APPS=gui2,drivers.bmv2,pipelines.basic,lldpprovider,hostprovider,fwd \
	onos

onos-debug:
	$(info ************ STARTING ONOS ************)
	ONOS_APPS=gui2,drivers.bmv2,pipelines.basic,lldpprovider,hostprovider,fwd \
	onos debug

onos-cli:
	$(info ************ STARTING ONOS CLI ************)
	onos-cli

topo:
	$(info ************ STARTING MININET TOPOLOGY ************)
	mn-stratum

netcfg:
	$(info ************ PUSHING NETCFG TO ONOS ************)
	onos-netcfg ${OCI} cfg/netcfg.json

clean:
	-cd p4src && make clean
