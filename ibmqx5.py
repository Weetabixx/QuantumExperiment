# -*- coding: utf-8 -*-

# Copyright 2017 IBM RESEARCH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

"""
GHZ state example illustrating mapping onto the backend.
"""

import sys
import os

# We don't know from where the user is running the example,
# so we need a relative position from this file path.
# TODO: Relative imports for intra-package imports are highly discouraged.
# http://stackoverflow.com/a/7506006
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from qiskit import QuantumProgram

import Qconfig

###############################################################
# Set the backend name and coupling map.
###############################################################
backend = "ibmqx5"
coupling_map = {1:[0, 2], 2:[3], 3:[4, 14], 5:[4], 6:[5, 7, 11], 7:[10], 8:[7], 9:[8, 10], 11:[10], 12:[5, 11, 13], 13:[4, 14], 15:[0, 2, 14]}

###############################################################
# Make a quantum program for the GHZ state.
###############################################################
QPS_SPECS = {
    "circuits": [{
        "name": "ghz",
        "quantum_registers": [{
            "name": "q",
            "size": 16
        }],
        "classical_registers": [
            {"name": "c",
             "size": 16}
        ]}]
}

qp = QuantumProgram(specs=QPS_SPECS)
qc = qp.get_circuit("ghz")
q = qp.get_quantum_register("q")
c = qp.get_classical_register("c")

# Create a GHZ state
qc.h(q[0])
for i in range(7):
    qc.cx(q[i], q[i+1])
# Insert a barrier before measurement
qc.barrier()
# Measure all of the qubits in the standard basis
for i in range(8):
    qc.measure(q[i], c[i])

###############################################################
# Set up the API and execute the program.
###############################################################
qp.set_api(Qconfig.APItoken, Qconfig.config["url"])

# Fourth version: map to qx2 coupling graph and run on qx2
print("map to %s, backend" % backend)
result = qp.execute(["ghz"], backend=backend,
                    coupling_map=coupling_map, shots=1024, timeout=120)
print(result)
print(result.get_counts("ghz"))
