#include<iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	// 递归。完成展开操作，并返回展开子树的最后一个节点
	TreeNode* core(TreeNode* cur) {
		// 边界
		if (!cur)
		{
			return NULL;
		}
		if (!cur->right && !cur->left) {
			return cur;
		}
		if (!cur->left) {
			//如果左子树为空，直接递归右子树
			return core(cur->right);
		}
		else {
			//左子树不为空。将左子树的根挂到右，同时保存右
			TreeNode* right = cur->right;
			cur->right = cur->left;
			cur->left = NULL;
			// 递归
			TreeNode* left_tail = core(cur->right);
			// 把右边递归结果挂在左边
			left_tail->right = right;
			return core(cur->right);
		}

	}
	void flatten(TreeNode* root) {
		core(root);
	}
};

//	最快解答,但是好像思路是一样的
//	static const void* ___ = []() {
//		ios::sync_with_stdio(false);
//		cin.tie(nullptr);
//		return nullptr;
//	}();
//	class Solution {
//	public:
//		void flatten(TreeNode* root) {
//			_flatten(root);
//		}
//	private:
//		TreeNode *_flatten(TreeNode *root) {
//			if (!root) return nullptr;
//			TreeNode *tmp = root->right;
//			root->right = root->left;
//			root->left = nullptr;
//			TreeNode *p = _flatten(root->right);
//			if (!tmp) return p ? p : root;
//			if (p)
//				p->right = tmp;
//			else
//				root->right = tmp;
//			return _flatten(tmp);
//		}
//	};