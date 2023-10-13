#include <bits/stdc++.h>
using namespace std;

//-----------使用广度优先搜素------------//
struct Point // 构建队列
{
    int x, y;
};
queue<Point> map_queue;

int dx[5] = {0, 0, 0, -1, 1}, dy[5] = {0, -1, 1, 0, 0}; // 方向数组
bool is_used[200][200];                               // 标记这个点有没有被搜索过
int distance[200][200];                               // 储存距离

int main()
{
    memset(is_used, false, sizeof(is_used)); // init
    int N, M;
    cin >> N >> M;
    int head = 0, tail = 0; // 队列首指针head=0; 尾指针tail=1；

    for (int i = 1; i <= N; i++)
    {
        string str;
        cin >> str;
        for (int j = 0; j < str.size(); j++)
        {
            if (str[j] == '0')
            {
                is_used[i][j + 1] = false;
            }
            else
            {
                ::distance[i][j + 1] = 0;
                is_used[i][j + 1] = true;
                map_queue.push({i, j + 1});
            }
        }
    }

    while (!map_queue.empty())
    {
        Point curr = map_queue.front();
        map_queue.pop();

        for (int i = 1; i <= 4; i++)
        {
            int nx = curr.x + dx[i];
            int ny = curr.y + dy[i];

            if (nx >= 1 && nx <= N && ny >= 1 && ny <= M && !is_used[nx][ny]) //判断距离
            {
                is_used[nx][ny] = true;
                ::distance[nx][ny] = ::distance[curr.x][curr.y] + 1;
                map_queue.push({nx, ny});
            }
        }
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            cout << ::distance[i][j] << " ";//all right
        }
        cout << endl;
    }
    return 0;
}
