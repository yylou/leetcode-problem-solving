class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #: (base case)
        if len(grid) == 1 and len(grid[0]) == 1: return 1 if grid[0][0] == "1" else 0
        
        # ==================================================
        #  BFS                                             =
        # ==================================================
        # time  : O(nm)
        # space : O(min(n,m))
        
        x = len(grid[0])
        y = len(grid)
        
        ans = 0
        
        for i in range( y ):
            for j in range( x ):
                if grid[i][j] == '1':
                    ans += 1
                    
                    visited = set()
                    visited.add( (i, j) )
                    
                    while visited:
                        row, col = visited.pop()
                        grid[row][col] = '0'
                        
                        if row   > 0 and grid[row-1][col] == '1': visited.add( (row-1, col) )
                        if row+1 < y and grid[row+1][col] == '1': visited.add( (row+1, col) )
                        if col   > 0 and grid[row][col-1] == '1': visited.add( (row, col-1) )
                        if col+1 < x and grid[row][col+1] == '1': visited.add( (row, col+1) )
                            
        return ans
        
        '''
        # ==================================================
        #  DFS                                             =
        # ==================================================
        # time  : O(nm)
        # space : O(nm)
        
        def explore(row, col):
            grid[row][col] = 0
            
            if row > 0              and grid[row-1][col] == '1': explore(row-1, col)
            if row < len(grid)-1    and grid[row+1][col] == '1': explore(row+1, col)
            if col > 0              and grid[row][col-1] == '1': explore(row, col-1)
            if col < len(grid[0])-1 and grid[row][col+1] == '1': explore(row, col+1)
            
        ans = 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    explore(i, j)
                    
        return ans
        '''
        
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(nm)
     * @space : O(nm)
     */

    public int numIslands(char[][] grid) {
        int count = 0;
        
        for(int i=0 ; i<grid.length ; i++) {
            for(int j=0 ; j<grid[0].length ; j++) {
                if(grid[i][j] == '1') {
                    count++;
                    explore(grid, i, j);
                }
            }
        }
        
        return count;
    }
    
    public void explore(char[][] grid, int x, int y) {
        if(x<0 || y<0 || x>= grid.length || y>= grid[0].length) {
            return;
        }
        
        if(grid[x][y] == '0') {
            return;
        }
        
        grid[x][y] = '0';
        
        explore(grid, x-1, y);
        explore(grid, x+1, y);
        explore(grid, x,   y-1);
        explore(grid, x,   y+1);
        
        return;
    }
}
==================================================================================================
'''
