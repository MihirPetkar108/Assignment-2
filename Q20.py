def population_counter(population, numberOfPastYears):
    if numberOfPastYears == 0:
        return population
    
    previous_population = population_counter(population, numberOfPastYears-1)
    current_population = previous_population / 1.12
    print(f"{numberOfPastYears}: {int(current_population)}")
    return current_population
    
population = 500000
numberOfPastYears = 10

population_counter(population, numberOfPastYears)