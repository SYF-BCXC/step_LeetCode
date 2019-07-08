/*
给出二叉树的根节点 root，树上每个节点都有一个不同的值。

如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

返回森林中的每棵树。你可以按任意顺序组织答案。

示例：

输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]

提示：

树中的节点数最大为 1000。
每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
to_delete.length <= 1000
to_delete 包含一些从 1 到 1000、各不相同的值。
*/


/**
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
    bool del[1050];

    void dfs(TreeNode* root,TreeNode* fa, vector<TreeNode*> &ans, bool flag){
        if (root==NULL) return;
        int v = root->val;
        if (del[v]){
            if(fa!=NULL){ // 需要被删除的同时，其父节点不为空
                if (fa->left==root) fa->left = NULL;
                if (fa->right==root) fa->right = NULL;
                dfs(root->left, root, ans, true);
                dfs(root->right, root, ans, true);
            }else{ //需要被删除的同时，父节点为空
                dfs(root->left, NULL, ans, true);
                dfs(root->right, NULL, ans, true);
            }
        }else{ // 不需要被删除，所以其子节点不构成新树
            if (flag) ans.push_back(root);
            dfs(root->left, root, ans, false);
            dfs(root->right, root, ans, false);
        }
    }

    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& v) {
        int n = v.size();
        for (int i=0; i<1050; i++){
            del[i]=false;
        }
        for (int i=0; i<n; i++){
            del[v[i]]=true;
        }

        vector<TreeNode*> ans;
        dfs(root, NULL, ans, true);

        return ans;
    }
};