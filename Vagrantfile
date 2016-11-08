Vagrant.configure("2") do |config|    
    config.vm.box = "bento/centos-7.2"

    ## For masterless, mount your salt file root
    config.vm.synced_folder "salt/roots/", "/srv/salt/"
  
    config.vm.provision :salt do |salt|
        salt.masterless = true
        salt.minion_config = "salt/minion"
        salt.run_highstate = true
    end
  
    config.vm.define "db" do |db|
        db.vm.hostname = "db.glassbrain"
        db.vm.network "forwarded_port", guest: 6379, host: 6379
    end
    
    config.vm.define "mq" do |mq|
        mq.vm.hostname = "mq.glassbrain"
    end
end
