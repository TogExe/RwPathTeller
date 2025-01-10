import heapq

# Dijkstra's algorithm
def dijkstra(graph, start, end,t):
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, distance, difficulty in graph[current_vertex]:
            total_distance = current_distance + distance * difficulty
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(queue, (total_distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.append(t[current])
        current = previous_nodes[current]

    path.reverse()

    if path[0] != t[start]:
        return "No path found"

    return path


# Interactive logic
def recursive_int_reply():
    while True:
        try:
            choice = int(input("Choose: \n1 - Add point \n2 - Get shortest route \n3 - Display map \n4 - Exit\n> "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")


# Main program
running = True

graph_map = {
    'SU': [('HI', 13.0, 1.0), ('DS', 17.0, 1.0), ('LF', 17.0, 1.0), ('OE', 6.0, 1.0)],
    'HI': [('SU', 6.0, 1.0), ('CC', 4.0, 1.0), ('GW', 7.0, 1.0), ('SH', 7.0, 1.0), ('VS', 7.0, 1.0)],
    'DS': [('SU', 6.0, 1.0), ('CC', 8.0, 1.0), ('GW', 9.0, 1.0), ('SB', 8.0, 1.0)],
    'CC': [('HI', 5.0, 1.0), ('DS', 9.0, 1.0), ('SI', 11.0, 1.0), ('UW', 12.0, 1.0)],
    'GW': [('HI', 12.0, 1.0), ('DS', 9.0, 1.0), ('SH', 15.0, 1.0), ('SL', 6.0, 1.0)],
    'SH': [('HI', 11.0, 1.0), ('GW', 10.0, 1.0), ('SL', 12.0, 1.0), ('UW', 15.0, 1.0)],
    'VS': [('HI', 7.0, 1.0), ('SL', 16.0, 1.0), ('SI', 8.0, 1.0), ('SB', 10.0, 1.0)],
    'SL': [('GW', 8.0, 1.0), ('SH', 7.0, 1.0), ('UW', 11.0, 1.0), ('SB', 12.0, 1.0), ('MS', 15.0, 1.0)],
    'SI': [('CC', 6.0, 1.0), ('VS', 8.0, 1.0), ('LF', 13.0, 1.0)],
    'LF': [('SU', 10.0, 1.0), ('DS', 11.0, 1.0), ('SI', 6.0, 1.0), ('SB', 11.0, 1.0)],
    'UW': [('SH', 9.0, 1.0), ('SL', 8.0, 1.0), ('SS', 5.0, 1.0)],
    'SS': [('UW', 4.0, 1.0)],
    'SB': [('VS', 7.0, 1.0), ('SL', 15.0, 1.0), ('OE', 14.0, 1.0)],
    'OE': [('SB', 20.0, 1.0)],
    'MS':[('SL',10,1.0)]
}
translations = {
    'SU':'Outskirts',
    'HI':'Industrial Complex',
    'DS':'Drainage System',
    'CC':'Chemney Canapoy',
    'GW':'Garbage Waste',
    'SH':'Shaded Citadel',
    'VS':'Pipeyard',
    'SL':'Shoreline',
    'SI':'Sky Islands',
    'LF':'Farm Arrays',
    'UW':'The Exterior',
    'SS':'Five Peeble',
    'SB':'Subterain',
    'OE':'Outer Expanse',
    'MS':'Submerged Structure'
}
translations2 = {}
for _ in translations:
    translations2[translations[_]]=_

for _ in graph_map:
    print(f"'"+_+f"':")

while running:
    action = recursive_int_reply()

    if action == 1:
        # Add a point and its connections
        name = input("Enter the name of the point: ")
        connections = []
        while True:
            neighbor = input("Enter connection name (or type 'stop' to finish): ")
            if neighbor.lower() == 'stop':
                break
            try:
                distance = float(input(f"Enter distance to {neighbor}: "))
                difficulty = float(input(f"Enter difficulty to {neighbor}: "))
                connections.append((neighbor, distance, difficulty))
            except ValueError:
                print("Invalid input for distance or difficulty. Try again.")

        if name in graph_map:
            graph_map[name].extend(connections)
        else:
            graph_map[name] = connections


    elif action == 2:
        # Get shortest route
        try:
            start = input("Enter the starting point: ")
            if start not in graph_map:
                if start in translations2:
                    start = translations2[start]
                else:
                    print(f"Start point '{start}' not found in the map.")
                    continue
            end = input("Enter the ending point: ")
            if end not in graph_map:
                if end in translations2:
                    end = translations2[end]
                else:
                    print(f"End point '{end}' not found in the map.")
                    continue
            shortest_path = dijkstra(graph_map, start, end, translations)
            print(f"Shortest path from {translations[start]} to {translations[end]} is: {shortest_path}")
        except Exception as e:
            print(f"Error calculating shortest path: {e}")


    elif action == 3:
        # Display the map
        print("Current map:")
        for point, connections in graph_map.items():
            print(f"{point}: {connections}")

    elif action == 4:
        # Exit the program
        print("Exiting...")
        running = False

    else:
        print("Invalid choice. Please choose a valid option.")