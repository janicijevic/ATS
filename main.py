'''

Recieve MAVLink packets from QGroundControl forwarding
'''
from pymavlink import mavutil

connection_string = 'udp:localhost:14551' 
master = mavutil.mavlink_connection(connection_string)

while True:
    try:
        message = master.recv_match(type='GPS_RAW_INT', blocking=True)
        if message:
            print(f"Time: {message.time_usec}")
            print(f"Fix Type: {message.fix_type}")
            print(f"Latitude: {message.lat / 1e7}")
            print(f"Longitude: {message.lon / 1e7}")
            print(f"Altitude: {message.alt / 1000.0} meters")
    except Exception as e:
        print(f"Error: {e}")
        break