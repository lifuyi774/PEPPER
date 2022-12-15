## Import packages
from pycaret.classification import *
import pandas as pd
from sklearn.metrics import *
import os
import re
from collections import Counter
from codes import readFasta, AAC, GAAC, CKSAAP, CKSAAGP, CTriad, KSCTriad, CTDC, CTDD, CTDT

def PGRS_predict(file, threshold, saveFeatures, out):
    allSeq = readFasta.readFasta(file)
    allFeatures = getAllFeatures(allSeq, out, saveFeatures)
    optimalFeatures = getOptimalFeatures(allFeatures)
    predictedResults = makePrediction(allFeatures, optimalFeatures, threshold, out)
    return predictedResults

def makePrediction(allFeatures, optimalFeatures, threshold, out):
    lightGBM = load_model('./model/final_lightGBM_111')
    results = predict_model(lightGBM, data=optimalFeatures, probability_threshold=float(threshold))
    results = pd.concat([allFeatures['#'], results['Label'], results['Score']], axis='columns')
    return results
    
def getOptimalFeatures(allFeatures):
    f=open("./model/selected_features_111.txt","r")
    IFS = f.readlines()
    for IFS_feature in IFS:
        IFS_feature = IFS_feature.replace('\n', '')
    f.close()
    for i in range(0, len(IFS)):
        IFS[i] = IFS[i].replace('\n','')
    optimalFeatures = allFeatures[IFS]
    return optimalFeatures
    
def getAllFeatures(allSeq, out, saveFeatures):
    f_AAC = AAC.AAC(allSeq)
    f_GAAC = GAAC.GAAC(allSeq)
    f_CTDC = CTDC.CTDC(allSeq)
    f_CTDD = CTDD.CTDD(allSeq)
    f_CTDT = CTDT.CTDT(allSeq)
    f_CTriad = CTriad.CTriad(allSeq)
    f_KSCTriad = KSCTriad.KSCTriad(allSeq)
    f_CKSAAP = CKSAAP.CKSAAP(allSeq)
    f_CKSAAGP = CKSAAGP.CKSAAGP(allSeq)
    
    allFeatures = pd.concat([f_AAC, f_GAAC.drop('#', axis='columns'), 
                         f_CTDC.drop('#', axis='columns'), f_CTDD.drop('#', axis='columns'), 
                         f_CTDT.drop('#', axis='columns'), f_CTriad.drop('#', axis='columns'), 
                         f_KSCTriad.drop('#', axis='columns'), f_CKSAAP.drop('#', axis='columns'), 
                         f_CKSAAGP.drop('#', axis='columns')], axis='columns')
    if saveFeatures.lower() == 'yes':
        allFeatures.to_csv(out + "/allFeatures.csv", index=None)
    
    return allFeatures