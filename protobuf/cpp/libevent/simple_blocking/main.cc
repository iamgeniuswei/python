#include <iostream>
#include <netinet/in.h>
//struct sockaddr_in
#include <netdb.h>
//gethostbyname()
//struct hostent
#include <sys/socket.h>
//socket()
//connect()

#include <unistd.h>
//close()

#include <string.h>
//strlen()

int main(int c, char **v)
{
    const char query[] = "GET / HTTP/1.0\r\n"
    "Host: www.baidu.com\r\n"
    "\r\n";
    const char hostname[] = "www.baidu.com";

    std::cout << hostname << std::endl;
    sockaddr_in sin;
    hostent *host = nullptr;

    host = gethostbyname(hostname);
    if(host == nullptr)
    {
        std::cerr << "Couldn't lookup " << hostname << std::endl;
        return 1;
    }

    int fd = socket(AF_INET, SOCK_STREAM, 0);
    if(fd < 0)
    {
        std::cerr << "socket() error" << std::endl;
        return 1;
    }

    //connect to the remote host
    sin.sin_family = AF_INET;
    sin.sin_port = htons(80);
    sin.sin_addr = *(in_addr*)(host->h_addr_list[0]);
    int rst = connect(fd, (sockaddr*)&sin, sizeof(sin));
    if(rst != 0)
    {
        std::cerr << "connect() error" << std::endl;
        close(fd);
        return 1;
    }
    
    //send the query
    const char *cp = query;
    ssize_t n_remaining = strlen(cp);
    ssize_t n_send = 0;
    while (n_remaining)
    {
        /* code */
        n_send = send(fd, cp, n_remaining, 0);
        if(n_send <=0 )
        {
            std::cerr << "send() error" << std::endl;
            close(fd);
            return 1;
        }
        n_remaining -= n_send;
        cp+=n_send;
    }
    
    //get an answer back.
    char buf[1024];
    while (true)
    {
        /* code */
        ssize_t result = recv(fd, buf, 1024, 0);
        if (result == 0)
            break;
        else if (result < 0)
        {
            /* code */
            std::cerr << "recv() error" << std::endl;
            close(fd);
            return 1;
        }
        std::cout << buf << std::endl;
    }

    close(fd);
}