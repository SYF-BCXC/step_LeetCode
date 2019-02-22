# include <iostream>
using namespace std;
#include<vector>

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) { }
};

/**
 * ��Ŀ��leetcode 113�⡣
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	vector<vector<int>> result;
	vector<int> path;
	int presum;

	void findPath(TreeNode* t, int &sum, vector<int> &path, int &presum, vector<vector<int>> &result) {
		// �߽��ж�
		if (!t) {
			return;
		}

		// ��ջ
		path.push_back(t->val);
		presum += t->val;

		// �ж��Ƿ������������
		if (presum == sum && !t->left && !t->right) {
			result.push_back(path);
		}

		// ����
		findPath(t->left, sum, path, presum, result);
		findPath(t->right, sum, path, presum, result);

		// ��ջ
		presum -= t->val;
		path.pop_back();
	}

	vector<vector<int>> pathSum(TreeNode* root, int sum) {
		this->presum = 0;
		findPath(root, sum, this->path, this->presum, this->result);
		return result;
	}
};