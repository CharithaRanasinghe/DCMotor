# DC Motor Simulation (State-Space Model)

This project demonstrates the mathematical modeling and simulation of a **DC motor** using the **state-space approach** in Python. It shows how armature current and angular velocity evolve over time under a constant applied voltage and load torque.

---

## 📘 Background

A DC motor can be modeled with two main equations:

1. **Electrical Equation (Armature circuit):**
   [
   L_a \frac{di_a}{dt} + R_a i_a + K_E \omega = V_a
   ]

2. **Mechanical Equation (Rotor dynamics):**
   [
   J \frac{d\omega}{dt} + D \omega = K_T i_a - T_L
   ]

Where:

* ( i_a ) = armature current (A)
* ( \omega ) = angular velocity (rad/s)
* ( V_a ) = armature voltage (V)
* ( T_L ) = load torque (Nm)
* ( L_a ) = armature inductance (H)
* ( R_a ) = armature resistance (Ω)
* ( K_E ) = back emf constant
* ( K_T ) = torque constant
* ( J ) = rotor inertia (kg·m²)
* ( D ) = viscous friction coefficient

These equations are converted into a **state-space representation** and simulated step by step.

---

## ⚙️ State-Space Representation

We define the state vector as:
[
X =
\begin{bmatrix}
i_a \
\omega \
\frac{di_a}{dt} \
\frac{d\omega}{dt}
\end{bmatrix}
]

The update equation is:
[
X_{k+1} = A X_k + B V_a + C T_L
]

Where matrices ( A, B, C ) are defined in the code.

---

## 🖥️ Simulation Setup

* **Armature inductance (La):** 0.04 H
* **Armature resistance (Ra):** 20 Ω
* **Motor constants (Ke, Kt):** 0.5
* **Rotor inertia (J):** 0.001 kg·m²
* **Damping (D):** 0.2
* **Input voltage (Va):** 12 V
* **Load torque (TL):** 0.05 Nm

Time is discretized with a step size of **dt = 0.0001 s** for **5000 steps**.

---

## 📊 Results

The simulation plots:

* Armature current ( i_a(t) )
* Angular velocity ( \omega(t) )

Both are shown as functions of time.

Example output:

![DC Motor Simulation Plot](example_plot.png)

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/CharithaRanasinghe/DcMotor.git
   cd DcMotor
   ```

2. Install dependencies:

   ```bash
   pip install numpy matplotlib
   ```

3. Run the simulation:

   ```bash
   python DcMotor.py
   ```

---

## 📌 Notes

* You can modify **V** (applied voltage) and **TL** (load torque) in the script to observe different motor behaviors.
* This model is simplified; advanced models can include nonlinearities, saturation, or controller design.

---

## 📖 References

* P. C. Sen, *Principles of Electric Machines and Power Electronics*
* Chapman, *Electric Machinery Fundamentals*
* Ogata, *Modern Control Engineering*

---

✍️ Developed as part of learning DC motor dynamics and control using Python.
