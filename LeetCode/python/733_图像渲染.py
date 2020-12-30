class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        self.fill(image, sr, sc, oldColor, newColor)
        return image
    def fill(self, image, x, y, oldColor, newColor):
        if x<0 or x>=len(image) or y<0 or y>=len(image[0]):
            return
        if image[x][y] != oldColor:
            return
        if image[x][y] == -1:
            return
        image[x][y] = -1
        self.fill(image, x+1, y, oldColor, newColor)
        self.fill(image, x-1, y, oldColor, newColor)
        self.fill(image, x, y+1, oldColor, newColor)
        self.fill(image, x, y-1, oldColor, newColor)
        image[x][y] = newColor