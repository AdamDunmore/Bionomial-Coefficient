import sys

#Declares Node Class
class Node:
    def __init__(self, index):
        self.node_connections = [index]
        self.index = index

    #Requests a connection to every node
    def connect(self, program, nodes):
        for x in range(len(nodes)):
            nodes[x].request_to_connect(program, self.index)
            self.node_connections.append(x)

    #Handles another nodes request to connect
    def request_to_connect(self, program, nodes_index):
        if not nodes_index in self.node_connections:
            self.node_connections.append(nodes_index)
            program.connections += 1
        

#Defines Program Class
class Program:
    def check(self, num_nodes):
        #Setups up list of nodes
        for x in range(num_nodes):
            self.nodes.append(Node(x))

        #Gets each node to check for connections
        for x in range(len(self.nodes)):
            self.nodes[x].connect(self, self.nodes)

        #Displays number of total connections
        print(f"The total number of connections with {num_nodes} nodes is {self.connections}")

    def __init__(self):
        #Initialises Global Variables
        self.nodes = []
        self.connections = 0

        #Runs program
        if len(sys.argv) > 1:
            number = int(sys.argv[1])
            try:
                number = int(sys.argv[1])
            except:
                print("Value entered was not an integer")

            finally:
                self.check(number)

        else:
            print("You need to pass the number of nodes for the program to run.")

p = Program()
