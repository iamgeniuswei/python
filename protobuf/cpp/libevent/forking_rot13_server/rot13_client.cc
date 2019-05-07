
#include <sys/socket.h>
#include <netinet/in.h>
#include <iostream>
using namespace std;
#include <unistd.h>
int main(int c, char **v)
{
    int fd = socket(AF_INET , SOCK_STREAM, 0);
    sockaddr_in sin;
    sin.sin_family = AF_INET;
    sin.sin_port = htons(12345);
    sin.sin_addr.s_addr = htonl(INADDR_ANY);
    //成功返回0， 失败返回-1, 错误原因存于errno
    int rst = connect(fd, (sockaddr*)&sin, sizeof(sin));
    if(rst != 0)
    {
        cerr << "connect() error!" << endl;
        return 1;
    }
    char buf[] = "ABCabc";
    int n_send = send(fd, buf, sizeof(buf), 0);
    char recv_buf[1024];
    int n_recv = recv(fd, recv_buf, 1024, 0);
    cout << recv_buf << endl;
    close(fd);
    return 0;
}