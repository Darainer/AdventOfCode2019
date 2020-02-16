represent the asteroid as a 2x2 grid (random access)
grid element is just binary IsAsteroid here
parse the input into a 2x2 grid format

create a 2d array/list for storing the viewing score of each element
    that can be done dynamically... list.append()

list of asteroids - can be sorted by distance to a specific point

Algorithm:
for each map position
1. Is asteroid here? -> can only put monitoring stations where asteroids are

If yes
Run routine
1. create a 2D map of visible/blocked positions from the station

2. sort all asteroids by distance to the potential station. 
can use the taxicab distance from day3 to ensure right order of processing

3. Process all asteroids in the list with iterator

If asteroid position is not Blocked

    1. add to the counter of visable asteroids from station
    2. calculate which grid points are obscured behind that asteroid
    (extend the line from the station to the asteroid until end of map)
    slope (y/x) - next integer match is blocked
    3. Update the blocked map for that monitoring station 
    
4  return counter of visable asteroids from this station
   
