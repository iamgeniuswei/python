#include <netinet/in.h>
#include <sys/socket.h>
#include <iostream>
using namespace std;
#include <unistd.h>

const int MAX_LINE = 16384;


char rot13_char(char c)
{
    if ((c >= 'a' && c <= 'm') || (c >= 'A' && c <= 'M'))
        return c + 13;
    else if ((c >= 'n' && c <= 'z') || (c >= 'N' && c <= 'Z'))
        return c - 13;
    else
        return c;
}



//connection-per-thread
//thread function.
void* child(void *arg)
{
    int fd = *(int*)arg;
    cout << "child process, fd=" << fd << endl;
    char outbuf[MAX_LINE+1];
    size_t outbuf_used = 0;
    ssize_t result = 0;
    while (true)
    {
        /* code */
        char ch;
        result = recv(fd, &ch, 1, 0);
        if(result == 0)
        {
            break;
        }
        else if (result == -1)
        {
            /* code */
            cerr << "recv() error" << endl;
            break;
        }

        if(outbuf_used < sizeof(outbuf))
        {
            outbuf[outbuf_used++] = rot13_char(ch);
        }
        
        if(ch == '\n')
        {
            send(fd, outbuf, outbuf_used, 0);
            outbuf_used = 0;
            continue;
        }        
    }    
}



void run(void)
{
    int listener;
    sockaddr_in sin;
    sin.sin_family = AF_INET;
    sin.sin_port = htons(12345);
    sin.sin_addr.s_addr = 0;           //ip地址字符串要转换成int32
    listener = socket(AF_INET, SOCK_STREAM, 0);

    #ifndef WIN32
    {
        int one = 1;
        setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &one, sizeof(one));
    }
    #endif

    int rst = bind(listener, (sockaddr*)&sin, sizeof(sin));
    if(rst < 0)
    {
        cerr << "bind() error!" << endl;
        close(listener);
        return;
    }
    if(listen(listener, 16) < 0)
    {
        cerr << "listen() error!" << endl;
        close(listener);
        return;
    }

    while (true)
    {
        /* code */
        sockaddr_storage ss;
        socklen_t slen = sizeof(ss);
        int child_fd = accept(listener, (sockaddr*)&ss, &slen);
        if(child_fd < 0)
        {
            cerr << "accept() error" << endl;            
        }
        else
        {
            pthread_t th;
            int *thread_ret = nullptr;
            int ret = pthread_create(&th, nullptr, child, &child_fd);
            if(ret != 0)
            {
                cerr << "pthread_create() error" << endl;
                continue;
            }
        }        
    }
    

}

int main(int c, char **v)
{
    run();
    return 0;
}