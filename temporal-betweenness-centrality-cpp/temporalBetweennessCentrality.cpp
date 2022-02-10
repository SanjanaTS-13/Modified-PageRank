#include <boost/graph/betweenness_centrality.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <bits/stdc++.h>
#include <iostream>
#include <iterator>
#include <algorithm>

typedef boost::property<boost::edge_weight_t, int> EdgeWeightProperty;
typedef boost::adjacency_list<boost::listS, boost::vecS, boost::directedS, boost::no_property> DirectedGraph;
typedef boost::graph_traits<DirectedGraph>::edge_iterator edge_iterator;
 



using namespace std;



void printGraph(vector<int> adj[], int V)
{
    for (int v = 0; v < V; ++v) {
        cout << "\n Adjacency list of vertex " << v
             << "\n head ";
        for (auto x : adj[v])
            cout << "-> " << x;
        printf("\n");
    }
}
int main()
{
    //input the temporal graph
    //roll it out as in the paper TODO: cite paper
    //run temporal betweenness centrality algo on it from boost

    //vertices are 0 indexed
    //time is square bracketed

    //making time to be integers for ease of use
    int tMin, tMax; //starting and ending time.
    int w; //window size
    int V; //number of vertices
    int E; //number of edges
    int t; //time at which temporal centrality is required

    cin >> w >> V >> E >> tMin >> tMax;
    int W = (tMax-tMin)/w;
    vector<int> temporalGraph[W+1][V];
    int tempi, tempj, tempt;
    for(int i = 0; i < E; i++)
    {
        cin >> tempi >> tempj >> tempt;
        temporalGraph[((tempt-tMin)/w)][tempj].push_back(tempi);
        temporalGraph[((tempt-tMin)/w)][tempi].push_back(tempj);
    }


    for(int i = 0; i <= W; i++) printGraph(temporalGraph[i], V);

    //convert into rolled out directed graph
    //indexing if you want to find vertex v a time step t belongs to [0, W+1]
    //then input idx = v + (V*t)

    DirectedGraph g;
    for(int i = 0; i <= W; i++)
    {
        for (int v = 0; v < V; ++v)
        {
            boost::add_edge(v+(i*V), v+(i+1*V), g);
            for (auto x : temporalGraph[i][v])
            {
                boost::add_edge(v+(i*V), x+((i+1)*V), g);
            }
        }
    }
    std::pair<edge_iterator, edge_iterator> ei = edges(g);
 
    std::cout << "Number of edges = " << num_edges(g) << "\n";
    std::cout << "Edge list:\n";
 
    std::copy( ei.first, ei.second,
                std::ostream_iterator<boost::adjacency_list<>::edge_descriptor>{
                    std::cout, "\n"});
 
    std::cout << std::endl;

    boost::shared_array_property_map<double, boost::property_map<DirectedGraph, boost::vertex_index_t>::const_type>
    centrality_map(num_vertices(g), get(boost::vertex_index, g));
    
    brandes_betweenness_centrality(g, centrality_map);
    for (int v = 0; v < V; ++v)
    {
        sum = 0;
        for(int i = 0; i <= W+1; i++)
        {
            sum += centrality_map[v+(i*v)];
            //cout << centrality_map[v + (i*V)]<< " ";
        }
        cout << sum << " ";
    }

}