#include <iostream>
using namespace std;
#include <vector>
#include <queue>

struct GraphNode
{
	int val;
	vector<GraphNode *> neighbours;
	GraphNode(int x) : val(x) {}
};

// 给定图中一个点，遍历能访问到的所有节点
void BFS_graph(GraphNode *node, int visit[])
{
	// 广度优先，先访问能访问的所有点，再依次访问这些点能访问的其他点
	queue<GraphNode *> q;
	q.push(node);
	vector<int> result;
	// 队列不为空，查看是否已经访问，未访问，则添加到result。

	// 访问result，打印结果
}

void DFS_graph()
{
}
/*
int main()
{
	//
	//	Graph:
	//	Label(0):2 4
	//	Label(1):0 2
	//	Label(2):3
	//	Label(3):4
	//	Label(4):3
	//
	const int MAX_N = 5;
	GraphNode *graph[MAX_N];
	for (int i = 0; i < MAX_N; i++)
	{
		graph[i] = new GraphNode(i);
	}
	graph[0]->neighbours.push_back(graph[2]);
	graph[0]->neighbours.push_back(graph[4]);
	graph[1]->neighbours.push_back(graph[0]);
	graph[1]->neighbours.push_back(graph[2]);
	graph[2]->neighbours.push_back(graph[3]);
	graph[3]->neighbours.push_back(graph[4]);
	graph[4]->neighbours.push_back(graph[3]);
	// 打印图的结构
	printf("Graph:\n");
	for (int i = 0; i < MAX_N; i++)
	{
		printf("Label(%d):", i);
		for (int j = 0; j < graph[i]->neighbours.size(); j++)
		{
			printf("%d ", graph[i]->neighbours[j]->val);
		}
		printf("\n");
	}
	// 深度优先
	cout << "深度优先:\n";

	// 广度优先
	cout << "广度优先:\n";

	// 释放内存
	for (int i = 0; i < MAX_N; i++)
	{
		delete graph[i];
	}
	system("pause");
	return 0;
}
*/
