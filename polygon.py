import math

class Polygon(object):
    def __init__(self, num_of_edges: "Number of edges", circum_radius: "Circum radius"):
        """ 
            Initializes a Polygon object by taking Number of edges and Circum-radius as args.
        """
        if num_of_edges < 3 or circum_radius <= 0:
            raise ValueError("Invalid properties passed. Edges cannot be less than 3, Circum-radius cannot be less than 0.")
        self.num_of_edges = int(num_of_edges)
        self.num_of_vertices = int(num_of_edges)
        self.circum_radius = int(circum_radius)
        self.interior_angle = (self.num_of_edges - 2) * 180 / self.num_of_edges
        self.edge_length = 2 * circum_radius * (math.sin(math.pi / self.num_of_edges))
        self.apothem = circum_radius * math.cos(math.pi / self.num_of_edges)
        self.area = 0.5 * num_of_edges * self.edge_length * self.apothem
        self.perimeter = self.num_of_edges * self.edge_length

    def __repr__(self):
        """ 
            Representation of Object of the class Polygon with its properties.
        """
        return f""" A Polygon Object with the properties: 
         - Num of Edges : {self.num_of_edges}
         - Num of Vertices : {self.num_of_vertices}
         - interior_angle : {self.interior_angle}
         - edge_length : {self.edge_length}
         - apothem : {self.apothem}
         - area : {self.area}
         - perimeter : {self.perimeter}"""

    def __eq__(self, polygon_obj: "An object of class polygon") -> bool:
        """
            CHECKS FOR THE EQUALITY OF TWO POLYGON OBJECTS BASED ON CIRCUM-RADIUS AND # VERTICES.
            Throws TypeError if the object is not of Polygon class
        """
        if type(polygon_obj) != type(self):
            raise TypeError("EQUALS - Operation not possible")

        if self.num_of_vertices == polygon_obj.num_of_vertices and self.circum_radius == polygon_obj.circum_radius:
            return True
        else:
            return False
    
    def __gt__(self, polygon_obj2: "Object of class Polygon") -> bool:
        """
            GREATER THAN OPERATION FOR THE POLYGON OBJECTS BASED ON THEN # VERTICES
            Throws TypeError if the object is not of Polygon class
        """
        if type(polygon_obj2) != type(self):
            raise TypeError("GT - Operation not possible")
        if self.num_of_vertices > polygon_obj2.num_of_vertices:
            return True
        else:
            return False