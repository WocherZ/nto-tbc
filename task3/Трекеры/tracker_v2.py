import math
from client2server import client2server


class tracker:
    def run(tracklog):
        try:
            c2s = client2server()
            MEM = [0 for i in range(10)]
            head = 0
            lt = 0
            dt = 1
            i = 0  #                                                                    26%
            P = 0.8  # 0.2, 0.2, 0.4, 0.4, 0.8, 0.4, 0.4, 0.8
            D = 2.8  # 0.3, 0.8, 1.6, 0.7, 3.2, 3.2, 0.8, 3.2
            C = 20  #
            R = 72
            Rp = 1500  # 3000 2200 1310
            P = 200  # 274 200 120
            k = 11
            mspeed = 69
            while i == 0:
                status = c2s.getStatus()
                dx = int(status) & 0x0fff
                time = int(status) >> 20 & 0x01ffff
                if time != lt:
                    dt = time - lt
                    lt = time
                absolut = int(status) >> 76 & 0x01fff
                tracklog.write(f"Time {time}\tAbs {absolut}\t".encode())
                if (dx > 2048):
                    dx = dx - 4096
                MEM[head] = int(dx)
                head = (head + 1) % 10
                tracklog.write("Received {} \t".format(dx).encode())
                if (abs(int(dx)) < 1000):  # тут было 500!!!!!
                    error = dx * P + (dx - MEM[head-1]) * D
                    speed = error
                    if (abs(int(dx)) < 9):
                        c2s.moveStop()
                        tracklog.write("Speed 0\t".encode())
                    elif abs(int(dx)) < 20:
                        speed = abs(int(dx)) - 5
                        tracklog.write("Speed {}\t".format(speed).encode())
                        if (int(dx) > 0):
                            speed = min(speed, mspeed)
                            c2s.moveLeft(speed)
                        else:
                            speed = min(abs(speed), mspeed)
                            c2s.moveRight(abs(speed))
                    else:
                        speed = math.sin(2*math.pi*k/R*dx)*2*math.pi*k
                        tracklog.write(f"Speed {speed}\t".encode())
                        if (dx > 0):
                            speed = min(speed, mspeed)
                            c2s.moveLeft(speed)
                        else:
                            speed = min(abs(speed), mspeed)
                            c2s.moveRight(abs(speed))
                else:
                    tracklog.write("TooFar".encode())
                tracklog.write("\n".encode())
        except Exception as e:
        	tracklog.write(f'{type(e)} {e}'.encode())
Закрыть
