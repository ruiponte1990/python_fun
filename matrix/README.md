Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.

Input  
 1  2  3  
 4  5  6  
 7  8  9  

Output:  
 3  6  9  
 2  5  8  
 1  4  7  

Input:  
 1  2  3  4  
 5  6  7  8  
 9 10 11 12  
13 14 15 16  

Output:  
 4  8 12 16  
 3  7 11 15  
 2  6 10 14  
 1  5  9 13  

My fun way of just cycling along the outside and recursing in: matrix.py (works how you think it should look)  

Canonical way where you reverse order of rows and take transpose: matrix_canon.py
