#include <iostream>
using namespace std;
// ��ʽ�����롣��ȫѡ����ctrl + A, Ȼ��ctrl + K + F
// ctrl+k+c �� ctrl+k+u
//int main()
//{
//	cout << "hello";
//
//	system("pause");
//
//	return 0;
//}


/* ��ʼ��vector������
����1��
vector<int> a = {1,2,3};
����2��
int a[3] = {1,2,3};
int a_length = sizeof(a)/sizeof(a[0]);
vector<int> b(a,a+length);
����3��
vector<int> list;//��ʼ��Ϊ�գ�sizeΪ0����Ҫ����push_back();
����4�����뷽��2��ʵ������ͬ������������ַ��
vector<int> ilist3(ilist.begin()+2,ilist.end()-1);
����5��
vector<int> list(4,2);//4��2(����Ĭ��ֵΪ0)


���vector������
for(vector<int>::iterator it = b.begin(); it != b.end(); it++)
{
	cout<<*it<<endl;
}
*/
/*
int a[10] = { 3,1,0,5,8,9,7,4,2,6 };
char b[3] = { 'a','b','\0' };
cout << a << endl;//��ַ
cout << &a << endl;//��ַ
cout << *a << endl;//3(ֵ)
cout << "***********" << endl;
cout << b << endl;//ab(ֵ����Ϊ�ַ�������\0��ֹ��)
cout << &b << endl;//��ַ
cout << *b << endl;//a(ֵ)
*/


// δ��ʼ��int���飬�����е�ֵΪ-842150451

/* ���鶨�����ʼ����
��̬ int array[100] = {1��2}���������岢��ʼ��������array
��̬ int* array = new int[100]; ��delete []array;�������˳���Ϊ100������array
*/

// ��ʽ�����롣��ȫѡ����ctrl + A, Ȼ��ctrl + K + F