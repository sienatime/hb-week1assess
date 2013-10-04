from nose.tools import *
from skills1 import skills1

ten_numbers = range(0,10)
buncha_numbers = [1,1,5,3,2,7,8,10,31,2,2,31,55,68,1324]
numbaz = [4,5,1,3,-5,0]
words = ["hambone","siena","cat","hackbright","awesome","fish","two"]
small_num = [1,3,5,1]

# assert_equal(skills1.FUNCTION(PARAM), [])

def setup():
    pass 

def teardown():
    print "TEAR DOWN!"

def test_all_odd():
    assert_equal(skills1.all_odd(ten_numbers), [1,3,5,7,9])
    assert_equal(skills1.all_odd(buncha_numbers), [1,1,5,3,7,31,31,55])

def test_all_even():
    assert_equal(skills1.all_even(ten_numbers), [0,2,4,6,8])
    assert_equal(skills1.all_even(buncha_numbers), [2,8,10,2,2,68,1324])

def test_long_words():
    assert_equal(skills1.long_words(words), ["hambone","siena","hackbright","awesome","fish"])

def test_smallest():
    assert_equal(skills1.smallest(ten_numbers), 0)
    assert_equal(skills1.smallest(buncha_numbers), 1)
    assert_equal(skills1.smallest(numbaz), -5)

def test_largest():
    assert_equal(skills1.largest(ten_numbers), 9)
    assert_equal(skills1.largest(buncha_numbers), 1324)
    assert_equal(skills1.largest(numbaz), 5)

def test_halvsies():
    assert_equal(skills1.halvesies(ten_numbers), [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5])
    assert_equal(skills1.halvesies(buncha_numbers), [0.5,0.5,2.5,1.5,1.0,3.5,4.0,5.0,15.5,1.0,1.0,15.5,27.5,34.0,662.0])
    assert_equal(skills1.halvesies(numbaz), [2.0,2.5,0.5,1.5,-2.5,0.0])

def test_word_lengths():
    assert_equal(skills1.word_lengths(words),[7,5,3,10,7,4,3])

def test_sum_numbers():
    assert_equal(skills1.sum_numbers(ten_numbers), 45)
    assert_equal(skills1.sum_numbers(buncha_numbers), 1550)
    assert_equal(skills1.sum_numbers(numbaz), 8)

def test_mult_numbers():
    assert_equal(skills1.mult_numbers(ten_numbers), 0)
    assert_equal(skills1.mult_numbers(buncha_numbers), 319780699392000L)
    assert_equal(skills1.mult_numbers(numbaz), 0)
    assert_equal(skills1.mult_numbers(small_num), 15)

def test_join_strings():
    assert_equal(skills1.join_strings(words), "hambonesienacathackbrightawesomefishtwo" )
    assert_equal(skills1.join_strings(["hello","world"]), "helloworld")

def test_average():
    assert_equal(skills1.average(ten_numbers), 4.5)
    assert_equal(skills1.average(numbaz), 1.3333333333333333)
    assert_equal(skills1.average(buncha_numbers), 103.33333333333333)