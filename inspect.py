import subprocess
import zipfile
import os

from logger import *

def zipDir(zipname, dir_to_zip):
    dir_to_zip_len = len(dir_to_zip.rstrip(os.sep)) + 1
    with zipfile.ZipFile(zipname, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for dirname, subdirs, files in os.walk(dir_to_zip):
            for filename in files:
                path = os.path.join(dirname, filename)
                entry = path[dir_to_zip_len:]
                zf.write(path, entry)

def get_dir_size(root):
    size = 0
    for path, dirs, files in os.walk(root):
        for f in files:
            size +=  os.path.getsize( os.path.join( path, f ) )
    return size
	
def getStatus():
	logHdr0("Get system status")
	logHdr("Hostname");
	process = subprocess.Popen(['hostname'], stdout = subprocess.PIPE)
	out, err = process.communicate()
	logInfo(out.strip())

	logHdr("User ID");
	process = subprocess.Popen(['whoami'], stdout = subprocess.PIPE)
	out, err = process.communicate()
	logInfo(out.strip())

	logHdr("OS Version")
	process = subprocess.Popen(['ver'], stdout = subprocess.PIPE, shell = True)
	out, err = process.communicate()
	logInfo(out.strip())
	
	logHdr("Date")
	process = subprocess.Popen(['date', '/t'], stdout = subprocess.PIPE, shell = True)
	out, err = process.communicate()
	logInfo(out.strip())
	
	logHdr("Time")
	process = subprocess.Popen(['time', '/t'], stdout = subprocess.PIPE, shell = True)
	out, err = process.communicate()
	logInfo(out.strip())
	
	logHdr("Boot time")
	p1 = subprocess.Popen(['systeminfo'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	output = subprocess.check_output(['find', 'Boot Time'], stdin = p1.stdout)
	p1.wait()
	logInfo(output)
	
def getVolatile():
	logHdr0("Get volatile data")
	
	logHdr("NetBios Sessions")
	with open("OUT\\netbios-sessions.txt", 'wb') as out:
		subprocess.Popen(['nbtstat', '/S'], shell = True, stdout = out)
	logOk("Saving to netbios-sessions.txt")
	
	logHdr("NetBios cache")
	with open("OUT\\netbios-cache.txt", 'wb') as out:
		subprocess.Popen(['nbtstat', '/c'], shell = True, stdout = out)
	logOk("Saving to netbios-cache.txt")
	
	logHdr("Open Shared files")	
	with open("OUT\\open-shared-files.txt", 'w') as out:
		subprocess.Popen(['net', 'file'], shell = True, stdout = out)
	logOk("Saving to open-shared-files.txt")
	
	logHdr("Network cards")
	with open("OUT\\network-cards.txt", 'w') as out:
		subprocess.Popen(['ipconfig', '/all'], shell = True, stdout = out)
	logOk("Saving to network-cards.txt")
	
	logHdr("Network connections")
	with open("OUT\\network-stats.txt", 'w') as out:
		process = subprocess.call(['netstat', '-anb'], shell = True, stdout = out)
	logOk("Saving to network-stats.txt")
	
	logHdr("Network endpoints");
	process = subprocess.Popen(['tools\cports.exe', '/stext', 'OUT\endpoints.txt'], 
		stdout = subprocess.PIPE)
	logOk("Saving to network-endpoints.txt")
	
	logHdr("Routing table")
	with open("OUT\\routing-table.txt", 'w') as out:
		subprocess.Popen(['netstat', '-rn'], shell = True, stdout = out)
	logOk("Saving to routing-table.txt")

	logHdr("ARP cache")
	with open("OUT\\arp-cache.txt", 'w') as out:
		subprocess.Popen(['arp', '-a'], shell = True, stdout = out)
	logOk("Saving to arp-cache.txt")

	logHdr("DNS cache")
	with open("OUT\\dns-cache.txt", 'w') as out:
		subprocess.Popen(['ipconfig', '/displaydns'], shell = True, stdout = out)
	logOk("Saving to dns-cache.txt")
	
	logHdr("Logged on users")
	with open("OUT\\users.txt", 'w') as out:
		subprocess.Popen(['tools\PsLoggedOn.exe', '/accepteula'], shell = True, 
		stdout = out, stderr = out)
	logOk("Saving to users.txt")	
	
	logHdr("Logon on sessions")
	with open("OUT\\sessions.txt", 'w') as out:
		subprocess.Popen(['tools\LogonSessions.exe', '/accepteula', '/p'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to sessions.txt")

	logHdr("Windows services")
	with open("OUT\\services.txt", 'w') as out:
		subprocess.Popen(['tools\PsService.exe', '/accepteula'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to services.txt")
	
	logHdr("Services hosted in each process")
	with open("OUT\\hosted-services.txt", 'w') as out:
		subprocess.Popen(['tasklist', '/svc'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to hosted-services.txt")
	
	logHdr("Detailed drivers info")
	with open("OUT\\drivers.txt", 'w') as out:
		subprocess.Popen(['driverquery', '/v', '/fo', 'list'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to drivers.txt")

	logHdr("Process tree (PsList)")
	with open("OUT\\process-tree.txt", 'w') as out:
		subprocess.Popen(['tools\PsList', '/accepteula', '/t'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to process-tree.txt")

	logHdr("Tasklist")
	with open("OUT\\tasklist.txt", 'w') as out:
		subprocess.Popen(['tasklist', '/v'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to tasklist.txt")

	logHdr("Scheduled tasks (at)")
	with open("OUT\\sched-tasks-at.txt", 'w') as out:
		subprocess.Popen(['at'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to sched-tasks-at.txt")

	logHdr("Scheduled tasks (schtasks)")
	with open("OUT\\sched-tasks-schtasks.txt", 'w') as out:
		subprocess.Popen(['schtasks'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to sched-tasks-schtasks.txt")
	
	logHdr("Processes (cprocess)");
	process = subprocess.Popen(['tools\cprocess.exe', '/stext', 'OUT\process-full.txt'], 
		stdout = subprocess.PIPE)
	logOk("Saving to process-full.txt")

	logHdr("List loaded DLLs")
	with open("OUT\\dlls.txt", 'w') as out:
		subprocess.Popen(['tools\ListDlls', '/accepteula'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to dlls.txt")

	logHdr("List all handles information")
	with open("OUT\\handles.txt", 'w') as out:
		subprocess.Popen(['tools\handle', '/accepteula', '/a', '/u'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to handles.txt")	

	logHdr("All autorun programs")
	with open("OUT\\autoruns.txt", 'w') as out:
		subprocess.Popen(['tools\\autorunsc', '/accepteula', '/a'], 
		shell = False, stdout = out, stderr = subprocess.PIPE)
	logOk("Saving to autoruns.txt")
	
def getNonVolatile():
	logHdr0("Get non-volatile data")
	logHdr("Dump users list")
	with open("OUT\\userlist.txt", 'w') as out:
		subprocess.call(['net', 'user'], 
			shell = True, stdout = out, stderr = out)
	logOk("Saving to userlist.txt")	

	logHdr("Last 20 logons")
	with open("OUT\\logons.txt", 'w') as out:
		subprocess.call(['tools\NtLast.exe', '-n', '20'], shell = True, 
		stdout = out, stderr = out)
	logOk("Saving to logons.txt")
	
	logHdr("Dump user rights")
	with open("OUT\\user-rights.txt", 'w') as out:
		subprocess.call(['tools\AccessChk', '/accepteula', '/v', '/a', '*'], 
			shell = True, stdout = out, stderr = out)
	logOk("Saving to user-rights.txt")	
	
	logHdr("Dump File access permissions")
	with open("OUT\\file-permissions.txt", 'w') as out:
		# Replace '.' with the folder to search from (e.g. c:\\)
		subprocess.call(['tools\AccessChk', '/accepteula', '/v', '/d', '/s', '.'], 
			shell = True, stdout = out, stderr = out)
	logOk("Saving to file-permissions.txt")	
	
	logHdr("Installed patched")
	with open("OUT\\systeminfo.txt", 'w') as out:
		subprocess.Popen(['systeminfo'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to systeminfo.txt")	

	logHdr("Installed software versions")
	with open("OUT\\software.txt", 'w') as out:
		subprocess.Popen(['tools\PsInfo', '/accepteula', '/s'], 
		shell = True, stdout = out, stderr = out)
	logOk("Saving to software.txt")	
	
	logHdr("Files timestamps")
	logOk("Saving to timestamps.txt ...")
	with open("OUT\\timestamps.txt", 'w') as out:
		# Replace '.' with the folder to search from (e.g. c:\\)
		subprocess.call(['tools\\find', '.', '-printf', '%Tc;%p\\n'], 
			shell = True, stdout = out, stderr = out)

	logHdr("Files accessed within the last 2 weeks")
	logOk("Saving to accessed-files.txt ...")
	with open("OUT\\accessed-files.txt", 'w') as out:
		# Replace '.' with the folder to search from (e.g. c:\\)
		subprocess.call(['tools\\afind', '/d', '14', '.'], 
			shell = True, stdout = out, stderr = out)
			
	logHdr("Dump audit policies")
	with open("OUT\\audit-policies.txt", 'w') as out:
		subprocess.Popen(['auditpol', '/get', '/category:*'], 
			shell = True, stdout = out, stderr = subprocess.PIPE)
	logOk("Saving to audit-policies.txt")

	logHdr("Event logs file names")
	with open("OUT\\evt-logs.txt", 'w') as out:
		subprocess.Popen(['wevtutil', 'el'], 
			shell = True, stdout = out, stderr = subprocess.PIPE)
	logOk("Saving to evt-logs.txt")

	logHdr("Dump local event logs")
	logOk("Saving to events.txt ...")
	with open("OUT\\events.txt", 'w') as out:
		subprocess.Popen(['tools\PsLogList', '/accepteula'], 
			shell = True, stdout = out, stderr = subprocess.PIPE)

	logHdr("Dump detailed security events")
	logOk("Saving to events-security.txt ...")
	with open("OUT\\events-security.txt", 'w') as out:
		subprocess.Popen(['tools\PsLogList', '/accepteula', '/s', '/x', 'Security'], 
			shell = True, stdout = out, stderr = subprocess.PIPE)
			
	logHdr("Extract HKLM registry hives")
	logOk("Exporting HKLM to hklm.reg ...")
	subprocess.call(['reg', 'export', 'HKLM', 'OUT\\hklm.reg', '/y'], 
		shell = True)
	logOk("Save SYSTEM hive to system.dat ...")
	subprocess.call(['reg', 'save', 'HKLM\SYSTEM', 'OUT\\system.dat', '/y'],
		shell = True)
	logOk("Save SOFTWARE hive to software.dat ...")
	subprocess.call(['reg', 'save', 'HKLM\SOFTWARE', 'OUT\\software.dat', '/y'],
		shell = True)

def save():
	folderName = "OUT"
	archiveName = "artefacts.zip"
	
	logHdr0("Zip artefacts")
	logInfo("Saving to %s ..." % archiveName)
	zipDir(archiveName, folderName)
	logInfo("Initial size: %s MB" % str(get_dir_size(folderName)/1024/1024))
	logInfo("Archive size: %s MB" % str(os.path.getsize(archiveName)/1024/1024))
	
if __name__ == "__main__":
	process = subprocess.Popen([r'md', 'OUT'], shell = True, 
		stderr = subprocess.PIPE)
	
	getStatus()
	getVolatile()
	getNonVolatile()
	save()