OCI = 127.0.0.1

onos:
	$(info ************ STARTING ONOS ************)
	ONOS_APPS=gui,drivers.bmv2,pipelines.fabric,segmentrouting,lldpprovider,hostprovider \
	onos

onos-cli:
	$(info ************ STARTING ONOS CLI ************)
	onos-cli

topo:
	$(info ************ STARTING MININET TOPOLOGY ************)
	cd mininet && mn-stratum --mac --custom topo.py --topo trellis

netcfg:
	$(info ************ PUSHING NETCFG TO ONOS ************)
	onos-netcfg ${OCI} cfg/netcfg.json
