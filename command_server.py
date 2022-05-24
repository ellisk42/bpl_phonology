import random
import time
import threading
import socket
import os
import sys
import SocketServer
import subprocess32 as subprocess



COMMANDSERVERPORT = 1540
PASSWORD = "superduper ultra-secure amazingly cryptographic password"
COMMANDSERVERSEMAPHORE = None
MAXIMUMNUMBEROFCONNECTIONS = None

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class CommandHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        p = self.rfile.readline()
        if p.strip() != PASSWORD:
            self.wfile.write("Bad password!")
            return
        
        k = self.rfile.readline()
        if k.strip() == "?":
            self.wfile.write(str(MAXIMUMNUMBEROFCONNECTIONS))
        else:
            timeout = float(k)
            k = self.rfile.readline()
            
            COMMANDSERVERSEMAPHORE.acquire()
            startTime = time.time()
            dt = None
            try:
                subprocess.call(k,
                                shell=True,
                                timeout=(None if timeout == float('inf') else timeout))
            except subprocess.TimeoutExpired:
                dt = "timeout"                
            dt = dt or time.time() - startTime
            self.wfile.write(str(dt))
            COMMANDSERVERSEMAPHORE.release()

def command_server_running():
    import psutil
    for p in psutil.process_iter(attrs=['name','cmdline']):
        if p.info['name'] == 'python' and 'command_server.py' in p.info['cmdline'] and 'KILL' not in p.info['cmdline']:
            return True
    return False

def start_server(CPUs):
    if command_server_running():
        print " [+] Found existing command server:", int(send_to_command_server("?")), "CPUs"
        return

    time.sleep(0.2 + random.random())
    if command_server_running():
        print " [+] Found existing command server:", int(send_to_command_server("?")), "CPUs"
        return
    
    print " [+] Launching command server w/ %d CPUs"%CPUs
    os.system("python command_server.py %d &"%CPUs)
    time.sleep(0.5)

def kill_servers():
    import psutil
    ps = []
    for p in psutil.process_iter(attrs=['name','cmdline']):
        if p.info['name'] == 'python' and 'command_server.py' in p.info['cmdline'] and 'KILL' not in p.info['cmdline']:
            ps.append(p.pid)
    for p in ps:
        print " [+] Killing command server with PID %d"%p
        os.system("kill -9 %s"%p)

def send_to_command_server(k,timeout=None):
    assert k == "?" or timeout is not None, "DEPRECATED: we now require timeouts"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if timeout: k = "%f\n%s"%(timeout,k)
    
    try:
        # Connect to server and send data
        sock.connect(("localhost", COMMANDSERVERPORT))
        sock.sendall(PASSWORD + "\n" + k + "\n")
        # Receive data from the server and shut down
        received = sock.recv(1024)
    finally:
        sock.close()

    try:
        return float(received)
    except:
        return received


        

if __name__ == "__main__":
    assert len(sys.argv) == 2, "Expected exactly one commandline argument: number of CPUs or KILL"
    a = sys.argv[1]
    if a == "KILL":
        kill_servers()
        sys.exit(0)
        
    CPUs = int(a)
    MAXIMUMNUMBEROFCONNECTIONS = CPUs

    host = "localhost"
    COMMANDSERVERSEMAPHORE = threading.Semaphore(CPUs)

    print("Command server reporting in, starting w/ %d CPUs"%CPUs)
    server = ThreadedTCPServer((host,COMMANDSERVERPORT),CommandHandler)
    server.serve_forever()
    
    
    
