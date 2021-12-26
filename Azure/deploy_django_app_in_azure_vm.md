# Deploying a Django application using Microsoft Azure using a virtual machine
##### Per December 2021
<br>
<br>
Here's a quick overview of the steps taken to deploy a Django web app via a virtual machine on Azure.

Note that the settings here are only **recommended for testing**.

1. Register a (free) account at [Azure.com](https://azure.com).
2. Create a [Virtual Machine](https://portal.azure.com/?quickstart=true#create/Microsoft.VirtualMachine) and be sure to change the size to a more affordable one vs the expensive default option. I've chosen the following settings:
* Select Ubuntu Server 20.04 LTS - Gen2.
* Size: Standard_B1s (USD 8.76/month) - this will be taken from the USD 200 free credits given when signing up.
* Inbound port rules: allow HTTP (80), HTTPS (443), SSH (22).
* Generate new SSH key pair (or use an existing one if you've already used Azure before).
* Confirm remaining settings and the VM will be created.
3. Azure will ask you to download the private SSH key as .pem file. You can do so
> $ ssh -i <path to .pem file> username@< ip-address of vm>
4. You'll get a prompt to confirm the authenticity of the host. You can find the public key in the Azure portal with the name provided at the setup of the VM
- alternatively, look for the public key in the Boot diagnostics (the key is generated upon first boot)
5. I prefer to have Python on the VM match the Python version on my desktop:
```
$ python3 -V 
Python 3.8.10
$ apt-get install python3.9
...
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/pyhon3.8 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/pyhon3.9 2
$ sudo update-alternatives --config python3
There are 2 choices for the alternative python3 (providing /usr/bin/python3).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3.9   2         auto mode
  1            /usr/bin/python3.8   1         manual mode
  2            /usr/bin/python3.9   2         manual mode

Press <enter> to keep the current choice[*], or type selection number: 2
$ python3 -V
Python 3.9.5
```
6. Ensure Git is installed
> $ git --version
7. Setup sitename, in my case I'm setting up my 'superlists' staging site, to superlists-staging.markhurenkamp.nl from my [TDD Book repo](https://github.com/MarkHurenkamp/TDDBook):
> $ export SITENAME=superlists.staging.markhurenkamp.nl
8. Clone git:
> $ git clone https://github.com/MarkHurenkamp/TDDBook.git ~sites/$SITENAME
9. Install venv and the requirements:
```
$ python3 -m venv venv
$ ./venv/bin/pip install -r requirements.txt
```
10. Setup Azure VM networking to soruce: any, source port ranges: *, Destination: any, Destination port ranges: 8000 on protocol TCP, to allow our staging site to be accessed remotely (*again, these are settings for testing*)
11. Perform migrations on the server:
> $ ./venv/bin/python manage.py migrate --noinput
12. Run server (with actual 0.0.0.0, no need to replace the IP address):
> $ ./venv/bin/python manage.py runserver 0.0.0.0:8000

Of course this is just a very basic setup for testing, using Django as the web server. 
For additional information, see my [Django deployment cheat-sheet](https://github.com/MarkHurenkamp/Cheat-sheets/tree/main/Python/Django%20deployment/) or chapters 9 and 10 of [Obey the Testing Goat.com](https://www.obeythetestinggoat.com)