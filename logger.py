#-*- coding:utf-8 -*-

import time

class Logger:
        DEBUG        = "DEBUG"
        INFO         = "INFO"
        ERROR        = "ERROR"
        Level            = INFO

        def print_out(self ,level , msg):
                localtime = time.localtime()
                y = localtime.tm_year
                mon = localtime.tm_mon
                d = localtime.tm_mday
                h = localtime.tm_hour
                m = localtime.tm_min
                s =  localtime.tm_sec

                if int(mon) < 10:
                        mon = "0"+str(mon)
                if int(d) < 10:
                        d = "0"+str(d)
                if int(h) < 10:
                        h = "0"+ str(h)
                if int(m) < 10:
                        m = "0"+ str(m)
                if int(s) < 10:
                        s = "0"+ str(s)

                fmt_time = "%s-%s-%s %s:%s:%s" % (y , mon , d , h , m , s)
                log = "%s %s %s" %(fmt_time , level , msg)
                print log

        def info(self , msg):
                if Logger.Level == Logger.INFO or Logger.Level == Logger.DEBUG:
                        self.print_out(Logger.INFO , msg)

        def debug(self , msg):
                if Logger.Level == Logger.DEBUG:
                        self.print_out(Logger.DEBUG , msg)

        def error(self , msg):
                if Logger.Level == Logger.ERROR \
                                or Logger.Level == Logger.DEBUG or Logger.Level == Logger.INFO:
                        self.print_out(Logger.ERROR , msg)

if __name__ == "__main__":
        print "Logger.Level=%s " % Logger.Level
	logger = Logger()
	logger.info("test print log")

