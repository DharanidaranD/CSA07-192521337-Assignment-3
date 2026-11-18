# CSA07 – Computer Networks: Assignment 3 (CO3)

* **Name:** DHARANIDARAN D
* **Register Number:** 192521337
* **Operating System:** [WiWindows1 / Ubuntu 22.04]
* **Python Version:** [Run 3.11]
* **Packet Tracer Version:** PythPythonyticalhon applicable (Python 3 & analytical tasks only)

#Runow to Run
Run any task script from the repository root using Python 3:
* `python3 Q1/q1_sockets.py`
* `python3 Q2/q2_cwnd.py`
* `python3 Q4/q4_dns.py`
* `python3 Q5/q5_mm1.py`
* `python3 Q7/q7_telehealth.py`

## Summary of Results
* **Q1 (Sockets & Overhead):** Verified 4-tuple TCP vs. 2-tuple UDP demultiplexing and 21.88% (UDP) vs. 28.57% (TCP) IPv4 header overhead.
* **Q2 (Congestion Window):** Simulated 20 RTTs; TCP Reno delivered 211 segments vs. TCP Tahoe's 144 (+67 segments).
* **Q3 (Web Page Load):** Reduced page load time from 8,100 ms (non-persistent) to 150 ms (pipelined) and <50 ms (cached).
* **Q4 (DNS Resolution):** Verified 12 vs. 120 queries/hr authoritative load and 0 queries on cached lookups.
* **Q5 (M/M/1 Queueing):** Identified >950 pkt/s delay spike (>20 ms) and 1.0 s token bucket burst duration.
* **Q6 (QUIC & TLS 1.3):** Compared 0-RTT/1-RTT QUIC handshakes against 2-RTT/3-RTT TCP+TLS and Connection ID migration.
* **Q7 (Telehealth Design):** Mapped SRTP/UDP for video and HTTP/3 (QUIC) for X-rays; verified chat and 500 KB file transfer via sockets.
