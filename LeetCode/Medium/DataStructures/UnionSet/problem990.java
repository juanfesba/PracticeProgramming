class Solution {
    static class HashObject{
        public HashMap<Integer,Boolean> map;
        
        public HashObject(){
            map=new HashMap<Integer,Boolean>();
            for(int i=0;i<26;i++){
                map.put(i,false);
            }
        }
    }
    static class UnionSet{
        public int[] parent;
        public int[] size;
        public int[] rank;
        public UnionSet(int nodes){
            parent=new int[nodes];
            Arrays.setAll(parent,p->p);
            size = new int[nodes];
            Arrays.fill(size,1);
            rank = new int[nodes];
            Arrays.fill(rank,1);
        }
        public int find(int x){
            if(x!=parent[x]){
                parent[x]=this.find(parent[x]);
            }
            return parent[x];
        }
        public void union(int x,int y){
            int px=this.find(x);
            int py=this.find(y);
            if(px!=py){
                int nx=rank[px];
                int ny=rank[py];
                if(nx<=ny){
                    parent[px]=py;
                    size[y]+=size[x];
                    if(nx==ny)rank[py]+=1;
                }
                else{
                    parent[py]=parent[px];
                    size[px]=size[py];
                }
            }
        }
    }
    public boolean equationsPossible(String[] equations) {
        UnionSet equal=new UnionSet(26);
        HashObject[] different=new HashObject[26];
        for(int i=0;i<26;i++)different[i]=new HashObject();
        boolean operation; String readS;
        int A,B,C;
        Set<Integer>set=new HashSet<Integer>();
        
        for(int i=0;i<equations.length;i++){
            readS=equations[i];
            if(readS.charAt(1)=='=')operation=true;
            else operation=false;
            
            A=(int)(readS.charAt(0)-'a');
            B=(int)(readS.charAt(3)-'a');
            
            A=equal.find(A);
            B=equal.find(B);
            
            
            if(operation){
                if(A==B)continue;
                if(different[A].map.get(B)==true ||
                   different[B].map.get(A)==true)return false;
                equal.union(A,B);
                C=equal.find(A);
                if(C==A){
                    set=different[B].map.keySet();
                    for(Integer diff : set)
                        different[A].map.put(equal.find(diff),
                                             different[B].map.get(diff) || 
                                             different[A].map.get(equal.find(diff)));
                }
                else{
                    set=different[A].map.keySet();
                    for(Integer diff : set)
                        different[B].map.put(equal.find(diff),
                                             different[A].map.get(diff) ||
                                             different[B].map.get(equal.find(diff)));
                }
            }
            else{
                if(A==B)return false;
                different[A].map.put(B,true);
                different[B].map.put(A,true);
            }
            
            
        }
        return true;
    }
}