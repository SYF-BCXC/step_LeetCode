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
	// �ݹ顣���չ��������������չ�����������һ���ڵ�
	TreeNode* core(TreeNode* cur) {
		// �߽�
		if (!cur)
		{
			return NULL;
		}
		if (!cur->right && !cur->left) {
			return cur;
		}
		if (!cur->left) {
			//���������Ϊ�գ�ֱ�ӵݹ�������
			return core(cur->right);
		}
		else {
			//��������Ϊ�ա����������ĸ��ҵ��ң�ͬʱ������
			TreeNode* right = cur->right;
			cur->right = cur->left;
			cur->left = NULL;
			// �ݹ�
			TreeNode* left_tail = core(cur->right);
			// ���ұߵݹ����������
			left_tail->right = right;
			return core(cur->right);
		}

	}
	void flatten(TreeNode* root) {
		core(root);
	}
};

//	�����,���Ǻ���˼·��һ����
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