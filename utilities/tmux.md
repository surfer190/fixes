# Tmux

A Terminal multiplexer, it allows multiple terminal sessions to be accessed from a single window.
It is useful to detach processes from their terminals and run more than 1 command line program at the same time.

Remember `C-b` means `ctrl + b`.

## Session Management

Create a new session

    tmux new -s my_session

List sessions

    tmux list-sessions

choose sessions from a list

    C-b s

Attach to a session

    tmux attach -t my_session

Switch to an existing session

    tmux switch -t my_session

Detach session

    tmux detach
    
    C-b d

Choose from available sessions

    C-b s

## Windows

Tmux has tabs, but it calls them windows.
It is a wise thing to name your sessions and windows about things you are working on.

Create a new window

    tmux new-window
    
    C-b c

Choose a window from a list

    C-b w

List windows

    tmux list-windows

Select a window

    tmux select-window -t :0-9
    
    C-b 1..

Rename a window

    tmux rename-window -t old_window test-window

## Panes

Split the window into 2 vertical panes

    tmux split-window
    
    C-b "

Split a window into 2 horizontal panes

    tmux split-window -h
    
    C-b % 

Swap a pane with another in a specified direction

    tmux swap-pane -[UDLR]
    
    C-b { (left)
    C-b } (right)

> UDLR means Up, Down, Left, Right

Change focus to another pane

    tmux select-pane -R [UDLR]
    
    C-a (arrow keys)

Change focus to another pane by number

    tmux select-pane -t :.1

## Help

List commands

    tmux list-commands

List out every session, window, pane, its pid

    tmux info

Reload the current tmux configuration

    tmux source-file ~/.tmux.conf

## Lets put it into practice

We will log into our server, split the panes.
One pane will view `/var/log/syslog` the other will write a message to it.

1. SSH to your server

    ssh backup 

2. Enter `tmux`

    tmux

3. Split the pane horizontally

    C-b % (means `ctrl + b`, then press `%`)

4. Tail the logs

    tail -f /var/log/syslog

5. Move to the other pane

    C-b left (means `ctrl + b`, then press `left arrow`)

6. Log a message

    logger hello world

You should see the message pop up on the other pane

### Source

* [A Tmux Crash Course](https://thoughtbot.com/blog/a-tmux-crash-course)
* [Tmux Cheatsheet](https://gist.github.com/andreyvit/2921703)
* [Write to Syslog](https://www.cyberciti.biz/tips/howto-linux-unix-write-to-syslog.html)
