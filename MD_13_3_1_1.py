import threading
import queue
from ftplib import FTP

# Define a constant for the email
DEFAULT_EMAIL = 'user@example.com'

# List of FTP servers with credentials
ftp_sites = [
    ('ftp.gnu.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.ubuntu.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.suse.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.slackware.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.perl.org', 'anonymous', DEFAULT_EMAIL),
    ('ftp.adobe.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.robelle3000.ai', 'anonymous', DEFAULT_EMAIL),
    ('ftp.rising.com.au', 'anonymous', DEFAULT_EMAIL),
    ('ftp.test.rebex.net', 'demo', DEFAULT_EMAIL),
    ('ftp.swin.edu.au', 'anonymous', DEFAULT_EMAIL),
    ('ftp.tip.csiro.au', 'anonymous', DEFAULT_EMAIL),
]

# Create a queue for the FTP sites
ftp_queue = queue.Queue()

# Populate the queue with FTP site details
for site in ftp_sites:
    ftp_queue.put(site)

# Create a lock for thread-safe writing to the file
write_lock = threading.Lock()

def ftp_worker(output_file):
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
            
            # Write the results to the file
            with write_lock:
                with open(output_file, 'a') as f:
                    f.write(f"\nConnected to {host}. Listing root directory:\n")
                    for file in files:
                        f.write(f"{file}\n")
            
            # Close the connection
            ftp.quit()
        except Exception as e:
            print(f"Failed to connect to {host}: {e}")
            with write_lock:
                with open(output_file, 'a') as f:
                    f.write(f"Failed to connect to {host}: {e}\n")
        finally:
            ftp_queue.task_done()

# Create and start threads
num_threads = 3
threads = []
output_file = 'ftp_results.txt'

# Ensure the output file is empty before starting
open(output_file, 'w').close()

for _ in range(num_threads):
    thread = threading.Thread(target=ftp_worker, args=(output_file,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All FTP sites processed. Results saved to ftp_results.txt.")
