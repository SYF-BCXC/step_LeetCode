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

// ����ͼ��һ���㣬�����ܷ��ʵ������нڵ�
void BFS_graph(GraphNode *node, int visit[])
{
	// ������ȣ��ȷ����ܷ��ʵ����е㣬�����η�����Щ���ܷ��ʵ�������
	queue<GraphNode *> q;
	q.push(node);
	vector<int> result;
	// ���в�Ϊ�գ��鿴�Ƿ��Ѿ����ʣ�δ���ʣ�����ӵ�result��

	// ����result����ӡ���
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
	// ��ӡͼ�Ľṹ
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
	// �������
	cout << "�������:\n";

	// �������
	cout << "�������:\n";

	// �ͷ��ڴ�
	for (int i = 0; i < MAX_N; i++)
	{
		delete graph[i];
	}
	system("pause");
	return 0;
}
*/
