#include<iostream>
using namespace std;
#include<vector>

struct GraphNode
{
	int val;
	vector<GraphNode*> neighbours;
	GraphNode(int x) :val(x) {}
};

void BFS_graph(GraphNode* node,int visit[]) {

}

void DFS_graph() {

}


int main() {
	/*
		Graph:
		Label(0):2 4
		Label(1):0 2
		Label(2):3
		Label(3):4
		Label(4):3
	*/
	const int MAX_N = 5;
	GraphNode* graph[MAX_N];
	for (int i = 0; i < MAX_N; i++) {
		graph[i] = new GraphNode(i);
	}
	graph[0]->neighbours.push_back(graph[2]);
	graph[0]->neighbours.push_back(graph[4]);
	graph[1]->neighbours.push_back(graph[0]);
	graph[1]->neighbours.push_back(graph[2]);
	graph[2]->neighbours.push_back(graph[3]);
	graph[3]->neighbours.push_back(graph[4]);
	graph[4]->neighbours.push_back(graph[3]);
	// 打印存储状态
	printf("Graph:\n");
	for (int i = 0; i < MAX_N; i++)
	{
		printf("Label(%d):", i);
		for (int j = 0; j < graph[i]->neighbours.size(); j++) {
			printf("%d ", graph[i]->neighbours[j]->val);
		}
		printf("\n");
	}
	// 广度优先遍历
	cout << "广度优先遍历:\n";


	// 深度优先遍历
	cout << "深度优先遍历:\n";


	// 删除等操作
	for (int i = 0; i < MAX_N; i++)
	{
		delete graph[i];
	}
	system("pause");
	return 0;
}