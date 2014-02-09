# twunnel-app-openshift

## install

```
rhc app create -a <APPLICATION-NAME> -t diy-0.1
cd <APPLICATION-NAME>
git remote add upstream -m master git://github.com/jvansteirteghem/twunnel-app-openshift.git
git pull -s recursive -X theirs upstream master
# configure <REMOTE.TAC-FILE>
git push
```