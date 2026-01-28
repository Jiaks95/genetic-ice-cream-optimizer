# Genetic Ice Cream Optimizer

A Python-based **Genetic Algorithm (GA)** developed to solve a complex **Constraint Optimization Problem**: finding the ideal ice cream combination based on multi-variable fitness criteria.

## 🧠 Project Overview
This project explores **Heuristic Search Methods** to navigate a vast search space of ingredients. Unlike a brute-force approach, this algorithm evolves a population of solutions to efficiently converge on an optimal configuration of flavors, bases, and toppings.

## 🧬 Technical Architecture

### The Fitness Function
The quality of each individual $f$ is calculated as the sum of its attributes:

$$f(x) = \sum_{i=1}^{n} (S_i + T_i + N_i)$$

Where:
* **$S$ (Flavor)**: Taste profile optimization.
* **$T$ (Texture)**: Structural mouthfeel evaluation.
* **$N$ (Novelty)**: Uniqueness score for the combination.

### Evolutionary Workflow
1.  **Truncation Selection**: High-pressure selection focusing on the top 50 individuals.
2.  **Heuristic Crossover**: Offspring inherit the best-performing traits, accelerating convergence.
3.  **Domain-Constrained Mutation**: A 20% probability introduces variability while maintaining category integrity.

---

## 🔍 2026 Performance Audit & Retrospective
*This project serves as a historical baseline of my early work in Bio-inspired Computing. Analyzing it today reveals several optimization vectors that I would now implement differently:*

### 1. Time Complexity & Bottlenecks
* **Fitness Memoization**: Currently, the algorithm recalculates fitness during every `sort` operation. A more efficient approach would involve **caching/memoizing** fitness scores within each object to reduce redundant computations from $O(G \cdot N \log N)$ to a more manageable overhead.
* **List Manipulations**: The use of `.remove()` inside selection loops introduces $O(N^2)$ complexity. In a production environment, I would utilize **pointer swapping** or **heap-based selection** to achieve $O(1)$ or $O(\log N)$ performance.

### 2. Architectural Design
* **Decoupling**: The current implementation is tightly coupled to specific ingredient categories. I would now refactor this into an **abstract Genetic Framework** where the data schema and fitness rules are injected as plugins, making the engine truly domain-agnostic.
* **Type Safety**: Transitioning to Python’s `dataclasses` or `Type Hints` would significantly improve maintainability and prevent the semantic ambiguity found in early iterations.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Jiaks95/genetic-ice-cream-optimizer.git](https://github.com/Jiaks95/genetic-ice-cream-optimizer.git)
    ```
2.  Run the optimizer:
    ```bash
    python genetic_algorithm.py
    ```

## 🌐 Localization Note
The core logic and documentation are in **English**, while the dataset (`data.py`) remains in **Spanish**. The algorithm is **language-agnostic**; it processes fitness values and constraints regardless of the string representation.

## 👤 Author
* **Óscar Jia** – Software Engineering Student [cite: 2025-09-10]
* [LinkedIn](https://www.linkedin.com/in/oscar-jia) | [GitHub](https://github.com/Jiaks95)