# coding: utf-8

# Load these rules in the P4RT-Shell using the %load magic command.

te = table_entry["ingress.table0_control.table0"](action = "ingress.table0_control.set_egress_port")
te.priority = 1
te.match["standard_metadata.ingress_port"] = ("1")
te.action['port'] = ("2")
te.insert()

te = table_entry["ingress.table0_control.table0"](action = "ingress.table0_control.set_egress_port")
te.priority = 1
te.match["standard_metadata.ingress_port"] = ("2")
te.action['port'] = ("1")
te.insert()

te = table_entry["ingress.table0_control.table0"]
te.read(lambda x: print(x))
