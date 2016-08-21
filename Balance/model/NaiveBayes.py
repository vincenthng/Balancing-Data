from pre_solving.pre_solving import *
from control.main_control import *
from numpy import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report

def naivebayes(file , outputfile):
    fn = []

    import glob
    for filename in glob.glob(r''+file+'/*.csv'):
        fn.append(filename)

    print fn

    for j in range(0, len(fn) - 1):

        read_file(fn[j])
        train=convert(listCsv[1:])

        read_file(fn[j+1])
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

        out = open(outputfile, "a")
        out.write(fn[j]+"->"+fn[j+1]+"\n"+"\n")
        out.write(classification_report(test[:,29], report, target_names=['neg', 'pos']))
        out.write("\n")
        out.close()


naivebayes("lang","result.txt")