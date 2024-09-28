import heapq

# Definir un grafo para el sistema de transporte
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Heurística (estimación de la distancia directa entre dos puntos)
heuristics = {
    'A': 10,
    'B': 5,
    'C': 12,
    'D': 20,
}

def a_star_search(graph, start, goal):
    # La cola de prioridad para seguir los nodos abiertos
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Mantener un diccionario con los costos desde el punto de inicio
    g_costs = {start: 0}
    
    # Mantener un diccionario de los caminos más cortos
    came_from = {start: None}
    
    while open_list:
        # Obtener el nodo con el costo más bajo
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            # Si llegamos al objetivo, reconstruir la ruta
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Devolver la ruta en orden inverso
        
        for neighbor, cost in graph[current].items():
            new_cost = g_costs[current] + cost
            if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current
    
    return None  # No se encontró una ruta

# Probar el algoritmo A* con puntos A y D
start_point = 'D'
end_point = 'A'
route = a_star_search(graph, start_point, end_point)

if route:
    print(f"La mejor ruta desde {start_point} hasta {end_point} es: {' -> '.join(route)}")
else:
    print("No se encontró una ruta.")
