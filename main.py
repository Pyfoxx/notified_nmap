import nmap
import click
import requests

@click.command()
@click.option("--port", default="0-1000", help="Port to scan")
@click.option("--ip", default="127.0.0.1", help="The target IP")
@click.option('--send', help="The URL where the result will be sent", required=True)
def scan(ip, port, send):
	nm = nmap.PortScanner()
	result = nm.scan(hosts=ip, ports=port, arguments="-sV -Pn")
	# arguments="-sV"
	notif = "Nmap over\n"
	for host in nm.all_hosts():
		notif = notif + '----------------------------------------------------\n'
		notif = notif + 'Host : %s (%s)\n' % (host, nm[host].hostname())
		notif = notif + 'State : %s\n' % nm[host].state()
		for proto in nm[host].all_protocols():
			notif = notif + '----------\n'
			notif = notif + 'Protocol : %s\n' % proto
			lport = nm[host][proto].keys()
			# lport.sort()
			for port in sorted(list(lport)):
				notif = notif + 'port : %s\tstate : %s\n' % (port, nm[host][proto][port]['state'])
	r = requests.post(url=send, data=notif)
	print("sent")
	print(r.status_code)
	return notif


if __name__ == "__main__":
	print("scanning")
	data = scan()
	print(data)


