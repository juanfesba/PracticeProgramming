class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Comparator<int[]> compare = new Comparator<int[]>(){
            @Override
            public int compare(int[] a,int[] b){
                return (int)Math.pow(a[0],2)+(int)Math.pow(a[1],2)-
                    (int)Math.pow(b[0],2)-(int)Math.pow(b[1],2);
            }
        };
        PriorityQueue<int[]> minHeap = new 
            PriorityQueue<int[]>(points.length+1,compare);
        for(int i=0;i<points.length;i++)minHeap.add(points[i]);
        
        int[][] ans=new int[K][2];
        for(int i=0;i<K;i++){
            ans[i]=minHeap.poll();
        }
        return ans;
    }
}