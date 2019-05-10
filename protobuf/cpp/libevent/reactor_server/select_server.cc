#include <unistd.h>
#include <fcntl.h>
#include <sys/select.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <iostream>
using namespace std;
const int MAX_LINE = 16348;


char rot13_char(char c)
{
    if ((c >= 'a' && c <= 'm') || (c >= 'A' && c <= 'M'))
        return c + 13;
    else if ((c >= 'n' && c <= 'z') || (c >= 'N' && c <= 'Z'))
        return c - 13;
    else
        return c;
}

struct fd_state
{
    /* data */
    char buf[MAX_LINE];
    size_t buffer_used;
    int writing;
    size_t n_written;
    size_t write_upto;
};

fd_state* allock_fd_state()
{
    fd_state *state = (fd_state*) malloc(sizeof(fd_state));
    if(!state)
        return NULL;
    memset(state, 0, sizeof(fd_state));
    return state;
}



void make_nonblocking(int fd)
{
    fcntl(fd, F_SETFL, O_NONBLOCK);
}

//写事件handler
int do_write(int fd, fd_state* state)
{
    while (state->n_written < state->write_upto)
    {
        /* code */
        ssize_t result = send(fd, state->buf + state->n_written, state->write_upto - state->n_written, 0);
        if(result < 0)
            if(errno == EAGAIN)
                return 0;
            return -1;
        state->n_written += result;
    }
    if(state->n_written == state->buffer_used)
        state->n_written = state->write_upto = state->buffer_used = 0;
    
    state->writing = 0;
    

    return 0;
}


//读事件handler
int do_read(int fd, fd_state* state)
{
    char buf[1024];
    int i;
    ssize_t result;
    while (true)
    {
        /* code */
        result = recv(fd, buf, 1024, 0);
        if(result < 0)
            break;
        for (int i = 0; i < result; i++)
        {
            /* code */
            if(state->buffer_used < sizeof(state->buf))
            {
                state->buf[state->buffer_used++] = rot13_char(buf[i]);

            }
            if(buf[i] == '\n')
            {
                state->writing = 1;
                state->write_upto = state->buffer_used;
            }
        }
    }
    if(result ==0 )
    {
        return 1;
    }
    else if (result < 0)
    {
        /* code */
        if(errno == EAGAIN)
            return 0;
        return -1;
    }  
    
    return 0;
}



void run()
{
    int listener;
    fd_state *state[FD_SETSIZE];
    sockaddr_in sin;
    fd_set readset, writeset, exset;
    int maxfd;


    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = 0;
    sin.sin_port = htons(12345);
    for (int i=0; i<FD_SETSIZE; i++)
        state[i] = nullptr;
    listener = socket(AF_INET, SOCK_STREAM, 0);
    make_nonblocking(listener);

    #ifndef WIN32
    {
        int one = 1;
        setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &one, sizeof(one));
    }
    #endif
    int rst = bind(listener, (sockaddr*)&sin, sizeof(sin));
    if(rst < 0)
    {
        cerr << "bind() error" << endl;
        close(listener);
        return;
    }

    rst = listen(listener, 16);
    if(rst < 0)
    {
        cerr << "listen() error" << endl;
        close(listener);
        return;
    }

    FD_ZERO(&readset);
    FD_ZERO(&writeset);
    FD_ZERO(&exset);
    
    while (true)
    {
        /* code */
        maxfd = listener;

        //重置FD_SET
        FD_ZERO(&readset);
        FD_ZERO(&writeset);
        FD_ZERO(&exset);

        FD_SET(listener, &readset);

        //遍历从0-FD_SETSIZE的所有socket描述符，如果存在，将其加入FD_SET
        for (int i = 0; i < FD_SETSIZE; i++)
        {
            /* code */
            if(state[i])
            {
                if(i > maxfd)
                    maxfd = i;
                FD_SET(i, &readset);
                FD_SET(i, &writeset);
                if(state[i]->writing)
                {
                    FD_SET(i, &writeset);
                }
            }
        }

        if(select(maxfd+1, &readset, &writeset, &exset, NULL) < 0)
        {
            cerr << "select() error!" << endl;
            //这里要close 所有socket描述符，为简化处理，暂时不处理
            return ;
        }

        //如果listener上有事件，表明有连接到达
        if(FD_ISSET(listener, &readset))
        {
            sockaddr_storage ss_client;
            socklen_t slen = sizeof(ss_client);
            int client = accept(listener, (sockaddr*)&ss_client, &slen);
            if(client < 0)
            {
                cerr << "accept() error!" << endl;
                return;
            }
            else if (client > FD_SETSIZE)
            {
                /* code */
                close(client);
            }
            else
            {
                make_nonblocking(client);
                state[client] = allock_fd_state();
                cout << "state " << client << " is " << state[client] << endl;
            }
        }

        //遍历0-maxfd的所有socket描述符，判断是否有事件发生
        for (int i = 0; i < maxfd+1; i++)
        {
            /* code */
            int result = 0;
            //listener事件已经处理过，并且只有读事件
            if(i == listener)
                continue;
            
            if(FD_ISSET(i, &readset))
            {
                result = do_read(i, state[i]);
            }
            if(result ==0 && FD_ISSET(i, &writeset))
            {
                result = do_write(i, state[i]);
            }
            if(result)
            {
                free(state[i]);
                state[i] = NULL;
                close(i);
            }
        }
    }
    

    
}

int main(int c, char **v)
{
    run();
    return 0;
}