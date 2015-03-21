from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')
def start():
    dt = datetime.datetime.now()
    day = int(dt.strftime("%w"))
    time = int(dt.strftime("%H%M"))
    timeTemp = time
    while timeTemp < 2400:
        while timeTemp not in timetableUni[day]:
            timeTemp += 1
        else:
            responseUni = (str(timeTemp)[0:2] + ":" + str(timeTemp)[2:4])
        timeTemp = time
        while timeTemp not in timetableLeam[day]:
            timeTemp += 1
        else:
            responseLeam = (str(timeTemp)[0:2] + ":" + str(timeTemp)[2:4])
        response = "2L" + responseUni + "2U" + responseLeam
        return str(response)
    return "0"


uniWeekday = [0754, 0x0824, 0x0908, 0x0938, 1008, 1038, 1108, 1138, 1208,
              1238, 1308, 1338, 1408, 1438, 1508, 1538, 1608, 1638, 1708,
              1738, 1808, 1838, 1914, 2014, 2114, 2239]
uniSat = [0x0816, 0x0846, 0x0916, 0x0946, 1016, 1046, 1116, 1146, 1216, 1246,
          1316, 1346, 1416, 1446, 1516, 1546, 1616, 1646, 1716, 1746, 1816,
          1910, 2010, 2110, 2239]
uniSun = [0x0920, 0x0940, 1000, 1020, 1040, 1100, 1120, 1140, 1200, 1220,
          1240, 1300, 1320, 1340, 1400, 1420, 1440, 1500, 1520, 1540, 1600,
          1620, 1640, 1700, 1720, 1740, 1800, 1820, 1850, 1920, 1950, 2031,
          2131, 2232]
leamWeekday = [0714, 0744, 0x0814, 0x0848, 0x0918, 1002, 1032, 1102, 1132,
               1202, 1232, 1302, 1332, 1402, 1432, 1502, 1532, 1602, 1632,
               1702, 1732, 1802, 1830, 1858, 2000, 2100]
leamSat = [0743, 0x0813, 0x0843, 0x0913, 0x0943, 1013, 1043, 1113, 1143, 1213,
           1243, 1313, 1343, 1413, 1443, 1513, 1543, 1613, 1643, 1713, 1743,
           1841, 1953, 2053]
leamSun = [0x0801, 0x0901, 0x0921, 0x0941, 1001, 1021, 1041, 1101, 1121, 1141,
           1201, 1221, 1241, 1301, 1321, 1341, 1401, 1421, 1441, 1501, 1521,
           1541, 1601, 1621, 1641, 1701, 1721, 1801, 1821, 1931, 2016, 2114,
           2214]

timetableUni = [uniWeekday] * 5
timetableUni.extend([uniSat, uniSun])
timetableLeam = [leamWeekday] * 5
timetableLeam.extend([leamSat, leamSun])


if __name__ == '__main__':
    app.debug = True
    app.run()
