from pre_solving.pre_solving import *
from control.main_control import *
from numpy import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report

def naivebayes(filename1,filename2):
    read_file(filename1)
    train=convert(listCsv[1:])

    read_file(filename2)
    test=convert(listCsv[1:])

    for i in test:
        if i[29]>0:
            i[29]=1

    for i in train:
        if i[29]>0:
            i[29]=1


    clf = MultinomialNB().fit(train[:,:29], train[:,29])
    doc_class_predicted = clf.predict(test[:,:29])

    print(mean(doc_class_predicted == test[:,29]))


    precision, recall, thresholds = precision_recall_curve(test[:,29], clf.predict(test[:,:29]))
    answer = clf.predict_proba(test[:,:29])[:, 1]
    report = answer > 0.5
    print(classification_report(test[:,29], report, target_names=['neg', 'pos']))

fn=[]

import glob
for filename in glob.glob(r'lang/*.csv'):
    fn.append(filename)

