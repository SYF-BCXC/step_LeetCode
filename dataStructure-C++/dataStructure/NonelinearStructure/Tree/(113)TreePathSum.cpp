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
 * 题目在leetcode 113题。
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
		// 边界判断
		if (!t) {
			return;
		}

		// 入栈
		path.push_back(t->val);
		presum += t->val;

		// 判断是否满足输出条件
		if (presum == sum && !t->left && !t->right) {
			result.push_back(path);
		}

		// 遍历
		findPath(t->left, sum, path, presum, result);
		findPath(t->right, sum, path, presum, result);

		// 出栈
		presum -= t->val;
		path.pop_back();
	}

	vector<vector<int>> pathSum(TreeNode* root, int sum) {
		this->presum = 0;
		findPath(root, sum, this->path, this->presum, this->result);
		return result;
	}
};