# Session 11 EPAI 3 Assignment

Here is the Google Colab link where various operations on the PolygonsIterator have been showcased - 
https://colab.research.google.com/drive/1WBiUHKWihnEuKMsFQcuPffVZ3yoNzi2n?usp=sharing

## Polygon class

The Polygon Class of the previous assignment is used without any changes and the test_polygon is also used from the previous assignment which tests the polygon class.

## Polygons Class

The Polygons Class from the previous assignment is refactored and converted into an iterable and an Iterator class is added to the class too.

As the Polygons Class has the ```__getitem__``` method, it acts both as a sequence type and iterable now.

The methods added to the Polygons Class:

### __iter__ method

Adding a ```__iter__``` method makes the Polygons Class an iterable, and we seperated out the Iterator logic into another class called PolygonsIterator and we are returning a new instance of the PolygonsIterator everytime ```__iter__``` is called

## PolygonsIterator Class

This is the iterator for the Polygons Class which contains 2 fields:

- _polygons_obj - This is the polygons object on which we the iterator acts upon
- _index        - This field contains the current index at which the iterator is upon

### __init__ method

This is the constructor of the PolygonsIterator class which takes the iterable object i.e. the instance of the Polygons Class,
on which this iterator iterates

It initializes the _index field to 0

### __iter__ method

This is an iterator instance hence it returns the self object itself when the ```__iter__``` is called.

### __next__ method

This method returns the next object in the iterable using the ```__getitem__``` function of Polygons class and the current _index value in the object
and raises a StopIteration Exception once the iterator is exhausted 

Before returning the object in the iterable it increments the _index value so that the next call to this function returns the next object

### Tests for the Iterator and Iterable

In test_polygons file the tests from previous assignment are there testing the Polygons Sequence Type nature, and 4 Tests have been added to it to test the Iterable and the Iterator.

- ```test_polygon_iterator_type``` - Tests if iter of Polygons object is returning an instance of PolygonsIterator
- ```test_polygon_iter_method_returning_new_iterator``` - Tests if iter of Polygons Object is returning a new instance of PolygonsIterator everytime
- ```test_polygon_iterator_next_method``` - Tests if the next method of the PolygonsIterator is working as an Iterator
- ```test_polygon_iterator_raising_stop_iteration``` - Tests if a StopIteration exception is raised once the iterator instance is exhausted.

