# Nansen

<pre>
  ┬ In the test dc:
  ├─┬ test-5-f6d0fda5
  │ └─  system5
  ├─┬ test-6-c95dfb8b
  │ └─  system6
  ├─┬ test-7-a6f6ae43
  │ └─  system7
  ├─┬ test-8-f039bf15
  │ ├─  system8
  ┴ └─  system9
</pre>

To install, run `sudo python setup.py install`

Nansen uses registrator, consul, docker and ssh to display a tree of machines and allow you to ssh (and, if needed, nsenter), to arrive in any machine or docker in your local consul data center. 

To use, you need registrator, and for registrator to have tagged all docker instances with the 'registrator' tag, and have a ssh service registered in consul. This can be done, for example, with 'util/ssh.json'




