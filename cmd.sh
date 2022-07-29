## Add ssh on server for connect with ssh without password ( read main.env)
# TODO make a playbook 4 this
ansible -i inventory.yaml -m lineinfile -a "path=/etc/sudoers line='dams ALL=(ALL:ALL) NOPASSWD: ALL'" --become-method=su --become --ask-become-pass all