# One-visibility-cops-and-robber-game-solution

Description:
This program is written in Python language. It is based on project-CS412-8 Section 3:
Algorithms including the algorithm1 and function compute-label. Instruction:
User can have two option for input data:
1. Use the built-in data of trees of Example 4.1 to 4.5. (line 70 to 92)
2. Enter the scale from 1 to 10. Then the program will construct the tree randomly. (line 109 to 133)
Since two options can not exist at the same time, the program set the code about the first
option as comment lines and use the second option by default. Make sure that set one part
of code comment lines if you set the other part of code active. For the first option, the data of Example 4.1 to 4.5 have stored. The data names are:
Example 4.1: tree_four_one, Example 4.2: tree_four_two, Example 4.3 and 4.4: tree_four_three, (since they have exact the same adjacent list and
vertices. Please set the root 0 for 4.3 and set the root 41 for 4.4)
Example 4.5: tree_four_five. If user wants to test 4.3, set the root 0; if user tests 4.4, set the root 41. Because the tree of Example 4.5 has different initial labels. If user tests example 4.5, set
line 155 to 160 as comment lines and set line 167 to 172 active. Display:
The output of the program are:
1. The root of the tree, 2. The list that every vertices are before their parents, 3. The total number of vertices, 4. The label of the root which implies the copnumber. In addition to the defaulted output, the program also has following output but set
comment lines they will make the output messy if there are too much vertices:
1. line 178 to 180, output the adjacent list and initial label for each vertex, 2. line 284, output the current T1 label after calling the compute label function, These output were used in some of the screen shot of examples.Notice:
In Example 4.1 to 4.5, each vertex is assigned a unique number to distinguish in each
tree
