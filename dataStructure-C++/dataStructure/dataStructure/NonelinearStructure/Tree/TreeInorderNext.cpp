# include <iostream>
using namespace std;

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode *father;
	// д��1.��ʼ����Ч�ʸ�
	TreeNode(int x) : val(x), left(NULL), right(NULL), father(NULL) { }
	// д��2.��ֵ��Ч�ʲ�
	// TreeNode(int x){val=x;left=NULL;right=NULL;}
};

/*
��һ���ڵ㣬�����������һ���ڵ��ֵ���������һ�ڵ��򷵻�-1.
*/
int inorderNext(TreeNode* t) {
	// �߽�

	// ���ҽڵ㡣��������������ڵ�
	TreeNode* cur_tree = t->right;
	if (cur_tree) {
		cur_tree = cur_tree->left;
		while (!cur_tree->right &&!cur_tree->left)
		{
			return cur_tree->val;
		}
	}
	// ���ҽڵ㡣�ݹ���ʸ��ڵ㣬ֱ��Ϊ���ڵ����ڵ㣬���߸��ڵ�ΪNULL
	else
	{
		cur_tree = t;
		while (cur_tree->father)
		{
			if (cur_tree == cur_tree->father->left)
			{
				return cur_tree->father->val;
			}
			else
			{
				cur_tree = cur_tree->father;
			}
		}
		return -1;
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
	layer_1_1.father = &root;
	layer_1_2.left = &layer_2_2;
	layer_1_2.right = &layer_2_3;
	layer_1_2.father = &root;
	layer_2_1.right = &layer_3_1;
	layer_2_1.father = &layer_1_1;
	layer_2_2.father = &layer_1_2;
	layer_2_3.father = &layer_1_2;
	layer_2_3.left = &layer_3_2;
	layer_3_1.father = &layer_2_1;
	layer_3_2.father = &layer_2_3;
	cout << inorderNext(&root);
	system("pause");
	return 0;
}
*/