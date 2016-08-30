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
            if i[len(i)-1]>0:
                i[len(i)-1]=1

        for i in train:
            if i[len(i)-1]>0:
                i[len(i)-1]=1

        clf = MultinomialNB().fit(train[:,:len(train[0])-1], train[:,len(train[0])-1])
        doc_class_predicted = clf.predict(test[:,:len(test[0])-1])

        print(mean(doc_class_predicted == test[:,len(test[0])-1]))


        precision, recall, thresholds = precision_recall_curve(test[:,len(test[0])-1], clf.predict(test[:,:len(test[0])-1]))
        answer = clf.predict_proba(test[:,:len(test[0])-1])[:, 1]
        report = answer > 0.5
        print(classification_report(test[:,len(test[0])-1], report, target_names=['neg', 'pos']))


        out.write(fn[j]+"->"+fn[j+1]+"\n"+"\n")
        out.write(classification_report(test[:,len(test[0])-1], report, target_names=['neg', 'pos']))
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

naivebayes("result/ant/0","result/ant/0/result.txt")
naivebayes("result/ant/1","result/ant/1/result.txt")
naivebayes("result/ant/2","result/ant/2/result.txt")
naivebayes("result/ant/3","result/ant/3/result.txt")

naivebayes("result/camel/0","result/camel/0/result.txt")
naivebayes("result/camel/1","result/camel/1/result.txt")
naivebayes("result/camel/2","result/camel/2/result.txt")
naivebayes("result/camel/3","result/camel/3/result.txt")

naivebayes("result/ivy/0","result/ivy/0/result.txt")
naivebayes("result/ivy/1","result/ivy/1/result.txt")
naivebayes("result/ivy/2","result/ivy/2/result.txt")
naivebayes("result/ivy/3","result/ivy/3/result.txt")

naivebayes("result/jedit/0","result/jedit/0/result.txt")
naivebayes("result/jedit/1","result/jedit/1/result.txt")
naivebayes("result/jedit/2","result/jedit/2/result.txt")
naivebayes("result/jedit/3","result/jedit/3/result.txt")

naivebayes("result/log4j/0","result/log4j/0/result.txt")
naivebayes("result/log4j/1","result/log4j/1/result.txt")
naivebayes("result/log4j/2","result/log4j/2/result.txt")
naivebayes("result/log4j/3","result/log4j/3/result.txt")

naivebayes("result/lucene/0","result/lucene/0/result.txt")
naivebayes("result/lucene/1","result/lucene/1/result.txt")
naivebayes("result/lucene/2","result/lucene/2/result.txt")
naivebayes("result/lucene/3","result/lucene/3/result.txt")

naivebayes("result/poi/0","result/poi/0/result.txt")
naivebayes("result/poi/1","result/poi/1/result.txt")
naivebayes("result/poi/2","result/poi/2/result.txt")
naivebayes("result/poi/3","result/poi/3/result.txt")

naivebayes("result/synapse/0","result/synapse/0/result.txt")
naivebayes("result/synapse/1","result/synapse/1/result.txt")
naivebayes("result/synapse/2","result/synapse/2/result.txt")
naivebayes("result/synapse/3","result/synapse/3/result.txt")

naivebayes("result/velocity/0","result/velocity/0/result.txt")
naivebayes("result/velocity/1","result/velocity/1/result.txt")
naivebayes("result/velocity/2","result/velocity/2/result.txt")
naivebayes("result/velocity/3","result/velocity/3/result.txt")

naivebayes("result/xalan/0","result/xalan/0/result.txt")
naivebayes("result/xalan/1","result/xalan/1/result.txt")
naivebayes("result/xalan/2","result/xalan/2/result.txt")
naivebayes("result/xalan/3","result/xalan/3/result.txt")

naivebayes("result/xerces/0","result/xerces/0/result.txt")
naivebayes("result/xerces/1","result/xerces/1/result.txt")
naivebayes("result/xerces/2","result/xerces/2/result.txt")
naivebayes("result/xerces/3","result/xerces/3/result.txt")

naivebayes("result/delete/lang","result/delete/lang/result.txt")
naivebayes("result/delete/time","result/delete/time/result.txt")
naivebayes("result/delete/math","result/delete/math/result.txt")
naivebayes("result/delete/ant","result/delete/ant/result.txt")
naivebayes("result/delete/camel","result/delete/camel/result.txt")
naivebayes("result/delete/ivy","result/delete/ivy/result.txt")
naivebayes("result/delete/jedit","result/delete/jedit/result.txt")
naivebayes("result/delete/log4j","result/delete/log4j/result.txt")
naivebayes("result/delete/lucene","result/delete/lucene/result.txt")
naivebayes("result/delete/poi","result/delete/poi/result.txt")
naivebayes("result/delete/synapse","result/delete/synapse/result.txt")
naivebayes("result/delete/velocity","result/delete/velocity/result.txt")
naivebayes("result/delete/xalan","result/delete/xalan/result.txt")
naivebayes("result/delete/xerces","result/delete/xerces/result.txt")

naivebayes("result/add/lang","result/add/lang/result.txt")
naivebayes("result/add/time","result/add/time/result.txt")
naivebayes("result/add/math","result/add/math/result.txt")
naivebayes("result/add/ant","result/add/ant/result.txt")
naivebayes("result/add/camel","result/add/camel/result.txt")
naivebayes("result/add/ivy","result/add/ivy/result.txt")
naivebayes("result/add/jedit","result/add/jedit/result.txt")
naivebayes("result/add/log4j","result/add/log4j/result.txt")
naivebayes("result/add/lucene","result/add/lucene/result.txt")
naivebayes("result/add/poi","result/add/poi/result.txt")
naivebayes("result/add/synapse","result/add/synapse/result.txt")
naivebayes("result/add/velocity","result/add/velocity/result.txt")
naivebayes("result/add/xalan","result/add/xalan/result.txt")
naivebayes("result/add/xerces","result/add/xerces/result.txt")


naivebayes("result/MORPH/lang","result/MORPH/lang/result.txt")
naivebayes("result/MORPH/time","result/MORPH/time/result.txt")
naivebayes("result/MORPH/math","result/MORPH/math/result.txt")
naivebayes("result/MORPH/ant","result/MORPH/ant/result.txt")
naivebayes("result/MORPH/camel","result/MORPH/camel/result.txt")
naivebayes("result/MORPH/ivy","result/MORPH/ivy/result.txt")
naivebayes("result/MORPH/jedit","result/MORPH/jedit/result.txt")
naivebayes("result/MORPH/log4j","result/MORPH/log4j/result.txt")
naivebayes("result/MORPH/lucene","result/MORPH/lucene/result.txt")
naivebayes("result/MORPH/poi","result/MORPH/poi/result.txt")
naivebayes("result/MORPH/synapse","result/MORPH/synapse/result.txt")
naivebayes("result/MORPH/velocity","result/MORPH/velocity/result.txt")
naivebayes("result/MORPH/xalan","result/MORPH/xalan/result.txt")
naivebayes("result/MORPH/xerces","result/MORPH/xerces/result.txt")
