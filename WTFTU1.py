from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')
def start():
    dt = datetime.datetime.now()
    DoW = int(dt.strftime("%w"))
    time24 = int(dt.strftime("%H%M"))
    if DoW == 0:
        return "Error: 1"  # uniSun
    elif DoW == 6:
        return "Error: 2"  # uniSat
    else:
        while True:
            if time24 not in uniWeekday:
                time24 += 1
            else:
                response = (str(time24)[0:2] + ":" + str(time24)[2:4])
                return response


uniWeekday = [1708, 1738, 1808, 1838, 1914, 2014, 2114, 2239]
uniSat = []
uniSun = []
leamWeekday = [1743, 1813, 1841, 1911, 1943, 2043, 2143, 2308]
leamSat = []
leamSun = []


if __name__ == '__main__':
    app.debug = True
    app.run()
