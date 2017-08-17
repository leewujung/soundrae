from gps import *
import time
import threading
import math

class GpsController(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE)
        self.running = False

    def run(self):
        self.running = True
        while self.running == True:
            self.gpsd.next()

    def stopController(self):
        self.running = False

    @property
    def fix(self):
        return self.gpsd.fix

    @property
    def utc(self):
        return self.gpsd.utc

    @property
    def satellites(self):
        return self.gpsd.satellites

if __name__ == '__main__':
    gpsc = GpsController()
    try:
        gpsc.start()
        while True:
            with open('gpsdata.txt', 'a+') as f:
                f.write("latitude: " + str(gpsc.fix.latitude) + "\n")
                f.write("longitude: " + str(gpsc.fix.longitude) + "\n")
                f.write("utc time: " + str(gpsc.utc) + "\n")
                f.write("\n")
                print "sent data at " + str(gpsc.utc)
                time.sleep(60)

    except KeyboardInterrupt:
        print "User cancelled"

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    finally:
        print "Stopping gps controller"
        gpsc.stopController()
        gpsc.join()

    print("Done")
