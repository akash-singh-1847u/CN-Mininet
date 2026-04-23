# CN-Mininet  Dynamic Host Blocking

# Akash Singh
# SRN-PES2UG24CS042

## Problem Statement

This project implements a **Dynamic Host Blocking System** using Software Defined Networking (SDN). The objective is to detect hosts generating excessive traffic and block them dynamically by installing appropriate OpenFlow rules in the switch.
---

## Tools & Technologies

* Mininet (Network Emulator)
* POX Controller
* OpenFlow Protocol
* Ubuntu (Virtual Machine)
---

## Setup & Execution Steps
### 1. Start POX Controller

```bash
cd ~/pox
./pox.py openflow.of_01 --port=6633 misc.dynamic_block
```

### 2. Start Mininet

```bash
sudo mn --topo single,2 --controller=remote,ip=127.0.0.1,port=6633
```

---

## Working of the System

1. Hosts send packets through the switch.
2. If the switch has no matching rule, it sends a **PacketIn** message to the controller.
3. The controller:
   * Monitors incoming packets
   * Counts traffic per host (based on MAC address)
4. If traffic exceeds a predefined threshold:

   * The controller installs a **DROP flow rule**
5. The switch then blocks all further packets from that host.

---

## Scenarios Demonstrated

### Normal Scenario

* Command: `h1 ping h2`
* Result: Successful communication between hosts.

### Attack Scenario

* Command: `h1 ping -f h2`
* Result: High traffic detected → host blocked → **100% packet loss**

---

## Proof of Execution

Screenshots included in `/screenshots` folder:

1. **Normal Ping** – successful packet transmission
2. **Blocked Ping** – packet loss after threshold exceeded
3. **Controller Logs** – shows packet count and blocking decision
4. **Flow Table** – displays OpenFlow rule with `actions=drop`

---

## Key Concepts Used

* SDN Architecture (Control Plane vs Data Plane)
* OpenFlow Protocol
* PacketIn Events
* Flow Table (Match–Action Rules)
* Dynamic Network Control

---

## Conclusion

This project demonstrates how SDN enables **programmable and dynamic network security**. The controller can monitor traffic and enforce policies in real-time by installing flow rules, without requiring changes in the underlying hardware.

---
