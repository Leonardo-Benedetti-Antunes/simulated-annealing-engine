# 🧠 Simulated Annealing Engine

A generic optimization engine based on **Simulated Annealing**, designed to solve problems using **constraints** and **iterative improvement of solutions**.

This project focuses on building a **modular and extensible core**, allowing different domains (e.g., scheduling, allocation, planning) to plug into the same optimization mechanism.

---

# 🚀 Overview

The engine works by:

* Representing a solution as a set of **nodes**
* Evaluating it using **constraints**
* Generating new candidate solutions using **moves**
* Iteratively improving the solution using **Simulated Annealing**

---

# 🏗️ Current Architecture

The current implementation is focused on the **core optimization engine**, composed of:

```
Solution → ConstraintLayer → Constraint → Evaluator → NeighborGenerator → SimulatedAnnealing
```

---

# 📂 Project Structure

```
domain/
├── models/
│   ├── solution.py
│   └── node.py
├── constraints/
│   ├── constraint.py
│   └── constraint_layer.py
└── moves/
    ├── move.py
    ├── swap_move.py
    ├── move_item_move.py
    └── change_attribute_move.py

engine/
├── evaluation/
│   └── evaluator.py
├── neighbor/
│   └── neighbor_generator.py
└── annealing/
    └── simulated_annealing.py

tests/
└── test_annealing.py
```

---

# 🧩 Core Concepts

## 🔹 Solution

Represents the current state of the problem.

It acts as a container for domain data (e.g., `turmas`, `professores`).

---

## 🔹 Node

A flexible structure representing an entity in the solution.

Example:

```
Node(items=[...], start=10, end=12)
```

---

## 🔹 Constraint

Defines a rule used to evaluate the solution.

```
class Constraint:
    def evaluate(self, solution, nodes):
        pass
```

Each constraint returns a **penalty value**.

---

## 🔹 ConstraintLayer

Groups constraints and defines **which nodes** they apply to.

```
ConstraintLayer(
    name="turmas",
    constraints=[...],
    node_selector=lambda s: s.turmas
)
```

---

## 🔹 Evaluator

Responsible for calculating the **total cost** of a solution by applying all constraints.

---

## 🔹 Move

Represents a small modification in the solution.

```
class Move:
    def apply(self, solution):
        pass
```

Examples:

* Swap elements between nodes
* Move items between nodes
* Modify attributes

---

## 🔹 NeighborGenerator

Generates new candidate solutions by applying random moves.

---

## 🔥 Simulated Annealing

The optimization algorithm that drives the system.

### How it works:

1. Start with an initial solution
2. Generate a neighbor
3. Evaluate both solutions
4. Accept better solutions
5. Sometimes accept worse ones (probabilistic)
6. Gradually reduce temperature

Acceptance probability:

```
P = e^(-Δ / T)
```

---

# 🧪 Testing

The project includes a basic test that verifies:

* The engine runs correctly
* Constraints are applied
* The algorithm improves (or maintains) the solution cost

---

# 🎯 Current Status

✅ Core engine implemented
✅ Constraint system
✅ Neighbor generation
✅ Simulated Annealing algorithm
✅ Basic test coverage

🚧 Not yet implemented:

* API layer
* Input configuration (JSON)
* Domain-specific models
* Advanced heuristics

---

# 🚀 Future Goals

* Add support for configuration-based problems (JSON)
* Improve move strategies (heuristic-based)
* Add multiple optimization algorithms
* Build an API interface