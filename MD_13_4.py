import ftplib

def test_ftp_connection(host, user="anonymous", password=""):
    """Tests the connection to an FTP site."""
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        print(f"Connected to {host}")
        ftp.quit()
        return True
    except Exception as e:
        print(f"Failed to connect to {host}: {e}")
        return False

# List of 40 FTP sites to test 
ftp_sites = [
    "ftp.kernel.org",
    "ftp.gnu.org",
    "ftp.mozilla.org",
    "ftp.debian.org",
    "ftp.ubuntu.com",
    "ftp.fedoraproject.org",
    "ftp.centos.org",
    "ftp.redhat.com",
    "ftp.suse.com",
    "ftp.opensuse.org",
    "ftp.archlinux.org",
    "ftp.gentoo.org",
    "ftp.slackware.com",
    "ftp.mandriva.com",
    "ftp.mageia.org",
    "ftp.gimp.org",
    "ftp.inkscape.org",
    "ftp.blender.org",
    "ftp.python.org",
    "ftp.perl.org",
    "ftp.php.net",
    "ftp.ruby-lang.org",
    "ftp.nodejs.org",
    "ftp.apache.org",
    "ftp.nginx.org",
    "ftp.mysql.com",
    "ftp.postgresql.org",
    "ftp.sqlite.org",
    "ftp.microsoft.com",
    "ftp.apple.com",
    "ftp.adobe.com", 
    "ftp.oracle.com", 
    "ftp.cisco.com",
    "ftp.juniper.net", 
    "ftp.huawei.com",
    "ftp.tencent.com",
    "ftp.alibaba.com", 
    "ftp.amazon.com", 
    "ftp.google.com", 
    "ftp.facebook.com", 
    "ftp.twitter.com", 
    "ftp.linkedin.com", 
    "ftp.wikipedia.org", 
    "ftp.github.com", 
    "ftp.stackoverflow.com" 
]

# Test the connection to each FTP site
for site in ftp_sites:
    if test_ftp_connection(site):
        print(f"{site} is reachable")
    else:
        print(f"{site} is unreachable")