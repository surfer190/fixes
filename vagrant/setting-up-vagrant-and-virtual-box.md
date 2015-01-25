#Setting up Vagrant and Virtual Box

1. Download Vagrant and Virtuals box
(Virtualbox)[https://www.virtualbox.org/wiki/Linux_Downloads]
(Vagrant)[http://www.vagrantup.com/downloads]

*Make sure to install command line tools*

2. Make a directory for vagrantfile and instructions

```
mkdir ~/vagrant
```

3. Find a virtual box you want


(puppetlabs boxes)[http://puppet-vagrant-boxes.puppetlabs.com/]
(vagrant ubuntu boxes)[https://github.com/mitchellh/vagrant/wiki/Available-Vagrant-Boxes]
(atlas)[https://atlas.hashicorp.com/boxes/search]

*Pick debian*

4. Add using `vagrant box add`

```
vagrant box add debian64 http://puppet-vagrant-boxes.puppetlabs.com/debian-73-x64-virtualbox-nocm.box
```

5. Create a default virtual server:
```
vagrant init debian64
```

6. Book the server
```
vagrant up
```

* If you get an error on about not being able to connect with ssh *

```
vim VagrantFile
```
Add:
```
config.vm.provider "virtualbox" do |v|
  v.gui = true
end
```
Restart:
```
vagrant halt

vagrant up
```

* You may still get this error *

```
VT-x/AMD-V hardware acceleration is not available on your system. Your 64-bit guest will fail to detect a 64-bit CPU and will not be able to boot.
```
You can check your system with:
```
egrep '(vmx|svm)' /proc/cpuinfo
```
 May need to acvtivate in bios `AMD-V/VT-x`

 In VM:
 ```
 Settings -> System -> Acceleration" and make sure that "Enable VT-x/AMD-V" is activated
 ```

(vagrant docs)[https://docs.vagrantup.com/v2/virtualbox/configuration.html]
(run 64bit guest virtualbox)[http://askubuntu.com/questions/41550/how-do-i-run-a-64-bit-guest-in-virtualbox]