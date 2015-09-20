# Macbook Initial Setup

* Open terminal: Launchpad -> Terminal

_Quick tip: `end` and `home` key functionality can be used with command (or fn) + right arrow / left arrow_

* Install Command line developer tools:

```
xcode-select --install
```

* Install pip

```
sudo easy_install pip
```

* Install ansible

```
sudo pip install ansible
```

* Clone (Geerling Guy's macbook setup git repo)[https://github.com/geerlingguy/mac-dev-playbook]:

```
https://github.com/geerlingguy/mac-dev-playbook.git
```

* Install the roles:

```
cd mac-dev-playbook
sudo ansible-galaxy install -r requirements.txt
```

* Run the playbook:

```
ansible-playbook main.yml -i inventory --ask-sudo-pass
```

[Source of Instructions](http://docs.ansible.com/ansible/intro_installation.html#latest-releases-via-pip)
