# Nansen

`nansen`

<pre>
  ┬ ECS:
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

Nansen uses ECS to display a tree of clusters, machines, and tasks and allows you to directly ssh (and, if needed, docker exec), to arrive in any machine or docker in AWS.

To use, you need to be using ECS

You can also use `nansen <matcher>` to only show some hosts clusters, and `nansen <matcher>` to perform that operation on the host when selected.  



