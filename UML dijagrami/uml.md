# Akteri / glavne funkcionalnosti (klase)  / ključni entiteti 
## Akteri
- Korisnik
- Admin
- Support

## Glavne funkcionalnosti
- prijava
- autentikacija
- kreiranje ticketa
- pregledavanje ticketa
- odgovaranje na ticket
- dodjela ticketa
- dodjela važnosti ticketa

## Ključni entiteti
- User entitet
- Ticket entitet
- Attachment entitet


# Use Case dijagram
## Use case kod
```
@startuml
left to right direction
actor "Korisnik" as User
actor "Admin" as Admin
actor "Support" as Support

rectangle "Helpdesk sustav" {
  usecase "Prijava" as UC1
  usecase "Autentikacija" as Auth 
  usecase "Kreiranje ticketa" as UC2
  usecase "Pregledavanje ticketa" as UC3
  usecase "Odgovaranje na ticket" as UC4
  usecase "Dodjeljivanje ticketa" as UC5
  usecase "Dodjeljivanje važnosti ticketu" as Važnost
}

User -- UC1
Admin -- UC1
Support -- UC1
UC1 ..> Auth : <<include>>

User -- UC2
User -- UC3

Support -- UC3
Support -- UC4

Admin -- UC3
Admin -- UC5
Važnost ..> UC5 : <<extend>>
@enduml
```
# Sequence dijagram
## Sequence kod
```
@startuml
actor User
participant UI as "Web UI"
participant API as "API service"
database DB as "Data Base"
 
 
User -> UI : openForm()
activate UI
UI -> API : submitTicket(data)
activate API
 
 
alt valid data
    API -> DB : saveTicket()
    activate DB
    DB --> API : ticketID
    deactivate DB
    API --> UI : success(ticketID)
else invalid data
    API --> UI : validationError
end
 
 
UI --> User : answer
deactivate API
deactivate UI
@enduml
```
# Class dijagram
## Class kod
```
@startuml
class User {
  - id : String
  - username : String
  - password : String
  - email : String
  - role : String
  + login() : boolean
}

class EndUser {
  + createTicket() : void
  + register() : boolean
}

class Support {
  + viewAssignedTickets() : List<Ticket>
  + updateTicketStatus() : void
}

class Admin {
  + assignTicket() : void
  + setPriority() : void
  + sortTicket() : void
}

class Attachment {
  - id : String
  - fileName : String
  - filePath : String
}

class Ticket {
  - id : String
  - title : String
  - description : String
  - status : String
  - priority : String
  - createdAt : Date
  + changeStatus() : void

}

EndUser --|> User
Admin --|> User
Support --|> User

EndUser "1" --> "0..*" Ticket : creates
Ticket "1" *-- "0..*" Attachment
Ticket "0..1" --> "1" Support : assignedTo
Admin "1" --> "0.." Ticket : manages
@enduml
```