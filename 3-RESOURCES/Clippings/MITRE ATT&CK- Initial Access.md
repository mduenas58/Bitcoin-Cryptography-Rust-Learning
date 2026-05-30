
- **Initial access** is the MITRE ATT&CK tactic where an attack moves from planning to active, malicious interaction with a target network.

- Before initial access, the *pre-attack* phase focuses on reconnaissance, resource development, and identifying vulnerabilities.  
- Initial access may be the first time the attacker intentionally interacts with the target system.  
- Boundaries between MITRE ATT&CK tactics can blur (e.g., SQL injection could cover reconnaissance, initial access, and data exfiltration).  
- Common initial access techniques include:  
  - Drive‑by compromise  
  - Exploitation of public‑facing applications (e.g., SQL injection)  
  - External remote services (VPN, RDP)  
  - Hardware modifications  
  - Phishing (links or attachments)  
  - Replication through removable media (e.g., weaponized USB drive)  
  - Supply chain compromise (software/hardware)  
  - Trusted relationship exploitation (e.g., vendor access)  
  - Valid accounts  
- Python can automate many initial access vectors.  
- Course focuses on two Python applications for initial access:  
  - **Valid accounts** → default account discovery sub‑technique.  
  - **Replication through removable media** → Python with AutoRun scripts on a USB drive.  
