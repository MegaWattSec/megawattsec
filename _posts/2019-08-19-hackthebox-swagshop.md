---
title: 'HackTheBox: SwagShop'
date: 2019-08-19T12:40:27-04:00
categories: [Walkthrough, HackTheBox]
tags: [Magento, vi]
---
## Recon

<img class="alignnone wp-image-125" src="/assets/img/2019/08/ss_html_cover.png" /> 

This site is a basic e-commerce site with just a few products filled in as examples. Magento is the platform and it&#8217;s very well-known.

### Port Scan

NMAP doesn&#8217;t show anything out of the ordinary for a web host:

{% highlight plain_text %}
PORT   STATE SERVICE REASON         VERSION
<strong>22/tcp open </strong> <strong>ssh    </strong> syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b6:55:2b:d2:4e:8f:a3:81:72:61:37:9a:12:f6:24:ec (RSA)
|   256 2e:30:00:7a:92:f0:89:30:59:c1:77:56:ad:51:c0:ba (ECDSA)
|_  256 4c:50:d5:f2:70:c5:fd:c4:b2:f0:bc:42:20:32:64:34 (ED25519)
<strong>80/tcp open </strong> <strong>http   </strong> syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 88733EE53676A47FC354A61C32516E82
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Home page
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.12 (95%), Linux 3.13 (95%), Linux 3.16 (95%), Linux 3.2 - 4.9 (95%), Linux 3.8 - 3.11 (95%), Linux 4.4 (95%), Linux 4.8 (95%), Linux 4.9 (95%), Linux 3.18 (95%), Linux 4.2 (95%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 0.003 days (since Tue Aug 13 09:45:05 2019)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
{% endhighlight %}

We can see that Apache 2.4.18 is the web server platform.

### Directory Scan

GoBuster was able to find quite a few directories related to Magento:

{% highlight plain_text %}
=====================================================
Gobuster v2.0.0              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://10.10.10.140/
[+] Threads      : 10
[+] Wordlist     : /usr/share/wordlists/dirb/big.txt
[+] Status codes : 200,204,301,302,307,403
[+] Expanded     : true
[+] Timeout      : 10s
=====================================================
2019/08/13 13:32:28 Starting gobuster
=====================================================
http://10.10.10.140/.htaccess (Status: 403)
http://10.10.10.140/.htpasswd (Status: 403)
http://10.10.10.140/app (Status: 301)
http://10.10.10.140/downloader (Status: 301)
http://10.10.10.140/errors (Status: 301)
http://10.10.10.140/favicon.ico (Status: 200)
http://10.10.10.140/includes (Status: 301)
http://10.10.10.140/js (Status: 301)
http://10.10.10.140/lib (Status: 301)
http://10.10.10.140/media (Status: 301)
http://10.10.10.140/pkginfo (Status: 301)
http://10.10.10.140/server-status (Status: 403)
http://10.10.10.140/shell (Status: 301)
http://10.10.10.140/skin (Status: 301)
http://10.10.10.140/var (Status: 301)
=====================================================
2019/08/13 13:33:45 Finished
=====================================================
{% endhighlight %}

Going through each of the directories and searching for anything out of the ordinary didn&#8217;t return very much results. However, the &#8216;downloader&#8217; page gives details on the version of Magento:

<img class="alignnone wp-image-126" src="/assets/img/2019/08/ss_html_downloader.png" /> 

We have Magento Connect Manager ver. 1.9.0.0, which the base version should match.

## Exploitation

### Research

With the information found so far, we can look for public exploits or vulnerabilities to use.

<img class="alignnone wp-image-127" src="/assets/img/2019/08/ss_searchsploit.png" /> 

There are a few that are applicable to this version, and after researching them for a little bit, it is obvious the [one we need](https://www.exploit-db.com/exploits/37977) is related to the ShopLift vuln. During research on the ShopLift vuln, I found another public [exploit](https://github.com/joren485/Magento-Shoplift-SQLI/blob/master/poc.py) that has slight differences, and it could be useful to have both.

### The Blackhat Way

After seeing there&#8217;s a preprogrammed password in the exploit, and it&#8217;s a very easily found one, I thought there might be some other hackers on the free server I&#8217;m using that would simply leave the default creds in. So I put them into the &#8216;/downloader&#8217; page, and voila!

<img class="alignnone wp-image-128" src="/assets/img/2019/08/ss_html_downloader_admin.png" /> 

There&#8217;s a &#8220;Return to Admin&#8221; button that will then take us to the normal admin dashboard. Or&#8230;

### The Not-Quite-As-Blackhat Way

If taking advantage of other hackers on the server isn&#8217;t your way, or if you&#8217;re alone on a paid server, it&#8217;s almost just as easy to exploit it yourself.

Thing is, the exploit code as it comes doesn&#8217;t work, even after changing the target to our host address.

So, good thing we found a second exploit version.

<img class="alignnone wp-image-129" src="/assets/img/2019/08/ss_exploit_diff.png" /> 

The critical difference is the addition of /index.php/ to the target URL, as shown in the screenshot.

After adding that change to the exploit code (don&#8217;t forget to modify the default credentials) it works!

## Shell Hunting

This is where I spent the most time looking around and poking at things, searching for command injection. Eventually, I stopped wasting time and started Googling and searching the forum.

I was able to find one [CVE](https://www.cvedetails.com/cve/CVE-2019-7932/) for code execution on this version. However, on the forum, several people mentioned abusing extensions to get to a shell. So that&#8217;s the direction I took instead of the CVE.

First I tried to manipulate the extension creation process to get some code exec result, but I eventually gave up that route and figured there&#8217;s probably already some extension to load that would help. Thanks to other hackers on the free server, it was relatively easy to figure out what extension that could be. On the Magento Downloader page, there is a section that lists which extensions are loaded:

<img class="alignnone wp-image-132" src="/assets/img/2019/08/ss_manage_extensions.png" /> 

<img class="alignnone wp-image-133" src="/assets/img/2019/08/ss_manage_extensions_2.png" /> 

And at the bottom of the list, there is an extension allowing access to the filesystem! That can&#8217;t be there normally&#8230;

Since it&#8217;s already loaded in this instance, I shouldn&#8217;t need to load it again, just learn how to use it. However, that is definitely not always the case. This box spends a lot of time being unavailable on the free server and has to get reset often, and when it does somebody will need to upload the Magpleasure extension. Turns out there&#8217;s a checkbox on the Magento Downloader that causes it to be unavailable if left checked during extension uploads&#8230; uncheck that when uploading.

How to use the extension:

<img class="alignnone wp-image-134" src="/assets/img/2019/08/ss_use_mpfilesystem.png" /> 

Once in the filesystem, I tried to create a file, but there was no clear way to do so with MagPleasure.

Another thing to do is to modify files already on the system, and there are several targets to choose from. From having to restart so many times dues to service unavailable issues, I&#8217;ve noticed other hackers tend to prefer the &#8216;get.php&#8217; file. To not get clobbered, I used the &#8216;install.php&#8217; file for my reverse shell.

<img class="alignnone wp-image-136" src="/assets/img/2019/08/ss_filesystem_shell.png" /> 

### Escalation

For the first shell connection, we&#8217;re logged in as &#8216;www-data&#8217;. Not too surprising. What is surprising though, is that www-data can access the user home directory! That&#8217;s not really a normal scenario, but I&#8217;ll take it! Just `cat /home/haris/user.txt` for the flag.

Now to find a privilege escalation to the user account.

<img class="alignnone wp-image-137" src="/assets/img/2019/08/ss_shell1.png" /> 

I was going to find a way to upload LinEnum and do proper enumeration, but I remember reading on several forum posts that there&#8217;s a very basic permissions issue to use for root privileges escalation. One of the very first things to look for is `sudo` permissions, so that&#8217;s what I did:

<img class="alignnone wp-image-138" src="/assets/img/2019/08/ss_sudo.png" /> 

Look at that! We can use `vi` as root, and then a simple shell escape from inside vi:

First, I used the command `sudo vi ./test.txt` &#8230; but it errors with &#8220;sudo: no tty present and no askpass program specified&#8221;

After trying a few things I landed on the fact that I didn&#8217;t type it in exactly as it is in `sudo -l` &#8230; so I tried again with: `sudo /usr/bin/vi /var/www/html/test.txt` and that let me in as root.

To use a shell escape in vi, we can type `:!/bin/sh` for the win 🙂