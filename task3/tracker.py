from client2server import client2server


# LEFT_FANCE_BORDERS = (750, 900)
# RIGHT_FANCE_BALANCE = (1075, 1200)

def parse_status(status):
    dx = int(status) & 0b111111111111 # 0 - 11
    if dx >= 2048:
        dx = dx - 4096

    radar_status = int(status) >> 12 & 0b1111  # 12 - 15
    radar_position = int(status) >> 16 & 0b1111  # 16 - 19
    timestatus = int(status) >> 20 & 0b1111111111111111  # 20 - 36
    radar_coord = int(status) >> 76 & 0b1111111111111 # 76 - 88

    result_status = {
        'dx': dx,
        'radar_status': radar_status,
        'radar_position': radar_position,
        'timestatus': timestatus,
        'radar_coord': radar_coord
    }

    return result_status

MAX_VALUE_SPEED = 100

def get_speed_by_dx(dx):
    k = 0.1
    abs_dx = abs(dx)

    if abs_dx < 10:
        k = 0.2
    elif abs_dx < 50:
        k = 0.4
    elif abs_dx < 100:
        k = 0.6
    else:
        k = 0.8

    if abs_dx > 500:
        k = 1

    return int(MAX_VALUE_SPEED * k)



class tracker:
  def run(tracklog):
      abs_x = 0

      coords = [0]
      dx_history = [0]

      c2s = client2server()
      i = 0
      while i == 0:
          status = c2s.getStatus()

          current_status = parse_status(status)

          dx = current_status.get('dx')
          radar_status = current_status.get('radar_status')
          radar_position = current_status.get('radar_position')
          timestatus = current_status.get('timestatus')
          radar_coord = current_status.get('radar_coord')

          tracklog.write(f"{dx}\n".encode())
          tracklog.write(f"{radar_status}\n".encode())
          tracklog.write(f"{radar_position}\n".encode())
          tracklog.write(f"{timestatus}\n".encode())
          tracklog.write(f"{radar_coord}\n".encode())
          tracklog.write(f"\n".encode())




          # Режим слежения спутника за зеркалами
          # if LEFT_FANCE_BORDERS[0] <= radar_coord <= LEFT_FANCE_BORDERS[1]:
          #     if radar_coord - coords[-1] <= 0 and dx > 0:
          #       c2s.moveLeft(MAX_VALUE_SPEED * 0.8)
          #     elif radar_coord - coords[-1] >= 0:
          #         c2s.moveRight(MAX_VALUE_SPEED * 0.5)
          # elif RIGHT_FANCE_BALANCE[0] <= radar_coord <= RIGHT_FANCE_BALANCE[1]:
          #     if radar_coord - coords[-1] >= 0 and dx < 0:
          #       c2s.moveRight(MAX_VALUE_SPEED * 0.8)
          #     elif radar_coord - coords[-1] <= 0:
          #         c2s.moveLeft(MAX_VALUE_SPEED * 0.5)

          # else:
          if abs(dx) < 5000:
              if abs(dx) < 10:
                  c2s.moveStop()
              else:
                  speed = get_speed_by_dx(dx)
                  if dx > 0:
                      c2s.moveLeft(speed)
                  else:
                      c2s.moveRight(speed)


          # coords.append(radar_coord)
          # dx_history.append(dx)