# include <iostream>
#include <vector>
using namespace std;


struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) { }
};

class Solution {
public:
	// �ҵ�p��·���������浽findPath��
	void find(TreeNode* root, TreeNode* p, vector<TreeNode*> &path, vector<TreeNode*> &result, int &flag) {
		// �߽�
		if (!root || flag) {
			return;
		}

		// ��ջ.�ж��Ƿ��ҵ���
		path.push_back(root);
		if (root == p) {
			result = path;
			flag = 1;
		}

		// ����
		find(root->left, p, path, result, flag);
		find(root->right, p, path, result, flag);

		// ��ջ
		path.pop_back();

	}
	TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
		// vector<TreeNode*> path;
		// vector<TreeNode*> pPath;
		// vector<TreeNode*> qPath;
		// int flag_p = 0;
		// int flag_q = 0;
		// find(root,p,path,pPath,flag_p);
		// path.clear();
		// find(root,q,path,qPath,flag_q);
		// int len = pPath.size()>qPath.size()? qPath.size():pPath.size();
		// for(int i = 0;i<len;i++){
		//     if(pPath[i] != qPath[i])
		//     {
		//         return pPath[i-1];
		//     }
		// }
		if (root == NULL || p == root || q == root) return root;
		TreeNode* left = lowestCommonAncestor(root->left, p, q);
		TreeNode* right = lowestCommonAncestor(root->right, p, q);
		if (left && right) return root;
		return left ? left : right;
	}
};