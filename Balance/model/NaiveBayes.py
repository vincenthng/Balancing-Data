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
    out = open(outputfile, "w")
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


        out.write(fn[j]+"->"+fn[j+1]+"\n"+"\n")
        out.write(classification_report(test[:,29], report, target_names=['neg', 'pos']))
        out.write("\n")
    out.close()


naivebayes("result/lang/0","result/lang/0/result.txt")
naivebayes("result/lang/1","result/lang/1/result.txt")
naivebayes("result/lang/2","result/lang/2/result.txt")
naivebayes("result/lang/3","result/lang/3/result.txt")
naivebayes("result/time/0","result/time/0/result.txt")
naivebayes("result/time/1","result/time/1/result.txt")
naivebayes("result/time/2","result/time/2/result.txt")
naivebayes("result/time/3","result/time/3/result.txt")
naivebayes("result/math/0","result/math/0/result.txt")
naivebayes("result/math/1","result/math/1/result.txt")
naivebayes("result/math/2","result/math/2/result.txt")
naivebayes("result/math/3","result/math/3/result.txt")
naivebayes("result/delete/lang","result/delete/lang/result.txt")
naivebayes("result/delete/time","result/delete/time/result.txt")
naivebayes("result/delete/math","result/delete/math/result.txt")
naivebayes("result/add/lang","result/add/lang/result.txt")
naivebayes("result/add/time","result/add/time/result.txt")
naivebayes("result/add/math","result/add/math/result.txt")
naivebayes("result/MORPH/lang","result/MORPH/lang/result.txt")
naivebayes("result/MORPH/time","result/MORPH/time/result.txt")
naivebayes("result/MORPH/math","result/MORPH/math/result.txt")
