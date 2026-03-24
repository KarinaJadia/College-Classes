class Point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        pass

    def __lt__ (self, other):
        """
        checks if the first point is less than the second point
        returns true if first point is less than second point
        """
        return self.dist_from_origin() < other.dist_from_origin()
    
    def __gt__ (self, other):
        """
        checks if the first point is greater than the second point
        returns true if first point is greater than second point
        """
        return self.dist_from_origin() > other.dist_from_origin()

    def __eq__ (self, other):
        """
        checks if the first point is equal to the second point
        returns true if first point is equal to second point
        """
        return self.dist_from_origin() == other.dist_from_origin()
    
    def __str__ (self):
        """
        returns a string of the point in the form "Point(x,y)"
        """
        return f'Point({self.x}, {self.y})'
    
    def dist_from_origin(Point):
        """
        uses the pythagorean theorem to find the distance from the origin (or the hypotenuse)
        """
        dist = ((Point.x)**2 + (Point.y)**2)**(1/2) # pythagorean theorem-ed it
        return dist



if __name__ == '__main__':
    p1 = Point(3,4) # dist = 5.0
    p2 = Point(5,6) # dist = 7.810249675906654
    p3 = Point(2,3) # dist = 3.605551275463989
    p4 = Point(1,5) # dist = 5.0990195135927845
    p5 = Point(3,4) # dist = 5.0
    
    ##### test init #####
    assert p1.x == 3 # expected true
    assert p1.y == 4 # expected true
    assert not(p2.x == 6) # expected false

    ##### test lt #####
    assert p1 < p2 # expected true
    assert not(p2 < p1) # expected false

    ##### test gt #####
    assert not (p1 > p4) # expected false
    assert p2 > p3 # expected true

    ##### test eq #####
    assert not(p1 == p2) # expected false
    assert p1 == p5 # expected true
    
    ##### test str #####
    assert str(p1) == 'Point(3, 4)' # expected true
    assert not(str(p3) == 'Point(3, 2)') # expected false

    ##### test dist_from_origin() #####
    assert p1.dist_from_origin() == 5.0 # expected true
    assert not(p3.dist_from_origin() == 3.6) # expected false