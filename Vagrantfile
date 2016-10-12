Vagrant.configure("2") do |config|
    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
    
    config.vm.box = "bento/centos-6.8"

    ## For masterless, mount your salt file root
    config.vm.synced_folder "salt/roots/", "/srv/salt/"
  
    config.vm.define "db" do |db|
        db.vm.hostname = "db.glassbrain"
        
        db.vm.provision :salt do |salt|
          salt.masterless = true
          salt.minion_config = "salt/minion"
          salt.run_highstate = true
        end
    end
end
