# Genetic Ingredient Optimizer

A Python-based project that explores **Evolutionary Algorithms** to find the best ice cream combination based on flavor, texture, and novelty scores.

## Project Overview
Created as an academic assignment during my early studies in Software Engineering, this project implements a basic **Genetic Algorithm (GA)** from scratch. It simulates natural selection (crossover, mutation, and selection) to optimize a product configuration without using external optimization libraries.

## How it Works

### The Goal
Maximize a fitness score calculated by summing the attributes of selected ingredients:
$$F(x) = \sum (Flavor + Texture + Novelty)$$

### The Process
1.  **Population:** Starts with random combinations of ingredients.
2.  **Selection:** Keeps the top performing combinations.
3.  **Crossover:** Combines "parents" to create new mixtures, aiming to inherit the best traits.
4.  **Mutation:** Randomly changes ingredients (with 20% probability) to introduce variety.

---

## Retrospective (2026)
*Looking back at this project as a 3rd-year student, I recognize it represents my initial steps into algorithmic logic. While the implementation uses basic Python structures, it helped me understand the core concepts of heuristics and constraints before learning formal data structures.*

* **Current Analysis:** The algorithm relies heavily on list manipulations which could be optimized today using Hash Maps or Sets for faster lookups ($O(1)$).
* **Architecture:** The logic is tightly coupled to the data. A modern approach would separate the algorithm engine from the specific ingredient data.

---

## Usage

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Jiaks95/genetic-ice-cream-optimizer.git](https://github.com/Jiaks95/genetic-ice-cream-optimizer.git)
    ```
2.  Run the simulation:
    ```bash
    python genetic_algorithm.py
    ```

## Author
**Óscar Jia** – Software Engineering Student | Python Developer
[LinkedIn](https://www.linkedin.com/in/oscar-jia) | [GitHub](https://github.com/Jiaks95)