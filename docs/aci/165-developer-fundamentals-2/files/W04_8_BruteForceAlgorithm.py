from typing import List, Tuple

class TravelingSalesman: 
   
    def __init__(self, num_cities: int, graph: List[List[int]]) -> None: 
      
        self.num_cities = num_cities 
        self.graph = graph 

    def solve_tsp(self) -> Tuple[List[int], int]: 
       
        def generate_permutations(arr): 
            if not arr: 
                return [[]] 
 
            permutations = [] 
            for i in range(len(arr)): 
                remaining = arr[:i] + arr[i + 1:] 
                for p in generate_permutations(remaining): 
                    permutations.append([arr[i]] + p) 
 
            return permutations 
 
        # Generate all possible permutations of cities 
        city_permutations = generate_permutations(list(range(self.num_cities))) 

        # Initialize variables to store the optimal tour and total distance
        optimal_tour = None 
        min_distance = float('inf')

        # Iterate through all permutations and calculate the total distance 
        for permutation in city_permutations: 
            distance = 0 
            for i in range(self.num_cities - 1): 
                distance += self.graph[permutation[i]][permutation[i + 1]] 
            distance += self.graph[permutation[-1]][permutation[0]]  # Return to the starting city 

            # Update optimal tour if current permutation is shorter distance 
            if distance < min_distance: 
                min_distance = distance 
                optimal_tour = permutation 
 
        return optimal_tour, min_distance 
 
# Example of usage 
num_cities = 4 
distance_graph = [ 
        [0, 10, 15, 20], 
        [10, 0, 35, 25], 
        [15, 35, 0, 30], 
        [20, 25, 30, 0] 
] 
 
tsp = TravelingSalesman(num_cities, distance_graph)
# Solve and print the optimal tour and total distance 
optimal_tour, total_distance = tsp.solve_tsp() 
print("Optimal tour:", optimal_tour) 
print("Total distance:", total_distance) 