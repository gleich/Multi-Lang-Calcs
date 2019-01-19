def triangles_classification(angles):
    if angles[0] == 90 or angles[1] == 90 or angles[2] == 90: #If one of the angles are 90 degrees
        print ("Triangle is a right triangle")
    elif angles[0] >= 120 or angles[1] >= 120 or angles[2] >= 120: #If one of the angles are obtuse (more than 120 degrees)
        print ("Triangle is a obtuse triangle")
    elif angles[0] == angles[1] or angles[0] == angles[3]: #If two are the angles are the same
        print ("Triangle is a isosceles triangle")
    elif angles[0] == 60 and angles[1] == 60 and angles[2] == 60:
        print ("Triangle is a equilateral triangle")
    else:
        print ("Didn't work")

#Examples
triangles_classification([60,60,60]) #This is a equilateral triangle
triangles_classification([45,45,90]) #This is a  right triangle 
