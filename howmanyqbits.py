import sys
import os
import math

# We don't know from where the user is running the example,
# so we need a relative position from this file path.
# TODO: Relative imports for intra-package imports are highly discouraged.
# http://stackoverflow.com/a/7506006
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from qiskit import QuantumProgram
import time
import Qconfig
n = 20
###############################################################
# Set the backend name and coupling map.
###############################################################
QPS_SPECS = {
    "circuits": [{
        "name": "ghz",
        "quantum_registers": [{
            "name": "q",
            "size": n
        }],
        "classical_registers": [
            {"name": "c",
             "size": n}
        ]}]
}
qp = QuantumProgram(specs=QPS_SPECS)
qc = qp.get_circuit("ghz")
q = qp.get_quantum_register("q")
c = qp.get_classical_register("c")

# Create a GHZ state
qc.h(q[0])
for i in range(n-1):
    qc.cx(q[i], q[i+1])
# Insert a barrier before measurement
qc.barrier()
# Measure all of the qubits in the standard basis
for i in range(n):
    qc.measure(q[i], c[i])

qp.set_api(Qconfig.APItoken, Qconfig.config["url"])

print("no mapping, simulator")
start = time.time()
result = qp.execute(["ghz"], backend='local_qasm_simulator',
                    coupling_map=None, shots=1024)
taken = time.time() - start

print(result)
print(result.get_counts("ghz"))
print("took " + str(taken) + " time")
