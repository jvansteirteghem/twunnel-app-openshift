# twunnel-app-openshift

## install

```
rhc app create -a <APPLICATION-NAME> -n <NAMESPACE-NAME> -t diy-0.1
cd <APPLICATION-NAME>
git remote add upstream -m master git://github.com/jvansteirteghem/twunnel-app-openshift.git
git pull -s recursive -X theirs upstream master
# configure <REMOTE.TAC-FILE>
git push
```

## !!!

- the remote proxy server type is ```WSS```
- the remote proxy server address is ```<APPLICATION-NAME>-<NAMESPACE-NAME>.rhcloud.com```
- the remote proxy server port is ```8443```
- the remote proxy server is stopped every 48 hours