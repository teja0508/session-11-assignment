import pytest
from polygon import Polygon
from polygons import Polygons


def test_create_polygon_sequence_with_invalid_max_number_of_vertices():

    with pytest.raises(ValueError) as execinfo:
        p = Polygons(-2, 10)
    
    with pytest.raises(ValueError) as execinfo:
        p = Polygons(0, 10)
    
    with pytest.raises(ValueError) as execinfo:
        p = Polygons(2, 10)

def test_create_polygon_sequence_with_with_invalid_circum_radius():

    with pytest.raises(ValueError) as execinfo:
        p = Polygons(10, -10)
    
    with pytest.raises(ValueError) as execinfo:
        p = Polygon(5, 0)
    

def test_create_polygon_sequence_with_valid_params():
    p = Polygons(5, 10)
    assert p.max_num_of_vertices == 5, "Polygon Sequence object is created incorrectly the max_num_of_vertices is not equal to the value passed"

    assert p.circum_radius == 10, "Polygon Sequence object is created incorrectly the circum_radius is not equal to the circum_radius passed"

    assert isinstance(p[0], Polygon), "Items in the sequence are of type Polygon"

    assert p[0].num_of_edges == 3, "First item in "

def test_polygon_sequence_length():
    p1_seq = Polygons(5, 10)
    p2_seq = Polygons(8, 10)
    assert len(p1_seq) == 3, "Length of the Polygon Sequence is not working as expected"
    assert len(p2_seq) == 6, "Length of the Polygon Sequence is not working as expected"

def test_polygon_sequence_repr():
    p_seq = Polygons(5,10)

    p_repr = p_seq.__repr__()

    assert "length_of_the_sequence" in p_repr , "The representation of the polygon sequence object does not contain the Length of the sequence"
    assert "max_num_of_vertices" in p_repr , "The representation of the polygon sequence object does not contain the max_num_of_vertices"
    assert "circum_radius" in p_repr , "The representation of the polygon sequence object does not contain the circum_radius"
    assert "max_efficiency_polygon" in p_repr , "The representation of the polygon sequence object does not contain the max_efficiency_polygon"
    
def test_polygon_sequence_list():
    p1 = Polygons(8, 10)

    assert type(list(p1)) == list, "List could not be created from the Polygon Sequence"

    assert p1[2].num_of_vertices == 5, "Polygon object in the sequence does not have the expected num_of_vertices"
    
def test_polygon_sequence_max_efficiency_polygon():
    p1 = Polygons(3, 10)

    p2 = Polygons(5, 10)

    assert p1.max_efficiency_polygon() == 3, "Polygon Sequence max efficiency Polygon is not working as expected"

    assert p2.max_efficiency_polygon() == 5, "Polygon Sequence max efficiency Polygon is not working as expected"

def test_polygon_sequence_max():

    p1 = Polygons(7, 10)

    assert max(p1).num_of_vertices == 7, "Max operation on the Polygon sequence in not working as expected"


def test_polygon_sequence_min():

    p1 = Polygons(7, 10)

    assert min(p1).num_of_vertices == 3, "Min operation on the Polygon sequence in not working as expected"

def test_polygon_iterator_type():
    
    p1 = Polygons(7, 10)

    p1_iter = iter(p1)

    assert type(p1_iter) == Polygons.PolygonsIterator

def test_polygon_iter_method_returning_new_iterator():
    p1 = Polygons(7, 10)

    p1_iter = iter(p1)

    p2_iter = iter(p1)

    assert id(p1_iter) != id(p2_iter), "Polygons Iterable returning same iterator instance every time"

def test_polygon_iterator_next_method():
    p1 = Polygons(7, 10)

    p1_iter = iter(p1)

    polygon1 = next(p1_iter)
    polygon2 = next(p1_iter)
    polygon3 = next(p1_iter)
    polygon4 = next(p1_iter)
    polygon5 = next(p1_iter)

    assert polygon1.num_of_vertices == 3, "Polygons Iterator is not working as expected"
    assert polygon2.num_of_vertices == 4, "Polygons Iterator is not working as expected"
    assert polygon3.num_of_vertices == 5, "Polygons Iterator is not working as expected"
    assert polygon4.num_of_vertices == 6, "Polygons Iterator is not working as expected"
    assert polygon5.num_of_vertices == 7, "Polygons Iterator is not working as expected"
    

def test_polygon_iterator_raising_stop_iteration():
    p1 = Polygons(4, 10)

    p1_iter = iter(p1)

    next(p1_iter)
    next(p1_iter)
    
    with pytest.raises(StopIteration) as execinfo:
        next(p1_iter)
    
    p2 = Polygons(5, 10)

    p2_iter = iter(p2)

    next(p2_iter)
    next(p2_iter)
    next(p2_iter)

    with pytest.raises(StopIteration) as execinfo:
        next(p2_iter)
    




