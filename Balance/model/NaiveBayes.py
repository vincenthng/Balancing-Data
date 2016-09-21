
from pre_solving.pre_solving import *
from control.main_control import *
from numpy import *
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report

def naivebayes(file,testset,outputfile,outputfile1,header1_row,header1_col,header2_row,header2_col):
    fn = []

    import glob
    for filename in glob.glob(r''+file+'/*.csv'):
        fn.append(filename)

    #print fn

    optemp=outputfile
    j=0
    while j < len(fn):
        setname=testset.split("/")[1]
        setname=setname.split('_')[0]
        setname1=setname.split('.')[1][0:4]
        if fn[j].split('/')[1] == setname1:
            temp1 = fn[j].split('/')[2]
        else:
            temp1 = fn[j].split('/')[1]
        
        outputfile=optemp+setname+"_"+temp1+"_"+str(j)+".csv"

        #out = open(outputfile, "w")


        read_file(fn[j])
        train=convert(listCsv[header1_row:])

        read_file(testset)
        test=convert(listCsv[header2_row:])

        for i in test:
            if i[len(i)-1]>0:
                i[len(i)-1]=1

        for i in train:
            if i[len(i)-1]>0:
                i[len(i)-1]=1

        clf = MultinomialNB().fit(train[:,header1_col:len(train[0])-1], train[:,len(train[0])-1])
        doc_class_predicted = clf.predict(test[header2_row:,header2_col:len(test[0])-1])

        #print(mean(doc_class_predicted == test[:,len(test[0])-1]))


        #precision, recall, thresholds = precision_recall_curve(test[:,len(test[0])-1], clf.predict(test[:,header2_col:len(test[0])-1]))
        answer = clf.predict_proba(test[:,header2_col:len(test[0])-1])[:, 1]
        report = answer > 0.5
        '''
        z=0
        for z in range(0,len(answer)):
            out.write(str(test[z,len(test[0])-1]))
            out.write(",")
            out.write(str(answer[z]))
            out.write("\n")
        out.close()
        '''
        out1 = open(outputfile1, "a")
        cm=metrics.confusion_matrix(test[:,len(test[0])-1],report)
        rc=metrics.recall_score(test[:, len(test[0]) - 1], report, average='binary')
        pr=metrics.precision_score(test[:, len(test[0]) - 1], report, average='binary')
        auc = metrics.roc_auc_score(test[:, len(test[0]) - 1], answer)
        f1=metrics.f1_score(test[:, len(test[0]) - 1], report)
        out1.write(setname+","+temp1+","+str(cm[0][0])+","+str(cm[0][1])+","+str(cm[1][0])+","+str(cm[1][1])+","+str(rc)+","+str(pr)+","+str(f1)+","+str(auc)+"\n")
        out1.close()
        
        '''
        out.write(fn[j]+"->"+testset+"\n"+"\n")
        out.write(classification_report(test[:,len(test[0])-1], report, target_names=['neg', 'pos']))
        out.write("\n")
        '''
        j=j+1


naivebayes("40%/lang/0/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/1/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/2/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/3/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)

naivebayes("40%/lang/0/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/1/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/2/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/3/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)

naivebayes("40%/lang/0/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/1/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/2/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/3/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)

naivebayes("40%/lang/0/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/1/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/2/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/3/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)

naivebayes("40%/lang/0/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/1/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/2/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/3/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)

naivebayes("40%/lang/0/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/1/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/2/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/3/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)

naivebayes("40%/lang/0/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/1/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/2/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/lang/3/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)




naivebayes("40%/math/0/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/1/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/2/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/3/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)

naivebayes("40%/math/0/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/1/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/2/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/3/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)

naivebayes("40%/math/0/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/1/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/2/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/3/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)

naivebayes("40%/math/0/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/1/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/2/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/3/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)

naivebayes("40%/math/0/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/1/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/2/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/3/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)

naivebayes("40%/math/0/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/1/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/2/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/3/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)

naivebayes("40%/math/0/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/1/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/2/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/math/3/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)




naivebayes("40%/time/0/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/1/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/2/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/3/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)

naivebayes("40%/time/0/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/1/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/2/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/3/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)

naivebayes("40%/time/0/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/1/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/2/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/3/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)

naivebayes("40%/time/0/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/1/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/2/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/time/3/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)



naivebayes("40%/origin/lang/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/origin/lang/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/origin/lang/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/origin/lang/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/origin/lang/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/origin/lang/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/origin/lang/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)


naivebayes("40%/origin/math/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/origin/math/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/origin/math/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/origin/math/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/origin/math/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/origin/math/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/origin/math/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)


naivebayes("40%/origin/time/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/origin/time/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/origin/time/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/origin/time/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)



naivebayes("40%/add/lang/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/add/lang/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/add/lang/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/add/lang/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/add/lang/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/add/lang/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/add/lang/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)


naivebayes("40%/add/math/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/add/math/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/add/math/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/add/math/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/add/math/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/add/math/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/add/math/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)


naivebayes("40%/add/time/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/add/time/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/add/time/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/add/time/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)



naivebayes("40%/delete/lang/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/delete/lang/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/delete/lang/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/delete/lang/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/delete/lang/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/delete/lang/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/delete/lang/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)


naivebayes("40%/delete/math/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/delete/math/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/delete/math/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/delete/math/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/delete/math/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/delete/math/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/delete/math/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)


naivebayes("40%/delete/time/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/delete/time/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/delete/time/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/delete/time/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)



naivebayes("40%/morph/lang/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/morph/lang/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/morph/lang/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/morph/lang/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/morph/lang/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/morph/lang/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/morph/lang/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)


naivebayes("40%/morph/math/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/morph/math/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/morph/math/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/morph/math/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/morph/math/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/morph/math/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/morph/math/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)


naivebayes("40%/morph/time/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/morph/time/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/morph/time/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/morph/time/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)


naivebayes("40%/smote/lang/2","test/1.lang2.2_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/smote/lang/3","test/2.lang2.3_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/smote/lang/4","test/3.lang2.4_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/smote/lang/5","test/4.lang2.5_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/smote/lang/6","test/5.lang3.0b_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/smote/lang/7","test/6.lang3.0_all.csv","tr/","lang_40%.csv",1,1,1,1)
naivebayes("40%/smote/lang/8","test/7.lang3.0.1_all.csv","tr/","lang_40%.csv",1,1,1,1)


naivebayes("40%/smote/math/2","test/1.math1.2S_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/smote/math/3","test/2.math1.2R_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/smote/math/4","test/3.math2.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/smote/math/5","test/4.math2.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/smote/math/6","test/5.math3.0_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/smote/math/7","test/6.math3.1_all.csv","tr/","math_40%.csv",1,1,1,1)
naivebayes("40%/smote/math/8","test/7.math3.1.1_all.csv","tr/","math_40%.csv",1,1,1,1)


naivebayes("40%/smote/time/2","test/1.time2.0_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/smote/time/3","test/2.time2.1_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/smote/time/4","test/3.time2.2_all.csv","tr/","time_40%.csv",1,1,1,1)
naivebayes("40%/smote/time/5","test/4.time2.3_all.csv","tr/","time_40%.csv",1,1,1,1)


'''

naivebayes("40%/ant/0","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/ant/1","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/ant/2","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/ant/3","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,1,1,1)


naivebayes("40%/camel/0","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/camel/1","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/camel/2","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/camel/3","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,1,1,1)

naivebayes("40%/ivy/0","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/ivy/1","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/ivy/2","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/ivy/3","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,1,1,1)

naivebayes("40%/jedit/0","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/jedit/1","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/jedit/2","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/jedit/3","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,1,1,1)

naivebayes("40%/poi/0","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/poi/1","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/poi/2","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/poi/3","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)

naivebayes("40%/xalan/0","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/xalan/1","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/xalan/2","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/xalan/3","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)

naivebayes("40%/xerces/0","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/xerces/1","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/xerces/2","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/xerces/3","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,1,1,1)


#naivebayes("40%/delete/lang","","40%/delete/lang/40%.txt")
#naivebayes("40%/delete/time","","40%/delete/time/40%.txt")
#naivebayes("40%/delete/math","","40%/delete/math/40%.txt")
naivebayes("40%/delete/ant","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/delete/camel","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/delete/ivy","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/delete/jedit","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/delete/poi","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/delete/xalan","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/delete/xerces","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,1,1,1)

#naivebayes("40%/add/lang","","40%/add/lang/40%.txt")
#naivebayes("40%/add/time","","40%/add/time/40%.txt")
#naivebayes("40%/add/math","","40%/add/math/40%.txt")
naivebayes("40%/add/ant","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/add/camel","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/add/ivy","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/add/jedit","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/add/poi","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/add/xalan","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/add/xerces","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,1,1,1)


naivebayes("40%/morph/ant","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/morph/camel","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/morph/ivy","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/morph/jedit","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/morph/poi","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/morph/xalan","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/morph/xerces","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,1,1,1)


naivebayes("40%/origin/ant","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/origin/camel","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/origin/ivy","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/origin/jedit","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/origin/poi","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/origin/xalan","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,1,1,1)
naivebayes("40%/origin/xerces","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,1,1,1)


naivebayes("40%/smote/ant","test/ant_4.1.6.csv","tr/","PRO_40%.csv",1,0,1,1)
naivebayes("40%/smote/camel","test/camel_2.1.2.csv","tr/","PRO_40%.csv",1,0,1,1)
naivebayes("40%/smote/ivy","test/ivy_3.2.0.csv","tr/","PRO_40%.csv",1,0,1,1)
naivebayes("40%/smote/jedit","test/jedit_5.4.3.csv","tr/","PRO_40%.csv",1,0,1,1)
naivebayes("40%/smote/poi","test/poi_3.2.5.csv","tr/","PRO_40%.csv",1,0,1,1)
naivebayes("40%/smote/xalan","test/xalan_2.2.5.csv","tr/","PRO_40%.csv",1,0,1,1)
naivebayes("40%/smote/xerces","test/xerces_3.1.3.csv","tr/","PRO_40%.csv",1,0,1,1)
'''