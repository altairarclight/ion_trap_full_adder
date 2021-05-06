from qiskit import *
from numpy import pi

def runAdderWithInputs(input_a, input_b, carry_in):
    qreg_q = QuantumRegister(4, 'q')
    creg_c = ClassicalRegister(4, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    # initialize adder values
    circuit.initialize(input_a, 0)
    circuit.initialize(input_b, 1)
    circuit.initialize(carry_in, 2)
    circuit.initialize([1, 0], 3)

    circuit.rz(-3*pi/4, qreg_q[0])
    circuit.rz(-pi/4, qreg_q[1])
    circuit.rz(pi/4, qreg_q[2])
    circuit.ry(pi/2, qreg_q[0])
    circuit.ry(pi/2, qreg_q[1])
    circuit.ry(pi/2, qreg_q[2])
    circuit.rx(-pi/2, qreg_q[3])
    circuit.rxx(pi/4, qreg_q[1], qreg_q[3])
    circuit.ry(-pi/2, qreg_q[1])
    circuit.barrier(qreg_q[2])
    circuit.barrier(qreg_q[3])
    circuit.rxx(pi/2, qreg_q[0], qreg_q[1])
    circuit.rxx(pi/4, qreg_q[2], qreg_q[3])
    circuit.rz(-pi/2, qreg_q[1])
    circuit.rz(-pi/2, qreg_q[2])
    circuit.rxx(pi/4, qreg_q[0], qreg_q[3])
    circuit.barrier(qreg_q[0])
    circuit.rxx(pi/2, qreg_q[1], qreg_q[2])
    circuit.ry(-pi/2, qreg_q[0])
    circuit.ry(pi/2, qreg_q[1])
    circuit.ry(pi/2, qreg_q[2])
    circuit.barrier(qreg_q[1])
    circuit.rxx(-pi/4, qreg_q[2], qreg_q[3])
    circuit.rz(pi, qreg_q[1])
    circuit.ry(-pi/2, qreg_q[2])
    circuit.rz(pi/4, qreg_q[2])
    circuit.barrier(range(4))
    circuit.measure(range(4), range(4))

    # Use Aer's qasm_simulator
    backend_sim = Aer.get_backend('qasm_simulator')

    job_sim = execute(circuit, backend_sim, shots=1)

    # Grab the results from the job.
    result_sim = job_sim.result()

    counts = result_sim.get_counts(circuit)
    print(circuit)
    print(counts)

ket = [[1, 0], [0, 1]]

runAdderWithInputs(ket[0], ket[0], ket[0])
print('expected 00')
runAdderWithInputs(ket[0], ket[0], ket[1])
print('expected 01')
runAdderWithInputs(ket[0], ket[1], ket[0])
print('expected 01')
runAdderWithInputs(ket[0], ket[1], ket[1])
print('expected 10')
runAdderWithInputs(ket[1], ket[0], ket[0])
print('expected 01')
runAdderWithInputs(ket[1], ket[0], ket[1])
print('expected 10')
runAdderWithInputs(ket[1], ket[1], ket[0])
print('expected 10')
runAdderWithInputs(ket[1], ket[1], ket[1])
print('expected 11')
