microservice-playground
=======================
A project for Python/Falcon microservice that will be used to find best practices for development of such applications.
It will also contain microservices in other technologies for comparison and performance test projects.

# Presentation draft

## Ogólne

### Ustalone
* ta prezentacja ma dać ludziom, który zaczynają wprowadzać mikroserwisy (albo tym, którzy już to zrobili, ale coś im nie idzie), zwięzłe wskazówki do rozwiązania praktycznych problemów
* dla nowych: jeśli macie rozwiązania, albo ich kombinacje, których jeszcze nie widzieliście, to może warto przygotować prezentację
* Fajnie mieć tablicę z architekturą komponentów

### TODO
1. (Iza) Does Heroku or Azure or other PaaSes have the mechanism of binding applications to each other or to services? Also look at Google App Engine and Python Anywhere.
1. Co mówią księgi?



## What infrastructure and automation you need to set up to go along smoothly;

### Ustalone
* Opisać wersjonowanie apek
* testy w testowym środowisku po pushu. Powinny wracać do ostatniego stabilnego, jeśli coś pójdzie nie tak. Co jeśli trzeba wcisnąć na raz dwie zmiany?
* Pokazać jak może wygląda autoryzacja/uwierzytelnienie z Oauthem i PyJWT.
* jak robić reuse kodu w innych komponentach? Może być swój własny PyPI (Python Package Index)
* jakie artefakty i gdzie przechowywać?

### TODO
1. Check if testing Falcon is easier than Flask.
 * it seems so with, Falcom being more elegant, but Flask has contexts and stuff.
 * show a good testing configuration (ddt, testtools)
1. Proper versioning
 * setting VERSION in the manifest or in environment after deployment
1. Manageable communication between microservices. Generating clients from Swagger docs? Testing contracts and integration.
1. How to elegantly pass authorization headers from REST resources to the models and their sub objects?
 * it seems that pre-request hook that set's some data in the request context and does some preliminary checks is OK.
1. How to set up your own PyPI (Python Package Index) for your organization?
1. What artifacts to store? How and where to store them? And use them?



## How thinking in PaaS terms can lead to robust and scalable designs

### Ustalone
* stosować zalecenie pojedynczego źródła prawdy, żeby można było wszystko robić asynchronicznie | ewentualnie tylko jeden może pisać
* Z reusem mikroserwisów jest jak z klasami: to, że wydzieliłeś nie znaczy, że jest reusable (prezentacja o reusable code). W sumie nie wszystkie muszą być teusable
* Trzeba używać frameworku, który ma mało magii i można że stacka wyczytać, co poszło nie tak.

### TODO
1. Async (publish/subscribe, queues, actor models) communication in WSGI apps. Can they go along with HTTP? CF has NATS built in. Maybe also look at ZMQ and AMQP. What's the security model for queues? Can you send tokens through it? Will they be encrypted?



## How to get real time metrics of your apps

### Ustalone
* Co to ELK stack?
* Co to Logsearch?
* Jak zbierać logi do Logsearcha?
* Co można z nich wyczytać i jak to zrobić?

### TODO
1. Sprawdzić, czy są jakieś tricki przy stawianiu Logsearcha. Pewnie są i trzeba się zastanowić, czy nie można ich pominąć.
1. Jak wysyłać logi do Logsearcha?
1. Jak formatować logi, żeby coś z nich ciekawego wyszło.



## What makes Python good for microservice

### Ustalone
* Swoboda testowania i pisania kodu
* dobra obiektowość, ale do niczego nie jesteś zmuszany; jak masz coś wymokować, to można się osrać np. w Jacie a tu jest spoko
* spring nie ma przewagi przydatnych feature'ów
* krótki development, możliwość szybkich zmian w architekturze, łatwe prototypowanie
* łatwiejsze zarządzanie strukturami danych (mapy, zbiory,listy)
* wystarczający performance?
* zwięzłość dająca czytelność
* zaawansowane struktury języka - domknięcia, metaklasy (ale to już jest wszędzie poza Javą)
* niestety brak typowania zwiększa skomplikowanie wstępnej walidacji danych, ale bez niego też byłaby potrzebna

### TODO
1. (Iza) Strict input validation for Python - how to do it? Look into Cerberus and other libraries. Can it work with Swagger to avoid schema definition duplication?



## What is Python's performance relative to some alternatives.

### Ustalone
Wszystko takie mniej więcej. I tak nie chodzi głównie o wydajność, a o to, żeby system działał sprawnie i mógł być szybko rozwijany.
Jak już się ustabilizuje i będziemy mieli miliony klientów to można newralgiczne komponenty zoptymalizować lub przepisać na coś szybszego - taka zaleta mikroserwisów.
* Dlaczego wybrałem taką a nie inną konfigurację dla Pythona?
* Jak ma do Springa/NodeJS/Go?
* Co ze zużyciem pamięci?
* Czas wykonywania się testów (przynajmniej dużo szybciej niż Springowe).

### TODO
1. (Iza) How does Cloud Foundry and Heroku assign processor time? Should we do tests on one or a few processors (of a VM)?
1. Benchmarki z "Optional Todos", ale tylko niektóre.




# Optional Todos
1. Checkout Python HAL library for getting higher levels of REST
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

# Findings
* Docker can throttle CPU time by relative share size or by assigning to a certain core (or both). More [here](https://goldmann.pl/blog/2014/09/11/resource-management-in-docker/)

# Benchmarking
Performance tests done with Gatling.

## Test applications
* simplest possible that only returns a string
* one that does some moderate calculations, like transforming JSON, iteration, etc., not number crunching
* one that calls a slow data-base or waits to simulate long-lasting connections

## Test types
* linear user increase
* linear user increase with peaks
* constant user number with peaks

