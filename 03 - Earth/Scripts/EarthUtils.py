class DataKey:
    name: str
    start: int
    end: int
    
    def __init__(self, name, start, end) -> None:
        self.name = name
        self.start = start
        self.end = end
        
class NRLMSIS_Table:
    table = []
    
    Year = DataKey("Year", 0, 4)
    Mon = DataKey("Mon", 5, 7)
    Day = DataKey("Day", 8, 10)
    DOY = DataKey("DOY", 11, 14)
    hour  = DataKey("hour", 15, 20)
    Heit  = DataKey("Heit", 21, 29)
    Lat = DataKey("Lat", 30, 35)
    Long = DataKey("Long", 36, 42)
    air = DataKey("air", 75, 84)
    T = DataKey("T", 85, 92)
    
    def __init__(self, tableName: str) -> None:
        import os
        path = os.path.dirname(os.path.abspath(__file__))+"\\"
        
        raw_data = []
        with open(path+tableName) as tbl:
            raw_data = tbl.readlines()
            raw_data.pop(0)
        
        for line in raw_data:
            lineData = {}
            lineData.update({self.Year.name: float(line[self.Year.start:self.Year.end])})
            lineData.update({self.Mon.name: float(line[self.Mon.start:self.Mon.end])})
            lineData.update({self.Day.name: float(line[self.Day.start:self.Day.end])})
            lineData.update({self.DOY.name: float(line[self.DOY.start:self.DOY.end])})
            lineData.update({self.hour.name: str(line[self.hour.start:self.hour.end])})
            lineData.update({self.Heit.name: float(line[self.Heit.start:self.Heit.end])})
            lineData.update({self.Lat.name: float(line[self.Lat.start:self.Lat.end])})
            lineData.update({self.Long.name: float(line[self.Long.start:self.Long.end])})
            lineData.update({self.air.name: float(line[self.air.start:self.air.end])*1000})
            lineData.update({self.T.name: float(line[self.T.start:self.T.end])})
            self.table.append(lineData)
        
        #Year Mon Day DOY hour Heit(km) Lat  Lon Oden(cm-3) N2den(cm-3) O2den(cm-3) air(gm/cm3) T(K) exoT(K) Heden(cm-3)Arden(cm-3) Hden(cm-3) Nden(cm-3) F107 F107a apdaily  ap0-3 ap3-6 ap6-9 ap9-12 ap12-33 ap33-59
        #YYYY MM DD DOY HR.MN HHHH.HHH DD.DD DDD.DD O.OOOESVVV O.OOOESVVV 5.065E+18 1.163E-03 VVVV.VV VVVV  1.258E+14  2.257E+17  9.999E-38  9.999E-38   71.4   72.9    5.2    3.0    6.0    7.0   12.0    2.2    3.2
        #2020  9 22 266 12.00    0.0    0.0   90.0  9.999E-38  1.889E+19  5.065E+18 1.163E-03  300.2   837  1.258E+14  2.257E+17  9.999E-38  9.999E-38   71.4   72.9    5.2    3.0    6.0    7.0   12.0    2.2    3.2
            
    
    
# def PressureFromDensity(filename: str):
#     '''
#     Pressure at altitude (z) is defined as 
#     \int_z^\infty \rho(\theta,)
    
#     '''

def KSPTempCurveFromTable(tableName: str):
    DataSet = NRLMSIS_Table(tableName)
    for data in DataSet.table:
        print(f"key = {data.get('Heit')*1000}, {data.get('T')}")


def Main() -> None:
    KSPTempCurveFromTable("Temp.txt")
    
Main()