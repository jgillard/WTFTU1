from flask import Flask
import datetime
import sys
import logging
app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


def findTime(timetable):
    dt = datetime.datetime.now()
    day = int(dt.strftime("%w"))
    time = int(dt.strftime("%H%M"))
    timeTemp = time
    for timeTemp in range(time, 2400):
        if timeTemp > 400:
            if timeTemp in timetable[day]:
                return formatTime(timeTemp)
        else:
            if timeTemp in timetable[day-1]:
                return formatTime(timeTemp)
    return "No buses you moron"


def formatTime(time):
    time = "%04d" % time
    return time[0:2] + ":" + time[2:4]


@app.route('/')
def start():
    t = datetime.datetime.now().strftime("%w@%H:%M")
    return "2L%s\n2U%sdebug%s" % (findTime(timetableUni), findTime(timetableLeam), t)

# NO MIDDLE TIMETABLE BUSES ADDED
# DAY SPECIFIC SUPER LATE BUSES
# leaving from uni
uniWeekday = [808, 822, 848, 859, 921, 932, 947, 1002, 1017, 1032,
              1047, 1102, 1117, 1132, 1147, 1202, 1217, 1232, 1247, 1302,
              1317, 1332, 1347, 1402, 1417, 1432, 1452, 1509, 1523,
              1540, 1555, 1615, 1629, 1637, 1649, 1659, 1718, 1731, 1740,
              1807, 1814, 1829, 1844, 1851, 1907, 1927, 1947, 2008, 2028,
              2048, 2108, 2128, 2148, 2208, 2228, 2248, 2348, 12, 42, 113, 118]
uniSat = [826, 846, 906, 926, 946, 1006, 1026, 1046, 1106, 1126, 1146, 1206,
          1226, 1246, 1306, 1326, 1346, 1406, 1426, 1446, 1506, 1526, 1546,
          1606, 1626, 1646, 1706, 1726, 1746, 1806, 1828, 1848, 1908, 1923,
          1938, 2008, 2038, 2108, 2138, 2208, 2238, 2308, 2348, 12, 42, 113,
          118, 213, 220]
uniSun = [920, 940, 1000, 1020, 1040, 1100, 1120, 1140, 1200, 1220, 1240,
          1300, 1320, 1340, 1400, 1420, 1440, 1500, 1520, 1540, 1600, 1620,
          1640, 1700, 1720, 1740, 1800, 1820, 1850, 1920, 1950, 2031, 2131,
          2232]
# leaving from leam
leamWeekday = [656, 711, 726, 736, 746, 756, 806, 815, 821, 843, 850, 903,
               909, 919, 928, 941, 949, 1004, 1013, 1024, 1039, 1054, 1109,
               1124, 1139, 1154, 1209, 1224, 1239, 1254, 1309,
               1324, 1339, 1354, 1414, 1429, 1444, 1459, 1514, 1529, 1549,
               1606, 1622, 1639, 1656, 1714, 1728, 1736, 1748, 1758, 1817,
               1835, 1850, 1900, 1940, 1959, 2019, 2039, 2059, 2119, 2139,
               2159, 2219, 2236, 2256, 2319, 2339, 37]
leamSat = [750, 810, 830, 850, 910, 930, 950, 1010, 1030, 1050, 1110, 1130,
           1150, 1210, 1230, 1250, 1310, 1330, 1350, 1410, 1430, 1450, 1510,
           1530, 1550, 1610, 1630, 1650, 1710, 1730, 1750, 1810, 1830, 1850,
           1910, 1925, 1945, 2005, 2035, 2105, 2135, 2205, 2235, 2305, 2335,
           5, 37, 101, 131]
leamSun = [801, 901, 921, 941, 1001, 1021, 1041, 1101, 1121, 1141, 1201,
           1221, 1241, 1301, 1321, 1341, 1401, 1421, 1441, 1501, 1521, 1541,
           1601, 1621, 1641, 1701, 1721, 1801, 1821, 1931, 2016, 2114, 2214]


timetableUni = [uniSun]
timetableUni.extend([uniWeekday] * 5)
timetableUni.extend([uniSat])
timetableLeam = [leamSun]
timetableLeam.extend([leamWeekday] * 5)
timetableLeam.extend([leamSat])


if __name__ == '__main__':
    app.debug = True
    app.run()
