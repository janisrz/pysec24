# Piemērs ar 3 threads, kas apstrādā FTP serverus no saraksta

import threading
import queue
from ftplib import FTP

# Define a constant for the email
DEFAULT_EMAIL = 'user@example.com'

# List of FTP servers with credentials
ftp_sites = [
    ('ftp.novell.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.dlptest.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.gnu.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.mozilla.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.freebsd.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.debian.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.redhat.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.kernel.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.openbsd.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.centos.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.archlinux.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.slackware.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.linuxmint.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.suse.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.gnome.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.kde.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.xiph.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.videolan.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.openoffice.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.w3.org', 'anonymous', DEFAULT_EMAIL)
]

# Create a queue for the FTP sites
ftp_queue = queue.Queue()

# Populate the queue with FTP site details
for site in ftp_sites:
    ftp_queue.put(site)

def ftp_worker():
    while not ftp_queue.empty():
        host, user, passwd = ftp_queue.get()
        try:
            # Connect to the FTP server
            ftp = FTP(host)
            ftp.login(user=user, passwd=passwd)
            print(f"\nConnected to {host}. Listing root directory:")
            
            # List files in the root directory
            files = ftp.nlst()
            print(files)
            
            # Close the connection
            ftp.quit()
        except Exception as e:
            print(f"Failed to connect to {host}: {e}")
        finally:
            ftp_queue.task_done()

# Create and start threads
num_threads = 3
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=ftp_worker)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All FTP sites processed.")
