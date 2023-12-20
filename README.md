# Set up packet sniffing
1. In QGroundControl go to Application settings > MAVLink, check `Enable MAVLink forwarding` and set hostname to `localhost:14551` (or whatever you want just update main.py)
2. Run main.py
3. It should be printing the information from GPS_RAW_INT packets


# Set up simulation
The simplest SITL(Software In The Loop) simulator is ArduPilot SITL. I used QGroundControl in Windows and ArduPilot on WSL.

1. Clone ArduPilot repo
```bash
git clone https://github.com/ArduPilot/ardupilot.git
cd ardupilot
git submodule update --init --recursive
```
1. Install ArduPilot Dependencies
```bash
Tools/environment_install/install-prereqs-ubuntu.sh -y
```
After installation, close the terminal and reopen it.

1. Start SITL Simulator
Navigate to the vehicle directory and start the SITL:

```bash
cd ArduCopter
../Tools/autotest/sim_vehicle.py -w
```
5. Connect to a Ground Control Station
Open QGroundControl, it should automatically connect to the SITL.
