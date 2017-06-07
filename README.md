This Script just try to Scan all hosts(computers, Smartphone, Routers, Servers, any device that can get assigned an IP and connect to the internet ....) which is here in Rwanda, just by pinging them one by one fast and forward on to the next one

The only thing you have to choose is which ISP to ping all its customers
then relax, few munites later all hosts served by the ISP you chose which are online anywhere in rwanda will respond to you,

You have to choose between well Known ISPs who are operating in Rwanda:
    1. Olleh Rwanda
    2. MTN RwandaCell
    3. New Artel
    4. Rwanda Ministry of Education
    5. Airtel
    6. BSC(BroadBand System Corporation)

I did i little search about which ISPs operate in RWanda and their blocks of IP addresses they manage.
i manage to get all these 6 ISPs above, maybe there's others i don't know, if you know one i didn't get to know and i didn't include it here, Please poke me, so i can add it, or if you are a developer you can contribute and add them :) 

the script is written in Python 3, i didn't bother to make it compatible with Python 2 (anyway Python 2 is going to rest soon as in 2020.. so that's it). but any contribution to make it compatible with Python 2 is welcomed.

Plus the script is supposed to run on any linux box with Nmap installed on it. when it comes to window you have to install nmap for window, Zenmap sorry, make it callable on CMD using python on windows pipes and subprocess... blah blah blah.... it's a lot of headache, sorry i didn't bother to do it :(

DEPENDENCIES:

    termcolor 1.1.0
    python-libnmap 0.7.0

Those are only python dependencies libraries you need
to make the script run correctly 

    so before running the script just pip install the libraries:
        pip3 install termcolor
        pip3 install python-libnmap