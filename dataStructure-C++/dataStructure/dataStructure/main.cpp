#include <iostream>
using namespace std;
// 格式化代码。先全选代码ctrl + A, 然后ctrl + K + F
// ctrl+k+c 和 ctrl+k+u
//int main()
//{
//	cout << "hello";
//
//	system("pause");
//
//	return 0;
//}


/* 初始化vector方法：
方法1、
vector<int> a = {1,2,3};
方法2、
int a[3] = {1,2,3};
int a_length = sizeof(a)/sizeof(a[0]);
vector<int> b(a,a+length);
方法3、
vector<int> list;//初始化为空，size为0，需要后期push_back();
方法4、（与方法2其实本质相同，传入两个地址）
vector<int> ilist3(ilist.begin()+2,ilist.end()-1);
方法5、
vector<int> list(4,2);//4个2(否则默认值为0)


输出vector方法：
for(vector<int>::iterator it = b.begin(); it != b.end(); it++)
{
	cout<<*it<<endl;
}
*/
/*
int a[10] = { 3,1,0,5,8,9,7,4,2,6 };
char b[3] = { 'a','b','\0' };
cout << a << endl;//地址
cout << &a << endl;//地址
cout << *a << endl;//3(值)
cout << "***********" << endl;
cout << b << endl;//ab(值，因为字符数组有\0终止符)
cout << &b << endl;//地址
cout << *b << endl;//a(值)
*/


// 未初始化int数组，数组中的值为-842150451

/* 数组定义与初始化：
静态 int array[100] = {1，2}；　　定义并初始化了数组array
动态 int* array = new int[100]; 　delete []array;　分配了长度为100的数组array
*/

// 格式化代码。先全选代码ctrl + A, 然后ctrl + K + F