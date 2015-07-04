microservice-playground
=======================
A project for Python/Falcon microservice that will be used to find best practices for development of such applications.
It will also contain microservices in other technologies for comparison and performance test projects.

# Układ prezentacji

## Czym będzie ta prezentacja
1. Bardzo krótkie przedstawienie mikroserwisów i PaaSa. Jak ludzi zaciekawi, to sobie doczytają.
1. ta prezentacja ma dać ludziom, który zaczynają wprowadzać mikroserwisy (albo tym, którzy już to zrobili, ale coś im nie idzie), zwięzłe wskazówki do rozwiązania praktycznych problemów
1. Skupię się na przedstawieniu konkretnych, Pythonowych przykładów, które sprawdziły się dla nas (lub mam nadzieję, że się sprawdzą). Wspomnę trochę o szerszym kontekście i wskażę dalsze źródła.
1. Nie zdążę, niestety, opowiedzieć o wszystkim, ale jeśli was zaciekawi tematyka mikroserwisów, to dam wam Pythonowe kawałki potrzebne do pracy.

## W skrócie o mikroserwisach
1. definicja z książki
1. co to 12-factor app
1. Co nam dają mikroserwisy?

## W skrócie o PaaSie
1. Co nam daje PaaS?
 * łatwe skalowanie
 * routing
 * łatwy deployment
 * weź jakąś oficjalną propagandę
1. Są różne PaaSy, ja będę pokazywał na przykładzie Cloud Foundry. Czym się charakteryzuje CF w skrócie? 

## Ogólny zarys dobrego rozwiązania z microservice'ami
1. dobre testy jednostkowe
1. testy jednoskowe
1. monitoring na produkcji (z latającymi co jakiś czas testami)

## General microservice work tips
1. *TODO (Iza)* Does Heroku or Azure or other PaaSes have the mechanism of binding applications to each other or to services? Also look at Google App Engine and Python Anywhere.
1. *TODO (Iza)* How does Cloud Foundry and Heroku assign processor time? Should we do tests on one or a few processors (of a VM)?
1. Stosować się oczywiście do 12-factor app i różnych mądrych porad (np. o testowaniu od Fowlera)
1. Stosować się do przykazań RESTa (kiedy używa się RESTa, co pewnie będzie się najczęściej działo)
1. Stosować umiar przy stosowaniu się do mądrych porad.
1. stosować zalecenie pojedynczego źródła prawdy, żeby można było wszystko robić asynchronicznie | ewentualnie tylko jeden może pisać
1. Z reusem mikroserwisów jest jak z klasami: to, że wydzieliłeś nie znaczy, że jest reusable (prezentacja o reusable code). W sumie nie wszystkie muszą być reusable.
1. Trzeba używać frameworku, który ma mało magii i można że stacka wyczytać, co poszło nie tak.
1. Używać frameworku, do którego łatwo robić testy jednostkowe.
1. Asynchroniczne wołanie/kolejki/service bus mogą się przydać w wielu sytuacjach. Zmniejszają liczbę bezpośrednich powiązań ułatwiając testowanie modułowe, chociaż nie są bez problemów (gdzie się podziała moja wiadomość?). Oczywiście trzeba je stosować tam, gdzie faktycznie się nadają. Czasem trzeba wołać asynchronicznie.
1. Fajnie mieć fizyczną tablicę z architekturą komponentów. Jak tylko ktoś coś zmienia to nakładamy. Jak nie siedzicie w jednym miejscu, to jakiś graf na wiki (np. Visio).

## Dlaczego Python się nadaje?
1. Swoboda testowania i pisania kodu
1. dobra obiektowość, ale do niczego nie jesteś zmuszany; jak masz coś wymokować, to można się osrać np. w Jacie a tu jest spoko
1. spring nie ma przewagi przydatnych feature'ów
1. krótki development, możliwość szybkich zmian w architekturze, łatwe prototypowanie
1. łatwiejsze zarządzanie strukturami danych (mapy, zbiory,listy)
1. zwięzłość dająca czytelność
1. zaawansowane struktury języka - domknięcia, metaklasy (ale to już jest wszędzie poza Javą)
1. niestety brak typowania zwiększa skomplikowanie wstępnej walidacji danych, ale bez niego też byłaby potrzebna
1. wystarczający performance? *TODO* trzeba zrobić benchmarki
 * Wszystko takie mniej więcej. I tak nie chodzi głównie o wydajność, a o to, żeby system działał sprawnie i mógł być szybko rozwijany.
 * Jak już się ustabilizuje i będziemy mieli miliony klientów to można newralgiczne komponenty zoptymalizować lub przepisać na coś szybszego - taka zaleta mikroserwisów.
 * *TODO* performancje Falcona z uWSGI (czyli ogólnie pojętej konfiguracji pythonowej) w porównaniu ze Springiem, NodeJSem i Go.
 * *TODO* zużycie pamięci pomiędzy zawodnikami jak wyżej.
 * Czas wykonywania się testów (przynajmniej dużo szybciej niż Springowe).
 * Nie używałem żadnych optymalizatorów w stylu PyPy, Nuitki, Cythona itp., a to mogłoby trochę poprawić wyniki.

## Taming microservices and PaaS with Python

### Selected language version, framework and server
You can, of course, use other Python version and another framework and be successful, I just find this configuration really neat.
1. *TODO* prepare sample Falcon app (downloader)
1. *TODO* show good falcon unit testing configuration (ddt, testtools)
1. Można w końcu Pythona 3!!! Bo mamy do czynienia z małymi (względnie) programami i można poeksperymentować. Poza tym Python 3 jest już bardzo szeroko wspierany przez poważne projekty. Wyjątkiem są niskopoziomowe, jak Gevent.
1. Falcon (bo dlaczego akurat taki framework spośród dziesiątek?)
 * backend w mikroserwisach powinien być prosty i bezstanowy - nie potrzebowałem jakiś rozbudowanych feature'ów
 * prostota jest zaletą; jasno widać przepływ (Flask robi kilka dziwnych rzeczy, np. wsadza body w inną zmienną w zależności od content type)
 * Falcon jest też dość nowy i dobrze zaprojektowany (Flask był dynamicznie rozbudowywany).
 * Falcon jest szybki (pokaż benchmark z innymi Pythonami)
 * Łatwo doklejać swoją funkcjonalność do Falcona przez jego prostotę.
1. uWSGI - bo jest szybki i lekki

### Communications
1. *TODO (Iza)* Strict input validation for Python - how to do it? Look into Cerberus, Colander and maybe other libraries. Can it work with Swagger to avoid schema definition duplication?
1. *TODO* Manageable communication between microservices. Generating clients from Swagger docs? Testing contracts and integration.
1. *TODO* Async (publish/subscribe, queues, actor models) communication in WSGI apps. Can they go along with HTTP? CF has NATS built in. Maybe also look at ZMQ and AMQP. What's the security model for queues? Can you send tokens through it? Will they be encrypted?
1. *TODO* Użycie biblioteki retrying albo tej drugiej do uodpornienia naszych aplikacji

### Testing and automation (Quality Assurance)
1. *TODO* dać przykład testów integracyjnych/kontraktowych
1. *TODO* Testy E2E w testowym środowisku po pushu. Powinny wracać do ostatniego stabilnego, jeśli coś pójdzie nie tak? Co jeśli trzeba wcisnąć na raz dwie zmiany?
1. *TODO* monitoring produkcji, okazyjne testy itp.
1. jak robić reuse kodu w innych komponentach? Może być swój własny PyPI (Python Package Index). Jest mowa o tym, że nie powinno się dzielić kodu, bo wprowadza to zależności między komponentami. Ale różne komponenty mogą być zależne od różnych wersji. Wtedy jest spoko.
1. Tricki z Pythonowym buildpackiem. Vendorowanie, co może iść nie tak? Modyfikacja buildpacka.
1.  What artifacts to store? How and where to store them? And use them?

### Misc
1. *TODO* Opisać wersjonowanie apek - VERSION w manifescie jest spoko?
1. *TODO* Pokazać jak może wygląda autoryzacja/uwierzytelnienie z Oauthem i PyJWT.
1. *TODO* How to elegantly pass authorization headers from REST resources to the models and their sub objects?
 * it seems that pre-request hook that set's some data in the request context and does some preliminary checks is OK.

### Metrics and log aggregation
1. Co to ELK stack?
1. Co to Logsearch?
1. *TODO* Jak zbierać logi do Logsearcha?
1. Co można z nich wyczytać i jak to zrobić?
1. *TODO* Sprawdzić, czy są jakieś tricki przy stawianiu Logsearcha. Pewnie są i trzeba się zastanowić, czy nie można ich pominąć.
1. *TODO* Jak formatować logi, żeby coś z nich ciekawego wyszło.

## Final remarks
1. dla nowych: jeśli macie rozwiązania, albo ich kombinacje, których jeszcze nie widzieliście, to może warto przygotować prezentację


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
1. Docker can throttle CPU time by relative share size or by assigning to a certain core (or both). More [here](https://goldmann.pl/blog/2014/09/11/resource-management-in-docker/)

# Benchmarking
Performance tests done with Gatling.

## Test applications
1. simplest possible that only returns a string
1. one that does some moderate calculations, like transforming JSON, iteration, etc., not number crunching
1. one that calls a slow data-base or waits to simulate long-lasting connections

## Test types
1. linear user increase
1. linear user increase with peaks
1. constant user number with peaks

