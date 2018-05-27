#include <iostream>
#include <winsock2.h>
#include <stdio.h>
#include <string>
using namespace  std;

int main(int argc, char** argv) {
	WSADATA wsaData;
	WORD sockVersion = MAKEWORD(2,0);
	WSAStartup(sockVersion,&wsaData);
	
	SOCKET s = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
	if(s==INVALID_SOCKET){
		cout << "Socket of Fail" << endl;
		WSACleanup();
		return -1; 

	}
	
	sockaddr_in in;
	in.sin_family = AF_INET;
	in.sin_port = htons(8080);
	in.sin_addr.S_un.S_addr = INADDR_ANY;
	
	if(bind(s,(LPSOCKADDR)&in,sizeof(in)) == SOCKET_ERROR){
		cout << "Bind Of Fail" <<endl;
		return -1; 
	}
	if(listen(s,2) == SOCKET_ERROR){
		cout << "Listen Of Fail" <<endl;
		return -1; 
		
	}
	sockaddr_in request;
	int Addlen = sizeof(request);
	SOCKET client;
	char text[] = "Server of dome";
	
	while(1){
		
		client = accept(s,(SOCKADDR*)&request,&Addlen);
		if(client == INVALID_SOCKET){
			cout << "Listen Of Fail" <<endl;
		return -1; 
		}
		
		cout << "have a accept in here" << inet_ntoa(request.sin_addr )<< endl;
		send(client,text,strlen(text),0);
		closesocket(client);
		
		
	}
	
	closesocket(s);
	WSACleanup();
	
	
	
	
	while(1){
	}
	return 0;
}
