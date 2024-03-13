# Linkedin Post Timestamp Extractor
A script that can extract the date and time of when you posted something on LinkedIn.

## Why?

Don't ask me why LinkedIn much like other platforms simply refuse to expose the timestamp of posts through their UIs, something that I'm sure every content creator would agree that it'd incredibly helpful for performance analysis to figure out what are the best days and times for you to post to your audience. 

So if you want to go back in time and figure out when you posted something exactly then you'll need to work a bit hard to get that information. But not too hard cuz now the work is done for you! 

Just run this script and off you go!

## Instructions

1. Copy the LinkedIn post url
![Screenshot of where to find the url for your LinkedIn post](/assets/imgs/copy-linkedin-post-url.PNG)

2. Clone the repo and run the script passing in the LinkedIn post as an argument. To be on the safe side so python doesn't complain about any special characters being used in the url just wrap the url with quotes (either single or double). Here's an example:

```
py app.py "https://www.linkedin.com/posts/codingmatheus_aws-news-new-charges-introduced-for-public-activity-7163147469877407744-SyL3?utm_source=share&utm_medium=member_desktop"

```

## Algorithm Explained

Full credit goes to Ollie Boyd, https://github.com/Ollie-Boyd, for reverse engineering LinkedIn's timestamp format and coming up with an algorithm to extract the information. 

Basically, the timestamp for a post is the 19-digit number present in every url. If you convert that to binary and take the first 41 binary digits and then covert back to an integer then you have an Unix Epoch timestamp! 

Say what? According to Ollie he did this through trial and error. Must've been a "fun" afternoon 😅

## Further Reading

Unix Epoch: If you want to know more timestamps and how they're stored in databases and how Unix Epoch works (and how it differs from Windows Epoch) this is a good article from Vineet Puranik, https://www.linkedin.com/pulse/timestamps-databases-vineet-puranik/

I also realized only after finishing this up that Ollie has actually created a simple web-based UI where you can paste your LinkedIn post to get the timestamp so you can also use that for something less programmatic: https://ollie-boyd.github.io/Linkedin-post-timestamp-extractor/. 



