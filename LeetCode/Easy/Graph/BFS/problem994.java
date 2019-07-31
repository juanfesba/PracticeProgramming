class Solution {
    static class Cell{
        public int x;
        public int y;
        
        public Cell(){}
        
        public Cell(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public int orangesRotting(int[][] grid) {
        int x = grid.length;
        int y = grid[0].length;
        int freshOranges=0;
        LinkedList<Cell> queue = new LinkedList<Cell>();
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(grid[i][j]==2)queue.add(new Cell(i,j));
                if(grid[i][j]==1)freshOranges++;
            }
        }
        if (freshOranges==0)return 0;
        
        Cell[] delta={new Cell(0,1),new Cell(1,0),new Cell(0,-1),new Cell(-1,0)};
        Cell tmp=new Cell();
        int ans=0; int cx; int cy;
        int sizeQ=queue.size();
        while(!queue.isEmpty()){
            tmp=queue.pop();
            sizeQ--;
            for(Cell cell : delta ){
                cx=tmp.x+cell.x;
                cy=tmp.y+cell.y;
                if(cx>-1 && cx<x && cy>-1 && cy<y && grid[cx][cy]==1){
                    grid[cx][cy]=0;
                    freshOranges--;
                    queue.add(new Cell(cx,cy));
                    
                    if(freshOranges==0)return ans+1;
                }
            }
            if (sizeQ==0){
                sizeQ=queue.size();
                ans++;
            }
        }
        return -1;
    }
}