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
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include<queue>
class Solution {
public:
	vector<int> rightSideView(TreeNode* root) {
		// 第一想法：层序遍历中，每层最后一个节点
		// 为了记录最后一个，需要记录每层的个数
		// 首先，第一层一个，然后根据其左右节点情况，让记录值加1。
		vector<int> result{};
		if (!root) {
			return result;
		}
		std::queue<TreeNode*> que;
		int tmp = 1; //记录当前层个数
		int tmp2 = 0; // 记录下一层的个数
		que.push(root);
		while (!que.empty()) {
			// 访问当前节点,tmp--,如果为0，说明为最后一个节点，记录到result中.
			TreeNode* curNode = que.front();
			tmp--;
			if (tmp == 0) {
				result.push_back(curNode->val);
			}
			// 左右节点压入队列。且压入一个tmp2++.
			if (curNode->left) {
				tmp2++;
				que.push(curNode->left);
			}
			if (curNode->right) {
				tmp2++;
				que.push(curNode->right);
			}
			// pop().若tmp==0时,将tmp更新为tmp2，并将tmp2归零。
			que.pop();
			if (tmp == 0) {
				tmp = tmp2;
				tmp2 = 0;
			}
		}
		return result;

	}
};