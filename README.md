# microtrain
The project involves creation of three microservices that meet the business requirements described below.

## Microservices description

### Train
Simulates the work of a train in a simplified way.
The only task is to send messages to the queue, it has no HTTP interface.

- Every 10 seconds a message about the current train speed is sent.
- Every 180 seconds a message about a station to which the train is approaching is sent.

### Headquarter
TODO

### Gatekeeper
TODO

## Quick Start

Review the set up guides to configure the app:

1. [setup-with-docker.md](setup-with-docker.md)
