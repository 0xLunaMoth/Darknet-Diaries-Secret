# Darknet Diaries Podcast

## All codes

```
A1 B2 C3 D4 E5 F6 G7 H8
A2 A5 A6 B1 B1 B4 B7 C1 C4 C7 D2 D3 D6
A1 A2 A3 A4 A5 B1 B3 B5 C1 C5
A2 A3 A4 B1 B5 C1 C5 D2 D4
A1 A2 A3 A4 A5 B3 B5 C2 C4 C5 D1
A1 A2 A3 A4 A5 B1 B3 B5 C1 C5

```

## EP1
Said fast at the end of the episode.
`A1 B2 C3 D4 E5 F6 G7 H8`

## EP2

**Morse code**
`.- ..---/.- ...../.- -..../-... .----/-... .----/-... ....-/-... --.../-.-. .----/-.-. ....-/-.-. --.../-.. ..---/-.. ...--/-.. -....`

**Translated morse code**
`A2 A5 A6 B1 B1 B4 B7 C1 C4 C7 D2 D3 D6`

## EP3
Said in reverse at the end of the episode.

**Reversed code**
`A1 A2 A3 A4 A5 B1 B3 B5 C1 C5`

## EP4
Said in the end of episode

**ASCII decimal values**
`97 50 32 97 51 32 97 52 32 98 49 32 98 53 32 99 49 32 99 53 32 100 50 32 100 52`

**Result from python script**
`A2 A3 A4 B1 B5 C1 C5 D2 D4`

## EP5

**Found in metadata**
`A1 A2 A3 A4 A5 B3 B5 C2 C4 C5 D1`

## EP6

Weird noises at the end of the episode

**Spectrogram**
`A1 A2 A3 A4 A5 B1 B3 B5 C1 C5`

## EP7

Said at the end of episode

`A5 B1 B2 B3 B4 B5 C5`

Afterwards it was said
`Let's play a game, your move`

# Darknet Diaries Website

# /secret
darknetdiaries.com/secret contains an image of the answer arranged on chessboards.
The image was titled 0x000000.jpg

As well as the following line of text:
`Can I tell you a secret? Can I trust you? How do I know you're not him?`

opening it with a hexeditor reveals the last portion of the file containing a string:

`Your move 2bd87cf22c40d4aa65a2e747ab8988a4`

# MD5 hash

The string is an MD5 hash that resolves to the word `chessmaster`

# /chessmaster

Visiting darknetdiaries.com/chessmaster reveals the following line of text:
`Hmm. Not gonna lie. You could use some practice. Rather than repeating your mistakes, you should develop your game a bit. Your move.`

Upon inspecting the source of the page, there's an additional line of text:

`The only way to patch a vulnerability is by exposing it first. How do I know you aren't a robot or anything?`

Which prompts me to look at the robots.txt section of the site. 

# robots.txt
```
User-agent: *
Disallow: /js/
Disallow: /css/
Disallow: /0x784251/
Disallow: /feedfree.xml
Sitemap: https://darknetdiaries.com/sitemap.xml
```

The robots.txt includes a weird line with a hex value. 
`0x784251` 

# /0x784251
`One game. I'll even let you have the first move. A game to end all games between us. We play, and the winner takes all.`

This page reveals this text accompanied by an input box. 

Upon inspecting the source of the site and looking at the JavaScript function used for the input box, the phrase:

`Winner takes all of what?`
Seems to be the answer to get the next clue. 

Upon entering this in the input field, an alert pops up with the following:
`/us`

# /us
`This game you are agreeing to is dangerous, my friend.
You are agreeing to destroy a part of yourself, win or lose, so yes, this matters a great deal, actually.
For better or worse, this game is a part of you that makes you you.
Annihilation is not the answer.`

In the source files of the page, an obfuscated JS function can be found.
Testing it in a JS sandbox and moving the code out of the function and changing eval to alert gives the following:

`var chat="I fail to see the logic";var input=document.getElementById("key").value;if(chat==input){alert(decodeURI('/%61%6E%6E%69%68%69l%61%74%69o%6E'))}`

Inputting the following line in the input field gives an alert with the next clue, `/annihilation`

# /annihilation
This page contains a lot of text that looks to be encoded in base64. 
It turns out to be a jpeg and decoding it reveals a jpg of the text 
`/existence`

# /existence
