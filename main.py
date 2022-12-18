import grpc
import RFM_pb2_grpc
import RFM_pb2
from concurrent import futures
import socket

import configparser
import json
import base64

import db

import queue1


def GetIp(n):

    with open('servers.json') as f:
        servers = json.load(f)

    for server in servers:
        if server["id"] == n:
            try:
                sock = socket.socket()
                sock.connect((server["ip"], server["port"]))
                sock.send(b"ok?")
                sock.close()
                return server["ip"]
            except:
                return "-1"


def getFile(i):
    obj = {"id": "", "path": "", "newPath": "", "type": 0, "file": ""}

    # собираем в него все содежимое
    obj["id"] = i.id
    obj["path"] = i.path
    obj["newPath"] = i.newPath
    obj["type"] = i.type
    obj["file"] = base64.b64encode(i.file).decode('ascii')

    return obj


# описание процедуры
class RemoteFolderManager(RFM_pb2_grpc.RemoteFolderManagerServicer):
    def actionF(self, request, context):

        config = configparser.ConfigParser()
        config.read("config.ini")

        obj = getFile(request)

        # создание дирректории
        if obj["type"] == 1:
            tup = db.getServ(config, obj["id"])

            id = tup[0]
            id_f = tup[1]

            if id == -3:
                return RFM_pb2.Resp(code=-3, diskId="")


            obj["ip"] = context.peer()

            ip = GetIp(id)
            obj["id"] = id_f
            queue1.send(obj, id, ip)
            return RFM_pb2.Resp(code=1, diskId=id_f)


        id = db.GetIPServer(config, obj["id"])

        # если хотим создать операцию с папкой а её нет то кидаем код ошибки
        if id == -1:
            return RFM_pb2.Resp(code=-1, diskId="")

        ip = GetIp(id)

        if ip == "-1":
            return RFM_pb2.Resp(code=-2, diskId="")

        obj["ip"] = context.peer()
        queue1.send(obj, id, ip)
        print(ip + " " + str(obj["id"]))
        return RFM_pb2.Resp(code=1, diskId="")


def server():
    config = configparser.ConfigParser()
    config.read("config.ini")

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=[
            ('grpc.max_send_message_length', 50*1024*1024),
                 ('grpc.max_receive_message_length', 50*1024*1024)
        ])

    RFM_pb2_grpc.add_RemoteFolderManagerServicer_to_server(RemoteFolderManager(), server)
    server.add_insecure_port(config['Conn']['ip'])
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server()
