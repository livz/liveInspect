liveInspect
===========
Python tool which wraps calls to various information extraction programs from different sources (SysInternals, Foundstone, NirSoft, ...) and native Windows programs to extract information from a live Windows machine. Information will be collected in the order of its volatility (*does not include memory dumping*).


System status
-------
|Data 	   |Command Line| Developer | Comments |
|:---------|:-----------|:----------|:---------|
|Hostname| 	hostname| 	Built-in ||
|User ID |	whoami| 	Built-in| 	Present since Win2k|
|OS version| 	ver| 	Built-in| |
|Current date| 	date /t| 	Built-in||
|Current time| 	time /t| 	Built-in||
|Boot time |	systeminfo | find "Boot Time"| 	Built-in|| 

Volatile data collection
-------
|Data 	   |Command Line| Developer | Comments |
|:---------|:-----------|:----------|:---------|
|NetBIOS sessions| 	nbtstat /S| 	Built-in| 	Sessions established over the network|
|NetBIOS cache| 	nbtstat /c 	|Built-in| 	Names Cache|
|Open shared files| 	net file| 	Built-in||	
|Network cards| 	ipconfig /all| 	Built-in|| 
|Network connections| 	netstat -anb| 	Built-in ||
|Network endpoints 	|cports /stext endpoints.txt| 	NirSoft 	|Detailed infor about the processes|
|Routing table| 	netstat -rn| 	Built-in|| 
|ARP cache| 	arp -a| 	Built-in|| 
|DNS cache| 	ipconfig /displaydns| 	Built-in ||
|Logged on users| 	PsLoggedOn /accepteula| 	SysInternals|| 
|Logon sessions| 	LogonSessions /accepteula /p| 	SysInternals ||
|Windows services 	|PsService.exe /accepteula| 	SysInternals|| 
|Hosted services| 	tasklist /svc 	|Built-in| 	Services hosted in each process|
|Drivers 	|driverquery /v /fo list| 	Built-in| 	Detailed drivers info|
|Process tree| 	PsList /accepteula /t| 	SysInternals|| 
|Tasklist| 	tasklist /v| 	Built-in|| 
|Scheduled tasks| 	at 	|Built-in|| 
|Scheduled tasks| 	schtasks| 	Built-in|| 
|Processes 	|cprocess /stext process-full.txt| 	NirSoft|| 
|Loaded DLLs| 	ListDlls /accepteula| 	SysInternals ||
|Handles 	|handle /accepteula /a /u| 	SysInternals|| 
|Autoruns 	|autorunsc /accepteula /a| 	SysInternals|| 

Non-volatile data collection
-------
|Data 	   |Command Line| Developer | Comments |
|:---------|:-----------|:----------|:---------|
|User list| 	net user| 	Built-in|| 
|Last N logins| 	NtLast -n 20| 	McAfee ||
|User rights| 	AccessChk /accepteula /v /a *| 	SysInternals|| 
|Permissions| 	AccessChk /accepteula /v /d /s C:\ 	|SysInternals| 	File access permissions|
|Installed patches| 	systeminfo 	|Built-In| 	Lists Hotfixes|
|Software| 	PsInfo /accepteula /s| 	SysInternals| 	Installed software and versions|
|Timestamps| 	find C:\ -printf "%Tc;%p\n"| 	UnxUtils|| 
|Last accessed| 	afind /d 14 C:\ 	|McAfee 	|Files accessed within last 2 weeks|
|Audit policies| 	auditpol /get /category:* 	|Built-in|| 
|Event logs| 	wevtutil el| 	Built-in| 	Event logs file names|
|Events 	|PsLogList /accepteula| 	SysInternals| 	Dump local events|
|Security events| 	PsLogList /accepteula /s /x Security| 	SysInternals ||
|HKLM hive| 	reg export HKLM hklm.reg /y| 	Built-in| 	Export as .reg|
|SYSTEM hive| 	reg save HKLM\SYSTEM system.dat| 	Built-in|| 
|SOFTWARE hive| 	reg save HKLM\SOFTWARE software.dat| 	Built-in||

[Windows live forensics - part 1](http://cyberinc.co.uk/windows-live-forensics/)

[Windows live forensics - part 2](http://cyberinc.co.uk/windows-live-forensics-part-2/)

[Windows live forensics - part 3](http://cyberinc.co.uk/windows-live-forensics-part-3/)


Notes
-------

- A ZIP archive with the artefacts is created at the end.
- A lot of the tools need administrator rights in order to run properly.
- Memory dumping should be done separately, if needed, before starting the artefacts collection process.
- Some of the licenses for the 3rd party tools do not allow distribution. However, personal and commercial use is permitted.

