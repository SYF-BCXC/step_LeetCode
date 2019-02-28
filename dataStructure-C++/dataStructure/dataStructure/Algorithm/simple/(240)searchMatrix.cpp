#include<iostream>
using namespace std;
#include<vector>
bool searchMatrix(vector<vector<int>>& matrix, int target)
{
    // 从右往左，先去掉多余列
    int row = matrix.size();
    if(row==0)
    {
        return false;
    }
    int column = matrix[0].size();
    if(column==0)
    {
        return false;
    }
    int cur_row = 0;
    int cur_column = column-1;
    while(cur_row<row && cur_column >= 0 && cur_row>=0 && cur_column<column && matrix[cur_row][cur_column] > target)
    {
        cur_column--;
    }
    // 在左半部分循环找
    while(cur_row<row && cur_column >= 0 && cur_row>=0 && cur_column<column)
    {
        // 再从上到下找到第一个大于target的值，如果正好找到了则直接返回
        while(cur_row<row && cur_row>=0 && cur_column>=0 && cur_column<column && matrix[cur_row][cur_column] <= target )
        {
            if(matrix[cur_row][cur_column] == target)
            {
                return true;
            }
            else
            {
                cur_row++;
            }
        }
        if(cur_row>=row)
        {
            return false;
        }
        cur_row--;
        cur_column--;
    }
    return false;
    // 最快解答
//         int n=f.size();
//             if(n==0)
//                 return false;
//             int m=f[0].size();

//             for(int c = 0,r = m - 1;c < n && r >= 0;)
//             {
//                if(f[c][r]>tar){
//                    --r;
//                }
//                 else if(f[c][r]<tar){
//                     ++c;
//                 }
//                 else
//                     return true;
//             }
//         return false;
}
int main()
{
    vector<vector<int>> matrix = {{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}};
    int target = 20;
    cout<<searchMatrix(matrix,target);
    system("pause");
    return 0;
}
