from control.main_control import *
from numpy import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report

def naivebayes_cv(file , outputfile):
    fn = []

    import glob
    for filename in glob.glob(r''+file+'/*.csv'):
        fn.append(filename)

    #print fn
    out = open(outputfile, "w")
    j=0
    while j < len(fn):

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

        #print(mean(doc_class_predicted == test[:,len(test[0])-1]))


        precision, recall, thresholds = precision_recall_curve(test[:,len(test[0])-1], clf.predict(test[:,:len(test[0])-1]))
        answer = clf.predict_proba(test[:,:len(test[0])-1])[:, 1]
        report = answer > 0.5
        #print(classification_report(test[:,len(test[0])-1], report, target_names=['neg', 'pos']))


        out.write(fn[j]+"->"+fn[j+1]+"\n"+"\n")
        out.write(classification_report(test[:,len(test[0])-1], report, target_names=['neg', 'pos']))
        out.write("\n")
        j=j+2
    out.close()


naivebayes_cv("result/promise/0","result/promise/0/result.txt")
naivebayes_cv("result/promise/1","result/promise/1/result.txt")
naivebayes_cv("result/promise/2","result/promise/2/result.txt")
naivebayes_cv("result/promise/3","result/promise/3/result.txt")
naivebayes_cv("result/promise/4","result/promise/4/result.txt")
naivebayes_cv("result/promise/add","result/promise/add/result.txt")
naivebayes_cv("result/promise/delete","result/promise/delete/result.txt")