# 🧠 Simulated Annealing Engine

**Simulated Annealing Constraint Optimization Engine API**

This project is a generic optimization engine based on **Simulated Annealing**, designed to solve complex problems involving **constraints** and **interdependent variables**.

The goal is to provide a decoupled and extensible API capable of handling different scenarios, such as:

- 📅 Timetable generation (schools, universities)
- 🏭 Resource allocation
- 👨‍💼 Workforce scheduling
- 🚚 Logistics optimization
- 📊 Combinatorial planning problems

---

# 🚀 Overview

The system receives a problem definition containing:

- **Nodes** → entities (e.g., classes, rooms, teachers)
- **Layers** → logical groupings
- **Constraints**:
  - **Hard** → must not be violated
  - **Soft** → preferences to be minimized

And returns:

- ✅ An optimized solution (if possible)
- 📉 Solution score
- ⚠️ Constraint violations (if any)

---

# 🏗️ Architecture

The project follows:

- **Clean Architecture**
- **SOLID principles**
- **Separation of Concerns**
- **Lightweight Domain-Driven Design (DDD)**

```
API → Use Case → Engine → Domain → Result
```

---

# 📂 Project Structure

```
SIMULATED-ANNEALING-ENGINE/
├── app/
├── domain/
├── engine/
├── infra/
├── shared/
├── tests/
└── main.py
```

---

# ⚙️ How Simulated Annealing Works

The algorithm explores the solution space as follows:

1. Starts with an initial solution
2. Generates small variations (neighbors)
3. Always accepts better solutions
4. Sometimes accepts worse solutions (to escape local minima)
5. Gradually reduces the "temperature"

Acceptance probability:

P = e^(-ΔE / T)

---

# 🧩 Problem Modeling

## Solution

```
class Solution:
    assignments: dict
    cost: float
```

## Constraint

```
class Constraint:
    def evaluate(self, solution: Solution) -> float:
        pass
```

---

# 🌐 API

## Main Endpoint

POST /optimize

---

# 🎯 Project Goals

- Build a generic and reusable optimization engine
- Support multiple domains
- Allow easy constraint extension
- Enable algorithm swapping in the future

---

# 📜 License

MIT
