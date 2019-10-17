#include <bits/stdc++.h>
using namespace std;
#define MAXSIZE 10
int N;

int minDistance(int dist[], bool sptSet[])
{
   int min = INT_MAX, min_index;
  
   for (int v = 0; v < N; v++)
     if (sptSet[v] == false && dist[v] <= min)
         min = dist[v], min_index = v;
  
   return min_index;
}
  

void dijkstra(int N,int graph[][10], int src)
{
	int dist[N];
	bool sptSet[N];
	for (int i = 0; i < N; i++)
        dist[i] = INT_MAX, sptSet[i] = false;
   	dist[src] = 0;
   	for (int count = 0; count < N-1; count++)
    {
       	int u = minDistance(dist, sptSet);
  		sptSet[u] = true;
  		for (int v = 0; v < N; v++)
  		 {
  		 	if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u]+graph[u][v] < dist[v])
            			dist[v] = dist[u] + graph[u][v];
       		}
     }
 	cout << "Vertex   Distance from Source"<<endl;
   	for (int i = 0; i < N; i++)
      		cout << i << "\t"<< dist[i] << endl;
}

int main()
{
	int e,i,j,c,n,src;
	cout << "Enter the required number of nodes for the network :";
	cin >> N;
	int g[10][10]={{0}};
	//memset(g,0,sizeof(g));
	
	cout << "Enter the total no.of edges(connections) between the nodes ";
	cin >> e;
	n=e;
	cout<<"Enter the nodes involved in the edge and the distance between them \n ";
	while(n--)
	{
		cout << "Enter the node pair: ";
		cin >> i >> j;
		cout << "Enter the respective distance between them ";
		cin >> c;
		g[i][j]=c;
		g[j][i]=c;
	}
	cout<<"The distance matrix is ";
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			cout << g[i][j] << " ";
		}
		cout << endl;
	}
	for(i=0;i<N;i++)
	{
		cout << "Source :"<<i<<endl;
		dijkstra(N,g,i);
	}
	return 0;
}
