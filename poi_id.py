#!/usr/bin/env python
# coding: utf-8


# Python 2.7

import sys
import pickle
import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import *
from support_functions import *

from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier




### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'exercised_stock_options', 'restricted_stock', 'shared_receipt_with_poi', 'expenses', 
                 'other', 'nf_to_poi']




### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)



### Task 2: Remove outliers
data_dict.pop('TOTAL', 0)
data_dict.pop('THE TRAVEL AGENCY IN THE PARK', 0)
data_dict.pop('LOCKHART EUGENE E',0)

fix_shifted_data(data_dict)

### Task 3: Create new feature(s)

# New variables: a proportion of messages sent to POI, and the proportion of messages recieved from poi

# nf_bonus
data_dict = create_feature(data_dict, "bonus", "total_payments", "nf_bonus")

# nf_salary
data_dict = create_feature(data_dict, "salary", "total_payments", "nf_salary")


# nf_exercised_stock
data_dict = create_feature(data_dict, "exercised_stock_options", "total_payments", "nf_exercised_stock")


# nf_to_poi
data_dict = create_feature(data_dict, "from_this_person_to_poi", "from_messages", "nf_to_poi")

# nf_poi_to
data_dict = create_feature(data_dict, "from_poi_to_this_person", "to_messages", "nf_poi_to")




# Add the  new features
features_list = features_list + ['nf_bonus', 'nf_salary', 'nf_exercised_stock', 'nf_to_poi', 'nf_poi_to']
                



### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)





### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

# setup 3 algo tests

# Naive Bayes
clf_NB = GaussianNB()

# Decision Tree
clf_TREE = DecisionTreeClassifier()

# AdaBoost:
clf_ADA = AdaBoostClassifier()


#test_classifier(clf_NB, data_dict, features_list)
#test_classifier(clf_TREE, data_dict, features_list)
#test_classifier(clf_ADA, data_dict, features_list)



### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html


# Import 
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier

'''
# Gridsearch for learning rate and estimator hyperparameters
parameters = {'learning_rate':[0.1, 0.2, 0.3, 0.5, 0.7,0.8, 0.9, 1, 2,3, 5, 10],
              'n_estimators':[1,5,8,10,11, 12, 13, 14, 15, 16, 17, 18,50,100,1000, 2000] }
clf_ADA = AdaBoostClassifier()
clf = GridSearchCV(clf_ADA, parameters, scoring = 'f1', cv = 10 )
clf.fit(features, labels)

print clf.best_params_
print clf.best_score_


# test performance
lr = clf.best_params_['learning_rate']
n_est = clf.best_params_['n_estimators']
clf_ADA = AdaBoostClassifier(learning_rate = lr, n_estimators = n_est)
test_classifier(clf_ADA, data_dict, features_list)
'''

# best parameters found 
clf = AdaBoostClassifier(learning_rate = 0.9, n_estimators = 4) 
test_classifier(clf, data_dict, features_list)





### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)


