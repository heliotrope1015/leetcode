import numpy as np
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        global count
        count=0
        grid=np.array(grid)
        sx = np.argwhere(grid == 1)[0][0]
        sy = np.argwhere(grid == 1)[0][1]
        start=(sx,sy)
        tx=np.argwhere(grid == 2)[0][0]
        ty = np.argwhere(grid == 2)[0][1]
        target=(tx,ty)
        # print tx,ty,sx,sy
        h=grid.shape[0]
        w=grid.shape[1]
        # print w,h
        def findpath((x,y)):
            pathlist = []
            if x-1>=0  and (grid[x-1][y]==0 or grid[x-1][y]==2) :
                pathlist.append((x-1,y))
            if y-1>=0 and (grid[x][y-1]==0 or grid[x][y-1]==2):
                pathlist.append((x,y-1))
            if x+1<h  and (grid[x+1][y]==0 or grid[x+1][y]==2):
                pathlist.append((x+1,y))
            if y+1<w and (grid[x][y+1]==0 or grid[x][y+1]==2):
                pathlist.append((x,y+1))
            return pathlist
        def select((x,y)):
            global count
            # print  str(step)+" "+str(np.argwhere(grid == 0))
            if target==(x,y) and str(np.argwhere(grid == 0))=='[]':
                count+=1

                return
            # pathlists[step]=findpath((x,y))
            for path in findpath((x,y)):
                grid[path[0]][path[1]]=1
                select(path)
                grid[path[0]][path[1]]=0
        select(start)
        return count



if __name__ == '__main__':
    grid=[[0,1],[2,0]]
    ans = Solution().uniquePathsIII(grid)
    print ans