import socket

# constants used for protocol messages
class prot:
    user_handshake = 'hi'
    user_leave = 'by'
    addr_request = 'ar'
    server_handshake = 'hi'
    user_userlist = 'ul'
    user_roomlist = 'rl'
    user_roomcreate = 'rc'
    user_roomjoin = 'rj'

users = {}
rooms = {}
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server launched on specified port
def launch(serv_port):
    # create socket
    serv_socket.bind(('0.0.0.0', serv_port))
    print('> Server listening for incoming requests...')
    # receive and parse messages
    while True:
        # receive bytes and address pair
        bytes_and_addr = serv_socket.recvfrom(1024)
        # split into bytes and address
        clnt_msg = bytes_and_addr[0]
        clnt_addr = bytes_and_addr[1]
        parse_msg(clnt_msg, clnt_addr)

# parses received message
def parse_msg(clnt_msg, clnt_addr):
    # split into tokens
    split_msg = clnt_msg.decode().split()
    command = split_msg[0]
    if command == prot.user_handshake:
        # new user registering to server
        if len(split_msg) == 2:
            u_name = split_msg[1]
            negotiate_username(clnt_addr, u_name)
        # ignore if invalid args
    elif command == prot.user_leave:
        # existing user wants to leave server
        send_msg(clnt_addr, prot.user_leave)
        remove_user(clnt_addr)
    elif command == prot.addr_request:
        # user requests address of user
        if len(split_msg) == 2:
            u_name = split_msg[1]
            send_address(clnt_addr, u_name)
    elif command == prot.user_userlist:
        # send userlist to user
        send_userlist(clnt_addr)
    elif command == prot.user_roomlist:
        # send roomlist to user
        send_roomlist(clnt_addr)
    elif command == prot.user_roomcreate:
        # cereat new room
        if len(split_msg) == 2:
            add_room(clnt_addr, split_msg[1])
    elif command == prot.user_roomjoin:
        if len(split_msg) == 2:
            join_room(clnt_addr, split_msg[1])

# add user to specified room
def join_room(clnt_addr, r_name):
    if not r_name in rooms:
        # invalid room name
        send_msg(clnt_addr, prot.user_roomjoin)
        return
    # valid room name
    # remove client from all rooms
    for room in rooms:
        if clnt_addr in rooms[room]:
            rooms[room].remove(clnt_addr)
    # clear peer list of client
    send_msg(clnt_addr, prot.user_roomjoin+' __clear_peers__')
    # add user to room
    rooms[r_name].append(clnt_addr)
    # send peer addresses
    for addr in rooms[r_name]:
        if addr != clnt_addr:
            send_msg(clnt_addr, prot.user_roomjoin+' '+addr[0]+' '+str(addr[1]))

# adds new room and adds user to this room
def add_room(clnt_addr, r_name):
    if r_name in rooms:
        # room already exists
        send_msg(clnt_addr, prot.user_roomcreate)
        return
    # create room
    rooms[r_name] = []
    send_msg(clnt_addr, prot.user_roomcreate+' '+r_name)

# send userlist to requesting user
def send_userlist(clnt_addr):
    if len(users)  == 0:
        send_msg(clnt_addr, prot.user_userlist)
        return
    for key in users.keys():
        send_msg(clnt_addr, prot.user_userlist + ' ' + key)

# send roomlist to requesting user
def send_roomlist(clnt_addr):
    if not rooms:
        send_msg(clnt_addr, prot.user_roomlist)
        return
    for room in rooms.keys():
        send_msg(clnt_addr, prot.user_roomlist + ' ' + room)

# send message as text to specified receiver
def send_msg(clnt_addr, serv_msg):
    serv_socket.sendto(serv_msg.encode(), clnt_addr)

# negoatiation of username with new clients
def negotiate_username(clnt_addr, u_name):
    if u_name in users:
        # username already taken -> decline with prot.server_handshake without username
        send_msg(clnt_addr, prot.server_handshake)
        return
    # username free -> ack username with prot.server_handshake + accepted username
    add_user(clnt_addr, u_name)
    send_msg(clnt_addr, prot.server_handshake+' '+u_name)

# add user to users
def add_user(clnt_addr, u_name):
    users[u_name] = clnt_addr
    print('> Add user: '+u_name)

# remove user from users
def remove_user(clnt_addr):
    del_name
    for u_name, u_addr in users.items():
        if u_addr  == clnt_addr:
            del_name = u_name
            break
    del users[del_name]
    print('Removed user: '+u_name)

# send the address of the user name to the client
def send_address(clnt_addr, u_name):
    # user exists -> gett addr and send to client
    if u_name in users:
        u_addr = users[u_name]
        send_msg(clnt_addr, prot.addr_request+' '+u_addr[0]+' '+str(u_addr[1]))
        return
    # usere doesn't exist -> inform client
    send_msg(clnt_addr, prot.addr_request)
