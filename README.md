# Awesome SaltStack  [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://yt3.ggpht.com/-u0bhYCAc9tQ/AAAAAAAAAAI/AAAAAAAAAAA/VzeLz4xM-AM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg" align="right" width="100">](https://SaltStack.com)

> A collaborative curated list of awesome SaltStack resources, tutorials and other salted stuff.

SaltStack is the other configuration management system built with Python.  
It takes a new approach to infrastructure management by developing software that is easy enough to get running in seconds, scalable enough to manage tens of thousands of servers, and fast enough to control and communicate with them in milliseconds.  
SaltStack software manages system infrastructure and the application stacks that run on it and is used by web-scale application developers, DevOps teams and systems administrators.

## Contents

- [Official resources](#official-resources)
- [Tutorials](#tutorials)
- [Code](#code)
- [Books](#books)
- [Videos](#videos)
- [Tools](#tools)
- [Presentations](#presentations)
- [Blogposts and opinions](#blogposts-and-opinions)
- [Discussions](#discussions)
- [Community](#community)
- [Formulas](#formulas)
- [Cheat sheets](#cheat-sheets)
- [Uncategorized](#uncategorized)

## Official resources

* [SaltStack site](https://saltstack.com/) - Company website.
* [GitHub repo](https://github.com/saltstack/salt) - Salt's source code, issues discussion and collaboration.
* [SaltStack Documentation](https://docs.saltstack.com/en/latest/) - Official documentation.
* [Training and certification](https://saltstack.com/training/) - Official training.

## Tutorials

* [Salt in 10 minutes](https://docs.saltstack.com/en/latest/topics/tutorials/walkthrough.html) - Official walkthrough.
* [About SaltStack](http://www.yet.org/2016/09/salt/) - Extensive blogpost with lots of in-depth information.
* [Managing Linux server configs with the SaltStack](https://techarena51.com/index.php/getting-started-with-saltstack/) - Managing Linux server configs with the SaltStack.
* [A dive into SaltStack](https://opencredo.com/a-dive-into-salt-stack/) - SaltStack uncovered - Configuration management has been a big leap forward for System Engineers.
* [How To Install Salt on Ubuntu 12.04](https://www.digitalocean.com/community/tutorials/how-to-install-salt-on-ubuntu-12-04) - Part 1 of 2 in the series _An Introduction to Salt_.
* [How To Create Your First Salt Formula](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-salt-formula) - Part 2 in the series _An Introduction to Salt_.
* [Automated Provisioning of DigitalOcean Cloud Servers with Salt Cloud on Ubuntu 12.04 ](https://www.digitalocean.com/community/tutorials/automated-provisioning-of-digitalocean-cloud-servers-with-salt-cloud-on-ubuntu-12-04) - Walkthrough on automated provisioning of DigitalOcean Cloud Servers with Salt Cloud on Ubuntu 12.04.
* [How To Install and Configure Salt Master and Minion Servers on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-salt-master-and-minion-servers-on-ubuntu-14-04) - SaltStack installation walkthrough for Ubuntu 14.04.
* [How To Use Salt Cloud Map Files to Deploy App Servers and an Nginx Reverse Proxy ](https://www.digitalocean.com/community/tutorials/how-to-use-salt-cloud-map-files-to-deploy-app-servers-and-an-nginx-reverse-proxy) - Walkthrough on how to use Salt Cloud Map Files to deploy application servers and an Nginx reverse proxy.
* [An Introduction to SaltStack Terminology and Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-saltstack-terminology-and-concepts) - Part 1 of 6 in the series _Managing Development Environments with SaltStack_.
* [SaltStack Infrastructure: Installing the Salt Master](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-installing-the-salt-master) - Part 2 of 6 in the series _Managing Development Environments with SaltStack_.
* [SaltStack Infrastructure: Configuring Salt-Cloud to Spin Up DigitalOcean Resources](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-configuring-salt-cloud-to-spin-up-digitalocean-resources) - Part 3 of 6 in the series _Managing Development Environments with SaltStack_.
* [SaltStack Infrastructure: Creating Salt States for Nginx Web Servers](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-creating-salt-states-for-nginx-web-servers) - Part 4 of 6 in the series _Managing Development Environments with SaltStack_.
* [SaltStack Infrastructure: Creating Salt States for HAProxy Load Balancers](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-creating-salt-states-for-haproxy-load-balancers) - Part 5 of 6 in the series _Managing Development Environments with SaltStack_.
* [SaltStack Infrastructure: Creating Salt States for MySQL Database Servers](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-creating-salt-states-for-mysql-database-servers) - Part 6 in the series _Managing Development Environments with SaltStack_.
* [Getting Started with SaltStack - the Other Configuration Management System Built with Python](https://www.linuxjournal.com/content/getting-started-salt-stack-other-configuration-management-system-built-python) - A Linux Journal "Getting started" from 2013.
* [Create an army of Salt minions on DigitalOcean](http://www.aaronbell.com/lets-make-salt-minions-on-digitalocean/) - Combine the simplicity of Salt with DigitalOcean's snapshot and image feature.
* [Vagrant & SaltStack Quickstart Tutorial](http://hittaruki.info/post/vagrant-saltstack-tutorial/) - Getting started with SaltStack and Vagrant.
* [Salt-API, A Crash Course](http://www.thereluctanttecchie.com/salt_api_a_crash_course/) - Get a barebones salt-api proof of concept up and running.
* [SaltStack: Keeping Salt Pillar data encrypted using GPG](http://fabianlee.org/2016/10/18/saltstack-keeping-salt-pillar-data-encrypted-using-gpg/) - On secure encryption/decryption of pillar data.
* [Secure Pillar in SaltStack with GPG](https://gijs.io/2017/02/28/secure-pillar-data-in-saltstack-with-gpg/) - Encrypting your pillar data can be done with GPG.
* [Getting Started with SaltStack - Part 1](http://blog.infracloud.io/saltstack-tutorial-part-1/) -  Simple setup and play around on the command line.
* [Getting Started with SaltStack - Part 2](http://blog.infracloud.io/saltstack-tutorial-part-2/) - Write a complete module for installing and configure a web server.
* [SaltStack Examples](https://www.unixmen.com/saltstack-examples/) - Will teach you some of default functions in a quick way.
* [Masterless Saltstack](https://honza.ca/2013/12/masterless-saltstack) - A simple guide on how to use SaltStack in masterless mode.

## Code

* [zulily/alkali](https://github.com/zulily/alkali) - A collections of SaltStack states and pillar data that provide just the basics for provisioning Linux instances that may be built upon.
* [zulily/buoyant](https://github.com/zulily/buoyant) - Leverages docker to provide an alternative to VM-centric SaltStack development environments.

## Books

* [O'Reilly - Salt Essentials](http://shop.oreilly.com/product/0636920033240.do) by Craig Sebenik, Thomas Hatch.
* [Leanpub - SaltStack For DevOps](https://leanpub.com/saltstackfordevops) by Aymen El Amri.
* [Leanpub - Getting Started with SaltStack](https://leanpub.com/gettingstartedwithsaltstack) by Ben Hosmer.
* [Packt - Learning SaltStack, 2nd ed.](https://www.packtpub.com/networking-and-servers/learning-saltstack-second-edition) by Colton Myers.
* [Packt - Mastering SaltStack, 2nd ed.](https://www.packtpub.com/networking-and-servers/mastering-saltstack-second-edition) by Joseph Hall.
* [Packt - Extending SaltStack](https://www.packtpub.com/networking-and-servers/extending-saltstack) by Joseph Hall.
* [Packt - Salt Cookbook](https://www.packtpub.com/networking-and-servers/salt-cookbook) by Anirban Saha.

## Videos

* [SaltStack](https://www.youtube.com/user/saltstack) - SaltStack's official YouTube channel.
* [Managing Your Infrastructure with SaltStack](https://www.youtube.com/watch?v=y-zQUqMHRX4&t=35s) - PyCon 2015 - April 11, 2015 - Colton Myers.
* [Beyond Configuration Management with SaltStack for Event-Driven Infrastructure](https://www.youtube.com/watch?v=cMCH6EizVVc) - Southern California Linux Expo - January 23, 2016 - David Boucha.
* [Automation and Orchestration with SaltStack and Twilio](https://vimeo.com/162183524) - Devops Chicago - March 2, 2016 - Nathan Brooks.
* [Herding Cattle with SaltStack and Targeting via CMDB](https://www.youtube.com/watch?v=F3K706JJ2EI) - SaltConf16 - April 21, 2016 - Onno Ebbinge.

## Tools

* [SaltPad](https://github.com/Lothiraldan/saltpad) - SaltPad is a GUI tool to manage SaltStack deployments + orchestration.
* [SaltShaker](https://github.com/yueyongyue/saltshaker) - Another good looking GUI for SaltStack.
* [SaltGUI](https://github.com/oliverdunk/SaltGUI) - A web interface for managing SaltStack based infrastructure.
* [Pepperboard](https://github.com/webedia-dev/pepperboard) - A simple and modular dashboard toolkit for SaltStack.

## Presentations

* [Getting Started with SaltStack](https://speakerdeck.com/pycon2014/getting-started-with-saltstack-by-peter-baumgartner) - by Peter Baumgartner.
* [An introduction to infrastructure management with SaltStack](http://www.slideshare.net/saltstack/an-overvisaltstack-presentation-clean) - by Aurelien Geron.
* [Saltpad: A SaltStack Web GUI](https://speakerdeck.com/lothiraldan/saltpad-a-saltstack-web-gui) - by Boris Feld.
* [Intro to SaltStack](http://www.justincarmony.com/slides/salt-tutorial/) - by Justin Carmony.

## Blogposts and opinions

* [Salt To Finish](http://www.salttofinish.com/) - "the original SaltStack blog".
* [Docker with SaltStack](https://opsnotice.xyz/docker-with-saltstack/) - How-to use SaltStack on a virtual cloud server based on Debian or Ubuntu.
* [Masterless SaltStack Provisioning to VirtualBox with Vagrant ](http://www.roblayton.com/2014/12/masterless-saltstack-provisioning-to.html) - Using SaltStack to cover a more automated approach to provisioning servers.
* [Moving away from Puppet: SaltStack or Ansible?](http://ryandlane.com/blog/2014/08/04/moving-away-from-puppet-saltstack-or-ansible/) -  Salt and Ansible as viable and excellent options for replacing Puppet.
* [One week of Salt: frustrations and reflections](https://stevebennett.me/2014/02/17/one-week-of-salt-frustrations-and-reflections/) - First hand experiences from a Chef user.
* [Getting started with SaltStack by example: Automatically Installing nginx](http://bencane.com/2013/09/03/getting-started-with-saltstack-by-example-automatically-installing-nginx/) - A good getting started guide for both Salt master and minions.
* [SaltStack: Manage entries in unmanaged files with File Blockreplace](https://makina-corpus.com/blog/metier/2014/saltstack-manage-entries-in-unmanaged-files-with-file-blockreplace) - how to use the SaltStack's core "file.blockreplace".
* [Docker Swarm 1.12 Cluster Orchestration with SaltStack](http://btmiller.com/2016/11/27/docker-swarm-1.12-cluster-orchestration-with-saltstack.html) - Let’s see how we can automate the spin-up of a cluster using SaltStack.
* [SaltStack - Review and how it fares against Ansible and Puppet](https://www.amon.cx/blog/saltstack-review/) - As seen from the Salt perspective.

## Discussions

* [Reddit: Vagrat, SaltStack, Ansible, Docker, Chef, Puppet, Packer.. Something](https://www.reddit.com/r/sysadmin/comments/2fmkvq/vagrat_saltstack_ansible_docker_chef_puppet/) - Discussion on Reddit, started Sept. 2014 in `/r/sysadmin`.

## Community

* [Salt IRC chat](http://webchat.freenode.net/?channels=salt&uio=Mj10cnVlJjk9dHJ1ZSYxMD10cnVl83) - IRC about Salt on Freenode.
* [Twitter feed](https://twitter.com/saltstack) - Official Twitter account.
* [Mailing list](https://groups.google.com/forum/#!forum/salt-users) - Salt-users mailinglist on Google Groups.
* [SaltStack Meetups](https://www.meetup.com/pro/saltstack/) - Worldwide Meetup groups.
* [SaltConf](http://saltconf.com/) - Annual user conference for SaltStack customers, users, partners, developers and community members.


## Formulas
* [SaltStack Formulas](https://github.com/saltstack-formulas/) - A central collection of formula repositories for SaltStack.
* [Salt Formulas](https://github.com/salt-formulas) - A community developed SaltStack formulas ecosystem.
* [Writing SaltStack formulas](http://ryepup.unwashedmeme.com/blog/2015/03/16/writing-saltstack-formulas/) - An overview on writing SaltStack formulas.
* [Salt Formulas](http://www.yet.org/2016/09/salt-formulas/) - In-depth blogpost about Salt Formulas.

## Cheat sheets

* [SaltStack Cheat Sheet Plus](https://github.com/fmdlc/saltstack-cheatsheet) - by Facu de la Cruz.
* [Salt Commands cheat sheet](https://sites.google.com/site/bladelogicwiki/salt-stack/guides/salt-commands) - List of common Salt commands (by "Bladelogic").
* [SaltStack Cheat Sheet](http://www.xenuser.org/saltstack-cheat-sheet/) - by Valentin Höbel.
* [SaltStack Wiki](https://github.com/saltstack/salt/wiki/Cheat-Sheet) - Cheat sheet in the SaltStack GitHub Wiki.

## Uncategorized

* [Salt (software)](https://en.wikipedia.org/wiki/Salt_(software)) - Wikipedia (English).
* [HubbleStack: Security for DevOps](https://hubblestack.io/) - Hubble is a modular, open-source security compliance framework built on top of SaltStack.

## License

[![CC0](https://camo.githubusercontent.com/60561947585c982aee67ed3e3b25388184cc0aa3/687474703a2f2f6d6972726f72732e6372656174697665636f6d6d6f6e732e6f72672f70726573736b69742f627574746f6e732f38387833312f7376672f63632d7a65726f2e737667)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Henk](https://hbokh.github.io/) has waived all copyright and related or neighboring rights to this work.
