#scikit learn and TensorFlow
#classifier, supervised learning (denetlenen) 
from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels) #find patterns in data
print clf.predict([[100,3]])

#	weihgt	texture		label
#	/		/			/	
#	150g	bumpy_0		orange_0
#	170g 	bumpy_0		orange_0
#	140g	smooth_1	apple_1
# 	130g	smooth_1 	apple_1
#