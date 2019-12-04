# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
  def __init__(self, name, lat, lon):
    super().__init__(self, name)
    self.name = name
    self.lat = lat
    self.lon = lon
  # def __repr__(self):
  #   return self.name, self.lat, self.lon
  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
  def __init__(self, name, lat, lon, size, diff):
    super().__init__(self, size, diff)
    self.name = name
    self.lat = lat
    self.lon = lon
    self.size = size
    self.diff = diff
  def __str__(self):
    return f"name: {self.name}, lat: {self.lat}, lon: {self.lon}, size: {self.size}, diff: {self.diff}"
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint('Catacombs', 41.70505, -121.51521).__str__()

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", diff=1.5, size=2, lat=44.052137, lon=-121.41556).__str__()
# Print it--also make this print more nicely
print(geocache)
