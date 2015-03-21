from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')
def start():
    dt = datetime.datetime.now()
    day = int(dt.strftime("%w"))
    time = int(dt.strftime("%H%M"))
    while time < 2400:
            if time not in TIMETABLE_DAY[day]:
                time += 1
            else:
                response = (str(time)[0:2] + ":" + str(time)[2:4])
                return response
    return "No Bus Time"


uniWeekday = [1708, 1738, 1808, 1838, 1914, 2014, 2114, 2239]
uniSat = []
uniSun = []
leamWeekday = [1743, 1813, 1841, 1911, 1943, 2043, 2143, 2308]
leamSat = []
leamSun = []

TIMETABLE_DAY = [uniWeekday] * 5
TIMETABLE_DAY.extend([uniSat, uniSun])


if __name__ == '__main__':
    app.debug = True
    app.run()
