import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes for corporation, departments, roles, and employees
G.add_node("Corporation", level="corporation")
G.add_node("CEO", level="executive")
G.add_node("CTO", level="executive")
G.add_node("HR Department", level="department")
G.add_node("IT Department", level="department")
G.add_node("HR Manager", level="role")
G.add_node("IT Manager", level="role")
G.add_node("HR Employee", level="employee")
G.add_node("IT Employee", level="employee")

# Add edges to represent relationships
G.add_edge("Corporation", "CEO")
G.add_edge("Corporation", "CTO")
G.add_edge("Corporation", "HR Department")
G.add_edge("Corporation", "IT Department")
G.add_edge("HR Department", "HR Manager")
G.add_edge("IT Department", "IT Manager")
G.add_edge("HR Manager", "HR Employee")
G.add_edge("IT Manager", "IT Employee")

# Set node positions for better visualization
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=12, font_weight='bold')
plt.title("Corporation Hierarchy")
plt.show()
