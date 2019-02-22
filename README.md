[Toc]

# 基础说明
1、本项目是本人LeetCode刷题的记录，方便后期回顾总结。
每一题本人都会自己写一遍，并且尽可能的写最多种解法，同时自己写的思路不对的代码也会保留并附上自己的反思，最后也会附上官方公布的最快代码，以示比较。

2、如无特殊情况，本人每天会刷两道题(如果题目太难可能会放慢速度)

3、如果有同样在刷LeetCode题的同学，可以一起讨论学习。本人联系邮箱:tangcaiyuan@hust.edu.cn如果发现代码中存在问题，还请不吝赐教。  
TCY 

# 基础内容
## STL标准库

### algorithm算法


### container容器
#### vector向量
#### list列表
#### set集合
#### stack栈
#### queue队列
#### priority_queue优先队列
#### map映射
#### multimap多重映射
#### deque双队列
#### multiset多重集合

### iterator迭代器

# 线性结构
## 数组

## 链表

## 队列和栈

# 非线性结构
## 树
### 存储结构：
struct TreeNode {
 int val;
 TreeNode *left;
 TreeNode *right;
 TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
### 遍历：
#### 问题：最大路径和
```
static const auto _ = []()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
 int res = INT_MIN;
 int maxPath(TreeNode* root) {
    // 边界判断
	 if (root == NULL)
		 return 0;
	// 遍历
	 int left_max = maxPath(root->left);
	 int right_max = maxPath(root->right);
	// 小于零则为0
	 left_max = left_max > 0 ? left_max : 0;
	 right_max = right_max > 0 ? right_max : 0;
	 // 计算和
	 int sum = left_max + right_max + root->val;
	 // 
	 res = max(res, sum);
	 return left_max > right_max ? (left_max+root->val) : (right_max+root->val);
 }
 int maxPathSum(TreeNode* root) {
	 maxPath(root);
	 return res;
 }
};
```
#### 问题：输出所有路径，路径的和为指定值
```
public vector<TreeNode> path = nullptr;
public int presum = 0;
public vector<vector<TreeNode>> result = nullptr;
// t:当前节点  sum: 目标值  path:当前路径  presum:当前和  result:所有结果路径
public void peroder(TreeNode *t, int sum, Stack path, int presum, vector<vector<int>> result) {
    // 递归的边界
    if(t == null){
        return;
    }
    // 入栈
    path.push(t->value);
    presum += t->value;
    
    // 输出的判断
    if ( !t->left && !t->right && presum == sum)
    {
        result.append(path);
    }
    
    // 遍历
    peroder(t->left,sum,path,presum,result);
    peroder(t->rigth,sum,path,presum,result);
    
    // 退栈
    path.pop();
}
```
#### 中序遍历的下一个节点
if(t.right){
    访问右子树的最左节点
} else {
    if(t is t.father.left){
        访问父节点
    } else if(t is t.father.right){
        递归网上找直到为父节点的左
    } else {
        // father is null
        说明t为中序最后一个节点，直接返回null
    }
}

## 图
### 存储
### 最小生成树
### 最短单元路径
### AOE网络与关键路径
### 广度搜索与深度搜索

# 查找

# 排序

# 搜索

# 递归与动态规划

# 分治

