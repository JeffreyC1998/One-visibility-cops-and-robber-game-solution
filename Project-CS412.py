import random
import collections

"""This part contains the object definition"""


class label:
    def __init__(self, s, v, Iwb, Jw, Ipb, J):
        self.s = s
        self.v = v
        self.Iwb = Iwb
        self.Jw = Jw
        self.Ipb = Ipb
        self.J = J

    def __str__(self):
        string = "({},{};{},{};{},{})"
        return string.format(self.s, self.v, self.Iwb, self.Jw, self.Ipb, self.J)

class node:
    def __init__(self, vertex, label):
        self.vertex = vertex
        self.label = label


"""object definition part ends"""

"""This part contains all function definition"""


# Using dfs to find and assign parent for each vertex
def findParent(v):
    child[v] = AjList[v][:]
    if v != root:
        child[v].remove(parents[v])
    for l in child[v]:
        parents[l] = v
        findParent(l)
    vertex_list.append(v)


# Define the function for deleting the vertex in the given tree
def deleteNeighbourVertex(tree, vertex):
    global subroot
    subroot = tree[:]
    subroot.remove(vertex)

# Define the function to travel all of a given vertex's descendants to construct a Tree
def finddepth(vertex, t_list):
    for l in child[vertex]:
         finddepth(l, t_list)
    t_list.append(vertex)


"""function definition part ends"""

vertex = []  # store the list of all vertices
AjList = []  # store the list of adjacent vertices of every vertices
child = []  # store the list of children of every vertices
vertex_list = []  # store the list of vertices so that every vertex is before its parent

"""
This part is for testing the given trees in the example 4. 
You will see the comment that indicate all codes of this part.
Make sure that you can only use either this part(given input) or next part(random input) at the same time.
Please comment all code of this part if you want to test random input.
"""


# ## Tree for example 4.1
# tree_four_one = {0: [1, 4, 8], 1: [0, 2], 2:[1, 3], 3:[2], 4:[0,5], 5:[4, 6], 6:[5, 7], 7:[6], 8:[0,9], 9:[8,10], 10:[9,11], 11:[10]}
# ## Tree for example 4.2
# tree_four_two = {0: [1, 4, 8], 1: [0, 2], 2:[1, 3], 3:[2, 12], 4:[0,5], 5:[4, 6], 6:[5, 7], 7:[6], 8:[0,9], 9:[8,10], 10:[9,11], 11:[10], 12:[3]}
# ## Tree for example 4.3 and 4.4
# tree_four_three = {0:[1,38], 1:[0,2], 2:[1,3], 3:[2,4], 4:[3,5], 5:[4,6,15,27,28,29], 6:[5,7,9,11], 7:[6,8], 8:[7], 9:[6,10], 10:[9], 11:[6,12,13], 12:[11], 13:[11,14], 14:[13], 15:[5,16,17,20],
#                    16:[15], 17:[15,18,19], 18:[17], 19:[17], 20:[15,21,23,26], 21:[20,22], 22:[21], 23:[20,24,25], 24:[23], 25:[23], 26:[20], 27:[5], 28:[5], 29:[5,30,31,37], 30:[29], 31:[29,32,33,36],
#                    32:[31], 33:[31,34,35], 34:[33], 35:[33], 36:[31], 37:[29], 38:[0, 39], 39:[38,40], 40:[39,41], 41:[40,42,52,63,66], 42:[41,43,44,49], 43:[42], 44:[42,45,46], 45:[44],
#                    46:[44,47,48], 47:[46], 48:[46], 49:[42,50,51], 50:[49], 51:[49], 52:[41,53,54,55,56], 53:[52], 54:[52], 55:[52], 56:[52,57,60], 57:[56,58,59], 58:[57], 59:[57], 60:[56,61,62],
#                    61:[60], 62:[60], 63:[41,64,65], 64:[63], 65:[63], 66:[41,67,68,69], 67:[66], 68:[66], 69:[66,70,71], 70:[69], 71:[69,72,73], 72:[71], 73:[71]}
# ## Tree for example 4.5
# tree_four_five = {0:[1,2,3,4,5], 1:[0], 2:[0], 3:[0], 4:[0], 5:[0]}
#
# root = 0 ## For testing example 4.4, assign the root 41; otherwise, 0
# tree = tree_four_one ## select the tree from example, copy the name of the tree and paste here
# numVertices = len(tree)
# parents = [None] * numVertices ## store the list of parent of every vertices, firstly initialize None
# nodes = [None] * numVertices ## store the list of label corresponding to its vertex, firstly initialize None
#
# for k in range(numVertices):
#     vertex.append(k)
#     AjList.append(tree.get(k))
#     child.append([])


"""Testing for given input part ends"""


"""
This part is for testing the random input.
You will see the comment that indicate all codes of this part.
Make sure that you can only use either this part(random input) or last part(given input) at the same time.
Please comment all code of this part if you want to test given input
"""


print("Please make sure your number is from 1 to 10, the program will multiply your input by 30")
inpu = int(input("Enter the vertices of a tree: "))

numVertices = inpu * 30
nodes = [None] * numVertices  # store the list of label corresponding to its vertex
numOfAj = []
lastLevel = 0
nodesBefore = 0
numOfChild = []  # store the list of the number of children of every vertices
parents = [None] * numVertices  # store the list of parent of every vertices, firstly initialize None

# randomly assign the adjacent list of each vertex
for i in range(numVertices):
    numOfAj.append(random.randint(1, 6))
    numOfChild.append(numOfAj[i] - 1)
    AjList.append([])
    child.append([])
    vertex.append(i)
    for l in range(i):
        if i in AjList[l]:
            AjList[i].append(l)
    if nodesBefore <= numVertices:
        for j in range(min(numVertices - nodesBefore - 1, numOfAj[i])):
            AjList[i].append(nodesBefore + j + 1)
        nodesBefore += numOfAj[i]
root = random.choice(vertex)  # randomly pick a vertex as the root of this tree
# root = 10  # pick a root instead of random
numOfChild[root] += 1


"""random input part ends"""


print("The root is: ", root)

findParent(root)
T_u = []

"""
This part is to initially assign label for each vertex.
It is divided in to two sub part:
Part A assigns the initial label for the vertices without any child. Please uncomment part A if you are testing example 4.1-4.4 and random input.
Part B assigns the initial label for Example 4.5. Please uncomment part A if you are testing example 4.5.
Make sure that you can only use either part A or next part B at the same time.
"""
# Part A, please comment all code of this part if you want to use part B
# For each vertex that has no child, set its label.
# let u be the first unlabeled vertex in the list currently.

for i in vertex_list:                                 # Part A starts from this line
    if child[i] == []:
        tempLabel = label(1, "perpendicular", 0, 0, 0, 0)
        nodes[i] = node(i, tempLabel)
    else:
        nodes[i] = node(i, "Not Define")

# Part A finish

# Part B,please comment all code of this part if you want to use part A
# Assign the initial labels for v1,v2,v3,v4,v5 in Example 4.5.

# nodes = [node(0, "Not Define"),                      # Part B starts from this line
#         node(1, label(4,"perpendicular",0,0,1,0)),
#         node(2, label(4,"perpendicular",0,0,1,0)),
#         node(3, label([5,2],["x1","perpendicular"],0,0,0,2)),
#         node(4, label([8,4],["x2","v4"],0,0,0,0)),
#         node(5, label([6,2],["x3","v5"],0,0,0,0))]

# Part B finish


# This for loop is for printing the adjacent list and all the initial label int the tree before computing
# for i in range(len(vertex_list)):
#     print(i, ":", AjList[i])
#     print(i, ':', nodes[i].label)

print("The list that every vertex is before its parent is: ", vertex_list)
print("The total number of vertices is:", numVertices)

# define compute label function
def computeLabel(T_u, k):
    num_k_wb = sum(nodes[l].label.Iwb for l in subroot if nodes[l].label.s == k)
    num_k_pb = sum(nodes[l].label.Ipb for l in subroot if nodes[l].label.s == k)
    num_k_c = sum(nodes[l].label.s == k for l in subroot)
    h_k_w = max(nodes[l].label.Jw for l in subroot if nodes[l].label.s == k)
    h_k = max(nodes[l].label.J for l in subroot if nodes[l].label.s == k)

    if num_k_wb > 1:
        return label(k + 1, "perpendicular", 0, 0, 0, 0)
    elif num_k_wb == 1 and num_k_pb >= 1:
        return label(k + 1, "perpendicular", 0, 0, 0, 0)
    elif num_k_wb == 1 and num_k_pb == 0 and num_k_c >= 2:
        if h_k_w == 2:
            return label(k + 1, "perpendicular", 0, 0, 0, 0)
        elif h_k_w == 1 and h_k >= 1:
            return label(k + 1, "perpendicular", 0, 0, 0, 0)
        elif h_k_w == 1 and h_k >= 0:
            return label(k, "perpendicular", 1, 2, 0, 0)
        elif h_k_w == 0 and h_k == 2:
            return label(k + 1, "perpendicular", 0, 0, 0, 0)
        elif h_k_w == 0 and h_k <= 1:
            return label(k, "perpendicular", 1, 1, 0, 0)
    elif num_k_wb == 1 and num_k_c == 1:
        if h_k_w == 2:
            return label(k, u, 0, 0, 0, 0)
        elif h_k_w == 1:
            return label(k, "perpendicular", 1, 2, 0, 0)
        elif h_k_w == 0:
            return label(k, "perpendicular", 1, 1, 0, 0)
    elif num_k_wb == 0:
        if num_k_pb >= 3:
            return label(k + 1, "perpendicular", 0, 0, 0, 0)
        elif num_k_pb == 2:
            return label(k, "perpendicular", 1, 0, 0, 0)
        elif num_k_pb == 1:
            return label(k, "perpendicular", 0, 0, 1, 0)
        elif num_k_pb == 0:
            if h_k == 2:
                return label(k, "perpendicular", 0, 0, 1, 0)
            elif h_k == 1:
                return label(k, "perpendicular", 0, 0, 0, 2)
            elif h_k == 0:
                return label(k, "perpendicular", 0, 0, 0, 1)


# If the root does not have obtained a label
# Implement step 3 to step 11 to compute the label by while loop
while nodes[root].label == "Not Define":
    # To find the first unlabel vertex as u and construct Tu that makes from u's descendants
    for i in vertex_list:
        if nodes[i].label == "Not Define":
           u = i
           T_u = []
           finddepth(u, T_u)
           break
    Iper = []  # Declare the list to store the values in I perpendicular
    Tper = []  # Declare the list to store the values that can not be in T1 when perpendicular
    Ib = []  # Declare the list to store the values in I branching
    L = [[], []]  # Declare a 2d array that the first element stores the list of keys and the second element stores the list of attributes
    tempVertex = []
    tempKeyValue = []  # Declare the temp list to store each key list
    tempAttributesValue = []  # Declare the temp list to store each attribute list

    # Step 5: construct T one
    for j in child[u]:
        if type(nodes[j].label.v) is list:
            if "perpendicular" in nodes[j].label.v:           # If Vj in I perpendicular
                tempVertex.append(j)
                tempKeyValue.append(nodes[j].label.s)         # Append the key to the temp list for backup later
                tempAttributesValue.append(nodes[j].label.v)  # Append the key to the temp list for backup later
                nodes[j].label.s = nodes[j].label.s[-1]       # Let key of label of vertex j become the last key whose attribute is perpendicular
                nodes[j].label.v = nodes[j].label.v[-1]       # Let attribute of label of vertex j become the last attribute that is perpendicular
                Iper.append(j)
                if child[j]:
                    finddepth(j, Tper)                        # Call the function to find all vertices that can not be in T1 when perpendicular
                    Tper.remove(j)
            if "perpendicular" not in nodes[j].label.v:       # If Vj in I branching
                finddepth(j, Ib)                              # Call the function to find all vertices that can not be in T1 when branching
        else:
            if nodes[j].label.v == "perpendicular":           # If Vj in I perpendicular
                Iper.append(j)
                if child[j]:
                    finddepth(j, Tper)                        # Call the function to find all vertices that can not be in T1 when perpendicular
                    Tper.remove(j)
            else:                                             # If Vj in I branching
                finddepth(j, Ib)                              # Call the function to find all vertices that can not be in T1 when branching

    Tb = Ib[:]  # Declare the list to store the values that can not be in T1 when branching

    T_one = [value for value in T_u if value not in Tper and value not in Tb]
    deleteNeighbourVertex(T_one, u)

    # Step 6: call compute label
    if u in T_one and len(T_one) == 1:  # If u is not the only vertex in T_one
        Label_T_one = label(1,"perpendicular", 0,0,0,0)
    else:
        k = max(nodes[l].label.s for l in subroot)
        Label_T_one = computeLabel(T_one, k)
    # print("T1 label:", Label_T_one)

    for l in tempVertex:  # Recover all the keys and attributes
        l_index = tempVertex.index(l)
        nodes[l].label.s = tempKeyValue[l_index]
        nodes[l].label.v = tempAttributesValue[l_index]

    if type(Label_T_one.s) is list:
        k = Label_T_one.s[0]
    else:
        k = Label_T_one.s

    # Step 7:
    for j in child[u]:
        if j in Iper:                                          # If Vj in I perpendicular
            # If the item and the key in the label is not a list, there are 6 components only. So not appending is the same as deleting
            if type(nodes[j].label.s) is list:  # If it is a list
                for i in range(len(nodes[j].label.s) - 1):
                    if nodes[j].label.s[i] >= k:
                        L[0].append(nodes[j].label.s[i])      # Append the keys except the last key
                        L[1].append(nodes[j].label.v[i])      # Append the attributes except the last attribute

        elif j in Ib:                                         # If Vj in I branching
            if type(nodes[j].label.s) is list:                # If it is a list
                for i in range(len(nodes[j].label.s)):
                    if nodes[j].label.s[i] >= k:
                        L[0].append(nodes[j].label.s[i])      # Append all the keys
                        L[1].append(nodes[j].label.v[i])      # Append all the attributes
            else:  # If it is not a list
                L[0].append(nodes[j].label.s)                 # Append the only key
                L[1].append(nodes[j].label.v)                 # Append the only attribute
    L[0].append(Label_T_one.s)                                # Append the key of label T1
    L[1].append(Label_T_one.v)                                # Append the attribute of label T1

    # Step 8
    if len(L[0]) == len(set(L[0])):                        # If no key is repeated
        nodes[u].label = Label_T_one
        if L[0] and L[1]:
            if len(L[0]) > 1:
                L[0].append(nodes[u].label.s)              # Append the key of T1 at the end
                L[1].append(nodes[u].label.v)              # Append the attribute of T1 at the end

                nodes[u].label.s = L[0][:]                 # Set the key of Label u be the list of key in L
                nodes[u].label.v = L[1][:]                 # Set the attribute of Label u be the list of attribute in L
            nodes[u].label.s = L[0][-1]                    # Set the key of label u be the only key of L if there is only one key in the key list
            nodes[u].label.v = L[1][-1]                    # Set the attribute of label u be the only attribute of L if there is only one attribute in the attribute list
    # Step 9 to 11
    else:  # If a key is repeated
        # Step 9
        k_sharp = max([item for item, count in collections.Counter(L[0]).items() if count > 1])  # Find the largest repeated key in the list
        K_temp = sorted(set(L[0]), reverse=True)                                                 # Sort the list in decreasing order
        # Step 10, create a list containing the distinct keys
        K = []
        L[1] = list(map(str, L[1]))                                                              # Covert all the types of attributes to string type
        Q = [x for _, x in sorted(zip(L[0], L[1]), reverse=True)]                                # Sort the list of attributes based on the list of keys and assign to Q
        K = K_temp                                                                               # Assign the sorted list of keys in K

        # Step 11, find the smallest index of h
        h = 1                                   # Intialize the index h as 1
        if len(K) == 1:                         # If there is only one key
            k_prime = K[0] + 1                  # K' become the only key + 1
        else:                                   # If there are more than one keys
            k_prime = K[-1]                     # Assume K' is the last index which is also the smallest in the list
            for i in range(len(K) - 1, 0, -1):  # Find the index h from travelling from the last element
                if K[i] != K[i-1] - 1:
                    k_prime = K[i] + 1
                    h = i + 1
                    break                       # break the loop if it satisfies the condition
        X = [[], []]                            # Declare a 2d array that the first element stores the list of keys and the second element stores the list of attributes
        for i in range(h-1):
            X[0].append(K[i])                   # Append each key in K to the first element of X
            attribute_index_L = K.index(K[i])   # Get the index of each key in K
            X[1].append(Q[attribute_index_L])   # Append each attribute in Q to the first element of X
        X[0].append(k_prime)                    # Append key in K' at the end of the first element of X
        X[1].append("perpendicular")            # Append perpendicular at the end of the second element of X
        X_label = label(X[0], X[1], 0, 0, 0, 0)
        nodes[u].label = X_label

print("\nThe label of root is:", nodes[root].label)
