from control.main_control import *
from numpy import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn import metrics

def naivebayes_cv(file , outputfile):
    fn = []

    import glob
    for filename in glob.glob(r''+file+'/*.csv'):
        fn.append(filename)

    #print fn
    out = open(outputfile, "w")
    j=0
    while j < len(fn)-1:

        read_file(fn[j])
        train=convert(listCsv[1:])

        read_file(fn[j+1])
        test=convert(listCsv[1:])

        for i in test:
            if i[len(i)-1]>0:
                i[len(i)-1]=1

        for i in train:
            if i[len(i)-1]>0:
                i[len(i)-1]=1

        clf = MultinomialNB().fit(train[:,:len(train[0])-1], train[:,len(train[0])-1])
        #doc_class_predicted = clf.predict(test[:,:len(test[0])-1])

        #print(mean(doc_class_predicted == test[:,len(test[0])-1]))


        #precision, recall, thresholds = precision_recall_curve(test[:,len(test[0])-1], clf.predict(test[:,:len(test[0])-1]))
        answer = clf.predict_proba(test[:,:len(test[0])-1])[:, 1]
        report = answer > 0.5
        #print(classification_report(test[:,len(test[0])-1], report, target_names=['neg', 'pos']))

        cm = metrics.confusion_matrix(test[:, len(test[0]) - 1], report)
        rc = metrics.recall_score(test[:, len(test[0]) - 1], report, average='binary')
        pr = metrics.precision_score(test[:, len(test[0]) - 1], report, average='binary')
        auc = metrics.roc_auc_score(test[:, len(test[0]) - 1], answer)
        f1 = metrics.f1_score(test[:, len(test[0]) - 1], report)
        setname=fn[j].split("/")[1]
        ver=fn[j].split('/')
        ver1 = fn[j+1].split('/')
        out.write(ver[len(ver)-1][2:5]+ ","+ver1[len(ver1)-1][2:5]+"," + str(cm[0][0]) + "," + str(cm[0][1]) + "," + str(cm[1][0]) + "," + str(cm[1][1]) + "," + str(rc) + "," + str(pr) + "," + str(f1) + "," + str(auc) + "\n")
        j=j+1
    out.close()


naivebayes_cv("data_20160416/lang","data_20160416/lang/lang.txt")
naivebayes_cv("data_20160416/math","data_20160416/math/math.txt")
naivebayes_cv("data_20160416/time","data_20160416/time/time.txt")
'''
naivebayes_cv("data_20160416/jedit","data_20160416/jedit/jedit.txt")
naivebayes_cv("data_20160416/poi","data_20160416/poi/poi.txt")
naivebayes_cv("data_20160416/xalan","data_20160416/xalan/xalan.txt")
naivebayes_cv("data_20160416/xerces","data_20160416/xerces/xerces.txt")
'''