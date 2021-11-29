# Floydwarshall

Floydwarshall is a directory that contains a function that uses recursion for Floyd-Warshall algorithm. This algorithm is used to find the shortest paths in a graph that has edge direction and works for positive and/or negative weights, provided there are no negative cycles.

## Installation
Use the package manager pip to install the package.
```bash
pip install floydwarshall
```

Use the package manager pip to install the dependencies.
```bash
pip install -r requirements.txt
```

## Usage
To use the function you need to import it into your script.
```python
from floydwarshall.function import floydWarshall

# Example input

# Use value for infinity to denote edges that do not exist
INF = float('inf')

# Add weights into a list with graph[i][j] meaning "the direct weight from i to j" 
# assuming each vertex is numbered consecutively from 0
graph = [[0, INF, 10],
         [INF, 0, INF],
         [INF, 2, 0]]

# Returns output
floydWarshall(graph)

# Example output
output = [[0, 12, 10],
          [INF, 0, INF],
          [INF, 2, 0]]
```

## Runnning Unit Tests
To run the unit tests use the following in the terminal for the test_cases.py file, or substitute with your own test cases.
```
python -m unittest tests/test_cases.py
```

## Runnning Performance Tests
To run the performance tests use the following in the terminal for the test_cases.py file, or substitute with your own test cases.
```
python -m cProfile tests/test_cases.py
```

## Contributing
Pull requests permitted. When contributing please update the test directory as appropriate with any additional requirements. 