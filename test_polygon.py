import pytest
from polygon import Polygon


def test_create_polygon_with_invalid_sides():

    with pytest.raises(ValueError) as execinfo:
        p = Polygon(-2, 10)
    
    with pytest.raises(ValueError) as execinfo:
        p = Polygon(0, 10)
    
    with pytest.raises(ValueError) as execinfo:
        p = Polygon(2, 10)

def test_create_polygon_with_invalid_circum_radius():

    with pytest.raises(ValueError) as execinfo:
        p = Polygon(3, -10)
    
    with pytest.raises(ValueError) as execinfo:
        p = Polygon(5, 0)
    

def test_create_polygon_with_valid_params():
    p = Polygon(5, 10)
    assert p.num_of_edges == 5, "Polygon object is created incorrectly the num_of_edges is not equal to the value passed"

    assert p.num_of_vertices == 5, "Polygon object is created incorrectly the num_of_vertices is not equal to the num_of_edges"

    assert p.circum_radius == 10, "Polygon object is created incorrectly the circum_radius is not equal to the circum_radius passed"

def test_len_of_polygon_sequence():
    p = Polygon(5, 10)

    assert p.interior_angle == 108, "Polygon object interior angle is computed incorrectly"
    assert round(p.edge_length, 4) == 11.7557, "Polygon object edge length is computed incorrectly"
    assert round(p.apothem, 4) == 8.0902, "Polygon object apothem is computed incorrectly"
    assert round(p.area, 4) == 237.7641, "Polygon object area is computed incorrectly"
    assert round(p.perimeter,4) == 58.7785, "Polygon object perimeter is computed incorrectly"

def test_polygon_repr():
    p = Polygon(5,10)

    p_repr = p.__repr__()

    assert "Num of Edges" in p_repr , "The representation of the polygon object does not contain the Num Of Edges"
    assert "Num of Vertices" in p_repr , "The representation of the polygon object does not contain the Num Of Vertices"
    assert "interior_angle" in p_repr , "The representation of the polygon object does not contain the interior_angle"
    assert "edge_length" in p_repr , "The representation of the polygon object does not contain the edge_length"
    assert "apothem" in p_repr , "The representation of the polygon object does not contain the apothem"
    assert "area" in p_repr , "The representation of the polygon object does not contain the area"
    assert "perimeter" in p_repr , "The representation of the polygon object does not contain the perimeter"
    
def test_polygon_equality_with_other_than_polygon_obj():
    p = Polygon(5, 10)

    with pytest.raises(TypeError) as execinfo:
        result = p + 5
    
    with pytest.raises(TypeError) as execinfo:
        result = p + (1,2,3)
    
    with pytest.raises(TypeError) as execinfo:
        result = p + [1,2,3]
    
def test_polygon_equality_with_polygon_obj():
    p1 = Polygon(5, 10)

    p2 = Polygon(6, 20)

    p3 = Polygon(5, 10)
    
    assert p1 != p2, "Polygon equality is not working as expected"

    assert p1 == p3, "Polygon equality is not working as expected"

def test_comparing_polygon_with_other_than_polygon_obj():
    p = Polygon(5, 10)

    with pytest.raises(TypeError) as execinfo:
        p > 5
    
    with pytest.raises(TypeError) as execinfo:
        p > (1,2,3)
    
    with pytest.raises(TypeError) as execinfo:
        p > [1,2,3]

def test_comparing_polygon_with_polygon_obj():
    p1 = Polygon(5, 10)

    p2 = Polygon(8, 10)

    assert p2 > p1, "Polygon Comparison is not working as expected"
