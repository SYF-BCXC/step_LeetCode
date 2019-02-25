# include <iostream>
using namespace std;
# include <stack>
#include<queue>

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) { val = x; left = NULL; right = NULL; }
	// TreeNode(int x) : val(x), left(NULL), right(NULL) { }
};

void preorder(TreeNode* t)
{
	// �߽�
	if (!t) {
		return;
	}
	// ���ʵ�ǰ�ڵ�
	cout << t->val << " ";
	// �ݹ����������
	preorder(t->left);
	// �ݹ����������
	preorder(t->right);
}

void inorder(TreeNode* t)
{
	// �߽�
	if (!t) {
		return;
	}
	// �ݹ����������
	inorder(t->left);
	// ���ʵ�ǰ�ڵ�
	cout << t->val << " ";
	// �ݹ����������
	inorder(t->right);
}

void afterorder(TreeNode* t)
{
	// �߽�
	if (!t) {
		return;
	}
	// �ݹ����������
	afterorder(t->left);
	// �ݹ����������
	afterorder(t->right);
	// ���ʵ�ǰ�ڵ�
	cout << t->val << " ";
}

// �������
void levelTraversal(TreeNode* t) {
	// ��Ҫ�õ�����
	queue<TreeNode*> que;
	que.push(t);
	while (!que.empty())
	{
		// ���ʵ�ǰ�ڵ�
		TreeNode* tmp = que.front();
		cout<<tmp->val<<" ";
		// push��ڵ���ҽڵ�
		if (tmp->left)
		{
			que.push(tmp->left);
		}
		if (tmp->right)
		{
			que.push(tmp->right);
		}
		// pop()
		que.pop();
	}

}

/*
int main() {
	//
	//		1
	//	 2		 3
	// 4	   5      6
	//	7           8
	//
	// ���Ĺ������д�ɺ������������õ���root������root��ָ���ݻ��ǻ��д��Ҳ���nullptr��
	TreeNode root(1);
	TreeNode layer_1_1(2);
	TreeNode layer_1_2(3);
	TreeNode layer_2_1(4);
	TreeNode layer_2_2(5);
	TreeNode layer_2_3(6);
	TreeNode layer_3_1(7);
	TreeNode layer_3_2(8);
	root.left = &layer_1_1;
	root.right = &layer_1_2;
	layer_1_1.left = &layer_2_1;
	layer_1_2.left = &layer_2_2;
	layer_1_2.right = &layer_2_3;
	layer_2_1.right = &layer_3_1;
	layer_2_3.left = &layer_3_2;
	cout << "�������:";
	preorder(&root);
	cout << "\r\n�������:";
	inorder(&root);
	cout << "\r\n�������:";
	afterorder(&root);
	cout << "\r\n�������:";
	levelTraversal(&root);


	system("pause");
	return 0;
}
*/