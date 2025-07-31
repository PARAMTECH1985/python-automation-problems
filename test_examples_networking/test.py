'''
service ip[lb ip]
2 servers[backend servers]
1 client
'''
import os
import requests

class TestService:
    def is_pingable(self,ip):
        os.system("ping ip1")
        return True

    def is_restcall_request(self,service):
        requests.get()

    def test_lb_service(self):
        print("request1 goes to lb ip-->ip1")
        print("request1 goes to lb ip-->ip2")
        print("request1 goes to lb ip-->ip3")
        print("request1 goes to lb ip-->ip3")
        ip1=""
        ip2 =""
        ip3 = ""
        ip4 = ""
        os.system("ping ip1")
        os.system("ping ip2")
        os.system("ping ip3")
        os.system("ping ip4")
        assert(True, self.is_pingable(ip1))
        assert(True, self.is_pingable(ip2))
        assert (True, self.is_pingable(ip3))
        assert (True, self.is_pingable(ip4))
        print("logs level verification")
        with open("test.log","r") as f:
            print(f.readline())

        #wget/curl-->http request
        #Rest Call Level
        #Verify Response Data
        #Verify request is going by lb




