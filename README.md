twunnel-app-openshift
=====================

- rhc app create -a twunnel -t diy-0.1
- cd twunnel
- git remote add upstream -m master git://github.com/jvansteirteghem/twunnel-app-openshift.git
- git pull -s recursive -X theirs upstream master
- git push
