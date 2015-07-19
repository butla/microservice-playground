microservice-playground
=======================
A project for Python/Falcon microservice that will be used to find best practices for development of such applications.
It will also contain microservices in other technologies for comparison and performance test projects.

# Findings
1. Docker can throttle CPU time by relative share size or by assigning to a certain core (or both). More [here](https://goldmann.pl/blog/2014/09/11/resource-management-in-docker/)
1. Multiple cores are available for the app in CF. uWSGI communicated that while starting.

