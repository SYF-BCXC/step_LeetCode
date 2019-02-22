# include <iostream>
using namespace std;

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) { }
};

/*
int main() {
	//
	//		1
	//	 2		 3
	// 4	   5     6
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
	layer_1_2.left = &layer_2_2;
	layer_1_2.right = &layer_2_3;
	layer_2_1.right = &layer_3_1;
	layer_2_3.left = &layer_3_2;

	system("pause");
	return 0;
}
*/