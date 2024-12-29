from ftplib import FTP

# Define a constant for the email
DEFAULT_EMAIL = 'user@example.com'

# List of example FTP servers (you can replace these with actual servers)
ftp_servers = [
    ('ftp.novell.com', 'anonymous', DEFAULT_EMAIL),
    ('ftp.dlptest.com', 'dlpuser@dlptest.com', 'eUj8GeW55SvYaswqUyDSm5v6N'),
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

def list_ftp_sites(servers):
    for host, user, passwd in servers:
        try:
            # Connect to the FTP server
            ftp = FTP(host)
            ftp.login(user=user, passwd=passwd)
            print(f"\nConnected to {host}. Listing files:")
            
            # List files in the current directory
            files = ftp.nlst()  # Use nlst() to get a list of file names
            print(files)
            
            # Close the connection
            ftp.quit()
        except Exception as e:
            print(f"Failed to connect to {host}: {e}")

# Execute the function
list_ftp_sites(ftp_servers)
