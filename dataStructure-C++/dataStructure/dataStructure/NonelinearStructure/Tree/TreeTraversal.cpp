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
	// 边界
	if (!t) {
		return;
	}
	// 访问当前节点
	cout << t->val << " ";
	// 递归访问左子树
	preorder(t->left);
	// 递归访问右子树
	preorder(t->right);
}

void inorder(TreeNode* t)
{
	// 边界
	if (!t) {
		return;
	}
	// 递归访问左子树
	inorder(t->left);
	// 访问当前节点
	cout << t->val << " ";
	// 递归访问右子树
	inorder(t->right);
}

void afterorder(TreeNode* t)
{
	// 边界
	if (!t) {
		return;
	}
	// 递归访问左子树
	afterorder(t->left);
	// 递归访问右子树
	afterorder(t->right);
	// 访问当前节点
	cout << t->val << " ";
}

// 层序遍历
void levelTraversal(TreeNode* t) {
	// 需要用到队列
	queue<TreeNode*> que;
	que.push(t);
	while (!que.empty())
	{
		// 访问当前节点
		TreeNode* tmp = que.front();
		cout<<tmp->val<<" ";
		// push左节点和右节点
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
	// 树的构造如果写成函数，尽管引用调用root，但是root所指内容还是会有错，且不是nullptr。
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
	cout << "先序遍历:";
	preorder(&root);
	cout << "\r\n中序遍历:";
	inorder(&root);
	cout << "\r\n后序遍历:";
	afterorder(&root);
	cout << "\r\n层序遍历:";
	levelTraversal(&root);


	system("pause");
	return 0;
}
*/