[TOC]

# 基础内容

## 指针与引用

## 函数

## STL标准库

### algorithm算法

```cpp
#include <algorithm>
// 1.sort
int a[3] = {1,2,3};
sort(a,a+3);
/*自定义compare实现自定义结构体等的sort*/
bool compare(int a, int b){
    return a>b;
}
sort(a,a+3,compare);

// 2.sort
int a = 1, b = 1;
swap(a,b);
```




### container容器
std::queue 若在线平台不让加头文件，用这种方法弥补
#### vector向量
vector实质上是数组。
```cpp
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	vector<int> test;
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
- vector和list的区别：  
vector:  
1. 本质为数组。可以随机访问
2. 可以在最后进行push_back()和pop_back()但是不能在头进行这种操作。
3. 内部插入效率低  
list:  
1. 本质为双向链表。方便插入删除。
2. 不支持随机访问。但是可以任意插入删除。
3. 占用内存多
#### list列表
list链表就是一个双向链表，可以高效插入删除元素。但不支持随机访问。
```
#include<list>
list<int> li;// 初始化
front();  // 第一个元素的引用
back(); // 返回最后一个元素的引用
reverse();  // 反转链表
push_back(); 
push_front();
pop_front();
pop_back();
```
#### set集合
逻辑本质是数学上的集合(每个元素至多出现一次)，并且set中元素已经从小到大排好序
```
#include<set>
begin()     　　 返回set容器的第一个元素的地址

end() 　　　　 返回set容器的最后一个元素地址

clear()   　　     删除set容器中的所有的元素

empty() 　　　 判断set容器是否为空

max_size() 　   返回set容器可能包含的元素最大个数

size() 　　　　 返回当前set容器中的元素个数

insert(x)		插入元素x

erase(it)        删除迭代器指针it处元素

遍历访问
for (set<int>::iterator it = s.begin(); != s.end(); ++it)    
{
    cout << *it << endl;
}

如果存struct，必须在struct内重载'<'运算符
struct info{
    string name;
    double score;
    bool operator < (const Info &a) const{
        // set中按照score由大到小排序
        return a.score < score;
    }
}
```
#### stack栈
```
#include<stack>
stack<int> st;//定义
push();  //放入元素
pop();  //移除栈顶元素，无返回值
top(); //返回栈顶元素
size();  //栈的长度
empty();  //是否为空
```
#### queue队列
```
#include<queue>
queue<int> que;// 定义
push();
pop();  //无返回值！
front();    // 返回第一个元素
back();  // 返回最后一个元素
size();
empty();
```

#### priority_queue优先队列

```c++
#include<queue>
// 适配器类型(用的vector，但是修改其接口，形成了另外一种风貌),操作类似于queue，只是队首保存当前最大元素
priority_queue<int> q;
q.push();
q.top();
q.pop();
```



#### map映射
#### multimap多重映射
#### deque双队列
#### multiset多重集合

### iterator迭代器
参考容器中的遍历。

## python常用包以及值得注意的细节

```python
Counter
    from collections import Counter
    cc = Counter(arr)	# 也可以直接传字符串，会返回字母的词频
    # Counter继承自字典，因此和字典的用法类似
    cc.items()
    cc.keys()
    ...

OrderedDict(记录插入顺序的字典)
	from collections import OrderedDict
    cc = OrderedDict()
    

heapq
    import heapq
    heapq.heappush(arr,(val,key))	#将(val,key)的元祖加入到arr中，并按照val的大小构建最小堆
    heaq.heappop(arr)	# 将arr堆中的根弹出(最小元素)
    
    lyst = [-3, 22, 45, 34, 99, 102, -44]
    low3 = heapq.nlargest(3, lyst)	# 直接获取Top3
    top3 = heapq.nsmallest(3, lyst)	# 直接获取最后三名

queue
    import queue
    q = queue.Queue()
    q.put()
    q.get()
    
PriorityQueue
	import queue
    q = queue.PriorityQueue()	# 保存当前最小元素
    q.put()
    q.get()
    
List
	插入：
    insert(loc,val)
    删除：
    remove(val)
    pop(loc)
    排序：
	sortedArr = sorted(arr,key=lambda x:x**2) 	# 将排序结果放入sortedArr中，Arr结果不变
    arr.sort()	# 原地排序

set
	s = set(arr)	# 也可以放string
    s.add(val)
    s.update(arr)	# 和add功能一样，这里可以直接放list,dict,tuple
    s.remove(val)
    val in s	# val是否在set中
    
bitset的类似实现
	# 用int和bin实现时，先构造二进制转int，然后<<，最后转回二进制，但是这时候二进制的
	a = [1 for _ in range(100)]
    b = [0 for _ in range(100)]
    c = list(map(lambda x,y:x & y, a, b))	# a和b的按位与
    c = list(map(lambda x,y:x | y, a, b))	# a和b的按位或

进制转换：
	0b101	#二进制
    0o101	#八进制
    0x101	#16进制
    bin(7)	#转为二进制字符串'0b111'(小心前面的0b)
    oct(7)	#转为八进制字符串'0o7'
    hex(7)	#转为16进制字符串'0x7'
    int(str,进制数)	#将指定进制数的字符串转回十进制.str可以带前面两个前缀，也可以不带
```



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

### 常见问题：
[对应源码](https://github.com/WhoseDangerousSmile/step_LeetCode/blob/master/dataStructure-C%2B%2B/dataStructure/dataStructure/NonelinearStructure/Tree/TreeTraversal.cpp)

#### (leetcode 113)最大路径和
[对应源码](https://github.com/WhoseDangerousSmile/step_LeetCode/blob/master/dataStructure-C%2B%2B/dataStructure/dataStructure/NonelinearStructure/Tree/(113)TreePathSum.cpp)

#### (剑指offer)中序遍历的下一个节点
[对应源码](https://github.com/WhoseDangerousSmile/step_LeetCode/blob/master/dataStructure-C%2B%2B/dataStructure/dataStructure/NonelinearStructure/Tree/TreeInorderNext.cpp)

#### (leetcode 236)最近公共祖先
[对应源码](https://github.com/WhoseDangerousSmile/step_LeetCode/blob/master/dataStructure-C%2B%2B/dataStructure/dataStructure/NonelinearStructure/Tree/(236)TreeLowestCommonAncestor.cpp)

#### (leetcode 114)二叉树展平为链表
[对应源码](https://github.com/WhoseDangerousSmile/step_LeetCode/blob/master/dataStructure-C%2B%2B/dataStructure/dataStructure/NonelinearStructure/Tree/(114)FlattenBinaryTree.cpp)
#### (leetcode 199)从右侧观察二叉树
[对应源码](https://github.com/WhoseDangerousSmile/step_LeetCode/blob/master/dataStructure-C%2B%2B/dataStructure/dataStructure/NonelinearStructure/Tree/(199)TreeRightSideView.cpp)

#### 树的前中后序遍历的递归与非递归版本

```cpp
//前序遍历
//递归版本
vector<int> ans;
void helper(TreeNode* root){
    if (root == nullptr) return;
    ans.push_back(root->val);
    if (root->left) helper(root->left);
    if (root->right) helper(root->right);
}
vector<int> preOder(TreeNode* root){
    helper(root);
    return ans;
}
//非递归版本
#include <stack>
vector<int> preOder(TreeNode* root){
    vector<int> ans;
    if (root == nullptr) return ans;
    stack<TreeNode*> s;
    s.push(root);
    while(!s.empty()){
        TreeNode* now = s.top();s.pop();
        ans.push_back(now->val);
        if(now->right) s.push(now->right);
        if(now->left) s.push(now->left);
    }
    return ans;
}

//中序
// 递归版本
vector<int> ans;
void helper(TreeNode* root){
    if (root == nullptr) return;
    if (root->left) helper(root->left);
    ans.push_back(root->val);
    if (root->right) helper(root->right);
}

vector<int> inorder(TreeNode* root){
    helper(root);
    return ans;
}
// 非递归版本
#include <stack>
vector<int> inorder(TreeNode* root){
    vector<int> ans;
    if(root == nullptr) return ans;
    stack<TreeNode*> s;
    TreeNode* p = root;
    while (!s.empty() || p){
        while(p){
            s.push(p);
            p = p -> left;
        }
        if (!s.empty()){
            p = s.top();s.pop();
            ans.push_back(p->val);
            p = p->right;
        }
    }
    return ans;
}
//后序
//递归版本
vector<int> ans;
void helper(TreeNode* root){
    if (root == nullptr) return;
    if (root->left) helper(root->left);
    if (root->right) helper(root->right);
    ans.push_back(root->val);
}
vector<int> afterorder(TreeNode* root){
    helper(root);
    return ans;
}

// 非递归版本(直接 根右左，然后逆序输出)
#include <stack>
vector<int> afteroder(TreeNode* root){
    vector<int> ans;
    if (root == nullptr) return ans;
    TreeNode* now = root;
    stack<TreeNode*> s;
    s.push(now);
    while(!s.empty()){
        now = s.top(); s.pop();
        ans.push_back(now->val);
        if (now->right) s.push(now->right);
        if (now->left) s.push(now->left);
    }
    reverse(ans.begin(),ans.end());
    return ans;
}

```




## 图
顶点+边 = 图；
### 存储
邻接矩阵
```
有边为1(带权则为权值)，无边为0.
const int MAX_NODE = 5; //顶点数
int Graph[MAX_NODE][MAX_NODE] = {0}; //边

```
邻接表
```
struct GraphNode{
    int val;
    vector<GraphNode*> neighbours;
    GraphNode(int x):val(x){};
}
const int MAX_NODE = 5; //顶点数
GraphNode* graph[MAX_NODE]; 
for(int i=0;i<MAX_NODE;i++){
    graph[i] = new GraphNode(i);
}
// 添加边
graph[0]->neighbours.push_back(graph[3]);
... ...
```
### 广度搜索与深度搜索

### 最小生成树

### 最短单元路径

### AOE网络与关键路径


# 算法
## 排序

## 贪心算法

## 搜索算法

二分以及变种

```python
def binarySearch(nums, target):
    """普通的二分查找
    找到返回位置，没找到返回-1
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binarySearchFB(nums, target):
    """找第一个大于等于target的值，如果所有值都小于target返回len(nums)"""
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return r + 1


def binarySearchLS(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
    return l - 1


while True:
    target = int(input())
    nums = [1, 2, 4, 5, 5, 5, 7, 10]
    print(binarySearchLS(nums, target))

```











## 递归、回溯与分治

## 动态规划


