def floodFill(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    m = len(image)
    n=len(image[0])
    originalColor = image[sr][sc]

    if originalColor==color:
        return image
    
    def dfs(row,col):
        if(row<0 or row >= m or col< 0 or col >= n or image[row][col] != originalColor):
            return 
        
        image[row][col] = color
        dfs(row+1,col)
        dfs(row-1,col)
        dfs(row,col+1)
        dfs(row,col-1)

    dfs(sr,sc)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]

sr = 1
sc = 1
color = 2

print(floodFill(image,sr,sc,color))