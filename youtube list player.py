#!/usr/bin/env python
import webbrowser,time,BeautifulSoup
import urllib2
print "-------------\n YOUTUBE MUSIC OPENER\n YOU CAN ENTER SONGS DO YOU WANT IN ORDER AND WRITE OKAY LAST LINE\n-------------"
user_list=[]
print "What do you want me to play.\n"
while True:
    user_want=raw_input("")
    print "\n"
    if user_want=="okay":
        break
    else:
        user_list.append(user_want)


#view source code
for words in user_list:
#Replace spaces with + because YouTube searchs this way.
    words = words.replace(" ", "+")
    youtube_link="https://www.youtube.com/results?search_query=%s" % (words)
    request=urllib2.Request(youtube_link)
    response=urllib2.urlopen(request)

    ans=response.readlines()

    #find wacth?v= in source code then program open first video in search page
    for item in ans:
            if "watch?v=" in item:
                a= item[item.index("watch?v="):]
                break


    youtube="https://www.youtube.com/"+a[0:19]
    request_video_link=urllib2.Request(youtube)
    response_video_link=urllib2.urlopen(request_video_link)
    ans_video_link=response_video_link.readlines()
    for item in ans_video_link:
        if "length_seconds" in item:
            time_counter=item[item.index("length_seconds")+17:item.index("length_seconds")+20]
            break
    time_counter=int(time_counter)
    webbrowser.open(youtube,autoraise=False)
    time.sleep(time_counter)