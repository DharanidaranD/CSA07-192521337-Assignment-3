# CSA07 – Computer Networks: Assignment 3 (CO3)

* **Student Name:** Dharanidaran D
* **Register Number:** 192521337
* **Course:** CSA07 – Computer Networks (CO3)
* **GitHub Repository:** [https://github.com/DharanidaranD/CSA07-192521337-Assignment3](https://github.com/DharanidaranD/CSA07-192521337-Assignment3)
* **Operating System:** Ubuntu 22.04 LTS / Windows 11
* **Python Version:** Python 3.11+
* **Packet Tracer:** Not applicable (Python 3 & analytical tasks only)

---

## Repository Structure

```text
CSA07-192521337-Assignment3/
├── README.md
├── CSA07_Assignment3_CO3_Solutions.docx
│
├── Q1/
│   ├── q1_sockets.py
│   ├── q1_output.txt
│   ├── q1_screenshot.png
│   └── q1_analysis.txt
│
├── Q2/
│   ├── q2_cwnd.py
│   ├── q2_output.txt
│   ├── q2_screenshot.png
│   └── q2_analysis.txt
│
├── Q3/
│   └── q3_analysis.txt
│
├── Q4/
│   ├── q4_dns.py
│   ├── q4_output.txt
│   ├── q4_screenshot.png
│   └── q4_analysis.txt
│
├── Q5/
│   ├── q5_mm1.py
│   ├── q5_output.txt
│   ├── q5_screenshot.png
│   └── q5_analysis.txt
│
├── Q6/
│   └── q6_analysis.txt
│
└── Q7/
    ├── q7_telehealth.py
    ├── q7_output.txt
    ├── q7_screenshot.png
    └── q7_analysis.txt
```

---

## Tasks Overview, Execution Commands & Summary Results

| Folder | Task Title | How to Run | Summary of Key Results |
| :--- | :--- | :--- | :--- |
| **`Q1/`** | Which Socket Gets the Segment? | `python3 Q1/q1_sockets.py` | Verified 4-tuple TCP vs. 2-tuple UDP demultiplexing, IPv4 header overhead (`21.88%` UDP vs. `28.57%` TCP), and HoL blocking impact (`600 freezes/min` at 2% loss). |
| **`Q2/`** | Read the Congestion Window | `python3 Q2/q2_cwnd.py` | Simulated Slow Start, Congestion Avoidance, and loss over 20 RTTs; TCP Reno delivered `211` segments vs. TCP Tahoe's `144` (`+67` segments). |
| **`Q3/`** | Why Does the Home Page Take 8 Seconds? | *Analytical Report (`Q3/q3_analysis.txt`)* | Reduced page load time from `8,100 ms` (non-persistent HTTP) to `1,500 ms` (6 parallel), `150 ms` (pipelined), and `< 50 ms` (`Cache-Control`). |
| **`Q4/`** | How Many Queries Reach the University's DNS Server? | `python3 Q4/q4_dns.py` | Implemented iterative root-to-authoritative DNS lookup (`4` queries on cold lookup, `0` queries on cached repeat lookup) and analyzed TTL/Anycast CDN load. |
| **`Q5/`** | When Will the Video Call Freeze? | `python3 Q5/q5_mm1.py` | Modeled M/M/1 link delay; identified `> 950 pkt/s` threshold for `20 ms` delay, `1.0 s` token bucket burst duration, and DiffServ (`EF`, `AF`, `BE`) isolation. |
| **`Q6/`** | Count the Round Trips Before the First Byte | *Analytical Report (`Q6/q6_analysis.txt`)* | Compared handshake setup (`300 ms` TCP+TLS 1.2, `200 ms` TCP+TLS 1.3, `100 ms` QUIC 1-RTT, `0 ms` QUIC 0-RTT) and Connection ID migration across Wi-Fi/5G. |
| **`Q7/`** | Choose the Protocols from First Principles | `python3 Q7/q7_telehealth.py` | Designed four-stage rural telehealth architecture (UDP/SRTP + HTTP/3 over QUIC), analyzed `1.75 Mbps` unscaled TCP limit, and verified `500 KB` X-ray + chat sockets. |

---

## How to Reproduce Outputs

1. Clone the repository:
   ```bash
   git clone https://github.com/DharanidaranD/CSA07-192521337-Assignment3.git
   cd CSA07-192521337-Assignment3
   ```
2. Run each Python 3 script (standard library only; no external `pip` packages required):
   ```bash
   python3 Q1/q1_sockets.py
   python3 Q2/q2_cwnd.py
   python3 Q4/q4_dns.py
   python3 Q5/q5_mm1.py
   python3 Q7/q7_telehealth.py
   ```
