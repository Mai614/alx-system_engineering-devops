**Postmortem: System Outage Incident - WordPress Application Typo**

**Issue Summary:**

- **Impact:**
  - Service: Holberton School’s WordPress application
  - User Experience: 100% of users experienced a 500 Internal Server
  - Error during the ten-minute outage.

- **Root Cause:**
  - A typo in the WordPress application's configuration file 
  (/var/www/html/wp-settings.php) led to a critical error when
  attempting to load the file class-wp-locale.phpp 
  instead of the correct class-wp-locale.php.

**Timeline:**
- **Issue Detection:**
  - January 22, 2018, 17:23 PST
  - A junior engineer noticed a 500 status code after deploying a WordPress update.

- **Investigation:**
  - January 22, 2018, 17:25 PST
  - Checked running processes; Apache2 and MySQL were running as expected,
   indicating a PHP/WordPress error.
  - Edited wp-config.php to enable debug mode.

- **Error Identification:**
  - January 22, 2018, 17:27 PST
  - A fatal error in the form of a missing file, class-wp-locale.phpp,
   was discovered in the debug output.
  - File existence confirmed using `ls`.

- **Resolution:**
  - January 22, 2018, 17:30 PST
  - Typographical error fixed using 
  `sed -i 's/phpp/php/' /var/www/html/wp-settings.php`.
  - Website service was tested and confirmed operational.

- **Preventative Measures:**
  - January 22, 2018, 17:32 PST
  - Developed a Puppet manifest (0-strace_is_your_friend.pp) to automate
   fixing similar errors in the future.

**Debugging Process:**

- **Bug Debugger (BDB) Steps:**
  - January 22, 2018, 19:20 PST
  - Checked running processes using `ps aux` - Apache2 processes were running as expected.
  - Explored the sites-available folder in /etc/apache2/, determined content location in /var/www/html/.
  - Used `strace` on the PID of the root Apache process but obtained no useful information.
  - Retried with the www-data process PID and identified an ENOENT error 
  for the file /var/www/html/wp-includes/class-wp-locale.phpp.
  - Located the typo in wp-settings.php and removed the trailing 'p'.
  - Developed a Puppet manifest for automated resolution.

**Summation:**
The root cause of the outage was a simple typo, resulting in the application
attempting to load a non-existent file. The issue was promptly resolved by
correcting the typo and deploying the fix using a Puppet manifest. Lessons
learned included the importance of thorough testing before deployment and 
implementing status monitoring to detect outages instantly.

**Prevention:**

- Regular testing of the application before deployment to catch errors like typos.
- Implementation of status monitoring services such as
 UptimeRobot for immediate outage alerts.
- Automation of error fixes using Puppet manifests to address
 identical issues swiftly in the future.

In conclusion, the outage served as a reminder of the need 
for meticulous testing and continuous monitoring in web application
deployment. The automated Puppet manifest adds an extra layer of defense
against similar errors, although, as programmers, we always strive for
perfection and to never make errors like this again.
