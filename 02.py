import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Define entities and their relationships
entities = {
    "products": ["Apple", "Banana", "Orange", "Milk", "Cheese", "Bread"],
    "aisles": ["Produce Aisle", "Dairy Aisle", "Bakery Aisle"],
    "departments": ["Produce", "Dairy", "Bakery"],
    "customers": ["Customer1", "Customer2", "Customer3"],
    "employees": ["Employee1", "Employee2", "Employee3"],
    "transactions": ["Transaction1", "Transaction2", "Transaction3"]
}

# Define relationships between entities
relationships = [
    ("products", "aisles"),
    ("products", "departments"),
    ("products", "transactions"),
    ("aisles", "departments"),
    ("departments", "employees"),
    ("transactions", "customers"),
    ("transactions", "employees")
]

# Add nodes and edges to the graph based on relationships
for entity, items in entities.items():
    G.add_node(entity)
    for item in items:
        G.add_node(item)
        G.add_edge(entity, item)

for relationship in relationships:
    G.add_edge(relationship[0], relationship[1])

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10)
plt.title("Semantic Network")
plt.show()
