# Projekt: Helpdeskt / ticketing sustav
## Članovi tima
- Dominik Karimović
- Tony Vargek
- Tin Fićok
- Petar Mikolčević
- Antonio Meleš

## GitHub repozitorij
- Link: https://github.com/pero12580/PR1
- Svi članovi dodani: DA

## User storyji
US-01 Kao user, želim se moći prijaviti i ostaviti ticket (zatražit pomoć).
      kako bih mogao doći u kontakt s IT službom.
US-02 Kao user, želim moći vidjet status svog ticketa (delivered, seen, assigned, solved).
US-03 Kao support, želim se moći prijaviti i vidjeti sve tickete stavljene od usera
      kako bi ih mogao rješiti.
US-04 Kao admin, želim se moći prijaviti i assignati tickete supportu kako bi ih
      mogli rješiti. 
US-05 Kao admin, želim moći dodati prioritet ticketa.

## Funkcijski zahjtevi
FZ-01 Sustav mora omogućiti prijavu.
FZ-02 Sustav omogućuje tri razine pristupa (korisnik, support, admin).
FZ-03 Sustav mora omogućiti useru da doda ticket (dodati naslov, opis problema, eventualno attachment).
FZ-04 Sustav nakon poslanog ticketa od usera mora vratiti povratnu informaciju da je ticket zaprimljen.
FZ-05 Sustav mora omogućiti vidljivost statusa svog ticketa.
FZ-06 Sustav mora omogućiti supportu vidljivost ticketa koji su mu assigned.
FZ-07 Sustav mora omogućiti adminu da sortira tickete po vremenu primitka.
FZ-08 Sustav mora omogućiti adminu da dodjeli supportu određeni ticket.
FZ-09 Sustav mora omogućiti adminu da doda prioritet ticketa.
FZ-10 Sustav mora spriječiti dodjeljivanje istog ticketa više članova supporta.

## Nefunkcijski zahtjevi
NZ-01 Sustav očitava X ticketa unutar 2s vremena u 95% slučajeva.
NZ-02 Odgovor korisniku mora biti vidljiv unutar aplikacije bez iznimke.
NZ-03 Sustav zahtjeva prijavu svakih 30 minuta
NZ-04 Sustav mora biti oblikovan kao microservice i containerizied.
NZ-05 Kreiranje ticketa mora biti ispod 5 koraka.
NZ-06 Sustav mora proći preko 95% testova.
NZ-07 Sustav ne smije uzeti više od 5 minuta slanja ticketa, te vraćanja odgovora.


## Taskovi
TASK-01 Napraviti model baze za helpdesk / ticketing sustav
TASK-02 Implementirati API za dohvaćanje ticketa
TASK-03 Implementirati API za registraciju korisnika.
TASK-04 Implementirati API za dohvaćanje supporta od strane admina
TASK-05 Implementirati API za dodjeljivanje ticketa supportu
TASK-06 Napisati testove za sustav/kod 
TASK-07 Implementirati autorizaciju korisnika
TASK-08 Containerize aplikaciju
TASK-09 Kreirati sučelje

## Raspodjela zadataka
Dominik: TASK-07, TASK-09, NZ-05, NZ-03, FZ-01, FZ-02
Petar: TASK-06, NZ-01, NZ-06, FZ-04, FZ-05, FZ-06
Antonio: TASK-01, TASK-08, NZ-04, FZ-03, FZ-06, FZ-10
Tin: TASK-04, TASK-05, NZ-07, FZ-04, FZ-07, FZ-10
Tony: TASK-02, TASK-03, NZ-02, FZ-03, FZ-08, FZ-09