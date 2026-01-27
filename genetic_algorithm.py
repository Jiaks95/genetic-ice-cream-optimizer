import random
from data import *

def get_duplicates():
    duplicates = {}
    ingredients = [set(ice_cream_flavors), set(sweeteners), set(toppings_syrups), set(ice_cream_bases)]
    
    sweetener_flavor = ingredients[0].intersection(ingredients[1])
    if len(sweetener_flavor) > 0:
        duplicates[list(sweetener_flavor)[0]] = ['ice_cream_flavors', 'sweeteners']
    
    topping_flavor = ingredients[0].intersection(ingredients[2])
    if len(topping_flavor) > 0:
        duplicates[list(topping_flavor)[0]] = ['ice_cream_flavors', 'toppings_syrups']

    base_flavor = ingredients[0].intersection(ingredients[3])
    if len(base_flavor) > 0:
        duplicates[list(base_flavor)[0]] = ['ice_cream_flavors', 'ice_cream_bases']

    sweetener_topping = ingredients[1].intersection(ingredients[2])
    if len(sweetener_topping) > 0:
        duplicates[list(sweetener_topping)[0]] = ['sweeteners', 'toppings_syrups']

    sweetener_base = ingredients[1].intersection(ingredients[3])
    if len(sweetener_base) > 0:
        duplicates[list(sweetener_base)[0]] = ['sweeteners', 'ice_cream_bases']

    topping_base = ingredients[2].intersection(ingredients[3])
    if len(topping_base) > 0:
        duplicates[list(topping_base)[0]] = ['toppings_syrups', 'ice_cream_bases']

    return duplicates
    
# Function to calculate the fitness of an ingredient
def get_ingredient_fitness(ingredient, category=None):
    fitness = 0
    if category:
        fitness += ingredients_fitness[category][ingredient]['Flavor']
        fitness += ingredients_fitness[category][ingredient]['Texture']
        fitness += ingredients_fitness[category][ingredient]['Novelty']
    
    if ingredient in ice_cream_flavors:
        fitness += ingredients_fitness['ice_cream_flavors'][ingredient]['Flavor']
        fitness += ingredients_fitness['ice_cream_flavors'][ingredient]['Texture']
        fitness += ingredients_fitness['ice_cream_flavors'][ingredient]['Novelty']
    
    elif ingredient in sweeteners:
        fitness += ingredients_fitness['sweeteners'][ingredient]['Flavor']
        fitness += ingredients_fitness['sweeteners'][ingredient]['Texture']
        fitness += ingredients_fitness['sweeteners'][ingredient]['Novelty']
    
    elif ingredient in toppings_syrups:
        fitness += ingredients_fitness['toppings_syrups'][ingredient]['Flavor']
        fitness += ingredients_fitness['toppings_syrups'][ingredient]['Texture']
        fitness += ingredients_fitness['toppings_syrups'][ingredient]['Novelty']
    
    elif ingredient in ice_cream_bases:
        fitness += ingredients_fitness['ice_cream_bases'][ingredient]['Flavor']
        fitness += ingredients_fitness['ice_cream_bases'][ingredient]['Texture']
        fitness += ingredients_fitness['ice_cream_bases'][ingredient]['Novelty']
    # I return the fitness, which is the sum of the flavor, texture and novelty of the ingredient
    return fitness

# Function to calculate the fitness of an ice_cream
def calculate_fitness(ice_cream):
    # Value of flavor, texture and novelty
    total_fitness = 0
    # Loop through each ingredient of the ice_cream to get their values
    for ingredient in ice_cream:
        total_fitness += get_ingredient_fitness(ingredient)
    # I return the fitness, which is the sum of the flavor, texture and novelty of the ingredients of the ice_cream
    return total_fitness

# Function to make the selection by range of the population
def selection_by_range(population, selected_range):
    selected_population = sorted(population, key=lambda ice_cream: calculate_fitness(ice_cream), reverse=True)[:selected_range]
    return selected_population

# Function to mimic the mutation of an ice_cream
def mutation(ice_cream):
    # Probability of 20% for the ice_cream to mutate
    if random.randint(1, 100) < 20:
        # Get a random ingredient from the ice_cream
        ingredient_to_modify = ice_cream.index(random.choice(ice_cream))
        if ice_cream[ingredient_to_modify] in duplicates.keys():
            if ingredient_to_modify in range(0, 5):
                ingredient_type = 'ice_cream_flavors'
            elif ingredient_to_modify in range(5, 8):
                ingredient_type = 'ice_cream_bases'
            elif ingredient_to_modify == 8:
                ingredient_type = 'sweeteners'
            elif ingredient_to_modify in range(9, 12):
                ingredient_type = 'toppings_syrups'
        # Get the type of the selected ingredient
        else:
            for type in ingredients_fitness.keys():
                if ice_cream[ingredient_to_modify] in ingredients_fitness[type].keys():
                    ingredient_type = type
                    break
        # Get a new ingredient of the same type of the one getting substituted, they must be different and not already present in the ice_cream
        while True:
            new_ingredient = random.choice(list(ingredients_fitness[ingredient_type].keys()))
            if new_ingredient == ice_cream[ingredient_to_modify]:
                continue
            elif new_ingredient != ice_cream[ingredient_to_modify]:
                if new_ingredient not in ice_cream:
                    break
                elif new_ingredient in ice_cream:
                    if new_ingredient in duplicates:
                        break
                    else:
                        continue   
        # Substitute the ingredient
        ice_cream[ingredient_to_modify] = new_ingredient
    return ice_cream

# Function to mimic the crossover of two ice creams
def crossover(ice_cream_1, ice_cream_2):
    # Empty ingredient list that will be the offspring of the crossover
    offspring = []
    # Loop through the ingredientes of the parent ice creams
    for ingredient_1, ingredient_2, index in zip(ice_cream_1, ice_cream_2, range(0, len(ice_cream_1))):
        ingredient_1_fitness = 0
        ingredient_2_fitness = 0
        if ingredient_1 in duplicates.keys():
            if index in range(0, 5):
                ingredient_1_fitness = get_ingredient_fitness(ingredient_1, 'ice_cream_flavors')
            elif index in range(5, 8):
                ingredient_1_fitness = get_ingredient_fitness(ingredient_1, 'ice_cream_bases')
            elif index == 8:
                ingredient_1_fitness = get_ingredient_fitness(ingredient_1, 'sweeteners')
            elif index in range(9, 12):
                ingredient_1_fitness = get_ingredient_fitness(ingredient_1, 'toppings_syrups')
        
        else:
            ingredient_1_fitness = get_ingredient_fitness(ingredient_1)
        
        if ingredient_2 in duplicates.keys():
            if index in range(0, 5):
                ingredient_2_fitness = get_ingredient_fitness(ingredient_2, 'ice_cream_flavors')
            elif index in range(5, 8):
                ingredient_2_fitness = get_ingredient_fitness(ingredient_2, 'ice_cream_bases')
            elif index == 8:
                ingredient_2_fitness = get_ingredient_fitness(ingredient_2, 'sweeteners')
            elif index in range(9, 12):
                ingredient_2_fitness = get_ingredient_fitness(ingredient_2, 'toppings_syrups')
        else:
            ingredient_2_fitness = get_ingredient_fitness(ingredient_2)
        
        if ingredient_1 in offspring and ingredient_1 not in duplicates:
            offspring.append(ingredient_2)
            continue
        elif ingredient_2 in offspring and ingredient_2 not in duplicates:
            offspring.append(ingredient_1)
            continue
        # The offspring inherit the ingredient with the best fitness and that's not inherited yet
        if ingredient_1_fitness >= ingredient_2_fitness:
            offspring.append(ingredient_1)
        else:
            offspring.append(ingredient_2)
    # Return the offspring, with a possible mutation
    return mutation(offspring)

# Function to mimic the genetic algorithm
def run_genetic_algorithm(initial_population):
    # Sort the initial population
    population = sorted(initial_population, key=lambda ice_cream: calculate_fitness(ice_cream), reverse=True)
    # The algorithm keeps running until a condition is met
    while True:
        # Selection by range of the population
        selected_population = selection_by_range(population, 50)
        # Empty list for the descendants
        descendants = []
        # Crossover of two random ice creams of the selected population
        while len(selected_population) != 0:
            parents = random.sample(selected_population, 2)
            offspring = crossover(parents[0], parents[-1])
            descendants.append(offspring)
            selected_population.remove(parents[0])
            selected_population.remove(parents[-1])
        
        # I substitute the ice creams with the worst fitness with the descendants from the crossover
        population = population[:len(population) - len(descendants)] + descendants
        population = sorted(population, key=lambda ice_cream: calculate_fitness(ice_cream), reverse=True)
        best_ice_cream = max(population, key=lambda ice_cream: calculate_fitness(ice_cream))
        # If there's an ice cream with a fitness equal or greater than the specified one, the algorithm stops
        if calculate_fitness(best_ice_cream) >= 289:
            break
    # I return the ice cream with that fitness
    return best_ice_cream

duplicates = get_duplicates()
best_ice_cream = run_genetic_algorithm(initial_population)
print("Best ice cream: ")
print(best_ice_cream)
print("Score: ")
print(calculate_fitness(best_ice_cream))
