#!/usr/bin/python

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()

t0 = time()

clf.fit(features_train, labels_train)

print "training time:", round(time() - t0, 3), "s" #0.031

print clf.score(features_test, labels_test) #0.916

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass