microservice-playground
=======================
A project for Python/Falcon microservice that will be used to find best practices for development of such applications.
It will also contain microservices in other technologies for comparison and performance test projects.

## To do
1. Check if testing Falcon is easier than Flask.
 * it seems so with, Falcom being more elegant, but Flask has contexts and stuff.
 * show a good testing configuration (ddt, testtools)
1. How to elegantly pass authorization headers from REST resources to the models and their sub objects?
 * it seems that pre-request hook that set's some data in the request context and does some preliminary checks is OK.
1. Does Heroku or Azure or other PaaSes have the mechanism of binding applications to each other or to services? Also look at Google App Engine and Python Anywhere.
1. How does Cloud Foundry and Heroku assign processor time?
1. Strict input validation for Python.
1. Benchmark: Falcon app on Docker / Vagrant / host to check how the rest of benchmarks should be done.
1. Benchmark: Spring Boot on Tomcat / Jetty
1. Check jar size of Spring Boot app.
1. Benchmark: memory usage of Spring Boot.
1. Benchmark: all combinations of Gunicorn / uWSGI with sync / async engines (gevent, tornado, asyncio?) with Falcon / Flask-Restful / wheezy.web
 * also check uWSGI and Gunicorn with PyPy or optimizing parts of the app with Nuitka, Numba or Cython
1. Check the size of the best Python candidate app with dependencies.
1. Benchmark: performance and memory usage on newest builds of Python for the best candidate combination.
1. Benchmark: Best Python candidates vs. NodeJS
1. Benchmark: test and deployment times for Spring and Python
1. Proper versioning
 * setting VERSION in the manifest or in environment after deployment
1. Checkout Python HAL library for getting higher levels of REST
1. Async (publish/subscribe, queues, actor models) communication in WSGI apps. Can they go along with HTTP? CF has NATS built in.
1. Dynamic statistics of apps with ELK stash and CF.
1. Communication between microservices. Generating clients from Swagger dosc? Testing contracts and integration.
1. How to set up your own PyPI (Python Package Index) for your organization?

## Findings
Nothing's here yet...

## Benchmarking
Performance tests done with Gatling.

### Test applications
* simplest possible that only returns a string
* one that does some moderate calculations, like transforming JSON, iteration, etc., not number crunching
* one that calls a slow data-base or waits to simulate long-lasting connections

### Test types
* linear user increase
* linear user increase with peaks
* constant user number with peaks

