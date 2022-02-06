# Chef

Install ruby
```bash
sudo apt-get install ruby-full
ruby -v
```


BDD
```bash
gem install rspec
rspec --init

create .rspec
create spec/spec_helper.rb
```




Workstation
Links download page: https://downloads.chef.io/tools/workstation
```bash
wget https://packages.chef.io/files/stable/chef-workstation/21.8.555/ubuntu/20.04/chef-workstation_21.8.555-1_amd64.deb
echo 8336deffef14dd9a51beaca41204fb4352f59a089a52e3b4395c9c0169f4bede
sha256sum chef-workstation_21.8.555-1_amd64.deb

dpkg -i chef-workstation_21.8.555-1_amd64.deb

# Check Chef is installed
chef -v

chef generate cookbook learn_chef
```



cd learn_chef
kitchen list

sudo apt update
sudo apt install virtualbox virtualbox-ext-
# Check VBoxManage installed
VBoxManage --version

curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update
sudo apt-get install vagrant

kitchen create


kitchen login ubuntu


