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
    void countNode(TreeNode* cur,int &all){
        if (cur == nullptr){
            return;
        }
        else{
            all++;
            countNode(cur->left, all);
            countNode(cur->right, all);
        }
    }

    bool findX(TreeNode* cur,TreeNode* &target,int x){
        if (cur == nullptr){
            return false;
        }
        if (cur->val == x){
            target = cur;
            return true;
        }else{
            if (findX(cur->left, target, x) == false){
                if(findX(cur->right,target,x)==false){
                    return false;
                }else{return true;}
            }else{
                return true;
            }

        }
    }

    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        // 为了赢，要堵住左右父三个方向上最大的一边，因此需要计算x这三个方向分别有多少节点
        int a = 0, b = 0;
        int leftCount = 0, rightCount = 0, fatherCount = 0;
        TreeNode* target = nullptr;
        findX(root, target, x);
        if (target == root){
            countNode(root->left, leftCount);
            countNode(root->right, rightCount);
        }else{
            countNode(target->left, leftCount);
            countNode(target->right, rightCount);
            int all = 0;
            countNode(root,all);
            fatherCount = all - leftCount - rightCount - 1;
        }
        b = max(fatherCount,max(leftCount,rightCount));
        a = leftCount + rightCount + fatherCount + 1 - b;
        if (b < a){
            return false;
        }else{
            return true;
        }
    }
};