# ⚔️ Windows System Engineer Speedrun Lab (2 Days)

## Day 1 — Build the Mini Empire

- [ ] **Setup Environment**
  - [x] DC01: Windows Server 2019/2022  
    - Static IP: `192.168.56.10`  
    - DNS: `192.168.56.10`  
    - Promote to domain controller: `lab.local`  
  - [ ] CLIENT01: Windows 10/11  
    - DNS: `192.168.56.10`  
    - Join domain: `lab.local`  
  - [ ] Verify login on CLIENT01 with `LAB\Administrator`

- [ ] **Active Directory Basics**
  - [ ] Create user `alice` (username: `alice`, password: `P@ssw0rd1!`)  
  - [ ] Create group `HR` and add `alice`  
  - [ ] Verify login on CLIENT01 as `LAB\alice` (`whoami` → `lab\alice`)

- [ ] **Group Policy Basics**
  - [ ] Create GPO: `WallpaperPolicy` or restrict Control Panel  
  - [ ] Link to `lab.local` domain  
  - [ ] Run `gpupdate /force` on CLIENT01  
  - [ ] Verify policy applied

- [ ] **DNS Check**
  - [ ] From CLIENT01: `ping dc01.lab.local` → resolves to `192.168.56.10`  
  - [ ] On DC01: check A record in DNS Manager

---

## Day 2 — Harden & Automate

- [ ] **Firewall Rule**
  - [ ] On DC01: create inbound rule → allow RDP (3389) only from `192.168.56.20`  
  - [ ] Verify RDP works from CLIENT01 but not elsewhere

- [ ] **Password Policy via GPO**
  - [ ] Edit Default Domain Policy  
  - [ ] Set min password length = 10  
  - [ ] Enforce complexity = Enabled  
  - [ ] Verify short/simple passwords rejected

- [ ] **PowerShell Automation**
  - [ ] Run:  
    ```powershell
    Import-Module ActiveDirectory
    New-ADUser -Name "Bob Ops" -SamAccountName bob -AccountPassword (ConvertTo-SecureString "P@ssw0rd1!" -AsPlainText -Force) -Enabled $true
    Get-ADUser -Filter * | Select-Object Name
    ```
  - [ ] Verify `Bob Ops` created and listed

- [ ] **Troubleshoot Drill**
  - [ ] On CLIENT01: set DNS to `8.8.8.8`  
  - [ ] Attempt domain login → fails  
  - [ ] Reset DNS to `192.168.56.10`  
  - [ ] Login works again

---

## Bonus (Optional)

- [ ] **RSAT Tools**
  - [ ] On CLIENT01: install RSAT AD tools  
  - [ ] Open ADUC remotely → verify control

- [ ] **BloodHound Recon**
  - [ ] Run SharpHound from CLIENT01  
  - [ ] Import into BloodHound GUI  
  - [ ] Verify graph of users/groups/computers

---

# 🎯 Brag Points for Interview
- [ ] Setup DC + client, joined to domain  
- [ ] Created users/groups in AD  
- [ ] Applied and tested GPOs  
- [ ] Hardened RDP with firewall rules  
- [ ] Enforced password policy via GPO  
- [ ] Automated provisioning with PowerShell  
- [ ] Simulated + fixed DNS login issue
