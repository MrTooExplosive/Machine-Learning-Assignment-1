#-------------------------------------------------------------------------
# AUTHOR: Makarius Salib
# FILENAME: Decision Tree
# SPECIFICATION: Creates a decision tree from the training data contact_lens.csv
# FOR: CS 4210- Assignment #1
# TIME SPENT: 15 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =
for i in range(len(db)):
  instance = []

  if db[i][0] == "Young":
    instance.append(1)
  elif db[i][0] == "Prepresbyopic":
    instance.append(2)
  elif db[i][0] == "Presbyopic":
    instance.append(3)
  
  if db[i][1] == "Myope":
    instance.append(1)
  elif db[i][1] == "Hypermetrope":
    instance.append(2)

  if db[i][2] == "No":
    instance.append(1)
  elif db[i][2] == "Yes":
    instance.append(2)

  if db[i][3] == "Reduced":
    instance.append(1)
  elif db[i][3] == "Normal":
    instance.append(2)

  X.append(instance)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
for i in range(len(db)):
  if db[i][4] == "No":
    Y.append(2)
  elif db[i][4] == "Yes":
    Y.append(1)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
