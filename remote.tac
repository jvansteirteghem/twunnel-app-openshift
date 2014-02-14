from twisted.application import service
import os
import twunnel.dns_resolver
import twunnel.logger
import twunnel.remote_proxy_server

configuration = \
{
    "LOGGER":
    {
        "LEVEL": 2
    },
    "DNS_RESOLVER":
    {
        "HOSTS":
        {
            "FILE": ""
        },
        "SERVERS":
        [
            # {
                # "ADDRESS": "",
                # "PORT": 0
            # }
        ]
    },
    "PROXY_SERVERS":
    [
        # {
            # "TYPE": "HTTPS",
            # "ADDRESS": "",
            # "PORT": 0,
            # "ACCOUNT":
            # {
            #     "NAME": "",
            #     "PASSWORD": ""
            # }
            
            # "TYPE": "SOCKS4",
            # "ADDRESS": "",
            # "PORT": 0,
            # "ACCOUNT":
            # {
            #     "NAME": ""
            # }
            
            # "TYPE": "SOCKS5",
            # "ADDRESS": "",
            # "PORT": 0,
            # "ACCOUNT":
            # {
            #     "NAME": "",
            #     "PASSWORD": ""
            # }
        # }
    ],
    "REMOTE_PROXY_SERVER":
    {
        # "TYPE": "SSH",
        # "ADDRESS": "",
        # "PORT": 0,
        # "KEY":
        # {
        #     "PUBLIC":
        #     {
        #         "FILE": "",
        #         "PASSPHRASE": ""
        #     },
        #     "PRIVATE":
        #     {
        #         "FILE": "",
        #         "PASSPHRASE": ""
        #     }
        # },
        # "ACCOUNTS":
        # [
        #     {
        #         "NAME": "",
        #         "PASSWORD": "",
        #         "KEYS":
        #         [
        #             {
        #                 "PUBLIC":
        #                 {
        #                     "FILE": "",
        #                     "PASSPHRASE": ""
        #                 }
        #             }
        #         ],
        #         "CONNECTIONS": 0
        #     }
        # ]
        
        "TYPE": "WS",
        "ADDRESS": str(os.environ["OPENSHIFT_DIY_IP"]),
        "PORT": int(os.environ["OPENSHIFT_DIY_PORT"]),
        "ACCOUNTS":
        [
            # {
            #     "NAME": "",
            #     "PASSWORD": ""
            # }
        ]
        
        # "TYPE": "WSS",
        # "ADDRESS": "",
        # "PORT": 0,
        # "CERTIFICATE":
        # {
        #     "FILE": "",
        #     "KEY":
        #     {
        #         "FILE": ""
        #     }
        # },
        # "ACCOUNTS":
        # [
        #     {
        #         "NAME": "",
        #         "PASSWORD": ""
        #     }
        # ]
    }
}

twunnel.logger.configure(configuration)

resolver = twunnel.dns_resolver.createResolver(configuration)
if resolver is not None:
    twunnel.dns_resolver.setDefaultResolver(resolver)

class ApplicationService(service.Service):
    def __init__(self, configuration):
        twunnel.logger.log(3, "trace: ApplicationService.__init__")
        
        self.port = twunnel.remote_proxy_server.createPort(configuration)
    
    def startService(self):
        twunnel.logger.log(3, "trace: ApplicationService.startService")
        
        if self.port != None:
            self.port.startListening()
    
    def stopService(self):
        twunnel.logger.log(3, "trace: ApplicationService.stopService")
        
        if self.port != None:
            self.port.stopListening()

application = service.Application("remote")
applicationService = ApplicationService(configuration)
applicationService.setServiceParent(application)