from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

allElectronicsData = open(r'input.csv') #

reader = csv.reader(allElectronicsData)

headers = next(reader)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[0])
    rowDict = {}
    for i in  range(1,len(row)):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
'''
print(featureList)
print(type(featureList[0]))
'''

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print("dummyX:\n" + str(dummyX))
print(vec.get_feature_names())
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:" + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX,dummyY)

print("clf:" + str(clf))

oneRowX = dummyX[0,:]
print("oneRowX:" + str(oneRowX))

predictedY = clf.predict(oneRowX.reshape(1,-1))
print("predictedY:" + str(predictedY))
