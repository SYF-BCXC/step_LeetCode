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
		// ��һ�뷨����������У�ÿ�����һ���ڵ�
		// Ϊ�˼�¼���һ������Ҫ��¼ÿ��ĸ���
		// ���ȣ���һ��һ����Ȼ����������ҽڵ�������ü�¼ֵ��1��
		vector<int> result{};
		if (!root) {
			return result;
		}
		std::queue<TreeNode*> que;
		int tmp = 1; //��¼��ǰ�����
		int tmp2 = 0; // ��¼��һ��ĸ���
		que.push(root);
		while (!que.empty()) {
			// ���ʵ�ǰ�ڵ�,tmp--,���Ϊ0��˵��Ϊ���һ���ڵ㣬��¼��result��.
			TreeNode* curNode = que.front();
			tmp--;
			if (tmp == 0) {
				result.push_back(curNode->val);
			}
			// ���ҽڵ�ѹ����С���ѹ��һ��tmp2++.
			if (curNode->left) {
				tmp2++;
				que.push(curNode->left);
			}
			if (curNode->right) {
				tmp2++;
				que.push(curNode->right);
			}
			// pop().��tmp==0ʱ,��tmp����Ϊtmp2������tmp2���㡣
			que.pop();
			if (tmp == 0) {
				tmp = tmp2;
				tmp2 = 0;
			}
		}
		return result;

	}
};