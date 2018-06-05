#!/usr/bin/python

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()

from sklearn.svm import SVC

clf = SVC(kernel="rbf", C=100000)

t0 = time()

clf.fit(features_train, labels_train)

print "training time:", round(time() - t0, 3), "s" #0.137

print clf.score(features_test, labels_test) #0.944

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass