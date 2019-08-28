

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """

    if(a <= 0 or b<=0 or c<= 0):
        return "NotATriangle"
    if((a + b <= c) or (a + c <= b) or (b + c <= a)):
        return "NotATriangle"
    if a == b == c: 
        return 'Equilateral'
    elif (a == b and b != c) or (a != b and b == c):
        return 'Isoceles'
    elif((a**2+b**2 == c**2) or (a**2+c**2 == b**2) or (b**2+c**2 == a**2)):
        return 'Right'
    else:
        return 'Scalene'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


class TestTriangles(unittest.TestCase):

    def testSet1(self): 
        #assert Equal tests
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(20,25,30),'Scalene')
        self.assertEqual(classifyTriangle(20,20,30),'Isoceles')
        self.assertEqual(classifyTriangle(0,0,0),'NotATriangle')

        
    def testMyTestSet2(self): 
        #assert NotEqual tests
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertNotEqual(classifyTriangle(6,8,10),'Scalene','Should be Right')
        self.assertNotEqual(classifyTriangle(10,10,40),'Isoceles','Should be NotATriangle')

        

if __name__ == '__main__':

    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    

    unittest.main(exit=True) 
