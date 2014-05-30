Current function: continuously calls back on predetermined IP/PORT untill it finds a listener, once connected a splat of garbage across screen(needs fix) then allows for shell interaction. The quit command exits the connection via a EOF error and implant goes back into continuous callback behavior until a new listener of same IP/PORT pair appear again.


Todo: 
1) Add time functionality to suppress constant beacon to a predetermined amount of time.
2) Add capability to supersede hard coded IP/PORT/Interval - perhaps ENV vars?
3) Add Put/Get functionality to allow for quick upload download capability
4) Add SSL wrapper for encryption / test with exploit/multi/https/handler 
5) Attempt to better handle exploit/multi/hander preamble rather than ignoring it (Research)
6) Add capability to both forward and reverse tunnel (Research)
7) Add a call in method for when we need that.
8) Brainstorm alternate ways of hard codding IP, (function that create random urls?)
9) Brainstorm alternate ways to supersede hard coded vars, (file, env vars, memory?)
10) Brainstorm alternate callback methods, (random times, example 189-234 seconds)
11) Brainstorm alternate protocols besides HTTP/HTTPS - perhaps not needed atm.
12) Research methods of Python to DLL, or PowerPoint exe in memory, exe as service