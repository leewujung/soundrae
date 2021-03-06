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
        while self.running = True
        self.gpsd.next()

    def stopController(self):
        self.running = False

    @property
    def fix(self):
        return self.gpsd.fox

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
                print "latitude ", gpsc.fix.latitude
                print "longitude ", gpsc.fix.longitude
                print "time utc ", gpsc.utc, " + ", gpsc.fix.time
                print "altitude (m)", gpsc.fix.altitude
                print "eps ", gpsc.fix.eps
                print "epx ", gpsc.fix.epx
                print "epv ", gpsc.fix.epv
                print "ept ", gpsc.gpsd.fix.ept
                print "speed (m/s) ", gpsc.fix.speed
                print "climb ", gpsc.fix.climb
                print "track ", gpsc.fix.track
                print "mode ", gpsc.fix.mode
                print "sats ", gpsc.satellites
                time.sleep(0.5)

        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

        except KeyboardInterrupt:
            print "User cancelled"

        finally:
            print "Stopping gps controller"
            gpsc.stopController()
            gpsc.join()

        print "Done"
