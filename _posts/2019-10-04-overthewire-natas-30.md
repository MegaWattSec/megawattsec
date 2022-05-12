---
title: 'OverTheWire: NATAS 30'
date: 2019-10-04T15:24:53-04:00
categories: [Walkthrough, OverTheWire]
tags: [web, perl, sqli]
---
<img class="alignnone size-large wp-image-381" src="/assets/img/2019/10/2019-10-04_15h26_33.png" />

This is another basic login form. The unique thing about this one is the sourcecode is in PERL.

{% highlight perl %}
#!/usr/bin/perl
use CGI qw(:standard);
use DBI;

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas30", "pass": "<censored>" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<!-- morla/10111 <3  happy birthday OverTheWire! <3  -->

<h1>natas30</h1>
<div id="content">

<form action="index.pl" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
END

if ('POST' eq request_method && param('username') && param('password')){
  my $dbh = DBI->connect( "DBI:mysql:natas30","natas30", "<censored>", {'RaiseError' => 1});
  my $query="Select * FROM users where username =".$dbh->quote(param('username')) . " and password =".$dbh->quote(param('password')); 

  my $sth = $dbh->prepare($query);
  $sth->execute();
  my $ver = $sth->fetch();
  if ($ver){
    print "win!<br>";
    print "here is your result:<br>";
    print @$ver;
  }
  else{
    print "fail :(";
  }
  $sth->finish();
  $dbh->disconnect();
}

print <<END;
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
END
{% endhighlight %}

From quick examination of the source, it&#8217;s clear that we&#8217;re intended to do SQL injection here. In fact, we don&#8217;t even have to extract the password, it should be given to us if we are able to get ANY successful result from the query. So a very simple SQL injection will do. Problem is, and the central challenge here, is the quote() function that&#8217;s supposed to be sanitizing our inputs. There must be a known way around quote().

A few minutes of searching Google and I found the [answer](https://stackoverflow.com/questions/40273267/is-perl-function-dbh-quote-still-secure) I was looking for. Turns out param() from CGI.pm introduces a vulnerability to quote(). From the post:

> You see, `param` is context-sensitive. In scalar context, if the parameter has a single value (`name=foo`), it returns that value, and if the parameter has multiple values (`name=foo&name=bar`) it returns an arrayref. In _list_ context, it returns a list of values, whether there are zero, one, or many. The argument list of a method (such as `quote`) is a list context. That means that someone using your app can cause `quote` to receive _two_ values, and `quote`&#8216;s optional second argument is an SQL data type that the first argument should be treated as. If the data type is a non-string type like `NUMERIC`, then `quote` will pass its first argument through _without any quoting_. This constitutes an opportunity for SQL injection.

To exploit the vuln, simply send `username=natas31&password=”or 1=1&password=2` in the POST data.