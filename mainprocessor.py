import xml.etree.ElementTree as ET
from readdata10000 import readdata10000
from V2QRScalculatornew import V2QRScalculatornew
from V3STEV60calculatornew import V3STEV60calculatornew
from ecgvalueprocessor import ecgvalueprocessor
from V4Rwavecalculatornew0712update import V4Rwavecalculatornew0712update

class mainprocessor:
    def __init__(self,path):
        self.path = path
        
    def mainprocessor(self):
        location = self.path
        tree = ET.parse(location)  
        root = tree.getroot()
        
        #取得QTc
        for RestingECGMeasurements in root.iter('RestingECGMeasurements'):#在所有RestingECGMeasurements包含的內容中
            QTc = int(RestingECGMeasurements.find('QTCorrected').text)#尋找RestingECGMeasurem
        
        #取得V2, V3, V4的ecg array（未還原）
        dataextract = readdata10000(self.path)#這個是class
        V2data = dataextract.V2data10000()
        V3data = dataextract.V3data10000()
        V4data = dataextract.V4data10000()
        #取得halfQRS duration(int)
        for RestingECGMeasurements in root.iter('RestingECGMeasurements'):#打開QRSTimesTypes 的第一層
            DoubleQRSDuration = RestingECGMeasurements.find('QRSDuration').text
            QRSDuration = int(int(DoubleQRSDuration)/2)
        halfQRSDuration = int(QRSDuration/2)

        #取得Timeindexlist(int)
        Timeindexlist = []
        for QRSTimesTypes in root.iter('QRSTimesTypes'):#打開QRSTimesTypes 的第一層
            for QRS in root.iter('QRS'):#開QRS(第二層)
                DoubleTime = QRS.find('Time').text
                Time = int(int(DoubleTime)/2)
                Timeindexlist.append(Time)
        
        
        #將V2data還原為原始量值
        newV2data = ecgvalueprocessor(V2data)#這個是class
        newV2arr10000 = newV2data.newecgvalue()
        #取得V2QRS的量值
        V2c = V2QRScalculatornew(newV2arr10000, Timeindexlist, halfQRSDuration)
        V2resultlist = V2c.V2QRS10000()
        V2QRSvalue = V2resultlist[0]
        V2Rwavelocation = V2resultlist[1]
        V2location = V2Rwavelocation*0.002

        #將V3data還原為原始量值
        newV3data = ecgvalueprocessor(V3data)#這個是class
        newV3arr10000 = newV3data.newecgvalue()
        #取得V3STE60的量值
        V3c = V3STEV60calculatornew(newV3arr10000, Timeindexlist, halfQRSDuration)
        V3STE60value = V3c.V3QRS10000()

        #將V4data還原為原始量值
        newV4data = ecgvalueprocessor(V4data)#這個是class
        newV4arr10000 = newV4data.newecgvalue()
        #取得RV4量值
        V4c = V4Rwavecalculatornew0712update(newV4arr10000, Timeindexlist, halfQRSDuration)
        RV4resultlist = V4c.V4QRS10000()
        RV4value = RV4resultlist[0]
        Rwavelocation = RV4resultlist[1]
        V4location = Rwavelocation*0.002

        #計算公式
        a = 0.052*QTc
        b = 0.151*V2QRSvalue
        c = 0.268*RV4value
        d = 1.062*V3STE60value
        result = a-b-c+d
        
        return QTc, V2QRSvalue, V3STE60value, RV4value, result
        







