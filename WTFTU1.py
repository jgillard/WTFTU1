from flask import Flask
import datetime
app = Flask(__name__)


def findTime(timetable):
    dt = datetime.datetime.now()
    day = int(dt.strftime("%w"))
    time = int(dt.strftime("%H%M"))
    timeTemp = time
    for timeTemp in range(time, 2400):
        if timeTemp in timetable[day]:
            return formatTime(timeTemp)
    return "No buses you moron"


def formatTime(time):
    time = "%04d" % time
    return time[0:2] + ":" + time[2:4]


@app.route('/')
def start():
    t = datetime.datetime.now().strftime("%w@%H:%M")
    return "2L%s\n2U%sdebug%s" % (findTime(timetableUni), findTime(timetableLeam), t)


# leaving from uni
uniWeekday = [754, 824, 908, 938, 1008, 1038, 1108, 1138, 1208, 1238,
              1308, 1338, 1408, 1438, 1508, 1538, 1608, 1638, 1708, 1738,
              1808, 1838, 1914, 2014, 2114, 2239]
uniSat = [816, 846, 916, 946, 1016, 1046, 1116, 1146, 1216, 1246, 1316,
          1346, 1416, 1446, 1516, 1546, 1616, 1646, 1716, 1746, 1816,
          1910, 2010, 2110, 2239]
uniSun = [920, 940, 1000, 1020, 1040, 1100, 1120, 1140, 1200, 1220, 1240,
          1300, 1320, 1340, 1400, 1420, 1440, 1500, 1520, 1540, 1600, 1620,
          1640, 1700, 1720, 1740, 1800, 1820, 1850, 1920, 1950, 2031, 2131,
          2232]
# leaving from leam
leamWeekday = [714, 744, 814, 848, 918, 1002, 1032, 1102, 1132,
               1202, 1232, 1302, 1332, 1402, 1432, 1502, 1532, 1602, 1632,
               1702, 1732, 1802, 1830, 1858, 2000, 2100]
leamSat = [743, 813, 843, 913, 943, 1013, 1043, 1113, 1143, 1213,
           1243, 1313, 1343, 1413, 1443, 1513, 1543, 1613, 1643, 1713, 1743,
           1841, 1953, 2053]
leamSun = [801, 901, 921, 941, 1001, 1021, 1041, 1101, 1121, 1141, 1201,
           1221, 1241, 1301, 1321, 1341, 1401, 1421, 1441, 1501, 1521, 1541,
           1601, 1621, 1641, 1701, 1721, 1801, 1821, 1931, 2016, 2114, 2214]


timetableUni = [uniSun]
timetableUni.extend([uniWeekday] * 5)
timetableUni.extend(uniSat)
timetableLeam = [leamSun]
timetableLeam.extend([leamWeekday] * 5)
timetableLeam.extend(leamSat)


if __name__ == '__main__':
    app.debug = True
    app.run()
