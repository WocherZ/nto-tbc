from client2server import client2server

def get_speed_by_dx(dx):
    if 1 < abs(dx) < 10:
        return 6
    elif 10 <= abs(dx) < 50:
        return 8
    elif 50 <= abs(dx) <= 300:
        return 12
    else:
        return 20


class tracker:
  def run(tracklog):
      # dx_history = []

      c2s = client2server()
      i = 0
      while i == 0:
          status = c2s.getStatus()
          dx = int(status) & 0x0fff
          if dx > 2048:
              dx = dx - 4096

          tracklog.write(f"{dx}".encode())

          # dx_history.append(dx)


          if abs(dx) < 500:
              if abs(dx) < 5:
                  c2s.moveStop()
              else:
                  speed = get_speed_by_dx(dx)
                  if dx > 0:
                      c2s.moveLeft(speed)
                  else:
                      c2s.moveRight(speed)
