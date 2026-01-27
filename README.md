# Genetic Ice Cream Optimizer

A Python-based **Genetic Algorithm (GA)** developed to solve a complex **Constraint Optimization Problem**: finding the ideal ice cream combination based on multi-variable fitness criteria.

## 🧠 Project Overview
This project explores **Heuristic Search Methods** to navigate a vast search space of ingredients. Unlike a brute-force approach, this algorithm evolves a population of solutions to efficiently converge on an optimal configuration of flavors, bases, and toppings.

## 🛠️ Key Engineering Features
* **Structured Chromosome Encoding**: Implements a fixed-position genotype where specific indices represent distinct categories (Flavors, Bases, Sweeteners, Toppings), ensuring structural consistency.
* **Context-Aware Fitness Function**: Evaluates the quality of an individual based on the specific role an ingredient plays, handling semantic ambiguity across categories.
* **Constraint Optimization**: Manages data intersections and category overlaps to prevent invalid or redundant ingredient configurations.

## 🧬 Technical Architecture

### The Fitness Function
The quality of each individual $f$ is calculated as the sum of its attributes:

$$f(x) = \sum_{i=1}^{n} (S_i + T_i + N_i)$$

Where:
* **$S$ (Flavor)**: Taste profile optimization.
* **$T$ (Texture)**: Structural mouthfeel evaluation.
* **$N$ (Novelty)**: Uniqueness score for the combination.

### Evolutionary Workflow
1.  **Truncation Selection**: Only the top 50 individuals are selected for the mating pool to ensure high-pressure selection.
2.  **Heuristic Crossover**: Offspring inherit the best-performing traits from their parents, accelerating convergence.
3.  **Domain-Constrained Mutation**: A 20% mutation probability introduces random variability within valid category bounds to avoid local optima.

## 🚀 Getting Started

### Prerequisites
* Python 3.x

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/oscarjia/genetic-ice-cream-optimizer.git](https://github.com/oscarjia/genetic-ice-cream-optimizer.git)
    ```
2.  Run the optimizer:
    ```bash
    python run_genetic_algorithm.py
    ```

---

## 📝 Engineering Note
> Originally developed as a freshman implementation of evolutionary algorithms, this project has been **refactored and professionally optimized** to showcase advanced concepts in constraint handling and search heuristics.

## 🌐 Data & Localization Note
While the core logic, function names, and documentation are implemented in **English** for international engineering standards, the ingredient dataset (`datos.py`) remains in **Spanish**. 

The algorithm is designed to be **language-agnostic**; it processes the underlying fitness values and constraints regardless of the string representation of the data.

## 👤 Author
* **Óscar Jia** – Software Engineering Student
* [LinkedIn](https://www.linkedin.com/in/oscar-jia) | [GitHub](https://github.com/oscarjia)