[TOC]
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
```
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	vector<int> test;
 
	test.push_back(8);
	test.push_back(5);
	test.push_back(3);
	test.push_back(7); //尾部加入元素
 
    reverse(test.begin(), test.end()); //反转vector
 
    for (vector<int>::iterator it = test.begin(); it != test.end(); ++it)
		cout << *it << endl;  //使用迭代器遍历
 
	for (int i = 0; i < test.size(); ++i)
		cout << test[i] << endl; //使用索引遍历
 
	cout << test.size() << endl;  //返回v的长度
 
	test.pop_back(); //删除v最后一个元素，类似于弹栈，因此可用来实现栈
 
	cout << test.back() << endl; //取最后一个元素
 
	vector<int>::iterator it = test.begin(); //声明迭代器
 
	it = test.erase(it); //删除迭代器it指向的元素,返回此迭代器的下一个迭代器
 
	sort(test.begin(), test.end()); //使元素由大到小排序,sort位于头文件algorithm
 
	test.resize(2);  //修改vector大小
 
	test.insert(it, -1); //在迭代器位置插入元素
	vector<int> another (3,2); //声明vector， 值为 2 2 2 
	test.insert(test.begin(), another.begin(), another.end()); //vector中插入vector
	int list[] = { 0, 1, 2, 3 };
	test.insert(test.begin(), list, list + 3); //vector中插入数组
 
	find(test.begin(), test.end(), 3); //在vector中查找元素3是否存在，若存在返回指定迭代器；不存在返回test.end()
 
	test.clear(); //清空test中元素
 
	test.empty(); //test是否为空
```
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
问题：(leetcode 113)Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
// t:当前节点  sum: 目标值  path:当前路径  presum:当前和  result:所有结果路径
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
    vector<vector<int>> result;
    vector<int> path;
    int presum;
    
    void findPath(TreeNode* t,int &sum, vector<int> &path, int &presum, vector<vector<int>> &result){
        // 边界判断
        if(!t){
            return;
        }
        
        // 入栈
        path.push_back(t->val);
        presum += t->val;
        
        // 判断是否满足输出条件
        if (presum == sum && !t->left && !t->right){
            result.push_back(path);
        }
        
        // 遍历
        findPath(t->left,sum,path,presum,result);
        findPath(t->right,sum,path,presum,result);
        
        // 出栈
        presum -= t->val;
        path.pop_back();
    }
    
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        this->presum = 0;
        findPath(root,sum,this->path,this->presum,this->result);
        return result;
    }
};
```
#### 中序遍历的下一个节点
```
# include <iostream>
using namespace std;

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode *father;
	// 写法1.初始化，效率高
	TreeNode(int x) : val(x), left(NULL), right(NULL), father(NULL) { }
	// 写法2.赋值，效率差
	// TreeNode(int x){val=x;left=NULL;right=NULL;}
};

/*
给一个节点，求其中序的下一个节点的值，如果无下一节点则返回-1.
*/
int inorderNext(TreeNode* t) {
	// 边界

	// 有右节点。访问右子树最左节点
	TreeNode* cur_tree = t->right;
	if (cur_tree) {
		cur_tree = cur_tree->left;
		while (!cur_tree->right &&!cur_tree->left)
		{
			return cur_tree->val;
		}
	}
	// 无右节点。递归访问父节点，直到为父节点的左节点，或者父节点为NULL
	else
	{
		cur_tree = t;
		while (cur_tree->father)
		{
			if (cur_tree == cur_tree->father->left)
			{
				return cur_tree->father->val;
			}
			else
			{
				cur_tree = cur_tree->father;
			}
		}
		return -1;
	}
}

/*
int main() {
	//
	//		1
	//	 2		 3
	// 4	   5      6
	//	7           8
	//
	TreeNode root(1);
	TreeNode layer_1_1(2);
	TreeNode layer_1_2(3);
	TreeNode layer_2_1(4);
	TreeNode layer_2_2(5);
	TreeNode layer_2_3(6);
	TreeNode layer_3_1(7);
	TreeNode layer_3_2(8);
	root.left = &layer_1_1;
	root.right = &layer_1_2;
	layer_1_1.left = &layer_2_1;
	layer_1_1.father = &root;
	layer_1_2.left = &layer_2_2;
	layer_1_2.right = &layer_2_3;
	layer_1_2.father = &root;
	layer_2_1.right = &layer_3_1;
	layer_2_1.father = &layer_1_1;
	layer_2_2.father = &layer_1_2;
	layer_2_3.father = &layer_1_2;
	layer_2_3.left = &layer_3_2;
	layer_3_1.father = &layer_2_1;
	layer_3_2.father = &layer_2_3;
	cout << inorderNext(&root);
	system("pause");
	return 0;
}
*/
```
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

