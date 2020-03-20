# microtrain
The project involves creation of three microservices that meet the business requirements described below.

## Microservices description

### Train
Simulates the work of a train in a simplified way.
The only task is to send messages to the queue, it has no HTTP interface.

- Every 10 seconds a message about the current train speed is sent.
- Every 180 seconds a message about a station to which the train is approaching is sent.

### Headquarter
Monitoring system for trains. It listens for new messages coming to message queue. Based on them,
it performs certain business rules, it doesn't have an HTTP interface.

- Messages about the actual speed of the train along with the current time are saved to a text file according to the following rules:
   - values in the range of 0.0-40.0 are saved to "slow.log"
   - values in the range of 40.1-140.0 are saved to "normal.log"
   - values in the range of 140.1-180.0 are saved to "fast.log"
-  Messages that the train is approaching the station are handled according to following scenario:
   - time of receiving the message is saved to "info.log"
   - microservice sends GET request to Gatekeeper with query about current state of railway barrier.
     - if barrier is open, closing POST request is sent to Gatekeeper 
     - if barrier is closed, it saves this information in "info.log" and goes to the next section
   - after 10 seconds, opening POST request is sent to Gatekeeper
   - barrier opening time is saved to "info.log"

### Gatekeeper
Doesn't communicate with message queue, has an HTTP interface. Gatekeeper provides following methods:

- [GET] /api/v1/barrier - gives the current status of the barrier in a format: {"status": state}
- [POST] /api/v1/barrier - opens or closes the barrier. 

The current state of the barrier with the last update time should be stored in a database in a dedicated table.

## Quick Start

Review the set up guides to configure the app:

1. [setup-with-docker.md](setup-with-docker.md)
